#
#  FOV Sphere by Lofty   (This is designed for use with a SPHERE object.)
# 
#      This add-on is used to calculate the correct Reprojection (Full)
#      FOV_Y import method parameters by comparing the data from two imports,
#      a Base and a Test. Follow the numbered steps to reach the final values.
#

import bpy
from bpy import context
import mathutils
from mathutils import *
from math import *
from bpy.props import (BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       )
from bpy.types import (PropertyGroup,
                       Panel,
                       Operator,
                       )

bl_info = {
    "name": "FoV Sphere",
    "blender": (2, 80, 0),
    "category": "Object",
    "author": "Lofty",
    "version": (1, 3),
    "description": "Determines the FoV_Y and Width import values for a Sphere Object",
}

#
##  Global Defines Section
##      Not good practice, but I am tired.
#

v_precise = 6

class FOVProperties(bpy.types.PropertyGroup):

    @classmethod
    def poll(cls, context): 
        obj = context.active_object
        return obj is not None and obj.type == 'MESH'

#
##  Common Section
#

    ns_gray : bpy.props.FloatVectorProperty(name= "", size= 4, default= (0.185, 0.185, 0.185, 1.0))
    ns_green : bpy.props.FloatVectorProperty(name= "", size= 4, default= (0.0, 1.0, 0.0, 1.0))
    ns_red : bpy.props.FloatVectorProperty(name= "", size= 4, default= (1.0, 0.0, 0.0, 1.0))
    ns_yellow : bpy.props.FloatVectorProperty(name= "", size= 4, default= (1.0, 1.0, 0.0, 1.0))

#
##  FoV Section
#
    def changeBaseFoV(self, context):
        scene = context.scene
        fovtool = scene.fov_tool

        fovtool.base_fov_bool = True

        if not fovtool.fov_expert_bool:
            ob = context.active_object
            fovtool.base_y_float = ob.dimensions[1]
            fovtool.base_z_float = ob.dimensions[2]
            fovtool.base_yz_bool = True


    def changeTestFoV(self, context):
        scene = context.scene
        fovtool = scene.fov_tool

        fovtool.test_fov_bool = True

        if not fovtool.fov_expert_bool:
            ob = context.active_object
            fovtool.test_y_float = ob.dimensions[1]
            fovtool.test_y_bool = True

    def copyFinalFoV(self, context):
        scene = context.scene
        fovtool = scene.fov_tool

        if not fovtool.hold_fov_bool and not fovtool.final_fov_bool:
            fovtool.hold_fov_bool = True
        elif fovtool.hold_fov_bool and not fovtool.final_fov_bool:
            fovtool.final_fov_bool = True


    base_fov_float : bpy.props.FloatProperty(name= "2. Enter Base FoV_Y", precision= v_precise, update= changeBaseFoV,
                                             min= 1.0, max= 360.0, default= 45.0)
    base_y_float : bpy.props.FloatProperty(name= "Base Y", default= 0.00, precision= v_precise)
    base_z_float : bpy.props.FloatProperty(name= "Base Z", default= 0.00, precision= v_precise)
    test_fov_float : bpy.props.FloatProperty(name= "5. Enter Test FoV_Y", precision= v_precise, update= changeTestFoV,
                                             min= 1.0, max= 360.0, default= 30.0)
    test_y_float : bpy.props.FloatProperty(name= "Test Y", default= 0.0, precision= v_precise)
    final_fov_float : bpy.props.FloatProperty(name= "8. Final FoV_Y", precision= v_precise, update= copyFinalFoV,
                                             min= 1.0, max= 360.0, default= 0.0)

    fov_expert_bool : bpy.props.BoolProperty(name= "Expert", default= False)
    base_fov_import_bool : bpy.props.BoolProperty(name= "", default= False)
    base_fov_bool : bpy.props.BoolProperty(name= "", default= False)
    base_yz_bool : bpy.props.BoolProperty(name= "", default= False)
    test_fov_import_bool : bpy.props.BoolProperty(name= "", default= False)
    test_fov_bool : bpy.props.BoolProperty(name= "", default= False)
    test_y_bool : bpy.props.BoolProperty(name= "", default= False)
    calc_fov_bool : bpy.props.BoolProperty(name= "", default= False)
    hold_fov_bool : bpy.props.BoolProperty(name= "", default= False)
    final_fov_bool : bpy.props.BoolProperty(name= "", default= False)

#
##  Width Section
#
    def changeBaseWidth(self, context):
        scene = context.scene
        fovtool = scene.fov_tool

        fovtool.base_width_bool = True

        if not fovtool.fov_expert_bool:
            ob = context.active_object
            fovtool.base_x_float = ob.dimensions[0]
            fovtool.base_x_bool = True


    def changeTestWidth(self, context):
        scene = context.scene
        fovtool = scene.fov_tool

        fovtool.test_width_bool = True

        if not fovtool.fov_expert_bool:
            ob = context.active_object
            fovtool.test_x_float = ob.dimensions[0]
            fovtool.test_z_float = ob.dimensions[2]
            fovtool.test_xz_bool = True


    def copyFinalWidth(self, context):
        scene = context.scene
        fovtool = scene.fov_tool

        if not fovtool.hold_width_bool and not fovtool.final_width_bool:
            fovtool.hold_width_bool = True
        elif fovtool.hold_width_bool and not fovtool.final_width_bool:
            fovtool.final_width_bool = True


    base_width_float : bpy.props.FloatProperty(name= "10. Enter Base Width", precision= v_precise, update= changeBaseWidth,
                                             min= 1.0, soft_max= 8192.0, default= 0.0)
    base_x_float : bpy.props.FloatProperty(name= "Base X", default= 0.00, precision= v_precise)
    test_width_float : bpy.props.FloatProperty(name= "13. Enter Test Width", precision= v_precise, update= changeTestWidth,
                                             min= 1.0, soft_max= 8192.0, default= 0.0)
    test_x_float : bpy.props.FloatProperty(name= "Test X", default= 0.0, precision= v_precise)
    test_z_float : bpy.props.FloatProperty(name= "Test Z", default= 0.00, precision= v_precise)
    final_width_float : bpy.props.FloatProperty(name= "16. Final Width", precision= v_precise, update= copyFinalWidth,
                                             min= 1.0, soft_max= 8192.0, default= 0.0)
    
    base_width_import_bool : bpy.props.BoolProperty(name= "", default= False)
    base_width_bool : bpy.props.BoolProperty(name= "", default= False)
    base_x_bool : bpy.props.BoolProperty(name= "", default= False)
    test_width_import_bool : bpy.props.BoolProperty(name= "", default= False)
    test_width_bool : bpy.props.BoolProperty(name= "", default= False)
    test_xz_bool : bpy.props.BoolProperty(name= "", default= False)
    calc_width_bool : bpy.props.BoolProperty(name= "", default= False)
    hold_width_bool : bpy.props.BoolProperty(name= "", default= False)
    final_width_bool : bpy.props.BoolProperty(name= "", default= False)


#
##
### FoV Panel
##
#

class FOV_PT_fov_panel(bpy.types.Panel):
    bl_label = "FoV_Y Calculator"
    bl_idname = "FOV_PT_fov_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "FoV Sphere"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        fovtool = scene.fov_tool
        layout.use_property_decorate = False  # No animation.

        box = layout.box()
        row = box.row()
        layout.use_property_split = False
        row.alignment = 'RIGHT'
        row.enabled = True
        row.prop(fovtool, "fov_expert_bool", text="Expert Mode")

        countRow = 1
#        labelRow = str(countRow) + ". Do 1st FoV_Y Import (Reset)"
        row = box.row()
        layout.use_property_split = False
        row.alignment = 'LEFT'
        row.enabled = True
        if fovtool.base_fov_import_bool and not fovtool.base_fov_bool:
            row.template_node_socket(color=(fovtool.ns_yellow))
        else:
            row.template_node_socket(color=(fovtool.ns_gray))
        row.operator("fovcalc.fov_baseimport", text="{}. Do 1st FoV_Y Import (Reset)".format(countRow))
#        row.operator("fovcalc.fov_baseimport", text=labelRow)

        countRow += 1
        labelRow = str(countRow) + ". Enter FoV_Y used"
        row = box.row()
        layout.use_property_split = False
        row.alignment = 'LEFT'
        row.enabled = fovtool.base_fov_import_bool
        if fovtool.fov_expert_bool:
            if fovtool.base_fov_bool and not fovtool.base_yz_bool:
                row.template_node_socket(color=(fovtool.ns_yellow))
            else:
                row.template_node_socket(color=(fovtool.ns_gray))
        else:
            if fovtool.base_fov_bool and not fovtool.test_fov_import_bool:
                row.template_node_socket(color=(fovtool.ns_yellow))
            else:
                row.template_node_socket(color=(fovtool.ns_gray))
        row.prop(fovtool, "base_fov_float", text=labelRow)

        if fovtool.fov_expert_bool:
            countRow += 1
            labelRow = str(countRow) + ". Record mesh data"
            row = box.row()
            row.use_property_split = False
            row.alignment = 'LEFT'
            row.enabled = fovtool.base_fov_bool
            if fovtool.base_yz_bool and not fovtool.test_fov_import_bool:
                row.template_node_socket(color=(fovtool.ns_yellow))
            else:
                row.template_node_socket(color=(fovtool.ns_gray))
            row.operator("fovcalc.fov_getbaseyz", text=labelRow)

            row = box.row()
            row.use_property_split = True
    #        row.alignment = 'LEFT'
            if fovtool.fov_expert_bool:
                row.enabled = fovtool.base_fov_bool
            else:
                row.enabled = False
            row.template_node_socket(color=(fovtool.ns_gray))
            row.prop(fovtool, "base_y_float")

            row = box.row()
            row.use_property_split = True
    #        row.alignment = 'LEFT'
            if fovtool.fov_expert_bool:
                row.enabled = fovtool.base_fov_bool
            else:
                row.enabled = False
            row.template_node_socket(color=(fovtool.ns_gray))
            row.prop(fovtool, "base_z_float")

        countRow += 1
        labelRow = str(countRow) + ". Do 2nd FoV_Y Import"
        row = box.row()
        layout.use_property_split = False
        row.alignment = 'LEFT'
        row.enabled = fovtool.base_yz_bool
        if fovtool.test_fov_import_bool and not fovtool.test_fov_bool:
            row.template_node_socket(color=(fovtool.ns_yellow))
        else:
            row.template_node_socket(color=(fovtool.ns_gray))
        row.operator("fovcalc.fov_testimport", text=labelRow)

        countRow += 1
        labelRow = str(countRow) + ". Enter FoV_Y used"
        row = box.row()
        row.use_property_split = False
        row.alignment = 'LEFT'
        row.enabled = fovtool.test_fov_import_bool
        if fovtool.fov_expert_bool:
            if fovtool.test_fov_bool and not fovtool.test_y_bool:
                row.template_node_socket(color=(fovtool.ns_yellow))
            else:
                row.template_node_socket(color=(fovtool.ns_gray))
        else:
            if fovtool.test_fov_bool and not fovtool.calc_fov_bool:
                row.template_node_socket(color=(fovtool.ns_yellow))
            else:
                row.template_node_socket(color=(fovtool.ns_gray))
        row.prop(fovtool, "test_fov_float", text=labelRow)

        if fovtool.fov_expert_bool:
            countRow += 1
            labelRow = str(countRow) + ". Record mesh data"
            row = box.row()
            row.use_property_split = False
            row.alignment = 'LEFT'
            row.enabled = fovtool.test_fov_bool
            if fovtool.test_y_bool and not fovtool.calc_fov_bool:
                row.template_node_socket(color=(fovtool.ns_yellow))
            else:
                row.template_node_socket(color=(fovtool.ns_gray))
            row.operator("fovcalc.fov_gettesty", text=labelRow)

            row = box.row()
            row.use_property_split = True
    #        row.alignment = 'LEFT'
            if fovtool.fov_expert_bool:
                row.enabled = fovtool.test_fov_bool
            else:
                row.enabled = False
            row.template_node_socket(color=(fovtool.ns_gray))
            row.prop(fovtool, "test_y_float")

        countRow += 1
        labelRow = str(countRow) + ". Do FoV_Y Calculation"
        row = box.row()
        row.use_property_split = False
        row.alignment = 'LEFT'
        row.enabled = fovtool.test_y_bool
        if fovtool.calc_fov_bool and not fovtool.final_fov_bool:
            row.template_node_socket(color=(fovtool.ns_yellow))
        else:
            row.template_node_socket(color=(fovtool.ns_gray))
        row.operator("fovcalc.fov_calculator", text=labelRow)

        countRow += 1
        labelRow = str(countRow) + ". Correct FoV_Y"
        row = box.row()
        row.use_property_split = False
        row.alignment = 'LEFT'
        row.enabled = fovtool.calc_fov_bool
        if fovtool.calc_fov_bool:
            row.template_node_socket(color=(fovtool.ns_green))
        else:
            row.template_node_socket(color=(fovtool.ns_red))
        row.prop(fovtool, "final_fov_float", text=labelRow)

class FOV_OT_BaseImport(bpy.types.Operator):
    """Do an import with the first FoV value
to be used in the calculation."""
    bl_label = "Do 1st FoV_Y Import (Reset)"
    bl_idname = "fovcalc.fov_baseimport"

    @classmethod
    def poll(cls, context): 
        obj = context.active_object
        return obj is not None and obj.type == 'MESH'

    def execute(self, context):
        scene = context.scene
        fovtool = scene.fov_tool

#        fovtool.base_fov_float = 45.0
        fovtool.base_y_float = 0.0
        fovtool.base_z_float = 0.0
#        fovtool.test_fov_float = 30.0
        fovtool.test_y_float = 0.0
        fovtool.final_fov_float = 0.0
        fovtool.final_width_float = 0.0
        
        fovtool.base_fov_import_bool = True
        fovtool.base_fov_bool = False
        fovtool.base_yz_bool = False
        fovtool.test_fov_import_bool = False
        fovtool.test_fov_bool = False
        fovtool.test_y_bool = False
        fovtool.calc_fov_bool = False
        fovtool.hold_fov_bool = False
        fovtool.final_fov_bool = False

#        fovtool.base_width_float = 1024.0
        fovtool.base_x_float = 0.0
#        fovtool.test_width_float = 768.0
        fovtool.test_x_float = 0.0
        fovtool.final_width_float = 0.0
        
        fovtool.base_width_import_bool = False
        fovtool.base_width_bool = False
        fovtool.base_x_bool = False
        fovtool.test_width_import_bool = False
        fovtool.test_width_bool = False
        fovtool.test_xz_bool = False
        fovtool.calc_width_bool = False
        fovtool.hold_width_bool = False
        fovtool.final_width_bool = False
        
        return {'FINISHED'}


class FOV_OT_getbaseYZ(bpy.types.Operator):
    """Gets the Y and Z dimensions of the Base object."""
    bl_label = "3. Get Base YZ"
    bl_idname = "fovcalc.fov_getbaseyz"

    @classmethod
    def poll(cls, context): 
        obj = context.active_object
        return obj is not None and obj.type == 'MESH'

    def execute(self, context):
        scene = context.scene
        fovtool = scene.fov_tool

        ob = context.active_object

        fovtool.base_y_float = ob.dimensions[1]
        fovtool.base_z_float = ob.dimensions[2]
        
        fovtool.base_yz_bool = True

        return {'FINISHED'}


class FOV_OT_TestImport(bpy.types.Operator):
    """Second half of FoV process."""
    bl_label = "4. 2nd Import - Test"
    bl_idname = "fovcalc.fov_testimport"

    @classmethod
    def poll(cls, context): 
        obj = context.active_object
        return obj is not None and obj.type == 'MESH'

    def execute(self, context):
        scene = context.scene
        fovtool = scene.fov_tool

        fovtool.test_fov_import_bool = True
        
        return {'FINISHED'}


class FOV_OT_gettestY(bpy.types.Operator):
    """Gets the Y dimension of the Test object."""
    bl_label = "6. Get Test Y"
    bl_idname = "fovcalc.fov_gettesty"

    @classmethod
    def poll(cls, context): 
        obj = context.active_object
        return obj is not None and obj.type == 'MESH'

    def execute(self, context):
        scene = context.scene
        fovtool = scene.fov_tool

        ob = context.active_object

        fovtool.test_y_float = ob.dimensions[1]

        fovtool.test_y_bool = True

        return {'FINISHED'}


class FOV_OT_calc(bpy.types.Operator):
    """Calculates the correct FoV_Y value from two sample FoV_Y imports."""
    bl_label = "7. Calculate FoV_Y"
    bl_idname = "fovcalc.fov_calculator"

    @classmethod
    def poll(cls, context): 
        obj = context.active_object
        return obj is not None and obj.type == 'MESH'

    def execute(self, context):
        scene = context.scene
        fovtool = scene.fov_tool

        ob = context.active_object

        FOV_Base = fovtool.base_fov_float
        BASE_Y = fovtool.base_y_float
        BASE_Z = fovtool.base_z_float

        FOV_Test = fovtool.test_fov_float
        TEST_Y = fovtool.test_y_float

        zdepth = 0
        if FOV_Base > 0 and FOV_Test > 0 and not BASE_Y == TEST_Y:
            zdepth = ((BASE_Y / 2) / tan(radians(FOV_Base /  2)) + \
                      (TEST_Y / 2) / tan(radians(FOV_Test /  2))) / 2
        FOV_Final = 0
        if zdepth > 0:
            FOV_Final = degrees(atan((BASE_Z / 2) / zdepth) * 2)

        if FOV_Final > 0:
            fovtool.final_fov_float = FOV_Final
            fovtool.calc_fov_bool = True
        else:
            fovtool.final_fov_float = -1
            fovtool.calc_fov_bool = False

        return {'FINISHED'}


#
##
### Width Panel
##
#

class WIDTH_PT_width_panel(bpy.types.Panel):
    bl_label = "Width Calculator"
    bl_idname = "WIDTH_PT_width_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "FoV Sphere"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        fovtool = scene.fov_tool
        layout.use_property_decorate = False  # No animation.

        if fovtool.fov_expert_bool:
            countRow = 9
        else:
            countRow = 7
        labelRow = str(countRow) + ". Do 1st Width Import (Reset)"
        box = layout.box()
        row = box.row()
        layout.use_property_split = False
        row.alignment = 'LEFT'
        row.enabled = fovtool.final_fov_bool
        if fovtool.base_width_import_bool and not fovtool.base_width_bool:
            row.template_node_socket(color=(fovtool.ns_yellow))
        else:
            row.template_node_socket(color=(fovtool.ns_gray))
        row.operator("fovcalc.width_base_import", text=labelRow)

        countRow += 1
        labelRow = str(countRow) + ". Enter Width used"
        row = box.row()
        layout.use_property_split = False
        row.alignment = 'LEFT'
        row.enabled = fovtool.base_width_import_bool
        if fovtool.fov_expert_bool:
            if fovtool.base_width_bool and not fovtool.base_x_bool:
                row.template_node_socket(color=(fovtool.ns_yellow))
            else:
                row.template_node_socket(color=(fovtool.ns_gray))
        else:
            if fovtool.base_width_bool and not fovtool.test_width_import_bool:
                row.template_node_socket(color=(fovtool.ns_yellow))
            else:
                row.template_node_socket(color=(fovtool.ns_gray))
        row.prop(fovtool, "base_width_float", text=labelRow)

        if fovtool.fov_expert_bool:
            countRow += 1
            labelRow = str(countRow) + ". Record mesh data"
            row = box.row()
            row.use_property_split = False
            row.alignment = 'LEFT'
            row.enabled = fovtool.base_width_bool
            if fovtool.base_x_bool and not fovtool.test_width_import_bool:
                row.template_node_socket(color=(fovtool.ns_yellow))
            else:
                row.template_node_socket(color=(fovtool.ns_gray))
            row.operator("fovcalc.width_getbasex", text=labelRow)

            row = box.row()
            row.use_property_split = True
    #        row.alignment = 'LEFT'
            if fovtool.fov_expert_bool:
                row.enabled = fovtool.base_width_bool
            else:
                row.enabled = False
            row.template_node_socket(color=(fovtool.ns_gray))
            row.prop(fovtool, "base_x_float")

        countRow += 1
        labelRow = str(countRow) + ". Do 2nd Width Import"
        row = box.row()
        layout.use_property_split = False
        row.alignment = 'LEFT'
        row.enabled = fovtool.base_x_bool
        if fovtool.test_width_import_bool and not fovtool.test_width_bool:
            row.template_node_socket(color=(fovtool.ns_yellow))
        else:
            row.template_node_socket(color=(fovtool.ns_gray))
        row.operator("fovcalc.width_testimport", text=labelRow)

        countRow += 1
        labelRow = str(countRow) + ". Enter Width used"
        row = box.row()
        row.use_property_split = False
        row.alignment = 'LEFT'
        row.enabled = fovtool.test_width_import_bool
        if fovtool.fov_expert_bool:
            if fovtool.test_width_bool and not fovtool.test_xz_bool:
                row.template_node_socket(color=(fovtool.ns_yellow))
            else:
                row.template_node_socket(color=(fovtool.ns_gray))
        else:
            if fovtool.test_width_bool and not fovtool.calc_width_bool:
                row.template_node_socket(color=(fovtool.ns_yellow))
            else:
                row.template_node_socket(color=(fovtool.ns_gray))
        row.prop(fovtool, "test_width_float", text=labelRow)

        if fovtool.fov_expert_bool:
            countRow += 1
            labelRow = str(countRow) + ". Record mesh data"
            row = box.row()
            row.use_property_split = False
            row.alignment = 'LEFT'
            row.enabled = fovtool.test_width_bool
            if fovtool.test_xz_bool and not fovtool.calc_width_bool:
                row.template_node_socket(color=(fovtool.ns_yellow))
            else:
                row.template_node_socket(color=(fovtool.ns_gray))
            row.operator("fovcalc.width_gettestxz", text=labelRow)

            row = box.row()
            row.use_property_split = True
    #        row.alignment = 'LEFT'
            if fovtool.fov_expert_bool:
                row.enabled = fovtool.test_width_bool
            else:
                row.enabled = False
            row.template_node_socket(color=(fovtool.ns_gray))
            row.prop(fovtool, "test_x_float")

            row = box.row()
            row.use_property_split = True
    #        row.alignment = 'LEFT'
            if fovtool.fov_expert_bool:
                row.enabled = fovtool.test_width_bool
            else:
                row.enabled = False
            row.template_node_socket(color=(fovtool.ns_gray))
            row.prop(fovtool, "test_z_float")

        countRow += 1
        labelRow = str(countRow) + ". Do Width Calculation"
        row = box.row()
        row.use_property_split = False
        row.alignment = 'LEFT'
        row.enabled = fovtool.test_xz_bool
        if fovtool.calc_width_bool and not fovtool.final_width_bool:
            row.template_node_socket(color=(fovtool.ns_yellow))
        else:
            row.template_node_socket(color=(fovtool.ns_gray))
        row.operator("fovcalc.width_calculator", text=labelRow)

        countRow += 1
        labelRow = str(countRow) + ". Correct Width"
        row = box.row()
        row.use_property_split = False
        row.alignment = 'LEFT'
        row.enabled = fovtool.calc_width_bool
        if fovtool.calc_width_bool:
            row.template_node_socket(color=(fovtool.ns_green))
        else:
            row.template_node_socket(color=(fovtool.ns_red))
        row.prop(fovtool, "final_width_float", text=labelRow)


class WIDTH_OT_BaseImport(bpy.types.Operator):
    """Beginning of Width process."""
    bl_label = "9. 3rd Import - Base (Reset)"
    bl_idname = "fovcalc.width_base_import"

    @classmethod
    def poll(cls, context): 
        obj = context.active_object
        return obj is not None and obj.type == 'MESH'

    def execute(self, context):
        scene = context.scene
        fovtool = scene.fov_tool

#        fovtool.base_width_float = 1024.0
        fovtool.base_x_float = 0.0
#        fovtool.test_width_float = 768.0
        fovtool.test_x_float = 0.0
        fovtool.test_z_float = 0.0
        fovtool.final_width_float = 0.0
        
        fovtool.base_width_import_bool = True
        fovtool.base_width_bool = False
        fovtool.base_x_bool = False
        fovtool.test_width_import_bool = False
        fovtool.test_width_bool = False
        fovtool.test_xz_bool = False
        fovtool.calc_width_bool = False
        fovtool.hold_width_bool = False
        fovtool.final_width_bool = False

        return {'FINISHED'}


class WIDTH_OT_getbaseX(bpy.types.Operator):
    """Gets the X dimension of the Base object."""
    bl_label = "11. Get Base X"
    bl_idname = "fovcalc.width_getbasex"

    @classmethod
    def poll(cls, context): 
        obj = context.active_object
        return obj is not None and obj.type == 'MESH'

    def execute(self, context):
        scene = context.scene
        fovtool = scene.fov_tool

        ob = context.active_object
        fovtool.base_x_float = ob.dimensions[0]
        fovtool.base_x_bool = True

        return {'FINISHED'}


class WIDTH_OT_TestImport(bpy.types.Operator):
    """Second half of Width process."""
    bl_label = "12. 4th Import - Test"
    bl_idname = "fovcalc.width_testimport"

    @classmethod
    def poll(cls, context): 
        obj = context.active_object
        return obj is not None and obj.type == 'MESH'

    def execute(self, context):
        scene = context.scene
        fovtool = scene.fov_tool

        fovtool.test_width_import_bool = True
        
        return {'FINISHED'}


class WIDTH_OT_gettestXZ(bpy.types.Operator):
    """Gets the X and Z dimension of the Test object."""
    bl_label = "14. Get Test XZ"
    bl_idname = "fovcalc.width_gettestxz"

    @classmethod
    def poll(cls, context): 
        obj = context.active_object
        return obj is not None and obj.type == 'MESH'

    def execute(self, context):
        scene = context.scene
        fovtool = scene.fov_tool

        ob = context.active_object
        fovtool.test_x_float = ob.dimensions[0]
        fovtool.test_z_float = ob.dimensions[2]
        fovtool.test_xz_bool = True

        return {'FINISHED'}


class WIDTH_OT_calc(bpy.types.Operator):
    """Calculates the correct Width value from two sample width imports using the correct FoV_Y."""
    bl_label = "15. Calculate Width"
    bl_idname = "fovcalc.width_calculator"

    @classmethod
    def poll(cls, context): 
        obj = context.active_object
        return obj is not None and obj.type == 'MESH'


    def execute(self, context):
        scene = context.scene
        fovtool = scene.fov_tool

        ob = context.active_object

        BASE_Width = fovtool.base_width_float
        BASE_X = fovtool.base_x_float

        TEST_Width = fovtool.test_width_float
        TEST_X = fovtool.test_x_float
        TEST_Z = fovtool.test_z_float

        WIDE_Diff = BASE_Width - TEST_Width
        BASE_Diff = BASE_X - TEST_Z
        TEST_Diff = BASE_X - TEST_X
        try:
            PERC_Chng = (TEST_Diff / BASE_Diff) * 100
        except:
            PERC_Chng = 0.0
        PERC_Offs = 100 - PERC_Chng
        try:
            WIDE_Final = TEST_Width - ((WIDE_Diff * PERC_Offs) / PERC_Chng)
        except:
            WIDE_Final = -1.0

        if WIDE_Final > 0:
            fovtool.final_width_float = WIDE_Final
            fovtool.calc_width_bool = True
        else:
            fovtool.final_width_float = -1
            fovtool.calc_width_bool = False


        return {'FINISHED'}

#
##  List of items for register and unregister
#
classes = [ FOVProperties,
            FOV_PT_fov_panel,
            FOV_OT_BaseImport,
            FOV_OT_getbaseYZ,
            FOV_OT_TestImport,
            FOV_OT_gettestY,
            FOV_OT_calc,
            WIDTH_PT_width_panel,
            WIDTH_OT_BaseImport,
            WIDTH_OT_getbaseX,
            WIDTH_OT_TestImport,
            WIDTH_OT_gettestXZ,
            WIDTH_OT_calc]


def register():

    for cls in classes:
        bpy.utils.register_class(cls)
        
    bpy.types.Scene.fov_tool = bpy.props.PointerProperty(type= FOVProperties)
 
def unregister():

    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.fov_tool
 
if __name__ == "__main__":
    register()
