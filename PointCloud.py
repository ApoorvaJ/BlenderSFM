import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import bpy
import subprocess
import threading
import osmbundler
import osmcmvs
from bpy.props import *

import imp
imp.reload(osmbundler)
imp.reload(osmcmvs)


##------------------------------------------------------------
class add_mesh_point_cloud(bpy.types.Operator):
    """"""
    bl_idname = "mesh.point_cloud_add"
    bl_label = "Add Point Cloud"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "Generate a point cloud from photographs"

    def startBundler(self):
        pluginPath = os.path.dirname(os.path.realpath(__file__))
        bundler = osmbundler.OsmBundler(pluginPath, "C:\sfminput", "C:\sfmoutput", "siftvlfeat", 1200, 1)
        bundler.preparePhotos()
        bundler.matchFeatures()
        bundler.doBundleAdjustment()
        # bundler.openResult()

        cmvs = osmcmvs.OsmCmvs(pluginPath, "C:\sfmoutput", 10)
        cmvs.doBundle2PMVS()
        cmvs.doCMVS()

        bpy.ops.import_mesh.ply(filepath="C:\sfmoutput\pmvs\models\option-0000.ply")
        

    ##### EXECUTE #####
    def execute(self, context):
        self.startBundler()
        return {'FINISHED'}
        
    ##### INVOKE #####
    def invoke(self, context, event):
        self.execute(context)
        return {'FINISHED'}