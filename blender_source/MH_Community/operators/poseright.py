#!/usr/bin/python
# -*- coding: utf-8 -*-

import bpy
from ..rig import RigInfo


class MHC_OT_PoseRightOperator(bpy.types.Operator):
    """This is a diagnostic operator, which poses both the capture & final armatures one frame at a time."""
    bl_idname = 'mh_community.pose_right'
    bl_label = '1 Right'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..mocap.sensor_runtime import Sensor

        armature = context.object
        rigInfo = RigInfo.determineRig(armature)
        Sensor.oneRight(rigInfo, context.scene.MhSensorAnimation_index)
        return {'FINISHED'}
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @classmethod
    def poll(cls, context):
        ob = context.object
        if ob is None or ob.type != 'ARMATURE': return False

        # can now assume ob is an armature
        rigInfo = RigInfo.determineRig(ob)
        if rigInfo is None or not rigInfo.isMocapCapable() or rigInfo.hasIKRigs(): return False

        return len(context.scene.MhSensorAnimations) > 0
