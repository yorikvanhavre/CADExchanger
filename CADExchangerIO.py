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

import subprocess,tempfile,os,FreeCAD

preferences = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/CADExchanger")
converter = preferences.GetString("ConverterPath","")

if FreeCAD.GuiUp:
    from PySide import QtCore, QtGui
    # Qt tanslation handling
    try:
        _encoding = QtGui.QApplication.UnicodeUTF8
        def translate(context, text, disambig=None):
            return QtGui.QApplication.translate(context, text, disambig, _encoding)
    except AttributeError:
        def translate(context, text, disambig=None):
            return QtGui.QApplication.translate(context, text, disambig)
else:
    def translate(ctxt,txt):
        return txt


def addPreferencePage():
    
    
    "Adds the CAD Exchanger preferences page"
    
    
    if FreeCAD.GuiUp:
        import FreeCADGui
        FreeCADGui.addPreferencePage(os.path.join(os.path.dirname(__file__),"CADExchangerIO.ui"),"Import-Export")



def getExtensions():


    "Get the list of supported file formats from CadExchangerConv executable"
    # this is currently not used but might prove handy some day...


    if not converter:
        FreeCAD.Console.PrintError(translate("CADExchanger","CAD Exchanger converter path is not set. Please check Preferences -> Import/Export/CAD Exchanger\n"))
        return
    if subprocess.call(converter) != 1:
        FreeCAD.Console.PrintError(translate("CADExchanger","Error while running CAD Exchanger\n"))
        return
    extensions = {}
    try:
        subprocess.check_output(converter)
    except subprocess.CalledProcessError as e:
        if e.output.startswith("Usage"):
            rec = False
            rest = ""
            for l in e.output.split("\n"):
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
        else:
            FreeCAD.Console.PrintError(translate("CADExchanger","Unable to retrieve file extensions from CAD Exchanger\n"))
    return extensions



def open(filename):


    "called by FreeCAD on opening a file"


    docname = (os.path.splitext(os.path.basename(filename))[0]).encode("utf8")
    doc = FreeCAD.newDocument(docname)
    doc.Label = docname
    FreeCAD.ActiveDocument = doc
    return insert(filename,doc.Name)



def insert(filename,docname,returnpath=False):


    "called on importing a file in an existing document"


    if not converter:
        FreeCAD.Console.PrintError(translate("CADExchanger","CAD Exchanger converter path is not set. Please check Preferences -> Import/Export/CAD Exchanger\n"))
        return
    if subprocess.call(converter) != 1:
        FreeCAD.Console.PrintError(translate("CADExchanger","Error while running CAD Exchanger\n"))
        return
    try:
        doc = FreeCAD.getDocument(docname)
    except NameError:
        doc = FreeCAD.newDocument(docname)
    FreeCAD.ActiveDocument = doc
    tempname = tempfile.mkstemp(suffix=".brep")[1]
    exstr = [converter, " -i ", filename, " -e ", tempname]
    print ("executing "+"".join(exstr))
    result = subprocess.call(exstr)
    if result != 0:
        FreeCAD.Console.PrintError(translate("CADExchanger","Error during CAD Exchanger conversion\n"))
        return
    if returnpath:
        return tempname
    else:
        import Part
        Part.show(Part.read(tempname))

    return doc



def export(exportList,filename):


    "called on exporting a file"


    if not converter:
        FreeCAD.Console.PrintError(translate("CADExchanger","CAD Exchanger converter path is not set. Please check Preferences -> Import/Export/CAD Exchanger\n"))
        return
    if subprocess.call(converter) != 1:
        FreeCAD.Console.PrintError(translate("CADExchanger","Error while running CAD Exchanger\n"))
        return
    import Part
    tempname = tempfile.mkstemp(suffix=".brep")[1]
    Part.export(exportList,tempname)
    exstr = [converter, " -i ", tempname, " -e ", filename]
    print ("executing "+"".join(exstr))
    result = subprocess.call(exstr)
    if result != 0:
        FreeCAD.Console.PrintError(translate("CADExchanger","Error during CAD Exchanger conversion\n"))
    return
