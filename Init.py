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


preferences = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/CADExchanger")
converter = preferences.GetString("ConverterPath","")

if converter:
    if preferences.GetBool("ImportStep",False):
        FreeCAD.addImportType("STEP (CAD Exchanger) (*.stp, *.step)","CADExchangerIO")
    if preferences.GetBool("ExportStep",False):
        FreeCAD.addExportType("STEP (CAD Exchanger) (*.stp, *.step)","CADExchangerIO")
    if preferences.GetBool("ImportIges",False):
        FreeCAD.addImportType("IGES (CAD Exchanger) (*.igs, *.iges)","CADExchangerIO")
    if preferences.GetBool("ExportIges",False):
        FreeCAD.addExportType("IGES (CAD Exchanger) (*.igs, *.iges)","CADExchangerIO")
    if preferences.GetBool("ImportAcis",False):
        FreeCAD.addImportType("ACIS/SAT (CAD Exchanger) (*.sat)","CADExchangerIO")
    if preferences.GetBool("ExportAcis",False):
        FreeCAD.addExportType("ACIS/SAT (CAD Exchanger) (*.sat)","CADExchangerIO")
    if preferences.GetBool("ImportParasolid",False):
        FreeCAD.addImportType("Parasolid-XT (CAD Exchanger) (*.x_t, *.x_b, *.xmt_txt, *.xmt_bin)","CADExchangerIO")
    if preferences.GetBool("ExportParasolid",False):
        FreeCAD.addExportType("Parasolid-XT (CAD Exchanger) (*.x_t, *.x_b, *.xmt_txt, *.xmt_bin)","CADExchangerIO")
    if preferences.GetBool("ImportJt",False):
        FreeCAD.addImportType("JT (CAD Exchanger) (*.jt)","CADExchangerIO")
    if preferences.GetBool("ExportJt",False):
        FreeCAD.addExportType("JT (CAD Exchanger) (*.jt)","CADExchangerIO")
    if preferences.GetBool("ImportRhino",False):
        FreeCAD.addImportType("Rhino (CAD Exchanger) (*.3dm)","CADExchangerIO")
    if preferences.GetBool("ExportRhino",False):
        FreeCAD.addExportType("Rhino (CAD Exchanger) (*.3dm)","CADExchangerIO")
    if preferences.GetBool("ImportObj",False):
        FreeCAD.addImportType("Wavefromt OBJ (CAD Exchanger) (*.obj)","CADExchangerIO")
    if preferences.GetBool("ExportObj",False):
        FreeCAD.addExportType("Wavefront OBJ (CAD Exchanger) (*.obj)","CADExchangerIO")
    if preferences.GetBool("ImportStl",False):
        FreeCAD.addImportType("STL (CAD Exchanger) (*.stl)","CADExchangerIO")
    if preferences.GetBool("ExportStl",False):
        FreeCAD.addExportType("STL (CAD Exchanger) (*.stl)","CADExchangerIO")
    if preferences.GetBool("ImportVrml",False):
        FreeCAD.addImportType("VRML (CAD Exchanger) (*.wrl)","CADExchangerIO")
    if preferences.GetBool("ExportVrml",False):
        FreeCAD.addExportType("VRML (CAD Exchanger) (*.wrl)","CADExchangerIO")
#    if preferences.GetBool("ImportX3d",False):
#        FreeCAD.addImportType("X3D (CAD Exchanger) (*.x3d)","CADExchangerIO")
    if preferences.GetBool("ExportX3d",False):
        FreeCAD.addExportType("X3D (CAD Exchanger) (*.x3d)","CADExchangerIO")
