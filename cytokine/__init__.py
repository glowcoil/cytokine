import bpy

from . import ct

bl_info = {
    "name": "Cytokine",
    "author": "Micah Johnston",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "category": "Object"
}

class OutputProperty(bpy.types.PropertyGroup):
    bl_idname = "ct_OutputProperty"

    name: bpy.props.StringProperty()

class CytokineNodeTree(bpy.types.NodeTree):
    bl_idname = "ct_Cytokine"
    bl_icon = "MOD_DATA_TRANSFER"
    bl_label = "Cytokine"

    mesh: bpy.props.PointerProperty(type=bpy.types.Mesh)
    outputs: bpy.props.CollectionProperty(type=OutputProperty)

    def update(self):
        print("update")

    def compute(self):
        pass

class MeshSocket(bpy.types.NodeSocket):
    bl_idname = "ct_MeshSocket"
    bl_label = "mesh"

    def draw(self, context, layout, node, text):
        layout.label(text="mesh")

    def draw_color(self, context, node):
        return (0.5, 0.5, 0.5, 0.5)

def on_update(self, context):
    ct.inspect_mesh(self.mesh)

class MeshInputNode(bpy.types.Node):
    bl_idname = "ct_MeshInputNode"
    bl_label = "Mesh Input"

    mesh: bpy.props.PointerProperty(type=bpy.types.Mesh, update=on_update)

    def init(self, context):
        self.outputs.new("ct_MeshSocket", "mesh")

    def draw_buttons(self, context, layout):
        layout.prop_search(self, "mesh", bpy.data, "meshes", icon="MESH_CUBE", text="")

class MeshOutputNode(bpy.types.Node):
    bl_idname = "ct_MeshOutputNode"
    bl_label = "Mesh Output"
    bl_width_default = 200

    object: bpy.props.PointerProperty(type=bpy.types.Object)

    def init(self, context):
        self.inputs.new("ct_MeshSocket", "object")

    def draw_buttons(self, context, layout):
        row = layout.row()
        row.prop(self, "object")
        row.enabled = False

class CytokineNodeTreePanel(bpy.types.Panel):
    bl_idname = "ct_CytokineNodeTreePanel"
    bl_label = "Cytokine"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Node"
    # bl_options = set()

    @classmethod
    def poll(cls, context):
        return isinstance(context.space_data.node_tree, CytokineNodeTree)

    def draw(self, context):
        layout = self.layout
        layout.operator("cytokine.compute", text="compute")
        layout.template_list("UI_UL_list", "outputs", context.space_data.node_tree, "outputs", context.space_data.node_tree, "active_output")

def add_menu(self, context):
    if not isinstance(context.space_data.node_tree, CytokineNodeTree): return

    layout = self.layout
    layout.operator_context = "INVOKE_DEFAULT"

    operator = layout.operator("node.add_node", text="Mesh Input")
    operator.type = "ct_MeshInputNode"
    operator.use_transform = True

    layout.operator("cytokine.add_output_mesh", text="Mesh Output")

class CytokineCompute(bpy.types.Operator):
    bl_idname = "cytokine.compute"
    bl_label = "compute"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        node_tree = context.space_data.edit_tree

        node_tree.compute()

        return {'FINISHED'}

class AddMeshOutput(bpy.types.Operator):
    bl_idname = "cytokine.add_output_mesh"
    bl_label = "Add Output Mesh"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        node_tree = context.space_data.edit_tree

        mesh = bpy.data.meshes.new('')
        obj = bpy.data.objects.new('', mesh)
        context.scene.collection.objects.link(obj)

        for n in node_tree.nodes:
            n.select = False

        node = node_tree.nodes.new("ct_MeshOutputNode")
        node.object = obj
        node.select = True
        node_tree.nodes.active = node
        node.location = context.space_data.cursor_location

        return {"FINISHED"}

    def invoke(self, context, event):
        if context.region.type == 'WINDOW':
            context.space_data.cursor_location_from_region(event.mouse_region_x, event.mouse_region_y)
        else:
            space.cursor_location = tree.view_center
        result = self.execute(context)
        if ('FINISHED' in result):
            bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')
        return result

def depsgraph_update_post(scene):
    pass

def register():
    bpy.utils.register_class(OutputProperty)
    bpy.utils.register_class(CytokineNodeTree)
    bpy.utils.register_class(CytokineNodeTreePanel)
    bpy.utils.register_class(MeshInputNode)
    bpy.utils.register_class(MeshOutputNode)
    bpy.utils.register_class(MeshSocket)
    bpy.utils.register_class(AddMeshOutput)
    bpy.utils.register_class(CytokineCompute)
    bpy.types.NODE_MT_add.append(add_menu)

    bpy.app.handlers.depsgraph_update_post.append(depsgraph_update_post)

def unregister():
    bpy.utils.unregister_class(CytokineNodeTree)
    bpy.utils.unregister_class(CytokineNodeTreePanel)
    bpy.utils.unregister_class(MeshInputNode)
    bpy.utils.unregister_class(MeshOutputNode)
    bpy.utils.unregister_class(MeshSocket)
    bpy.utils.unregister_class(OutputProperty)
    bpy.utils.unregister_class(AddMeshOutput)
    bpy.utils.unregister_class(CytokineCompute)
    bpy.types.NODE_MT_add.remove(add_menu)

    bpy.app.handlers.depsgraph_update_post.remove(depsgraph_update_post)
