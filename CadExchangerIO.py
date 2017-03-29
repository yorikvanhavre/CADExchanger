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

__title__="FreeCAD CadExchanger importer/exporter"
__author__ = "Yorik van Havre"
__url__ = "http://www.freecadweb.org"

import subprocess,tempfile,os,FreeCAD

preferences = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/CadExchanger")
converter = preferences.GetString("ConverterPath","")



def addPreferencePage():
    
    
    "Adds the CadExchanger preferences page"
    
    
    if FreeCAD.GuiUp:
        import FreeCADGui
        FreeCADGui.addPreferencePage(os.path.join(os.path.dirname(__file__),"CadExchangerIO.ui"),"Import-Export")


def registerExtensions():


    "Registers CadExchanger extensions"


    if not converter:
        return
    if preferences.GetBool("ImportStep",False):
        FreeCAD.addImportType("STEP (CadExchanger) (*.stp, *.step)","CadExchangerIO")
    if preferences.GetBool("ExportStep",False):
        FreeCAD.addExportType("STEP (CadExchanger) (*.stp, *.step)","CadExchangerIO")
    if preferences.GetBool("ImportIges",False):
        FreeCAD.addImportType("IGES (CadExchanger) (*.igs, *.iges)","CadExchangerIO")
    if preferences.GetBool("ExportIges",False):
        FreeCAD.addExportType("IGES (CadExchanger) (*.igs, *.iges)","CadExchangerIO")
    if preferences.GetBool("ImportAcis",False):
        FreeCAD.addImportType("ACIS/SAT (CadExchanger) (*.sat)","CadExchangerIO")
    if preferences.GetBool("ExportAcis",False):
        FreeCAD.addExportType("ACIS/SAT (CadExchanger) (*.sat)","CadExchangerIO")
    if preferences.GetBool("ImportParasolid",False):
        FreeCAD.addImportType("Parasolid-XT (CadExchanger) (*.x_t, *.x_b, *.xmt_txt, *.xmt_bin)","CadExchangerIO")
    if preferences.GetBool("ExportParasolid",False):
        FreeCAD.addExportType("Parasolid-XT (CadExchanger) (*.x_t, *.x_b, *.xmt_txt, *.xmt_bin)","CadExchangerIO")
    if preferences.GetBool("ImportJt",False):
        FreeCAD.addImportType("JT (CadExchanger) (*.jt)","CadExchangerIO")
    if preferences.GetBool("ExportJt",False):
        FreeCAD.addExportType("JT (CadExchanger) (*.jt)","CadExchangerIO")
    if preferences.GetBool("ImportRhino",False):
        FreeCAD.addImportType("Rhino (CadExchanger) (*.3dm)","CadExchangerIO")
    if preferences.GetBool("ExportRhino",False):
        FreeCAD.addExportType("Rhino (CadExchanger) (*.3dm)","CadExchangerIO")
    if preferences.GetBool("ImportObj",False):
        FreeCAD.addImportType("Wavefromt OBJ (CadExchanger) (*.obj)","CadExchangerIO")
    if preferences.GetBool("ExportObj",False):
        FreeCAD.addExportType("Wavefront OBJ (CadExchanger) (*.obj)","CadExchangerIO")
    if preferences.GetBool("ImportStl",False):
        FreeCAD.addImportType("STL (CadExchanger) (*.stl)","CadExchangerIO")
    if preferences.GetBool("ExportStl",False):
        FreeCAD.addExportType("STL (CadExchanger) (*.stl)","CadExchangerIO")
#    if preferences.GetBool("ImportVrml",False):
#        FreeCAD.addImportType("VRML (CadExchanger) (*.wrl)","CadExchangerIO")
    if preferences.GetBool("ExportVrml",False):
        FreeCAD.addExportType("VRML (CadExchanger) (*.wrl)","CadExchangerIO")
#    if preferences.GetBool("ImportX3d",False):
#        FreeCAD.addImportType("X3D (CadExchanger) (*.x3d)","CadExchangerIO")
    if preferences.GetBool("ExportX3d",False):
        FreeCAD.addExportType("X3D (CadExchanger) (*.x3d)","CadExchangerIO")



def getExtensions():


    "Get the list of supported file formats from CadExchangerConv executable"
    # this is currently not used but might prove handy some day...


    if not converter:
        FreeCAD.PrintError(translate("CadExchanger","CadExchanger converter path is not set. Please check Preferences -> Import/Export/CadExchanger\n"))
        return
    if subprocess.call(converter) != 1:
        FreeCAD.PrintError(translate("CadExchanger","Error while running CadExchanger\n"))
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
            FreeCAD.PrintError(translate("CadExchanger","Unable to retrieve file extensions from CadExchanger\n"))
    return extensions



def open(filename):


    "called by FreeCAD on opening a file"


    docname = (os.path.splitext(os.path.basename(filename))[0]).encode("utf8")
    doc = FreeCAD.newDocument(docname)
    doc.Label = docname
    FreeCAD.ActiveDocument = doc
    return insert(filename,doc)



def insert(filename,docname):


    "called on importing a file in an existing document"


    if not converter:
        FreeCAD.PrintError(translate("CadExchanger","CadExchanger converter path is not set. Please check Preferences -> Import/Export/CadExchanger\n"))
        return
    if subprocess.call(converter) != 1:
        FreeCAD.PrintError(translate("CadExchanger","Error while running CadExchanger\n"))
        return
    try:
        doc = FreeCAD.getDocument(docname)
    except NameError:
        doc = FreeCAD.newDocument(docname)
    FreeCAD.ActiveDocument = doc
    tempname = tempfile.mkstemp(suffix=".brep")[1]
    exstr = [converter, " -i ", filename, " -e ", tempname]
    print "executing "+" ".join(exstr)
    result = subprocess.call(exstr)
    if not result:
        FreeCAD.PrintError(translate("CadExchanger","Error while running CadExchanger\n"))
        return
    import Part
    Part.show(Part.read(tempname))

    return doc



def export(exportList,filename):


    "called on exporting a file"


    if not converter:
        FreeCAD.PrintError(translate("CadExchanger","CadExchanger converter path is not set. Please check Preferences -> Import/Export/CadExchanger\n"))
        return
    if subprocess.call(converter) != 1:
        FreeCAD.PrintError(translate("CadExchanger","Error while running CadExchanger\n"))
        return
    import Part
    tempname = tempfile.mkstemp(suffix=".brep")[1]
    Part.export(exportList,tempname)
    exstr = [converter, " -i ", tempname, " -e ", filename]
    print "executing "+" ".join(exstr)
    result = subprocess.call(exstr)
    if not result:
        FreeCAD.PrintError(translate("CadExchanger","Error while running CadExchanger\n"))
        return
