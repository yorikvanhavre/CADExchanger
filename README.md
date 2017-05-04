## CAD Exchanger addon for FreeCAD

![example](https://forum.freecadweb.org/download/file.php?id=37230)

This addons allows [FreeCAD](http//www.freecadweb.org) to import and export to several additional file formats supported by the [CAD Exchanger](http://cadexchanger.com/) application. See the CAD Exchanger website for details on support of these formats.

CAD Exchanger is a paid application, it must be purchased on their website (a free 30-day evaluation is available). It allows to import and export to several commercial file formats such as Rhino 3dm or ACIS sat into/from FreeCAD.

This addon can be installed via FreeCAD's addon manager, available in FreeCAD in version 0.17 or via the [addons installer macro](https://github.com/FreeCAD/FreeCAD-addons) for older versions.

It can also simply be installed manually by downloading and copying the contents of this repository into a "CADExchanger" folder inside your FreeCAD/Mod directory.

Once this addon is installed, and CAD Exchanger installed on your system, you can access its preference page from FreeCAD, menu Edit->Preferences->Import/Export>CAD Exchanger. You must then set the path to your ExchangerConv or ExchangerConv.exe executable for the plugin to work. You can also choose which file extension will be enabled.

On opening a CAD Exchanger-supported file, the ExchangerConv will be ran to convert the given file into a brep file, which is OpenCasCade (and therefore FreeCAD's) native file format. This brep file is then loaded into FreeCAD. The same goes for export, the FreeCAD document is saved to the brep format and then converted to the desired file format.

CAD Exchanger supports several mesh-based formats as well (like OBJ and STL). Upon import, these meshes will also be turned into brep geometry.
