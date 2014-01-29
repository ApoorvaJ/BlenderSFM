
bl_info = {
    "name": "BlenderSFM",
    "author": "Apoorva Joshi",
    "version": (0, 1),
    "blender": (2, 6, 9),
    "location": "View3D > Add > Mesh",
    "description": "Construct point cloud from photographs",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Add Mesh"}

if "bpy" in locals():
    import imp
    imp.reload(PointCloud)
else:
    from blenderSFM import PointCloud

import bpy
import sys

################################################################################
##### REGISTER #####

def add_mesh_point_cloud(self, context):
    self.layout.operator(PointCloud.add_mesh_point_cloud.bl_idname, text="Point Cloud", icon="GROUP_VERTEX")


def register():
    bpy.utils.register_module(__name__)

    bpy.types.INFO_MT_mesh_add.append(add_mesh_point_cloud)
    #bpy.types.VIEW3D_PT_tools_objectmode.prepend(add_mesh_point_cloud) #just for testing

def unregister():
    bpy.utils.unregister_module(__name__)

    bpy.types.INFO_MT_mesh_add.remove(add_mesh_point_cloud)
    #bpy.types.VIEW3D_PT_tools_objectmode.remove(add_mesh_point_cloud) #just for testing
    
if __name__ == "__main__":
    register()
