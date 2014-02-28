<p align="center">
  <img src="http://thegamecoder.com/wp-content/uploads/2014/02/BlenderSFMCircle.png" />
</p>

BlenderSFM
==========
BlenderSFM is an add-on for Blender that provides an easy way to perform Structure From Motion. 

The plugin takes as input, multiple photographs of an object or scene taken from different angles. It then generates 3D geometry by extracting depth information from these photographs.

The code behind this plugin is adapted from the Python Photogrammetry Toolkit.

The main goal behind this project is ease of installation and ease of use. This is why, I am integrating the existing SFM codebase with Blender.

Notes
-----

The project is currently at a very early stage in development. I will be adding features and refactoring the code in the coming weeks.

These are the main areas I will be focusing on:
- Developing a GUI. Currently the add-on takes photos from C:\sfminput and writes to C:\sfmoutput. Progress is only seen in the console window.
- Refactoring the code.
- Adding support for Linux. Currently, the code has only been tested on 32-bit Windows.
- Support for adding camera specs.

Installation and Execution
--------------------------

1. Download the project as ZIP, extract it and place the BlenderSFM-master folder in the Blender addons folder e.g. C:\Program Files\Blender Foundation\Blender\2.69\scripts\addons.
2. Rename the BlenderSFM-master folder to blenderSFM.
3. Create a C:\sfminput folder and place input photos inside this folder. Sample images: https://github.com/TheFrenchLeaf/Bundler/tree/master/examples
4. Create an empty folder C:\sfmoutput
5. Run Blender as administrator, enable the addon "BlenderSFM"
6. Window -> Toggle System Console
7. Add -> Mesh -> Point Cloud
