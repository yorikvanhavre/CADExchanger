## CAD Exchanger Addon for FreeCAD

This addons allows [FreeCAD](https://www.freecadweb.org) to import and export to several additional file formats supported by the CAD Exchanger application (refer to the [CAD Exchanger](https://cadexchanger.com/) website for details on support of these formats).

![screenshot](https://forum.freecadweb.org/download/file.php?id=37230)

## Description
CAD Exchanger is a paid application, it must be purchased on their website (a free 30-day evaluation is available). It allows to import and export to several commercial file formats such as Rhino 3dm or ACIS sat into/from FreeCAD.

## Installation
This addon can be installed via FreeCAD's [Addon Manager](https://github.com/FreeCAD/FreeCAD-addons#installing) (available in FreeCAD >= v0.17) or via the [addons installer macro](https://github.com/FreeCAD/FreeCAD-addons) for older versions.

It can also simply be installed manually by downloading and copying the contents of this repository into a "CADExchanger" folder inside your ``~/FreeCAD/Mod` directory.

Once this addon is installed, and CAD Exchanger installed on your system, you can access its preference page from FreeCAD, menu `Edit > Preferences > Import/Export > CAD Exchanger`. You must then set the path to your `ExchangerConv` or `ExchangerConv.exe` executable for the plugin to work. You can also choose which file extension will be enabled.

## Usage
On opening a CAD Exchanger-supported file, the `ExchangerConv` will be run to convert the given file into a `brep` file, which is `OpenCasCade` (and therefore FreeCAD's) native file format. This `brep` file is then loaded into FreeCAD. The same goes for export, the FreeCAD document is saved to the `brep` format and then converted to the desired file format.

CAD Exchanger supports several mesh-based formats as well (like OBJ and STL). Upon import, these meshes will also be turned into brep geometry.

### Troubleshooting

When you run any of the cadexchanger supported operations, you will see in the report window of FreeCAD a line like this:

```
executing /home/yorik/cadexchanger/bin/exchangerconv -i /tmp/tmpc0fkp6e8.brep -e /home/yorik/test.obj
```

If you see the "Error during CAD Exchanger conversion" message, it is because running that command did return an error.
you can run that command (everything after the "executing" word) in a terminal, and see for yourself what happens.
You can also run it inside the python console of FreeCAD like this:

```
import subprocess
subprocess.call("/home/yorik/cadexchanger/bin/exchangerconv -i /tmp/tmpc0fkp6e8.brep -e /home/yorik/test.obj".split(" "))
```

if it returns 0, it means the command ran successfully.
But running in the terminal is better, because `subprocess.call` won't let you see the internal messages that `cadexchangerconv` prints, only the result.

This can give you a better idea of why `exchangerconv` failed.

## Feedback
Further discussions about this Addon will get better exposure when posting to its [dedicated FreeCAD forum thread](). Please include version of FreeCAD and make sure you are running the most up to date version of the Addon.

## Developer
Yorik Van Havre AKA [@yorikvanhavre](http://github.com/yorikvanhavre)

## License
