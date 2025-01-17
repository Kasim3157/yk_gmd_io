from mathutils import Quaternion

import bpy
from yk_gmd_blender.blender.common import root_name_for_gmd_file

from yk_gmd_blender.blender.importer.scene_creators.base import BaseGMDSceneCreator, GMDSceneCreatorConfig
from yk_gmd_blender.yk_gmd.v2.abstract.gmd_scene import GMDScene
from yk_gmd_blender.yk_gmd.v2.abstract.nodes.gmd_bone import GMDBone
from yk_gmd_blender.yk_gmd.v2.abstract.nodes.gmd_object import GMDSkinnedObject, GMDUnskinnedObject
from yk_gmd_blender.yk_gmd.v2.errors.error_reporter import ErrorReporter
import bpy
from mathutils import Quaternion

from yk_gmd_blender.blender.common import root_name_for_gmd_file
from yk_gmd_blender.blender.importer.scene_creators.base import BaseGMDSceneCreator, GMDSceneCreatorConfig
from yk_gmd_blender.yk_gmd.v2.abstract.gmd_scene import GMDScene
from yk_gmd_blender.yk_gmd.v2.abstract.nodes.gmd_bone import GMDBone
from yk_gmd_blender.yk_gmd.v2.abstract.nodes.gmd_object import GMDSkinnedObject, GMDUnskinnedObject
from yk_gmd_blender.yk_gmd.v2.errors.error_reporter import ErrorReporter


class GMDUnskinnedSceneCreator(BaseGMDSceneCreator):
    """
    Implementation of a GMDSceneCreator that focuses on skinned meshes.
    """

    def __init__(self, filepath: str, gmd_scene: GMDScene, config: GMDSceneCreatorConfig, error: ErrorReporter):
        super().__init__(filepath, gmd_scene, config, error)

    def validate_scene(self):
        # Skinned Importer checks for duplicate "bone" names (technically node names).
        # Skeletons can't have duplicate bones, but objects can.
        # We remove the Blender-enforced duplicate suffix e.g. "object.001" on export, so nothing will break if we import duplicates
        if len([node for node in self.gmd_scene.overall_hierarchy.depth_first_iterate() if isinstance(node, GMDSkinnedObject)]) != 0:
            self.error.recoverable(f"This import method cannot import skinnned objects. Please use the [Skinned] variant")


    def make_objects(self, collection: bpy.types.Collection):
        """
        Populate the Blender scene with Blender objects for each node in the scene hierarchy representing a GMDUnskinnedObject.
        :param collection: The collection the import process is adding objects and meshes to.
        :return: Nothing
        """

        gmd_objects = {}

        root_name = root_name_for_gmd_file(self.gmd_scene)
        root_obj = bpy.data.objects.new(f"{root_name}", None)
        collection.objects.link(root_obj)

        # Still create the vertex group list, so we create the vertex groups, but don't actually deform anything
        vertex_group_list = [node.name for node in self.gmd_scene.overall_hierarchy.depth_first_iterate() if isinstance(node, GMDBone)]
        vertex_group_indices = {
            name: i
            for i, name in enumerate(vertex_group_list)
        }

        for gmd_node in self.gmd_scene.overall_hierarchy.depth_first_iterate():
            if isinstance(gmd_node, GMDUnskinnedObject):
                overall_mesh = self.build_object_mesh(collection, gmd_node, vertex_group_indices)
                node_obj = bpy.data.objects.new(f"{gmd_node.name}", overall_mesh)
            else:
                node_obj = bpy.data.objects.new(f"{gmd_node.name}", None)
                node_obj.empty_display_size = 0.1

            if gmd_node.parent:
                # Parenting an object to another object is easy
                node_obj.parent = gmd_objects[id(gmd_node.parent)]
            else:
                node_obj.parent = root_obj

            # Set the GMDNode position, rotation, scale
            node_obj.location = self.gmd_to_blender_world @ gmd_node.pos.xyz
            # TODO: Use a proper function for this - I hate that the matrix multiply doesn't work
            node_obj.rotation_quaternion = Quaternion(
                (gmd_node.rot.w, -gmd_node.rot.x, gmd_node.rot.z, gmd_node.rot.y))
            # TODO - When applying gmd_to_blender_world to (1,1,1) you get (-1,1,1) out. This undoes the previous scaling applied to the vertices.
            #  .xzy is used to swap the components for now, but there's probably a better way?
            node_obj.scale = gmd_node.scale.xzy

            # Add the object to the gmd_objects map, and link it to the scene. We're done!
            gmd_objects[id(gmd_node)] = node_obj
            collection.objects.link(node_obj)
