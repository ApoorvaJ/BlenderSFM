<p align="center">
  <img src="http://thegamecoder.com/wp-content/uploads/2014/02/BlenderSFMCircle.png" />
</p>

BlenderSFM
==========
BlenderSFM is an add-on for Blender 2.69 that provides an easy way to perform Structure From Motion. 

The plugin takes as input, multiple photographs of an object or scene taken from different angles. It then generates 3D geometry by extracting depth information from these photographs.

The code behind this plugin is adapted from the Python Photogrammetry Toolkit.

The main goal behind this project is ease of installation and ease of use. This is why, I am integrating the existing SFM codebase with Blender.

Notes
-----

The project is currently at a very early stage in development. I will be adding features and refactoring the code in the coming weeks.

These are the main areas I will be focusing on:
- Refactoring the code.
- Support for adding camera specs.

Installation and Execution
--------------------------

1. Download the project as ZIP, extract it and place the BlenderSFM-master folder in the Blender addons folder e.g. C:\Program Files\Blender Foundation\Blender\2.69\scripts\addons.
2. Rename the BlenderSFM-master folder to blenderSFM.
3. Run Blender as administrator, enable the addon "BlenderSFM" from the User Preferences menu (Ctrl + Alt + U)
4. Select the folder with the JPG photos in the SFM Panel in the Tools section, and click on Start SFM.
