#***************************************************************************
#*                                                                         *
#*   Copyright (c) 2017 Yorik van Havre <yorik@uncreated.net>              *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This program is distributed in the hope that it will be useful,       *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Library General Public License for more details.                  *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with this program; if not, write to the Free Software   *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************

from __future__ import print_function

__title__="FreeCAD CAD Exchanger importer/exporter"
__author__ = "Yorik van Havre"
__url__ = "http://www.freecadweb.org"

import os
import sys
import subprocess
import tempfile
import platform
import FreeCAD

# a list of filetypes we don't want to handle with CADExchanger
builtins = ["step","iges","brep"]

# Save the native open function to avoid collisions with the function declared here
if open.__module__ in ['__builtin__', 'io']: pythonopen = open

def translate(ctx,txt):

    """Convenience Qt translate() wrapper"""

    if FreeCAD.GuiUp:
        from PySide import QtCore, QtGui
        try:
            _encoding = QtGui.QApplication.UnicodeUTF8
            return QtGui.QApplication.translate(ctx, txt, None, _encoding)
        except AttributeError:
            return QtGui.QApplication.translate(ctx, txt, None)
    else:
        return txt


def getConverter():

    """Returns the path to the ExchangerConv executable, if set in preferences or autolocated"""

    # look in preferences
    preferences = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/CADExchanger")
    converter = preferences.GetString("ConverterPath","")
    if not converter:
        # try autolocating
        from distutils import spawn
        for prog in ["ExchangerConv","ExchangerConv.exe"]:
            loc = spawn.find_executable(prog)
            if loc:
                converter = loc
                preferences.SetString("ConverterPath",converter)
                break
    devnull = pythonopen(os.devnull, 'w') # redirect cadexchanger output
    if subprocess.call(converter,stdout=devnull, stderr=devnull) != 1:
        return None
    return converter


def addPreferencePage():

    """Adds the CAD Exchanger preferences page to FreeCAD"""

    if FreeCAD.GuiUp:
        import FreeCADGui
        FreeCADGui.addPreferencePage(os.path.join(os.path.dirname(__file__),"CADExchangerIO.ui"),"Import-Export")


def getExtensions():

    """Returns two dicts representing supported import and export file formats from the ExchangerConv executable"""

    converter = getConverter()
    if not converter:
        return
    extensions = {}
    import_extensions = {}
    export_extensions = {}
    try:
        subprocess.check_output(converter)
    except subprocess.CalledProcessError as e:
        outp = e.output
        if not isinstance(outp,str):
            outp = outp.decode("utf8")
        if outp.startswith("Usage"):
            rec = False
            rest = ""
            for l in outp.split("\n"):
                if rec:
                    if not l:
                        rec = False
                    else:
                        l = l.split(":\t")
                        if len(l) == 1:
                            rest = l[0].strip() + " "
                        else:
                            extensions[l[-1].strip()] = rest + l[0].strip()
                            rest = ""
                elif "recognized extensions" in l.lower():
                    rec = True
                elif l.lower().startswith("import formats"):
                    fmts = [f.strip() for f in l.split(":")[1].split(",")]
                    #print(len(fmts),"import formats:",fmts)
                    for fmt in fmts:
                        for key in extensions.keys():
                            if (fmt.lower() in key.lower()) and (fmt.lower() not in builtins):
                                import_extensions[key] = extensions[key]
                elif l.lower().startswith("export formats"):
                    fmts = [f.strip() for f in l.split(":")[1].split(",")]
                    #print(len(fmts),"export formats:",fmts)
                    for fmt in fmts:
                        for key in extensions.keys():
                            if (fmt.lower() in key.lower()) and (fmt.lower() not in builtins):
                                export_extensions[key] = extensions[key]

        else:
            FreeCAD.Console.PrintError(translate("CADExchanger","Unable to retrieve file extensions from CADExchanger\n"))
    #print(len(import_extensions),"import:",import_extensions)
    #print(len(export_extensions),"export:",export_extensions)
    if not import_extensions or not export_extensions:
        FreeCAD.Console.PrintError(translate("CADExchanger","Unable to retrieve import/export filters from CADExchanger\n"))
    return import_extensions,export_extensions


def addExtensions():

    """Adds the CADExchanger extensions to FreeCAD"""

    importfmts,exportfmts = getExtensions()
    for key,value in importfmts.items():
        FreeCAD.addImportType(key+" ("+value+")","CADExchangerIO")
    for key,value in exportfmts.items():
        FreeCAD.addExportType(key+" ("+value+")","CADExchangerIO")


def open(filename):

    """Called by FreeCAD on opening a file"""

    docname = (os.path.splitext(os.path.basename(filename))[0])
    if sys.version_info.major < 3:
        docname = docname.encode("utf8")
    doc = FreeCAD.newDocument(docname)
    doc.Label = docname
    FreeCAD.ActiveDocument = doc
    return insert(filename,doc.Name)


def insert(filename,docname,returnpath=False):

    """Called by FreeCAD on importing a file in an existing document"""

    converter = getConverter()
    if not converter:
        FreeCAD.Console.PrintError(translate("CADExchanger","CAD Exchanger converter path is not set. Please check Preferences -> Import/Export/CAD Exchanger\n"))
        return
    try:
        doc = FreeCAD.getDocument(docname)
    except NameError:
        doc = FreeCAD.newDocument(docname)
    FreeCAD.ActiveDocument = doc
    tempname = tempfile.mkstemp(suffix=".brep")[1]
    #exstr = [converter, " -i ", filename, " -e ", tempname]
    exstr = [converter, " -i \"", filename, "\" -e \"", tempname, "\""]
    print ("executing "+"".join(exstr))
    #result = subprocess.call(exstr)
    result = subprocess.Popen("".join(exstr), shell=True, stdout=subprocess.PIPE)
    stdout = result.communicate()[0]
    if result.returncode != 0:
        FreeCAD.Console.PrintError(translate("CADExchanger","Error during CADExchanger conversion\n"))
        if not isinstance(stdout,str):
            stdout = stdout.decode("utf8")
        print('CADExchanger output:\n' + stdout)
        return
    if returnpath:
        return tempname
    else:
        import Part
        Part.show(Part.read(tempname))

    return doc


def export(exportList,filename):

    """Called by FreeCAD on exporting a file"""

    import Part

    converter = getConverter()
    if not converter:
        FreeCAD.Console.PrintError(translate("CADExchanger","CAD Exchanger converter path is not set. Please check Preferences -> Import/Export/CAD Exchanger\n"))
        return
    tempname = tempfile.mkstemp(suffix=".brep")[1]
    Part.export(exportList,tempname)
    exstr = [converter, " -i \"", tempname, "\" -e \"", filename, "\""]
    print ("executing "+"".join(exstr))
    #result = subprocess.call(exstr)
    result = subprocess.Popen("".join(exstr), shell=True, stdout=subprocess.PIPE)
    stdout = result.communicate()[0]
    if result.returncode != 0:
        FreeCAD.Console.PrintError(translate("CADExchanger","Error during CADExchanger conversion\n"))
        if not isinstance(stdout,str):
            stdout = stdout.decode("utf8")
        print('CADExchanger output:\n' + stdout)
    return
