## CADExchanger Addon for FreeCAD

This addon allows [FreeCAD](https://www.freecadweb.org) to import and export to all the commercial CAD file formats supported by [CADExchanger](https://cadexchanger.com/).

![screenshot](https://forum.freecadweb.org/download/file.php?id=37230)

## Description
[CADExchanger](https://cadexchanger.com) is a multi-platform (Windows, MacOS and Linux) commercial, paid application, it must be purchased on their website (a free 30-day evaluation is available). This add-on uses CADEXchanger under the hood to allow FreeCAD to open, import and export to several commercial file formats such as Solidworks, Catia, Siemens NX, Autodesk DWG and many more. See the full list of [supported file formats](https://cadexchanger.com/formats).

## Installation
1. Download and install the 30-day trial version of the [CADExchanger GUI application](https://cadexchanger.com/products/gui) or buy a license
2. Install this add-on via the FreeCAD [Addons Manager](https://wiki.freecadweb.org/Std_AddonMgr) found under menu *Tools -> Addons Manager*
3. Restart FreeCAD
4. Under menu *Edit -> Preferences -> Import/Export -> CADExchanger*, set the correct path to your ExchangerConv (Linux and MacOS) or ExchangerConv.exe (Windows) file that is bundled together with the CADExchanger GUI application
5. Restart FreeCAD once again to see the new file formats added to *File -> Open*, *File -> Import* and *File -> Export* menus

## Usage
On opening or importing a CADExchanger-supported file, the `ExchangerConv` utility will be run to convert the given file into a BREP file, which is OpenCasCade (and therefore FreeCAD's) native geometry format. This BREP file is then loaded into FreeCAD. The same goes for export, the FreeCAD document is saved to a BREP file and then converted to the desired file format using `ExchangerConv`.

CADExchanger supports several mesh-based formats as well (like OBJ and STL). Upon import, these meshes will also be turned into BREP geometry.

### Troubleshooting

When you run any of the CADExchanger supported operations (open, import or export), you will see in the report window of FreeCAD a line like this:

```
executing /home/yorik/cadexchanger/bin/exchangerconv -i /tmp/tmpc0fkp6e8.brep -e /home/yorik/test.obj
```

If you see the "Error during CADExchanger conversion" message, it is because running that command did not run successfully. If CADExchanger printed any error message, you will see it below the above message. 

You can run the above command (everything after the "executing" word) manually in a terminal window, This can give you additional error messages and a better idea of why the command failed.

Running `/home/yorik/cadexchanger/bin/exchangerconv`alone, without arguments, will print a help text and show you the available options.



## Feedback
Further discussions about this Addon will get better exposure when posting to its [dedicated FreeCAD forum thread](https://forum.freecadweb.org/viewtopic.php?f=9&t=22227&p=462421). Please include version of FreeCAD and make sure you are running the most up to date version of the Addon.

## Developer
Yorik Van Havre AKA [@yorikvanhavre](http://github.com/yorikvanhavre)

## License

This add-on is licensed under the [LGPL2+](LICENSE.md) terms, but the CADExchanger application is not part of this license and uses its own [commercial license](https://cadexchanger.com/blog/cad-exchanger-gui-licensing-explained) terms.

 
