BlenderSFM
==========

BlenderSFM is an add-on for Blender that provides an easy way to perform Structure From Motion. 

The plugin takes as input, multiple photographs of an object or scene taken from different angles. It then generates 3D geometry by extracting depth information from these photographs.

The code behind this plugin is adapted from the Python Photogrammetry Toolkit.

The main goal behind this project is ease of installation and ease of use. Hence, I am integrating the existing SFM codebase with Blender.

Notes
-----

The project is currently at a very early stage in development. I will be adding features and refactoring the code in the coming weeks.

These are the main areas I will be focusing on:
- Developing a GUI. Currently the add-on takes photos from C:\sfminput and writes to C:\sfmoutput. Also, progress is only seen in the console window.
- Refactoring the code.
- Adding support for Linux. Currently, the code has only been tested on 32-bit Windows.
- Support for unknown camera profiles.
- A single zip file for installation.

Installation and Execution
--------------------------

1. Place the code into Blender's addon folder. e.g. C:\Program Files\Blender Foundation\Blender\2.69\scripts\addons\blenderSFM
2. Install Python 3.3
3. Install PIL for Python 3.3
4. Copy the PIL folder from Python 3.3's lib/site-packages to the addon folder
5. Create a C:\sfminput folder with the input photos. The photos need to be taken by a known camera profile. These sample images work: https://github.com/TheFrenchLeaf/Bundler/tree/master/examples
6. Create an empty folder C:\sfmoutput
7. Run Blender as administrator, enable the addon "BlenderSFM"
8. Window -> Toggle System Console
9. Add -> Mesh -> Point Cloud