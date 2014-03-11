import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import bpy
import subprocess
import threading
import queue
from time import sleep
import osmbundler
import osmcmvs

from bpy.props import *

import imp
imp.reload(osmbundler)
imp.reload(osmcmvs)

bpy.types.Scene.photoPath = StringProperty(
    name="Path to photos",
    subtype="DIR_PATH",
    description="Path to the folder containing the JPG photos"
    )

bpy.types.Scene.currentStatus = StringProperty(
    name="Current Status",
    description=""
    )

# ==================================================================================================
# The menu option Add->Mesh->Point Cloud
class StartSFMOperator(bpy.types.Operator):
    bl_idname = "sfm.start"
    bl_label = "Start SFM"
    bl_options = {'UNDO'}
    bl_description = "Start the Structure From Motion process to generate the point cloud"

    params = bpy.props.StringProperty() # defining the property

    status = " ";

    def execute(self, context):
        q = queue.Queue();
        thr = threading.Thread(target=self.foo, args=(context,q))
        thr.start()
        while (True):
            if not q.empty():
                message = q.get()
                context.scene.currentStatus = message
                self.__class__.status = context.scene.currentStatus
                self.report({'INFO'}, str(self.__class__.status))
                print(context.scene.currentStatus)
                if (message=="DONE"):
                    break
            sleep(1)
        
        return {'FINISHED'}

    def foo(self, context, q):
        pluginPath = os.path.dirname(os.path.realpath(__file__))
        absolutePhotoPath = os.path.abspath(bpy.path.abspath(context.scene.photoPath))

        print("params: " + self.params + absolutePhotoPath)

        photos = osmbundler.getPhotosFromDirectory(absolutePhotoPath)
        numberOfPhotos = photos.__len__()

        bundler = osmbundler.OsmBundler(pluginPath, absolutePhotoPath, "C:\sfmoutput", "siftvlfeat", 1200, 1)
        bundler.openFiles()

        for i in range(0, numberOfPhotos):
            # context.scene.currentStatus = "Processing photo {0} of {1}".format(i+1,numberOfPhotos)
            q.put("Processing photo {0} of {1}".format(i+1,numberOfPhotos))
            print("PUT")
            # self.report({'INFO'}, str(self.__class__.status))


            photoInfo = dict(dirname=absolutePhotoPath, basename=photos[i])
            bundler._preparePhoto(photoInfo)
            # thr1 = threading.Thread(target=bundler._preparePhoto, args=(photoInfo,))
            # thr1.start()
            # thr1.join()

        bundler.closeFiles()
        os.chdir("C:\\")
        print("DONE")
        q.put("DONE")


class OBJECT_PT_Panel(bpy.types.Panel):
    bl_idname = "mesh.point_cloud_add"
    bl_label = "Add Point Cloud"
    bl_description = "Generate a point cloud from photographs"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene, "photoPath")
        layout.operator("sfm.start")
        layout.label(context.scene.currentStatus)
        layout.label(StartSFMOperator.status)