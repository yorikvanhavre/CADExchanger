## CadExchanger addon for FreeCAD

This addons allows [FreeCAD](http//www.freecadweb.org) to import and export to several additional file formats supported by the [CadExchanger](http://cadexchanger.com/) application. See the CadExchanger website for details on support of these formats.

CadExchanger is a paid application, it must be purchased on their website (a free 30-day evaluation is available). It allows to import and export to several commercial file formats into/from FreeCAD.

This addon can be installed via FreeCAD's addon manager, available in FreeCAD in version 0.17 or via the (addons installer macro)[https://github.com/FreeCAD/FreeCAD-addons] for older versions.

It can also simply be installed manually by downloading and copying the contents of this repository into a "CadExchanger" folder inside your FreeCAD/Mod directory.

Once this addon is installed, and CadExchanger installed on your system, you can access its preference page from FreeCAD, menu Edit->Preferences->Import/Export>CadExchanger. You must then set the path to your ExchangerConv or ExchangerConv.exe executable for the plugin to work. You can also choose which file extension will be enabled.

On opening a CadExchanger-supported file, the ExchangerConv will be ran to convert the given file into a brep file, which is OpenCasCade (and therefore FreeCAD's) native file format. This brep file is then loaded into FreeCAD. The same goes for export, the FreeCAd document is saved to the brep format and then converted to the desired file format.

CadExchanger supports several mesh-based formats as well (like OBJ and STL). Upon import, these meshes will also be turned into brep geometry.
