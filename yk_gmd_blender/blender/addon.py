# This file was based on https://github.com/KhronosGroup/glTF-Blender-IO/blob/master/addons/io_scene_gltf2/__init__.py

#
# Script reloading (if the user calls 'Reload Scripts' from Blender)
#

# def reload_package(module_dict_main):
#     import importlib
#     from pathlib import Path
#
#     def reload_package_recursive(current_dir, module_dict):
#         for path in current_dir.iterdir():
#             if "__init__" in str(path) or path.stem not in module_dict:
#                 continue
#
#             if path.is_file() and path.suffix == ".py":
#                 importlib.reload(module_dict[path.stem])
#             elif path.is_dir():
#                 reload_package_recursive(path, module_dict[path.stem].__dict__)
#
#     reload_package_recursive(Path(__file__).parent, module_dict_main)
#
#
# if "bpy" in locals():
#     reload_package(locals())

#
# Import Class
#
import bpy
from bpy.props import PointerProperty

from yk_gmd_blender.blender.importer.image_relink import YakuzaImageRelink, menu_func_yk_image_relink
from yk_gmd_blender.blender.materials import YakuzaPropertyGroup, YakuzaPropertyPanel, YakuzaTexturePropertyGroup
from .export.gmd_exporter import ExportSkinnedGMD, menu_func_export
from .importer.gmd_importers import ImportSkinnedGMD, menu_func_import_skinned, menu_func_import_unskinned, \
    ImportUnskinnedGMD

classes = (
    ImportSkinnedGMD,
    ImportUnskinnedGMD,
    ExportSkinnedGMD,
    YakuzaImageRelink,
    YakuzaPropertyGroup,
    YakuzaPropertyPanel,
    YakuzaTexturePropertyGroup,
)

def register():
    for c in classes:
        bpy.utils.register_class(c)

    # add to the export / import menu
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import_skinned)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import_unskinned)
    bpy.types.TOPBAR_MT_file_external_data.append(menu_func_yk_image_relink)

    bpy.types.Material.yakuza_data = PointerProperty(type=YakuzaPropertyGroup)
    bpy.types.Image.yakuza_data = PointerProperty(type=YakuzaTexturePropertyGroup)


def unregister():
    del bpy.types.Image.yakuza_data
    del bpy.types.Material.yakuza_data

    for c in classes:
        bpy.utils.unregister_class(c)
    #for f in extension_panel_unregister_functors:
    #    f()
    #extension_panel_unregister_functors.clear()

    # remove from the export / import menu
    bpy.types.TOPBAR_MT_file_external_data.remove(menu_func_yk_image_relink)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import_unskinned)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import_skinned)
