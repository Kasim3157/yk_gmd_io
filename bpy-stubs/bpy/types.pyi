"""


Types (bpy.types)
*****************

"""

import typing

import mathutils

import idprop

class bpy_struct:

  """

  built-in base class for all classes in bpy.types.

  Note: Note that :class:`bpy.types.bpy_struct` is not actually available from within Blender,
it only exists for the purpose of documentation.

  """

  def as_pointer(self) -> int:

    """

    Returns the memory address which holds a pointer to Blender's internal data

    Note: This is intended only for advanced script writers who need to
pass blender data to their own C/Python modules.

    """

    ...

  def driver_add(self, path: str, index: int = -1) -> typing.Union[FCurve, typing.List[typing.Any]]:

    """

    Adds driver(s) to the given property

    """

    ...

  def driver_remove(self, path: str, index: int = -1) -> bool:

    """

    Remove driver(s) from the given property

    """

    ...

  def get(self, key: str, default: typing.Any = None) -> None:

    """

    Returns the value of the custom property assigned to key or default
when not found (matches Python's dictionary function of the same name).

    Note: Only the :class:`bpy.types.ID`, :class:`bpy.types.Bone` and
:class:`bpy.types.PoseBone` classes support custom properties.

    """

    ...

  def id_properties_clear(self) -> None:

    ...

  def id_properties_ensure(self) -> IDPropertyGroup:

    ...

  def id_properties_ui(self, key: typing.Any) -> IDPropertyUIManager:

    ...

  def is_property_hidden(self, property: typing.Any) -> bool:

    """

    Check if a property is hidden.

    """

    ...

  def is_property_overridable_library(self, property: typing.Any) -> bool:

    """

    Check if a property is overridable.

    """

    ...

  def is_property_readonly(self, property: typing.Any) -> bool:

    """

    Check if a property is readonly.

    """

    ...

  def is_property_set(self, property: typing.Any, ghost: bool = True) -> bool:

    """

    Check if a property is set, use for testing operator properties.

    Note: Properties defined at run-time store the values of the properties as custom-properties.This method checks if the underlying data exists, causing the property to be considered *set*.A common pattern for operators is to calculate a value for the properties
that have not had their values explicitly set by the caller
(where the caller could be a key-binding, menu-items or Python script for example).In the case of executing operators multiple times, values are re-used from the previous execution.For example: subdividing a mesh with a smooth value of 1.0 will keep using
that value on subsequent calls to subdivision, unless the operator is called with
that property set to a different value.This behavior can be disabled using the ``SKIP_SAVE`` option when the property is declared (see: :mod:`bpy.props`).The ``ghost`` argument allows detecting how a value from a previous execution is handled.

      * When true: The property is considered unset even if the value from a previous call is used.

      * When false: The existence of any values causes ``is_property_set`` to return true.

      While this argument should typically be omitted, there are times when
it's important to know if a value is anything besides the default.For example, the previous value may have been scaled by the scene's unit scale.
In this case scaling the value multiple times would cause problems, so the ``ghost`` argument should be false.

    """

    ...

  def items(self) -> idprop.type.IDPropertyGroupViewItems:

    """

    Returns the items of this objects custom properties (matches Python's
dictionary function of the same name).

    Note: Only the :class:`bpy.types.ID`, :class:`bpy.types.Bone` and
:class:`bpy.types.PoseBone` classes support custom properties.

    """

    ...

  def keyframe_delete(self, data_path: str, index: int = -1, frame: float = bpy.context.scene.frame_current, group: str = '') -> bool:

    """

    Remove a keyframe from this properties fcurve.

    """

    ...

  def keyframe_insert(self, data_path: str, index: int = -1, frame: float = bpy.context.scene.frame_current, group: str = '', options: typing.Any = set()) -> bool:

    """

    Insert a keyframe on the property given, adding fcurves and animation data when necessary.

    This is the most simple example of inserting a keyframe from python.

    .. code::

      import bpy

      obj = bpy.context.object

      # set the keyframe at frame 1
      obj.location = (3.0, 4.0, 10.0)
      obj.keyframe_insert(data_path="location", frame=1)

    Note that when keying data paths which contain nested properties this must be
done from the :class:`ID` subclass, in this case the :class:`Armature` rather
than the bone.

    .. code::

      import bpy
      from bpy.props import (
          FloatProperty,
          PointerProperty,
      )


      # Define a nested property.
      class MyPropGroup(bpy.types.PropertyGroup):
          nested: FloatProperty(name="Nested", default=0.0)


      # Register it so its available for all bones.
      bpy.utils.register_class(MyPropGroup)
      bpy.types.Bone.my_prop = PointerProperty(
          type=MyPropGroup,
          name="MyProp",
      )

      # Get a bone.
      obj = bpy.data.objects["Armature"]
      arm = obj.data

      # Set the keyframe at frame 1.
      arm.bones["Bone"].my_prop.nested = 10
      arm.keyframe_insert(
          data_path='bones["Bone"].my_prop.nested',
          frame=1,
          group="Nested Group",
      )

    """

    ...

  def keys(self) -> idprop.type.IDPropertyGroupViewKeys:

    """

    Returns the keys of this objects custom properties (matches Python's
dictionary function of the same name).

    Note: Only the :class:`bpy.types.ID`, :class:`bpy.types.Bone` and
:class:`bpy.types.PoseBone` classes support custom properties.

    """

    ...

  def path_from_id(self, property: str = '') -> str:

    """

    Returns the data path from the ID to this object (string).

    """

    ...

  def path_resolve(self, path: str, coerce: bool = True) -> None:

    """

    Returns the property from the path, raise an exception when not found.

    """

    ...

  def pop(self, key: str, default: typing.Any = None) -> None:

    """

    Remove and return the value of the custom property assigned to key or default
when not found (matches Python's dictionary function of the same name).

    Note: Only the :class:`bpy.types.ID`, :class:`bpy.types.Bone` and
:class:`bpy.types.PoseBone` classes support custom properties.

    """

    ...

  def property_overridable_library_set(self, property: typing.Any, overridable: typing.Any) -> bool:

    """

    Define a property as overridable or not (only for custom properties!).

    """

    ...

  def property_unset(self, property: typing.Any) -> None:

    """

    Unset a property, will use default value afterward.

    """

    ...

  def type_recast(self) -> typing.Any:

    """

    Return a new instance, this is needed because types
such as textures can be changed at runtime.

    """

    ...

  def values(self) -> idprop.type.IDPropertyGroupViewValues:

    """

    Returns the values of this objects custom properties (matches Python's
dictionary function of the same name).

    Note: Only the :class:`bpy.types.ID`, :class:`bpy.types.Bone` and
:class:`bpy.types.PoseBone` classes support custom properties.

    """

    ...

  id_data: typing.Any = ...

  """

  The :class:`bpy.types.ID` object this datablock is from or None, (not available for all data types)

  """

class bpy_prop_collection:

  """

  built-in class used for all collections.

  Note: Note that :class:`bpy.types.bpy_prop_collection` is not actually available from within Blender,
it only exists for the purpose of documentation.

  """

  def find(self, key: str) -> int:

    """

    Returns the index of a key in a collection or -1 when not found
(matches Python's string find function of the same name).

    """

    ...

  def foreach_get(self, attr: typing.Any, seq: typing.Any) -> None:

    """

    This is a function to give fast access to attributes within a collection.

    Only works for 'basic type' properties (bool, int and float)!
Multi-dimensional arrays (like array of vectors) will be flattened into seq.

    .. code::

      collection.foreach_get(attr, some_seq)

      # Python equivalent
      for i in range(len(seq)):
          some_seq[i] = getattr(collection[i], attr)

    """

    ...

  def foreach_set(self, attr: typing.Any, seq: typing.Any) -> None:

    """

    This is a function to give fast access to attributes within a collection.

    Only works for 'basic type' properties (bool, int and float)!
seq must be uni-dimensional, multi-dimensional arrays (like array of vectors) will be re-created from it.

    .. code::

      collection.foreach_set(attr, some_seq)

      # Python equivalent
      for i in range(len(some_seq)):
          setattr(collection[i], attr, some_seq[i])

    """

    ...

  def get(self, key: str, default: typing.Any = None) -> None:

    """

    Returns the value of the item assigned to key or default when not found
(matches Python's dictionary function of the same name).

    """

    ...

  def items(self) -> typing.List[typing.Tuple[typing.Any, ...]]:

    """

    Return the identifiers of collection members
(matching Python's dict.items() functionality).

    """

    ...

  def keys(self) -> typing.List[str]:

    """

    Return the identifiers of collection members
(matching Python's dict.keys() functionality).

    """

    ...

  def values(self) -> typing.List[typing.Any]:

    """

    Return the values of collection
(matching Python's dict.values() functionality).

    """

    ...

class ActionFCurves(bpy_struct):

  """

  Collection of action F-Curves

  """

  def new(self, data_path: str, index: int = 0, action_group: str = '') -> FCurve:

    """

    Add an F-Curve to the action

    """

    ...

  def find(self, data_path: str, index: int = 0) -> FCurve:

    """

    Find an F-Curve. Note that this function performs a linear scan of all F-Curves in the action.

    """

    ...

  def remove(self, fcurve: FCurve) -> None:

    """

    Remove action group

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ActionGroup(bpy_struct):

  """

  Groups of F-Curves

  """

  channels: typing.Union[typing.Sequence[FCurve], typing.Mapping[str, FCurve], bpy_prop_collection] = ...

  """

  F-Curves in this group

  """

  color_set: str = ...

  """

  Custom color set to use

  """

  colors: ThemeBoneColorSet = ...

  """

  Copy of the colors associated with the group's color set

  """

  is_custom_color_set: bool = ...

  """

  Color set is user-defined instead of a fixed theme color set

  """

  lock: bool = ...

  """

  Action group is locked

  """

  name: str = ...

  select: bool = ...

  """

  Action group is selected

  """

  show_expanded: bool = ...

  """

  Action group is expanded except in graph editor

  """

  show_expanded_graph: bool = ...

  """

  Action group is expanded in graph editor

  """

  use_pin: bool = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ActionGroups(bpy_struct):

  """

  Collection of action groups

  """

  def new(self, name: str) -> ActionGroup:

    """

    Create a new action group and add it to the action

    """

    ...

  def remove(self, action_group: ActionGroup) -> None:

    """

    Remove action group

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ActionPoseMarkers(bpy_struct):

  """

  Collection of timeline markers

  """

  active: TimelineMarker = ...

  """

  Active pose marker for this action

  """

  active_index: int = ...

  """

  Index of active pose marker

  """

  def new(self, name: str) -> TimelineMarker:

    """

    Add a pose marker to the action

    """

    ...

  def remove(self, marker: TimelineMarker) -> None:

    """

    Remove a timeline marker

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Addon(bpy_struct):

  """

  Python add-ons to be loaded automatically

  """

  module: str = ...

  """

  Module name

  """

  preferences: AddonPreferences = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class AddonPreferences(bpy_struct):

  bl_idname: str = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Addons(bpy_struct):

  """

  Collection of add-ons

  """

  @classmethod

  def new(cls) -> Addon:

    """

    Add a new add-on

    """

    ...

  @classmethod

  def remove(cls, addon: Addon) -> None:

    """

    Remove add-on

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class AnimData(bpy_struct):

  """

  Animation data for data-block

  """

  action: Action = ...

  """

  Active Action for this data-block

  """

  action_blend_type: str = ...

  """

  Method used for combining Active Action's result with result of NLA stack

  * ``REPLACE``
Replace -- The strip values replace the accumulated results by amount specified by influence.

  * ``COMBINE``
Combine -- The strip values are combined with accumulated results by appropriately using addition, multiplication, or quaternion math, based on channel type.

  * ``ADD``
Add -- Weighted result of strip is added to the accumulated results.

  * ``SUBTRACT``
Subtract -- Weighted result of strip is removed from the accumulated results.

  * ``MULTIPLY``
Multiply -- Weighted result of strip is multiplied with the accumulated results.

  """

  action_extrapolation: str = ...

  """

  Action to take for gaps past the Active Action's range (when evaluating with NLA)

  * ``NOTHING``
Nothing -- Strip has no influence past its extents.

  * ``HOLD``
Hold -- Hold the first frame if no previous strips in track, and always hold last frame.

  * ``HOLD_FORWARD``
Hold Forward -- Only hold last frame.

  """

  action_influence: float = ...

  """

  Amount the Active Action contributes to the result of the NLA stack

  """

  drivers: typing.Union[AnimDataDrivers, typing.Sequence[FCurve], typing.Mapping[str, FCurve], bpy_prop_collection] = ...

  """

  The Drivers/Expressions for this data-block

  """

  nla_tracks: typing.Union[NlaTracks, typing.Sequence[NlaTrack], typing.Mapping[str, NlaTrack], bpy_prop_collection] = ...

  """

  NLA Tracks (i.e. Animation Layers)

  """

  use_nla: bool = ...

  """

  NLA stack is evaluated when evaluating this block

  """

  use_pin: bool = ...

  use_tweak_mode: bool = ...

  """

  Whether to enable or disable tweak mode in NLA

  """

  def nla_tweak_strip_time_to_scene(self, frame: float, invert: bool = False) -> float:

    """

    Convert a time value from the local time of the tweaked strip to scene time, exactly as done by built-in key editing tools. Returns the input time unchanged if not tweaking.

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class AnimDataDrivers(bpy_struct):

  """

  Collection of Driver F-Curves

  """

  def new(self, data_path: str, index: int = 0) -> FCurve:

    """

    new

    """

    ...

  def remove(self, driver: FCurve) -> None:

    """

    remove

    """

    ...

  def from_existing(self, src_driver: FCurve = None) -> FCurve:

    """

    Add a new driver given an existing one

    """

    ...

  def find(self, data_path: str, index: int = 0) -> FCurve:

    """

    Find a driver F-Curve. Note that this function performs a linear scan of all driver F-Curves.

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class AnimViz(bpy_struct):

  """

  Settings for the visualization of motion

  """

  motion_path: AnimVizMotionPaths = ...

  """

  Motion Path settings for visualization

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class AnimVizMotionPaths(bpy_struct):

  """

  Motion Path settings for animation visualization

  """

  bake_location: str = ...

  """

  When calculating Bone Paths, use Head or Tips

  * ``HEADS``
Heads -- Calculate bone paths from heads.

  * ``TAILS``
Tails -- Calculate bone paths from tails.

  """

  frame_after: int = ...

  """

  Number of frames to show after the current frame (only for 'Around Current Frame' Onion-skinning method)

  """

  frame_before: int = ...

  """

  Number of frames to show before the current frame (only for 'Around Current Frame' Onion-skinning method)

  """

  frame_end: int = ...

  """

  End frame of range of paths to display/calculate (not for 'Around Current Frame' Onion-skinning method)

  """

  frame_start: int = ...

  """

  Starting frame of range of paths to display/calculate (not for 'Around Current Frame' Onion-skinning method)

  """

  frame_step: int = ...

  """

  Number of frames between paths shown (not for 'On Keyframes' Onion-skinning method)

  """

  has_motion_paths: bool = ...

  """

  Are there any bone paths that will need updating (read-only)

  """

  show_frame_numbers: bool = ...

  """

  Show frame numbers on Motion Paths

  """

  show_keyframe_action_all: bool = ...

  """

  For bone motion paths, search whole Action for keyframes instead of in group with matching name only (is slower)

  """

  show_keyframe_highlight: bool = ...

  """

  Emphasize position of keyframes on Motion Paths

  """

  show_keyframe_numbers: bool = ...

  """

  Show frame numbers of Keyframes on Motion Paths

  """

  type: str = ...

  """

  Type of range to show for Motion Paths

  * ``CURRENT_FRAME``
Around Frame -- Display Paths of poses within a fixed number of frames around the current frame.

  * ``RANGE``
In Range -- Display Paths of poses within specified range.

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class AnyType(bpy_struct):

  """

  RNA type used for pointers to any possible data

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class AOV(bpy_struct):

  is_valid: bool = ...

  """

  Is the name of the AOV conflicting

  """

  name: str = ...

  """

  Name of the AOV

  """

  type: str = ...

  """

  Data type of the AOV

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class AOVs(bpy_struct):

  """

  Collection of AOVs

  """

  def add(self) -> AOV:

    """

    add

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Area(bpy_struct):

  """

  Area in a subdivided screen, containing an editor

  """

  height: int = ...

  """

  Area height

  """

  regions: typing.Union[typing.Sequence[Region], typing.Mapping[str, Region], bpy_prop_collection] = ...

  """

  Regions this area is subdivided in

  """

  show_menus: bool = ...

  """

  Show menus in the header

  """

  spaces: typing.Union[AreaSpaces, typing.Sequence[Space], typing.Mapping[str, Space], bpy_prop_collection] = ...

  """

  Spaces contained in this area, the first being the active space (NOTE: Useful for example to restore a previously used 3D view space in a certain area to get the old view orientation)

  """

  type: str = ...

  """

  Current editor type for this area

  * ``EMPTY``
Empty.

  * ``VIEW_3D``
3D Viewport -- Manipulate objects in a 3D environment.

  * ``IMAGE_EDITOR``
UV/Image Editor -- View and edit images and UV Maps.

  * ``NODE_EDITOR``
Node Editor -- Editor for node-based shading and compositing tools.

  * ``SEQUENCE_EDITOR``
Video Sequencer -- Video editing tools.

  * ``CLIP_EDITOR``
Movie Clip Editor -- Motion tracking tools.

  * ``DOPESHEET_EDITOR``
Dope Sheet -- Adjust timing of keyframes.

  * ``GRAPH_EDITOR``
Graph Editor -- Edit drivers and keyframe interpolation.

  * ``NLA_EDITOR``
Nonlinear Animation -- Combine and layer Actions.

  * ``TEXT_EDITOR``
Text Editor -- Edit scripts and in-file documentation.

  * ``CONSOLE``
Python Console -- Interactive programmatic console for advanced editing and script development.

  * ``INFO``
Info -- Log of operations, warnings and error messages.

  * ``TOPBAR``
Top Bar -- Global bar at the top of the screen for global per-window settings.

  * ``STATUSBAR``
Status Bar -- Global bar at the bottom of the screen for general status information.

  * ``OUTLINER``
Outliner -- Overview of scene graph and all available data-blocks.

  * ``PROPERTIES``
Properties -- Edit properties of active object and related data-blocks.

  * ``FILE_BROWSER``
File Browser -- Browse for files and assets.

  * ``SPREADSHEET``
Spreadsheet -- Explore geometry data in a table.

  * ``PREFERENCES``
Preferences -- Edit persistent configuration settings.

  """

  ui_type: str = ...

  """

  Current editor type for this area

  """

  width: int = ...

  """

  Area width

  """

  x: int = ...

  """

  The window relative vertical location of the area

  """

  y: int = ...

  """

  The window relative horizontal location of the area

  """

  def tag_redraw(self) -> None:

    """

    tag_redraw

    """

    ...

  def header_text_set(self, text: str) -> None:

    """

    Set the header status text

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class AreaSpaces(bpy_struct):

  """

  Collection of spaces

  """

  active: Space = ...

  """

  Space currently being displayed in this area

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ArmatureBones(bpy_struct):

  """

  Collection of armature bones

  """

  active: Bone = ...

  """

  Armature's active bone

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ArmatureConstraintTargets(bpy_struct):

  """

  Collection of target bones and weights

  """

  def new(self) -> ConstraintTargetBone:

    """

    Add a new target to the constraint

    """

    ...

  def remove(self, target: ConstraintTargetBone) -> None:

    """

    Delete target from the constraint

    """

    ...

  def clear(self) -> None:

    """

    Delete all targets from object

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ArmatureEditBones(bpy_struct):

  """

  Collection of armature edit bones

  """

  active: EditBone = ...

  """

  Armatures active edit bone

  """

  def new(self, name: str) -> EditBone:

    """

    Add a new bone

    """

    ...

  def remove(self, bone: EditBone) -> None:

    """

    Remove an existing bone from the armature

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class AssetLibraryReference(bpy_struct):

  """

  Identifier to refer to the asset library

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class AssetMetaData(bpy_struct):

  """

  Additional data stored for an asset data-block

  """

  active_tag: int = ...

  """

  Index of the tag set for editing

  """

  author: str = ...

  """

  Name of the creator of the asset

  """

  catalog_id: str = ...

  """

  Identifier for the asset's catalog, used by Blender to look up the asset's catalog path. Must be a UUID according to RFC4122

  """

  catalog_simple_name: str = ...

  """

  Simple name of the asset's catalog, for debugging and data recovery purposes

  """

  description: str = ...

  """

  A description of the asset to be displayed for the user

  """

  tags: typing.Union[AssetTags, typing.Sequence[AssetTag], typing.Mapping[str, AssetTag], bpy_prop_collection] = ...

  """

  Custom tags (name tokens) for the asset, used for filtering and general asset management

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class AssetTag(bpy_struct):

  """

  User defined tag (name token)

  """

  name: str = ...

  """

  The identifier that makes up this tag

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class AssetTags(bpy_struct):

  """

  Collection of custom asset tags

  """

  def new(self, name: str, skip_if_exists: bool = False) -> AssetTag:

    """

    Add a new tag to this asset

    """

    ...

  def remove(self, tag: AssetTag) -> None:

    """

    Remove an existing tag from this asset

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Attribute(bpy_struct):

  """

  Geometry attribute

  """

  data_type: str = ...

  """

  Type of data stored in attribute

  * ``FLOAT``
Float -- Floating-point value.

  * ``INT``
Integer -- 32-bit integer.

  * ``FLOAT_VECTOR``
Vector -- 3D vector with floating-point values.

  * ``FLOAT_COLOR``
Color -- RGBA color with floating-point values.

  * ``BYTE_COLOR``
Byte Color -- RGBA color with 8-bit values.

  * ``STRING``
String -- Text string.

  * ``BOOLEAN``
Boolean -- True or false.

  * ``FLOAT2``
2D Vector -- 2D vector with floating-point values.

  """

  domain: str = ...

  """

  Domain of the Attribute

  * ``POINT``
Point -- Attribute on point.

  * ``EDGE``
Edge -- Attribute on mesh edge.

  * ``FACE``
Face -- Attribute on mesh faces.

  * ``CORNER``
Face Corner -- Attribute on mesh face corner.

  * ``CURVE``
Spline -- Attribute on spline.

  """

  name: str = ...

  """

  Name of the Attribute

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class AttributeGroup(bpy_struct):

  """

  Group of geometry attributes

  """

  active: Attribute = ...

  """

  Active attribute

  """

  active_index: int = ...

  def new(self, name: str, type: str, domain: str) -> Attribute:

    """

    Add an attribute

    """

    ...

  def remove(self, attribute: Attribute) -> None:

    """

    Remove an attribute

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BakeSettings(bpy_struct):

  """

  Bake data for a Scene data-block

  """

  cage_extrusion: float = ...

  """

  Inflate the active object by the specified distance for baking. This helps matching to points nearer to the outside of the selected object meshes

  """

  cage_object: Object = ...

  """

  Object to use as cage instead of calculating the cage from the active object with cage extrusion

  """

  filepath: str = ...

  """

  Image filepath to use when saving externally

  """

  height: int = ...

  """

  Vertical dimension of the baking map

  """

  image_settings: ImageFormatSettings = ...

  margin: int = ...

  """

  Extends the baked result as a post process filter

  """

  max_ray_distance: float = ...

  """

  The maximum ray distance for matching points between the active and selected objects. If zero, there is no limit

  """

  normal_b: str = ...

  """

  Axis to bake in blue channel

  """

  normal_g: str = ...

  """

  Axis to bake in green channel

  """

  normal_r: str = ...

  """

  Axis to bake in red channel

  """

  normal_space: str = ...

  """

  Choose normal space for baking

  * ``OBJECT``
Object -- Bake the normals in object space.

  * ``TANGENT``
Tangent -- Bake the normals in tangent space.

  """

  pass_filter: typing.Set[str] = ...

  """

  Passes to include in the active baking pass

  """

  save_mode: str = ...

  """

  Where to save baked image textures

  * ``INTERNAL``
Internal -- Save the baking map in an internal image data-block.

  * ``EXTERNAL``
External -- Save the baking map in an external file.

  """

  target: str = ...

  """

  Where to output the baked map

  * ``IMAGE_TEXTURES``
Image Textures -- Bake to image data-blocks associated with active image texture nodes in materials.

  * ``VERTEX_COLORS``
Vertex Colors -- Bake to active vertex color layer on meshes.

  """

  use_automatic_name: bool = ...

  """

  Automatically name the output file with the pass type (external only)

  """

  use_cage: bool = ...

  """

  Cast rays to active object from a cage

  """

  use_clear: bool = ...

  """

  Clear Images before baking (internal only)

  """

  use_pass_color: bool = ...

  """

  Color the pass

  """

  use_pass_diffuse: bool = ...

  """

  Add diffuse contribution

  """

  use_pass_direct: bool = ...

  """

  Add direct lighting contribution

  """

  use_pass_emit: bool = ...

  """

  Add emission contribution

  """

  use_pass_glossy: bool = ...

  """

  Add glossy contribution

  """

  use_pass_indirect: bool = ...

  """

  Add indirect lighting contribution

  """

  use_pass_transmission: bool = ...

  """

  Add transmission contribution

  """

  use_selected_to_active: bool = ...

  """

  Bake shading on the surface of selected objects to the active object

  """

  use_split_materials: bool = ...

  """

  Split external images per material (external only)

  """

  width: int = ...

  """

  Horizontal dimension of the baking map

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BezierSplinePoint(bpy_struct):

  """

  Bezier curve point with two handles

  """

  co: typing.Tuple[float, float, float] = ...

  """

  Coordinates of the control point

  """

  handle_left: typing.Tuple[float, float, float] = ...

  """

  Coordinates of the first handle

  """

  handle_left_type: str = ...

  """

  Handle types

  """

  handle_right: typing.Tuple[float, float, float] = ...

  """

  Coordinates of the second handle

  """

  handle_right_type: str = ...

  """

  Handle types

  """

  hide: bool = ...

  """

  Visibility status

  """

  radius: float = ...

  """

  Radius for beveling

  """

  select_control_point: bool = ...

  """

  Control point selection status

  """

  select_left_handle: bool = ...

  """

  Handle 1 selection status

  """

  select_right_handle: bool = ...

  """

  Handle 2 selection status

  """

  tilt: float = ...

  """

  Tilt in 3D View

  """

  weight_softbody: float = ...

  """

  Softbody goal weight

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendData(bpy_struct):

  """

  Main data structure representing a .blend file and all its data-blocks

  """

  actions: typing.Union[BlendDataActions, typing.Sequence[Action], typing.Mapping[str, Action], bpy_prop_collection] = ...

  """

  Action data-blocks

  """

  armatures: typing.Union[BlendDataArmatures, typing.Sequence[Armature], typing.Mapping[str, Armature], bpy_prop_collection] = ...

  """

  Armature data-blocks

  """

  brushes: typing.Union[BlendDataBrushes, typing.Sequence[Brush], typing.Mapping[str, Brush], bpy_prop_collection] = ...

  """

  Brush data-blocks

  """

  cache_files: typing.Union[BlendDataCacheFiles, typing.Sequence[CacheFile], typing.Mapping[str, CacheFile], bpy_prop_collection] = ...

  """

  Cache Files data-blocks

  """

  cameras: typing.Union[BlendDataCameras, typing.Sequence[Camera], typing.Mapping[str, Camera], bpy_prop_collection] = ...

  """

  Camera data-blocks

  """

  collections: typing.Union[BlendDataCollections, typing.Sequence[Collection], typing.Mapping[str, Collection], bpy_prop_collection] = ...

  """

  Collection data-blocks

  """

  curves: typing.Union[BlendDataCurves, typing.Sequence[Curve], typing.Mapping[str, Curve], bpy_prop_collection] = ...

  """

  Curve data-blocks

  """

  filepath: str = ...

  """

  Path to the .blend file

  """

  fonts: typing.Union[BlendDataFonts, typing.Sequence[VectorFont], typing.Mapping[str, VectorFont], bpy_prop_collection] = ...

  """

  Vector font data-blocks

  """

  grease_pencils: typing.Union[BlendDataGreasePencils, typing.Sequence[GreasePencil], typing.Mapping[str, GreasePencil], bpy_prop_collection] = ...

  """

  Grease Pencil data-blocks

  """

  images: typing.Union[BlendDataImages, typing.Sequence[Image], typing.Mapping[str, Image], bpy_prop_collection] = ...

  """

  Image data-blocks

  """

  is_dirty: bool = ...

  """

  Have recent edits been saved to disk

  """

  is_saved: bool = ...

  """

  Has the current session been saved to disk as a .blend file

  """

  lattices: typing.Union[BlendDataLattices, typing.Sequence[Lattice], typing.Mapping[str, Lattice], bpy_prop_collection] = ...

  """

  Lattice data-blocks

  """

  libraries: typing.Union[BlendDataLibraries, typing.Sequence[Library], typing.Mapping[str, Library], bpy_prop_collection] = ...

  """

  Library data-blocks

  """

  lightprobes: typing.Union[BlendDataProbes, typing.Sequence[LightProbe], typing.Mapping[str, LightProbe], bpy_prop_collection] = ...

  """

  Light Probe data-blocks

  """

  lights: typing.Union[BlendDataLights, typing.Sequence[Light], typing.Mapping[str, Light], bpy_prop_collection] = ...

  """

  Light data-blocks

  """

  linestyles: typing.Union[BlendDataLineStyles, typing.Sequence[FreestyleLineStyle], typing.Mapping[str, FreestyleLineStyle], bpy_prop_collection] = ...

  """

  Line Style data-blocks

  """

  masks: typing.Union[BlendDataMasks, typing.Sequence[Mask], typing.Mapping[str, Mask], bpy_prop_collection] = ...

  """

  Masks data-blocks

  """

  materials: typing.Union[BlendDataMaterials, typing.Sequence[Material], typing.Mapping[str, Material], bpy_prop_collection] = ...

  """

  Material data-blocks

  """

  meshes: typing.Union[BlendDataMeshes, typing.Sequence[Mesh], typing.Mapping[str, Mesh], bpy_prop_collection] = ...

  """

  Mesh data-blocks

  """

  metaballs: typing.Union[BlendDataMetaBalls, typing.Sequence[MetaBall], typing.Mapping[str, MetaBall], bpy_prop_collection] = ...

  """

  Metaball data-blocks

  """

  movieclips: typing.Union[BlendDataMovieClips, typing.Sequence[MovieClip], typing.Mapping[str, MovieClip], bpy_prop_collection] = ...

  """

  Movie Clip data-blocks

  """

  node_groups: typing.Union[BlendDataNodeTrees, typing.Sequence[NodeTree], typing.Mapping[str, NodeTree], bpy_prop_collection] = ...

  """

  Node group data-blocks

  """

  objects: typing.Union[BlendDataObjects, typing.Sequence[Object], typing.Mapping[str, Object], bpy_prop_collection] = ...

  """

  Object data-blocks

  """

  paint_curves: typing.Union[BlendDataPaintCurves, typing.Sequence[PaintCurve], typing.Mapping[str, PaintCurve], bpy_prop_collection] = ...

  """

  Paint Curves data-blocks

  """

  palettes: typing.Union[BlendDataPalettes, typing.Sequence[Palette], typing.Mapping[str, Palette], bpy_prop_collection] = ...

  """

  Palette data-blocks

  """

  particles: typing.Union[BlendDataParticles, typing.Sequence[ParticleSettings], typing.Mapping[str, ParticleSettings], bpy_prop_collection] = ...

  """

  Particle data-blocks

  """

  scenes: typing.Union[BlendDataScenes, typing.Sequence[Scene], typing.Mapping[str, Scene], bpy_prop_collection] = ...

  """

  Scene data-blocks

  """

  screens: typing.Union[BlendDataScreens, typing.Sequence[Screen], typing.Mapping[str, Screen], bpy_prop_collection] = ...

  """

  Screen data-blocks

  """

  shape_keys: typing.Union[typing.Sequence[Key], typing.Mapping[str, Key], bpy_prop_collection] = ...

  """

  Shape Key data-blocks

  """

  sounds: typing.Union[BlendDataSounds, typing.Sequence[Sound], typing.Mapping[str, Sound], bpy_prop_collection] = ...

  """

  Sound data-blocks

  """

  speakers: typing.Union[BlendDataSpeakers, typing.Sequence[Speaker], typing.Mapping[str, Speaker], bpy_prop_collection] = ...

  """

  Speaker data-blocks

  """

  texts: typing.Union[BlendDataTexts, typing.Sequence[Text], typing.Mapping[str, Text], bpy_prop_collection] = ...

  """

  Text data-blocks

  """

  textures: typing.Union[BlendDataTextures, typing.Sequence[Texture], typing.Mapping[str, Texture], bpy_prop_collection] = ...

  """

  Texture data-blocks

  """

  use_autopack: bool = ...

  """

  Automatically pack all external data into .blend file

  """

  version: typing.Tuple[int, int, int] = ...

  """

  File format version the .blend file was saved with

  """

  volumes: typing.Union[BlendDataVolumes, typing.Sequence[Volume], typing.Mapping[str, Volume], bpy_prop_collection] = ...

  """

  Volume data-blocks

  """

  window_managers: typing.Union[BlendDataWindowManagers, typing.Sequence[WindowManager], typing.Mapping[str, WindowManager], bpy_prop_collection] = ...

  """

  Window manager data-blocks

  """

  workspaces: typing.Union[BlendDataWorkSpaces, typing.Sequence[WorkSpace], typing.Mapping[str, WorkSpace], bpy_prop_collection] = ...

  """

  Workspace data-blocks

  """

  worlds: typing.Union[BlendDataWorlds, typing.Sequence[World], typing.Mapping[str, World], bpy_prop_collection] = ...

  """

  World data-blocks

  """

  def batch_remove(self, ids: typing.Any) -> None:

    """

    Remove (delete) several IDs at once.

    WARNING: Considered experimental feature currently.

    Note that this function is quicker than individual calls to :func:`remove()` (from :class:`bpy.types.BlendData`
ID collections), but less safe/versatile (it can break Blender, e.g. by removing all scenes...).

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

  def orphans_purge(self) -> None:

    """

    Remove (delete) all IDs with no user.

    """

    ...

  def temp_data(self, filepath: str = None) -> BlendData:

    """

    A context manager that temporarily creates blender file data.

    """

    ...

  def user_map(self, subset: typing.Sequence[typing.Any], key_types: typing.Set[str], value_types: typing.Set[str]) -> typing.Dict[str, typing.Any]:

    """

    Returns a mapping of all ID data-blocks in current ``bpy.data`` to a set of all datablocks using them.

    For list of valid set members for key_types & value_types, see: :class:`bpy.types.KeyingSetPath.id_type`.

    """

    ...

class BlendDataActions(bpy_struct):

  """

  Collection of actions

  """

  def new(self, name: str) -> Action:

    """

    Add a new action to the main database

    """

    ...

  def remove(self, action: Action, do_unlink: bool = True, do_id_user: bool = True, do_ui_user: bool = True) -> None:

    """

    Remove an action from the current blendfile

    """

    ...

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataArmatures(bpy_struct):

  """

  Collection of armatures

  """

  def new(self, name: str) -> Armature:

    """

    Add a new armature to the main database

    """

    ...

  def remove(self, armature: Armature, do_unlink: bool = True, do_id_user: bool = True, do_ui_user: bool = True) -> None:

    """

    Remove an armature from the current blendfile

    """

    ...

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataBrushes(bpy_struct):

  """

  Collection of brushes

  """

  def new(self, name: str, mode: str = 'TEXTURE_PAINT') -> Brush:

    """

    Add a new brush to the main database

    """

    ...

  def remove(self, brush: Brush, do_unlink: bool = True, do_id_user: bool = True, do_ui_user: bool = True) -> None:

    """

    Remove a brush from the current blendfile

    """

    ...

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  def create_gpencil_data(self, brush: Brush) -> None:

    """

    Add grease pencil brush settings

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataCacheFiles(bpy_struct):

  """

  Collection of cache files

  """

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataCameras(bpy_struct):

  """

  Collection of cameras

  """

  def new(self, name: str) -> Camera:

    """

    Add a new camera to the main database

    """

    ...

  def remove(self, camera: Camera, do_unlink: bool = True, do_id_user: bool = True, do_ui_user: bool = True) -> None:

    """

    Remove a camera from the current blendfile

    """

    ...

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataCollections(bpy_struct):

  """

  Collection of collections

  """

  def new(self, name: str) -> Collection:

    """

    Add a new collection to the main database

    """

    ...

  def remove(self, collection: Collection, do_unlink: bool = True, do_id_user: bool = True, do_ui_user: bool = True) -> None:

    """

    Remove a collection from the current blendfile

    """

    ...

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataCurves(bpy_struct):

  """

  Collection of curves

  """

  def new(self, name: str, type: str) -> Curve:

    """

    Add a new curve to the main database

    """

    ...

  def remove(self, curve: Curve, do_unlink: bool = True, do_id_user: bool = True, do_ui_user: bool = True) -> None:

    """

    Remove a curve from the current blendfile

    """

    ...

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataFonts(bpy_struct):

  """

  Collection of fonts

  """

  def load(self, filepath: str, check_existing: bool = False) -> VectorFont:

    """

    Load a new font into the main database

    """

    ...

  def remove(self, vfont: VectorFont, do_unlink: bool = True, do_id_user: bool = True, do_ui_user: bool = True) -> None:

    """

    Remove a font from the current blendfile

    """

    ...

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataGreasePencils(bpy_struct):

  """

  Collection of grease pencils

  """

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  def new(self, name: str) -> GreasePencil:

    """

    Add a new grease pencil datablock to the main database

    """

    ...

  def remove(self, grease_pencil: GreasePencil, do_unlink: bool = True, do_id_user: bool = True, do_ui_user: bool = True) -> None:

    """

    Remove a grease pencil instance from the current blendfile

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataImages(bpy_struct):

  """

  Collection of images

  """

  def new(self, name: str, width: int, height: int, alpha: bool = False, float_buffer: bool = False, stereo3d: bool = False, is_data: bool = False, tiled: bool = False) -> Image:

    """

    Add a new image to the main database

    """

    ...

  def load(self, filepath: str, check_existing: bool = False) -> Image:

    """

    Load a new image into the main database

    """

    ...

  def remove(self, image: Image, do_unlink: bool = True, do_id_user: bool = True, do_ui_user: bool = True) -> None:

    """

    Remove an image from the current blendfile

    """

    ...

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataLattices(bpy_struct):

  """

  Collection of lattices

  """

  def new(self, name: str) -> Lattice:

    """

    Add a new lattice to the main database

    """

    ...

  def remove(self, lattice: Lattice, do_unlink: bool = True, do_id_user: bool = True, do_ui_user: bool = True) -> None:

    """

    Remove a lattice from the current blendfile

    """

    ...

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataLibraries(bpy_struct):

  """

  Collection of libraries

  """

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  def remove(self, library: Library, do_unlink: bool = True, do_id_user: bool = True, do_ui_user: bool = True) -> None:

    """

    Remove a library from the current blendfile

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataLights(bpy_struct):

  """

  Collection of lights

  """

  def new(self, name: str, type: str) -> Light:

    """

    Add a new light to the main database

    """

    ...

  def remove(self, light: Light, do_unlink: bool = True, do_id_user: bool = True, do_ui_user: bool = True) -> None:

    """

    Remove a light from the current blendfile

    """

    ...

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataLineStyles(bpy_struct):

  """

  Collection of line styles

  """

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  def new(self, name: str) -> FreestyleLineStyle:

    """

    Add a new line style instance to the main database

    """

    ...

  def remove(self, linestyle: FreestyleLineStyle, do_unlink: bool = True, do_id_user: bool = True, do_ui_user: bool = True) -> None:

    """

    Remove a line style instance from the current blendfile

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataMasks(bpy_struct):

  """

  Collection of masks

  """

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  def new(self, name: str) -> Mask:

    """

    Add a new mask with a given name to the main database

    """

    ...

  def remove(self, mask: Mask, do_unlink: bool = True, do_id_user: bool = True, do_ui_user: bool = True) -> None:

    """

    Remove a mask from the current blendfile

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataMaterials(bpy_struct):

  """

  Collection of materials

  """

  def new(self, name: str) -> Material:

    """

    Add a new material to the main database

    """

    ...

  def create_gpencil_data(self, material: Material) -> None:

    """

    Add grease pencil material settings

    """

    ...

  def remove_gpencil_data(self, material: Material) -> None:

    """

    Remove grease pencil material settings

    """

    ...

  def remove(self, material: Material, do_unlink: bool = True, do_id_user: bool = True, do_ui_user: bool = True) -> None:

    """

    Remove a material from the current blendfile

    """

    ...

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataMeshes(bpy_struct):

  """

  Collection of meshes

  """

  def new(self, name: str) -> Mesh:

    """

    Add a new mesh to the main database

    """

    ...

  def new_from_object(self, object: Object, preserve_all_data_layers: bool = False, depsgraph: Depsgraph = None) -> Mesh:

    """

    Add a new mesh created from given object (undeformed geometry if object is original, and final evaluated geometry, with all modifiers etc., if object is evaluated)

    """

    ...

  def remove(self, mesh: Mesh, do_unlink: bool = True, do_id_user: bool = True, do_ui_user: bool = True) -> None:

    """

    Remove a mesh from the current blendfile

    """

    ...

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataMetaBalls(bpy_struct):

  """

  Collection of metaballs

  """

  def new(self, name: str) -> MetaBall:

    """

    Add a new metaball to the main database

    """

    ...

  def remove(self, metaball: MetaBall, do_unlink: bool = True, do_id_user: bool = True, do_ui_user: bool = True) -> None:

    """

    Remove a metaball from the current blendfile

    """

    ...

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataMovieClips(bpy_struct):

  """

  Collection of movie clips

  """

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  def remove(self, clip: MovieClip, do_unlink: bool = True, do_id_user: bool = True, do_ui_user: bool = True) -> None:

    """

    Remove a movie clip from the current blendfile.

    """

    ...

  def load(self, filepath: str, check_existing: bool = False) -> MovieClip:

    """

    Add a new movie clip to the main database from a file (while ``check_existing`` is disabled for consistency with other load functions, behavior with multiple movie-clips using the same file may incorrectly generate proxies)

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataNodeTrees(bpy_struct):

  """

  Collection of node trees

  """

  def new(self, name: str, type: str) -> NodeTree:

    """

    Add a new node tree to the main database

    """

    ...

  def remove(self, tree: NodeTree, do_unlink: bool = True, do_id_user: bool = True, do_ui_user: bool = True) -> None:

    """

    Remove a node tree from the current blendfile

    """

    ...

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataObjects(bpy_struct):

  """

  Collection of objects

  """

  def new(self, name: str, object_data: ID) -> Object:

    """

    Add a new object to the main database

    """

    ...

  def remove(self, object: Object, do_unlink: bool = True, do_id_user: bool = True, do_ui_user: bool = True) -> None:

    """

    Remove an object from the current blendfile

    """

    ...

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataPaintCurves(bpy_struct):

  """

  Collection of paint curves

  """

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataPalettes(bpy_struct):

  """

  Collection of palettes

  """

  def new(self, name: str) -> Palette:

    """

    Add a new palette to the main database

    """

    ...

  def remove(self, palette: Palette, do_unlink: bool = True, do_id_user: bool = True, do_ui_user: bool = True) -> None:

    """

    Remove a palette from the current blendfile

    """

    ...

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataParticles(bpy_struct):

  """

  Collection of particle settings

  """

  def new(self, name: str) -> ParticleSettings:

    """

    Add a new particle settings instance to the main database

    """

    ...

  def remove(self, particle: ParticleSettings, do_unlink: bool = True, do_id_user: bool = True, do_ui_user: bool = True) -> None:

    """

    Remove a particle settings instance from the current blendfile

    """

    ...

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataProbes(bpy_struct):

  """

  Collection of light probes

  """

  def new(self, name: str, type: str) -> LightProbe:

    """

    Add a new light probe to the main database

    """

    ...

  def remove(self, lightprobe: LightProbe, do_unlink: bool = True, do_id_user: bool = True, do_ui_user: bool = True) -> None:

    """

    Remove a light probe from the current blendfile

    """

    ...

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataScenes(bpy_struct):

  """

  Collection of scenes

  """

  def new(self, name: str) -> Scene:

    """

    Add a new scene to the main database

    """

    ...

  def remove(self, scene: Scene, do_unlink: bool = True) -> None:

    """

    Remove a scene from the current blendfile

    """

    ...

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataScreens(bpy_struct):

  """

  Collection of screens

  """

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataSounds(bpy_struct):

  """

  Collection of sounds

  """

  def load(self, filepath: str, check_existing: bool = False) -> Sound:

    """

    Add a new sound to the main database from a file

    """

    ...

  def remove(self, sound: Sound, do_unlink: bool = True, do_id_user: bool = True, do_ui_user: bool = True) -> None:

    """

    Remove a sound from the current blendfile

    """

    ...

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataSpeakers(bpy_struct):

  """

  Collection of speakers

  """

  def new(self, name: str) -> Speaker:

    """

    Add a new speaker to the main database

    """

    ...

  def remove(self, speaker: Speaker, do_unlink: bool = True, do_id_user: bool = True, do_ui_user: bool = True) -> None:

    """

    Remove a speaker from the current blendfile

    """

    ...

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataTexts(bpy_struct):

  """

  Collection of texts

  """

  def new(self, name: str) -> Text:

    """

    Add a new text to the main database

    """

    ...

  def remove(self, text: Text, do_unlink: bool = True, do_id_user: bool = True, do_ui_user: bool = True) -> None:

    """

    Remove a text from the current blendfile

    """

    ...

  def load(self, filepath: str, internal: bool = False) -> Text:

    """

    Add a new text to the main database from a file

    """

    ...

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataTextures(bpy_struct):

  """

  Collection of textures

  """

  def new(self, name: str, type: str) -> Texture:

    """

    Add a new texture to the main database

    """

    ...

  def remove(self, texture: Texture, do_unlink: bool = True, do_id_user: bool = True, do_ui_user: bool = True) -> None:

    """

    Remove a texture from the current blendfile

    """

    ...

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataVolumes(bpy_struct):

  """

  Collection of volumes

  """

  def new(self, name: str) -> Volume:

    """

    Add a new volume to the main database

    """

    ...

  def remove(self, volume: Volume, do_unlink: bool = True, do_id_user: bool = True, do_ui_user: bool = True) -> None:

    """

    Remove a volume from the current blendfile

    """

    ...

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataWindowManagers(bpy_struct):

  """

  Collection of window managers

  """

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataWorkSpaces(bpy_struct):

  """

  Collection of workspaces

  """

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlendDataWorlds(bpy_struct):

  """

  Collection of worlds

  """

  def new(self, name: str) -> World:

    """

    Add a new world to the main database

    """

    ...

  def remove(self, world: World, do_unlink: bool = True, do_id_user: bool = True, do_ui_user: bool = True) -> None:

    """

    Remove a world from the current blendfile

    """

    ...

  def tag(self, value: bool) -> None:

    """

    tag

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BlenderRNA(bpy_struct):

  """

  Blender RNA structure definitions

  """

  structs: typing.Union[typing.Sequence[Struct], typing.Mapping[str, Struct], bpy_prop_collection] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BoidRule(bpy_struct):

  name: str = ...

  """

  Boid rule name

  """

  type: str = ...

  """

  * ``GOAL``
Goal -- Go to assigned object or loudest assigned signal source.

  * ``AVOID``
Avoid -- Get away from assigned object or loudest assigned signal source.

  * ``AVOID_COLLISION``
Avoid Collision -- Maneuver to avoid collisions with other boids and deflector objects in near future.

  * ``SEPARATE``
Separate -- Keep from going through other boids.

  * ``FLOCK``
Flock -- Move to center of neighbors and match their velocity.

  * ``FOLLOW_LEADER``
Follow Leader -- Follow a boid or assigned object.

  * ``AVERAGE_SPEED``
Average Speed -- Maintain speed, flight level or wander.

  * ``FIGHT``
Fight -- Go to closest enemy and attack when in range.

  """

  use_in_air: bool = ...

  """

  Use rule when boid is flying

  """

  use_on_land: bool = ...

  """

  Use rule when boid is on land

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BoidSettings(bpy_struct):

  """

  Settings for boid physics

  """

  accuracy: float = ...

  """

  Accuracy of attack

  """

  active_boid_state: BoidRule = ...

  active_boid_state_index: int = ...

  aggression: float = ...

  """

  Boid will fight this times stronger enemy

  """

  air_acc_max: float = ...

  """

  Maximum acceleration in air (relative to maximum speed)

  """

  air_ave_max: float = ...

  """

  Maximum angular velocity in air (relative to 180 degrees)

  """

  air_personal_space: float = ...

  """

  Radius of boids personal space in air (% of particle size)

  """

  air_speed_max: float = ...

  """

  Maximum speed in air

  """

  air_speed_min: float = ...

  """

  Minimum speed in air (relative to maximum speed)

  """

  bank: float = ...

  """

  Amount of rotation around velocity vector on turns

  """

  health: float = ...

  """

  Initial boid health when born

  """

  height: float = ...

  """

  Boid height relative to particle size

  """

  land_acc_max: float = ...

  """

  Maximum acceleration on land (relative to maximum speed)

  """

  land_ave_max: float = ...

  """

  Maximum angular velocity on land (relative to 180 degrees)

  """

  land_jump_speed: float = ...

  """

  Maximum speed for jumping

  """

  land_personal_space: float = ...

  """

  Radius of boids personal space on land (% of particle size)

  """

  land_smooth: float = ...

  """

  How smoothly the boids land

  """

  land_speed_max: float = ...

  """

  Maximum speed on land

  """

  land_stick_force: float = ...

  """

  How strong a force must be to start effecting a boid on land

  """

  pitch: float = ...

  """

  Amount of rotation around side vector

  """

  range: float = ...

  """

  Maximum distance from which a boid can attack

  """

  states: typing.Union[typing.Sequence[BoidState], typing.Mapping[str, BoidState], bpy_prop_collection] = ...

  strength: float = ...

  """

  Maximum caused damage on attack per second

  """

  use_climb: bool = ...

  """

  Allow boids to climb goal objects

  """

  use_flight: bool = ...

  """

  Allow boids to move in air

  """

  use_land: bool = ...

  """

  Allow boids to move on land

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BoidState(bpy_struct):

  """

  Boid state for boid physics

  """

  active_boid_rule: BoidRule = ...

  active_boid_rule_index: int = ...

  falloff: float = ...

  name: str = ...

  """

  Boid state name

  """

  rule_fuzzy: float = ...

  rules: typing.Union[typing.Sequence[BoidRule], typing.Mapping[str, BoidRule], bpy_prop_collection] = ...

  ruleset_type: str = ...

  """

  How the rules in the list are evaluated

  * ``FUZZY``
Fuzzy -- Rules are gone through top to bottom (only the first rule which effect is above fuzziness threshold is evaluated).

  * ``RANDOM``
Random -- A random rule is selected for each boid.

  * ``AVERAGE``
Average -- All rules are averaged.

  """

  volume: float = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Bone(bpy_struct):

  """

  Bone in an Armature data-block

  """

  bbone_curveinx: float = ...

  """

  X-axis handle offset for start of the B-Bone's curve, adjusts curvature

  """

  bbone_curveinz: float = ...

  """

  Z-axis handle offset for start of the B-Bone's curve, adjusts curvature

  """

  bbone_curveoutx: float = ...

  """

  X-axis handle offset for end of the B-Bone's curve, adjusts curvature

  """

  bbone_curveoutz: float = ...

  """

  Z-axis handle offset for end of the B-Bone's curve, adjusts curvature

  """

  bbone_custom_handle_end: Bone = ...

  """

  Bone that serves as the end handle for the B-Bone curve

  """

  bbone_custom_handle_start: Bone = ...

  """

  Bone that serves as the start handle for the B-Bone curve

  """

  bbone_easein: float = ...

  """

  Length of first Bezier Handle (for B-Bones only)

  """

  bbone_easeout: float = ...

  """

  Length of second Bezier Handle (for B-Bones only)

  """

  bbone_handle_type_end: str = ...

  """

  Selects how the end handle of the B-Bone is computed

  * ``AUTO``
Automatic -- Use connected parent and children to compute the handle.

  * ``ABSOLUTE``
Absolute -- Use the position of the specified bone to compute the handle.

  * ``RELATIVE``
Relative -- Use the offset of the specified bone from rest pose to compute the handle.

  * ``TANGENT``
Tangent -- Use the orientation of the specified bone to compute the handle, ignoring the location.

  """

  bbone_handle_type_start: str = ...

  """

  Selects how the start handle of the B-Bone is computed

  * ``AUTO``
Automatic -- Use connected parent and children to compute the handle.

  * ``ABSOLUTE``
Absolute -- Use the position of the specified bone to compute the handle.

  * ``RELATIVE``
Relative -- Use the offset of the specified bone from rest pose to compute the handle.

  * ``TANGENT``
Tangent -- Use the orientation of the specified bone to compute the handle, ignoring the location.

  """

  bbone_handle_use_ease_end: bool = ...

  """

  Multiply the B-Bone Ease Out channel by the local Y scale value of the end handle. This is done after the Scale Easing option and isn't affected by it

  """

  bbone_handle_use_ease_start: bool = ...

  """

  Multiply the B-Bone Ease In channel by the local Y scale value of the start handle. This is done after the Scale Easing option and isn't affected by it

  """

  bbone_handle_use_scale_end: typing.Tuple[bool, bool, bool] = ...

  """

  Multiply B-Bone Scale Out channels by the local scale values of the end handle. This is done after the Scale Easing option and isn't affected by it

  """

  bbone_handle_use_scale_start: typing.Tuple[bool, bool, bool] = ...

  """

  Multiply B-Bone Scale In channels by the local scale values of the start handle. This is done after the Scale Easing option and isn't affected by it

  """

  bbone_rollin: float = ...

  """

  Roll offset for the start of the B-Bone, adjusts twist

  """

  bbone_rollout: float = ...

  """

  Roll offset for the end of the B-Bone, adjusts twist

  """

  bbone_scalein: typing.Tuple[float, float, float] = ...

  """

  Scale factors for the start of the B-Bone, adjusts thickness (for tapering effects)

  """

  bbone_scaleout: typing.Tuple[float, float, float] = ...

  """

  Scale factors for the end of the B-Bone, adjusts thickness (for tapering effects)

  """

  bbone_segments: int = ...

  """

  Number of subdivisions of bone (for B-Bones only)

  """

  bbone_x: float = ...

  """

  B-Bone X size

  """

  bbone_z: float = ...

  """

  B-Bone Z size

  """

  children: typing.Union[typing.Sequence[Bone], typing.Mapping[str, Bone], bpy_prop_collection] = ...

  """

  Bones which are children of this bone

  """

  envelope_distance: float = ...

  """

  Bone deformation distance (for Envelope deform only)

  """

  envelope_weight: float = ...

  """

  Bone deformation weight (for Envelope deform only)

  """

  head: typing.Tuple[float, float, float] = ...

  """

  Location of head end of the bone relative to its parent

  """

  head_local: typing.Tuple[float, float, float] = ...

  """

  Location of head end of the bone relative to armature

  """

  head_radius: float = ...

  """

  Radius of head of bone (for Envelope deform only)

  """

  hide: bool = ...

  """

  Bone is not visible when it is not in Edit Mode (i.e. in Object or Pose Modes)

  """

  hide_select: bool = ...

  """

  Bone is able to be selected

  """

  inherit_scale: str = ...

  """

  Specifies how the bone inherits scaling from the parent bone

  * ``FULL``
Full -- Inherit all effects of parent scaling.

  * ``FIX_SHEAR``
Fix Shear -- Inherit scaling, but remove shearing of the child in the rest orientation.

  * ``ALIGNED``
Aligned -- Rotate non-uniform parent scaling to align with the child, applying parent X scale to child X axis, and so forth.

  * ``AVERAGE``
Average -- Inherit uniform scaling representing the overall change in the volume of the parent.

  * ``NONE``
None -- Completely ignore parent scaling.

  * ``NONE_LEGACY``
None (Legacy) -- Ignore parent scaling without compensating for parent shear. Replicates the effect of disabling the original Inherit Scale checkbox.

  """

  layers: typing.Tuple[bool, ...] = ...

  """

  Layers bone exists in

  """

  length: float = ...

  """

  Length of the bone

  """

  matrix: typing.Tuple[typing.Tuple[float, float, float], typing.Tuple[float, float, float], typing.Tuple[float, float, float]] = ...

  """

  3x3 bone matrix

  """

  matrix_local: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]] = ...

  """

  4x4 bone matrix relative to armature

  """

  name: str = ...

  parent: Bone = ...

  """

  Parent bone (in same Armature)

  """

  select: bool = ...

  select_head: bool = ...

  select_tail: bool = ...

  show_wire: bool = ...

  """

  Bone is always displayed in wireframe regardless of viewport shading mode (useful for non-obstructive custom bone shapes)

  """

  tail: typing.Tuple[float, float, float] = ...

  """

  Location of tail end of the bone relative to its parent

  """

  tail_local: typing.Tuple[float, float, float] = ...

  """

  Location of tail end of the bone relative to armature

  """

  tail_radius: float = ...

  """

  Radius of tail of bone (for Envelope deform only)

  """

  use_connect: bool = ...

  """

  When bone has a parent, bone's head is stuck to the parent's tail

  """

  use_cyclic_offset: bool = ...

  """

  When bone doesn't have a parent, it receives cyclic offset effects (Deprecated)

  """

  use_deform: bool = ...

  """

  Enable Bone to deform geometry

  """

  use_endroll_as_inroll: bool = ...

  """

  Add Roll Out of the Start Handle bone to the Roll In value

  """

  use_envelope_multiply: bool = ...

  """

  When deforming bone, multiply effects of Vertex Group weights with Envelope influence

  """

  use_inherit_rotation: bool = ...

  """

  Bone inherits rotation or scale from parent bone

  """

  use_inherit_scale: bool = ...

  """

  DEPRECATED: Bone inherits scaling from parent bone

  """

  use_local_location: bool = ...

  """

  Bone location is set in local space

  """

  use_relative_parent: bool = ...

  """

  Object children will use relative transform, like deform

  """

  use_scale_easing: bool = ...

  """

  Multiply the final easing values by the Scale In/Out Y factors

  """

  basename: typing.Any = ...

  """

  The name of this bone before any '.' character

  (readonly)

  """

  center: typing.Any = ...

  """

  The midpoint between the head and the tail.

  (readonly)

  """

  children: typing.Any = ...

  """

  A list of all the bones children.

    Note: Takes ``O(len(bones))`` time.

  (readonly)

  """

  children_recursive: typing.Any = ...

  """

  A list of all children from this bone.

    Note: Takes ``O(len(bones)**2)`` time.

  (readonly)

  """

  children_recursive_basename: typing.Any = ...

  """

  Returns a chain of children with the same base name as this bone.
Only direct chains are supported, forks caused by multiple children
with matching base names will terminate the function
and not be returned.

  Note: Takes ``O(len(bones)**2)`` time.

  (readonly)

  """

  parent_recursive: typing.Any = ...

  """

  A list of parents, starting with the immediate parent

  (readonly)

  """

  vector: typing.Any = ...

  """

  The direction this bone is pointing.
Utility function for (tail - head)

  (readonly)

  """

  x_axis: typing.Any = ...

  """

  Vector pointing down the x-axis of the bone.

  (readonly)

  """

  y_axis: typing.Any = ...

  """

  Vector pointing down the y-axis of the bone.

  (readonly)

  """

  z_axis: typing.Any = ...

  """

  Vector pointing down the z-axis of the bone.

  (readonly)

  """

  def evaluate_envelope(self, point: typing.Tuple[float, float, float]) -> float:

    """

    Calculate bone envelope at given point

    """

    ...

  def convert_local_to_pose(self, matrix: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]], matrix_local: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]], parent_matrix: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]] = ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), parent_matrix_local: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]] = ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), invert: bool = False) -> typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]]:

    """

    Transform a matrix from Local to Pose space (or back), taking into account options like Inherit Scale and Local Location. Unlike Object.convert_space, this uses custom rest and pose matrices provided by the caller. If the parent matrices are omitted, the bone is assumed to have no parent.

    This method enables conversions between Local and Pose space for bones in
the middle of updating the armature without having to update dependencies
after each change, by manually carrying updated matrices in a recursive walk.

    .. code::

      def set_pose_matrices(obj, matrix_map):
          "Assign pose space matrices of all bones at once, ignoring constraints."

          def rec(pbone, parent_matrix):
              matrix = matrix_map[pbone.name]

              ## Instead of:
              # pbone.matrix = matrix
              # bpy.context.view_layer.update()

              # Compute and assign local matrix, using the new parent matrix
              if pbone.parent:
                  pbone.matrix_basis = pbone.bone.convert_local_to_pose(
                      matrix,
                      pbone.bone.matrix_local,
                      parent_matrix=parent_matrix,
                      parent_matrix_local=pbone.parent.bone.matrix_local,
                      invert=True
                  )
              else:
                  pbone.matrix_basis = pbone.bone.convert_local_to_pose(
                      matrix,
                      pbone.bone.matrix_local,
                      invert=True
                  )

              # Recursively process children, passing the new matrix through
              for child in pbone.children:
                  rec(child, matrix)

          # Scan all bone trees from their roots
          for pbone in obj.pose.bones:
              if not pbone.parent:
                  rec(pbone, None)

    """

    ...

  @classmethod

  def MatrixFromAxisRoll(cls, axis: typing.Tuple[float, float, float], roll: float) -> typing.Tuple[typing.Tuple[float, float, float], typing.Tuple[float, float, float], typing.Tuple[float, float, float]]:

    """

    Convert the axis + roll representation to a matrix

    """

    ...

  @classmethod

  def AxisRollFromMatrix(cls, matrix: typing.Tuple[typing.Tuple[float, float, float], typing.Tuple[float, float, float], typing.Tuple[float, float, float]], axis: typing.Tuple[float, float, float] = (0.0, 0.0, 0.0)) -> None:

    """

    Convert a rotational matrix to the axis + roll representation. Note that the resulting value of the roll may not be as expected if the matrix has shear or negative determinant.

    """

    ...

  def parent_index(self, parent_test: typing.Any) -> None:

    """

    The same as 'bone in other_bone.parent_recursive'
but saved generating a list.

    """

    ...

  def translate(self, vec: typing.Any) -> None:

    """

    Utility function to add *vec* to the head and tail of this bone

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BoneGroup(bpy_struct):

  """

  Groups of Pose Channels (Bones)

  """

  color_set: str = ...

  """

  Custom color set to use

  """

  colors: ThemeBoneColorSet = ...

  """

  Copy of the colors associated with the group's color set

  """

  is_custom_color_set: bool = ...

  """

  Color set is user-defined instead of a fixed theme color set

  """

  name: str = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BoneGroups(bpy_struct):

  """

  Collection of bone groups

  """

  active: BoneGroup = ...

  """

  Active bone group for this pose

  """

  active_index: int = ...

  """

  Active index in bone groups array

  """

  def new(self, name: str = 'Group') -> BoneGroup:

    """

    Add a new bone group to the object

    """

    ...

  def remove(self, group: BoneGroup) -> None:

    """

    Remove a bone group from this object

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BoolAttributeValue(bpy_struct):

  """

  Bool value in geometry attribute

  """

  value: bool = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BrushCapabilities(bpy_struct):

  """

  Read-only indications of supported operations

  """

  has_overlay: bool = ...

  has_random_texture_angle: bool = ...

  has_smooth_stroke: bool = ...

  has_spacing: bool = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BrushCapabilitiesImagePaint(bpy_struct):

  """

  Read-only indications of supported operations

  """

  has_accumulate: bool = ...

  has_color: bool = ...

  has_radius: bool = ...

  has_space_attenuation: bool = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BrushCapabilitiesSculpt(bpy_struct):

  """

  Read-only indications of which brush operations are supported by the current sculpt tool

  """

  has_accumulate: bool = ...

  has_auto_smooth: bool = ...

  has_color: bool = ...

  has_direction: bool = ...

  has_gravity: bool = ...

  has_height: bool = ...

  has_jitter: bool = ...

  has_normal_weight: bool = ...

  has_persistence: bool = ...

  has_pinch_factor: bool = ...

  has_plane_offset: bool = ...

  has_rake_factor: bool = ...

  has_random_texture_angle: bool = ...

  has_sculpt_plane: bool = ...

  has_secondary_color: bool = ...

  has_smooth_stroke: bool = ...

  has_space_attenuation: bool = ...

  has_strength_pressure: bool = ...

  has_tilt: bool = ...

  has_topology_rake: bool = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BrushCapabilitiesVertexPaint(bpy_struct):

  """

  Read-only indications of supported operations

  """

  has_color: bool = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BrushCapabilitiesWeightPaint(bpy_struct):

  """

  Read-only indications of supported operations

  """

  has_weight: bool = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BrushGpencilSettings(bpy_struct):

  """

  Settings for grease pencil brush

  """

  active_smooth_factor: float = ...

  """

  Amount of smoothing while drawing

  """

  angle: float = ...

  """

  Direction of the stroke at which brush gives maximal thickness (0Â° for horizontal)

  """

  angle_factor: float = ...

  """

  Reduce brush thickness by this factor when stroke is perpendicular to 'Angle' direction

  """

  aspect: typing.Tuple[float, float] = ...

  brush_draw_mode: str = ...

  """

  Preselected mode when using this brush

  * ``ACTIVE``
Active -- Use current mode.

  * ``MATERIAL``
Material -- Use always material mode.

  * ``VERTEXCOLOR``
Vertex Color -- Use always Vertex Color mode.

  """

  caps_type: str = ...

  """

  The shape of the start and end of the stroke

  """

  curve_jitter: CurveMapping = ...

  """

  Curve used for the jitter effect

  """

  curve_random_hue: CurveMapping = ...

  """

  Curve used for modulating effect

  """

  curve_random_pressure: CurveMapping = ...

  """

  Curve used for modulating effect

  """

  curve_random_saturation: CurveMapping = ...

  """

  Curve used for modulating effect

  """

  curve_random_strength: CurveMapping = ...

  """

  Curve used for modulating effect

  """

  curve_random_uv: CurveMapping = ...

  """

  Curve used for modulating effect

  """

  curve_random_value: CurveMapping = ...

  """

  Curve used for modulating effect

  """

  curve_sensitivity: CurveMapping = ...

  """

  Curve used for the sensitivity

  """

  curve_strength: CurveMapping = ...

  """

  Curve used for the strength

  """

  dilate: int = ...

  """

  Number of pixels to dilate fill area

  """

  direction: str = ...

  """

  * ``ADD``
Add -- Add effect of brush.

  * ``SUBTRACT``
Subtract -- Subtract effect of brush.

  """

  eraser_mode: str = ...

  """

  Eraser Mode

  * ``SOFT``
Dissolve -- Erase strokes, fading their points strength and thickness.

  * ``HARD``
Point -- Erase stroke points.

  * ``STROKE``
Stroke -- Erase entire strokes.

  """

  eraser_strength_factor: float = ...

  """

  Amount of erasing for strength

  """

  eraser_thickness_factor: float = ...

  """

  Amount of erasing for thickness

  """

  extend_stroke_factor: float = ...

  """

  Strokes end extension for closing gaps, use zero to disable

  """

  fill_direction: str = ...

  """

  Direction of the fill

  * ``NORMAL``
Normal -- Fill internal area.

  * ``INVERT``
Inverted -- Fill inverted area.

  """

  fill_draw_mode: str = ...

  """

  Mode to draw boundary limits

  * ``BOTH``
All -- Use both visible strokes and edit lines as fill boundary limits.

  * ``STROKE``
Strokes -- Use visible strokes as fill boundary limits.

  * ``CONTROL``
Edit Lines -- Use edit lines as fill boundary limits.

  """

  fill_factor: float = ...

  """

  Factor for fill boundary accuracy, higher values are more accurate but slower

  """

  fill_layer_mode: str = ...

  """

  Layers used as boundaries

  * ``VISIBLE``
Visible -- Visible layers.

  * ``ACTIVE``
Active -- Only active layer.

  * ``ABOVE``
Layer Above -- Layer above active.

  * ``BELOW``
Layer Below -- Layer below active.

  * ``ALL_ABOVE``
All Above -- All layers above active.

  * ``ALL_BELOW``
All Below -- All layers below active.

  """

  fill_leak: int = ...

  """

  Size in pixels to consider the leak closed

  """

  fill_simplify_level: int = ...

  """

  Number of simplify steps (large values reduce fill accuracy)

  """

  fill_threshold: float = ...

  """

  Threshold to consider color transparent for filling

  """

  gpencil_paint_icon: str = ...

  gpencil_sculpt_icon: str = ...

  gpencil_vertex_icon: str = ...

  gpencil_weight_icon: str = ...

  hardness: float = ...

  """

  Gradient from the center of Dot and Box strokes (set to 1 for a solid stroke)

  """

  input_samples: int = ...

  """

  Generate intermediate points for very fast mouse movements. Set to 0 to disable

  """

  material: Material = ...

  """

  Material used for strokes drawn using this brush

  """

  pen_jitter: float = ...

  """

  Jitter factor for new strokes

  """

  pen_smooth_factor: float = ...

  """

  Amount of smoothing to apply after finish newly created strokes, to reduce jitter/noise

  """

  pen_smooth_steps: int = ...

  """

  Number of times to smooth newly created strokes

  """

  pen_strength: float = ...

  """

  Color strength for new strokes (affect alpha factor of color)

  """

  pen_subdivision_steps: int = ...

  """

  Number of times to subdivide newly created strokes, for less jagged strokes

  """

  pin_draw_mode: bool = ...

  """

  Pin the mode to the brush

  """

  random_hue_factor: float = ...

  """

  Random factor to modify original hue

  """

  random_pressure: float = ...

  """

  Randomness factor for pressure in new strokes

  """

  random_saturation_factor: float = ...

  """

  Random factor to modify original saturation

  """

  random_strength: float = ...

  """

  Randomness factor strength in new strokes

  """

  random_value_factor: float = ...

  """

  Random factor to modify original value

  """

  show_fill: bool = ...

  """

  Show transparent lines to use as boundary for filling

  """

  show_fill_boundary: bool = ...

  """

  Show help lines for filling to see boundaries

  """

  show_fill_extend: bool = ...

  """

  Show help lines for stroke extension

  """

  show_lasso: bool = ...

  """

  Do not display fill color while drawing the stroke

  """

  simplify_factor: float = ...

  """

  Factor of Simplify using adaptive algorithm

  """

  use_default_eraser: bool = ...

  """

  Use this brush when enable eraser with fast switch key

  """

  use_edit_position: bool = ...

  """

  The brush affects the position of the point

  """

  use_edit_strength: bool = ...

  """

  The brush affects the color strength of the point

  """

  use_edit_thickness: bool = ...

  """

  The brush affects the thickness of the point

  """

  use_edit_uv: bool = ...

  """

  The brush affects the UV rotation of the point

  """

  use_fill_limit: bool = ...

  """

  Fill only visible areas in viewport

  """

  use_jitter_pressure: bool = ...

  """

  Use tablet pressure for jitter

  """

  use_material_pin: bool = ...

  """

  Keep material assigned to brush

  """

  use_occlude_eraser: bool = ...

  """

  Erase only strokes visible and not occluded

  """

  use_pressure: bool = ...

  """

  Use tablet pressure

  """

  use_random_press_hue: bool = ...

  """

  Use pressure to modulate randomness

  """

  use_random_press_radius: bool = ...

  """

  Use pressure to modulate randomness

  """

  use_random_press_sat: bool = ...

  """

  Use pressure to modulate randomness

  """

  use_random_press_strength: bool = ...

  """

  Use pressure to modulate randomness

  """

  use_random_press_uv: bool = ...

  """

  Use pressure to modulate randomness

  """

  use_random_press_val: bool = ...

  """

  Use pressure to modulate randomness

  """

  use_settings_postprocess: bool = ...

  """

  Additional post processing options for new strokes

  """

  use_settings_random: bool = ...

  """

  Random brush settings

  """

  use_settings_stabilizer: bool = ...

  """

  Draw lines with a delay to allow smooth strokes. Press Shift key to override while drawing

  """

  use_strength_pressure: bool = ...

  """

  Use tablet pressure for color strength

  """

  use_stroke_random_hue: bool = ...

  """

  Use randomness at stroke level

  """

  use_stroke_random_radius: bool = ...

  """

  Use randomness at stroke level

  """

  use_stroke_random_sat: bool = ...

  """

  Use randomness at stroke level

  """

  use_stroke_random_strength: bool = ...

  """

  Use randomness at stroke level

  """

  use_stroke_random_uv: bool = ...

  """

  Use randomness at stroke level

  """

  use_stroke_random_val: bool = ...

  """

  Use randomness at stroke level

  """

  use_trim: bool = ...

  """

  Trim intersecting stroke ends

  """

  uv_random: float = ...

  """

  Random factor for auto-generated UV rotation

  """

  vertex_color_factor: float = ...

  """

  Factor used to mix vertex color to get final color

  """

  vertex_mode: str = ...

  """

  Defines how vertex color affect to the strokes

  * ``STROKE``
Stroke -- Vertex Color affects to Stroke only.

  * ``FILL``
Fill -- Vertex Color affects to Fill only.

  * ``BOTH``
Stroke and Fill -- Vertex Color affects to Stroke and Fill.

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ByteColorAttributeValue(bpy_struct):

  """

  Color value in geometry attribute

  """

  color: typing.Tuple[float, float, float, float] = ...

  """

  RGBA color in scene linear color space

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class CacheObjectPath(bpy_struct):

  """

  Path of an object inside of an Alembic archive

  """

  path: str = ...

  """

  Object path

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class CacheObjectPaths(bpy_struct):

  """

  Collection of object paths

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class CameraBackgroundImage(bpy_struct):

  """

  Image and settings for display in the 3D View background

  """

  alpha: float = ...

  """

  Image opacity to blend the image against the background color

  """

  clip: MovieClip = ...

  """

  Movie clip displayed and edited in this space

  """

  clip_user: MovieClipUser = ...

  """

  Parameters defining which frame of the movie clip is displayed

  """

  display_depth: str = ...

  """

  Display under or over everything

  """

  frame_method: str = ...

  """

  How the image fits in the camera frame

  """

  image: Image = ...

  """

  Image displayed and edited in this space

  """

  image_user: ImageUser = ...

  """

  Parameters defining which layer, pass and frame of the image is displayed

  """

  offset: typing.Tuple[float, float] = ...

  rotation: float = ...

  """

  Rotation for the background image (ortho view only)

  """

  scale: float = ...

  """

  Scale the background image

  """

  show_background_image: bool = ...

  """

  Show this image as background

  """

  show_expanded: bool = ...

  """

  Show the expanded in the user interface

  """

  show_on_foreground: bool = ...

  """

  Show this image in front of objects in viewport

  """

  source: str = ...

  """

  Data source used for background

  """

  use_camera_clip: bool = ...

  """

  Use movie clip from active scene camera

  """

  use_flip_x: bool = ...

  """

  Flip the background image horizontally

  """

  use_flip_y: bool = ...

  """

  Flip the background image vertically

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class CameraBackgroundImages(bpy_struct):

  """

  Collection of background images

  """

  def new(self) -> CameraBackgroundImage:

    """

    Add new background image

    """

    ...

  def remove(self, image: CameraBackgroundImage) -> None:

    """

    Remove background image

    """

    ...

  def clear(self) -> None:

    """

    Remove all background images

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class CameraDOFSettings(bpy_struct):

  """

  Depth of Field settings

  """

  aperture_blades: int = ...

  """

  Number of blades in aperture for polygonal bokeh (at least 3)

  """

  aperture_fstop: float = ...

  """

  F-Stop ratio (lower numbers give more defocus, higher numbers give a sharper image)

  """

  aperture_ratio: float = ...

  """

  Distortion to simulate anamorphic lens bokeh

  """

  aperture_rotation: float = ...

  """

  Rotation of blades in aperture

  """

  focus_distance: float = ...

  """

  Distance to the focus point for depth of field

  """

  focus_object: Object = ...

  """

  Use this object to define the depth of field focal point

  """

  use_dof: bool = ...

  """

  Use Depth of Field

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class CameraStereoData(bpy_struct):

  """

  Stereoscopy settings for a Camera data-block

  """

  convergence_distance: float = ...

  """

  The converge point for the stereo cameras (often the distance between a projector and the projection screen)

  """

  convergence_mode: str = ...

  """

  * ``OFFAXIS``
Off-Axis -- Off-axis frustums converging in a plane.

  * ``PARALLEL``
Parallel -- Parallel cameras with no convergence.

  * ``TOE``
Toe-in -- Rotated cameras, looking at the convergence distance.

  """

  interocular_distance: float = ...

  """

  Set the distance between the eyes - the stereo plane distance / 30 should be fine

  """

  pivot: str = ...

  pole_merge_angle_from: float = ...

  """

  Angle at which interocular distance starts to fade to 0

  """

  pole_merge_angle_to: float = ...

  """

  Angle at which interocular distance is 0

  """

  use_pole_merge: bool = ...

  """

  Fade interocular distance to 0 after the given cutoff angle

  """

  use_spherical_stereo: bool = ...

  """

  Render every pixel rotating the camera around the middle of the interocular distance

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ChannelDriverVariables(bpy_struct):

  """

  Collection of channel driver Variables

  """

  def new(self) -> DriverVariable:

    """

    Add a new variable for the driver

    """

    ...

  def remove(self, variable: DriverVariable) -> None:

    """

    Remove an existing variable from the driver

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ChildParticle(bpy_struct):

  """

  Child particle interpolated from simulated or edited particles

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ClothCollisionSettings(bpy_struct):

  """

  Cloth simulation settings for self collision and collision with other objects

  """

  collection: Collection = ...

  """

  Limit colliders to this Collection

  """

  collision_quality: int = ...

  """

  How many collision iterations should be done. (higher is better quality but slower)

  """

  damping: float = ...

  """

  Amount of velocity lost on collision

  """

  distance_min: float = ...

  """

  Minimum distance between collision objects before collision response takes effect

  """

  friction: float = ...

  """

  Friction force if a collision happened (higher = less movement)

  """

  impulse_clamp: float = ...

  """

  Clamp collision impulses to avoid instability (0.0 to disable clamping)

  """

  self_distance_min: float = ...

  """

  Minimum distance between cloth faces before collision response takes effect

  """

  self_friction: float = ...

  """

  Friction with self contact

  """

  self_impulse_clamp: float = ...

  """

  Clamp collision impulses to avoid instability (0.0 to disable clamping)

  """

  use_collision: bool = ...

  """

  Enable collisions with other objects

  """

  use_self_collision: bool = ...

  """

  Enable self collisions

  """

  vertex_group_object_collisions: str = ...

  """

  Triangles with all vertices in this group are not used during object collisions

  """

  vertex_group_self_collisions: str = ...

  """

  Triangles with all vertices in this group are not used during self collisions

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ClothSettings(bpy_struct):

  """

  Cloth simulation settings for an object

  """

  air_damping: float = ...

  """

  Air has normally some thickness which slows falling things down

  """

  bending_damping: float = ...

  """

  Amount of damping in bending behavior

  """

  bending_model: str = ...

  """

  Physical model for simulating bending forces

  * ``ANGULAR``
Angular -- Cloth model with angular bending springs.

  * ``LINEAR``
Linear -- Cloth model with linear bending springs (legacy).

  """

  bending_stiffness: float = ...

  """

  How much the material resists bending

  """

  bending_stiffness_max: float = ...

  """

  Maximum bending stiffness value

  """

  collider_friction: float = ...

  compression_damping: float = ...

  """

  Amount of damping in compression behavior

  """

  compression_stiffness: float = ...

  """

  How much the material resists compression

  """

  compression_stiffness_max: float = ...

  """

  Maximum compression stiffness value

  """

  density_strength: float = ...

  """

  Influence of target density on the simulation

  """

  density_target: float = ...

  """

  Maximum density of hair

  """

  effector_weights: EffectorWeights = ...

  fluid_density: float = ...

  """

  Density (kg/l) of the fluid contained inside the object, used to create a hydrostatic pressure gradient simulating the weight of the internal fluid, or buoyancy from the surrounding fluid if negative

  """

  goal_default: float = ...

  """

  Default Goal (vertex target position) value, when no Vertex Group used

  """

  goal_friction: float = ...

  """

  Goal (vertex target position) friction

  """

  goal_max: float = ...

  """

  Goal maximum, vertex group weights are scaled to match this range

  """

  goal_min: float = ...

  """

  Goal minimum, vertex group weights are scaled to match this range

  """

  goal_spring: float = ...

  """

  Goal (vertex target position) spring stiffness

  """

  gravity: typing.Tuple[float, float, float] = ...

  """

  Gravity or external force vector

  """

  internal_compression_stiffness: float = ...

  """

  How much the material resists compression

  """

  internal_compression_stiffness_max: float = ...

  """

  Maximum compression stiffness value

  """

  internal_friction: float = ...

  internal_spring_max_diversion: float = ...

  """

  How much the rays used to connect the internal points can diverge from the vertex normal

  """

  internal_spring_max_length: float = ...

  """

  The maximum length an internal spring can have during creation. If the distance between internal points is greater than this, no internal spring will be created between these points. A length of zero means that there is no length limit

  """

  internal_spring_normal_check: bool = ...

  """

  Require the points the internal springs connect to have opposite normal directions

  """

  internal_tension_stiffness: float = ...

  """

  How much the material resists stretching

  """

  internal_tension_stiffness_max: float = ...

  """

  Maximum tension stiffness value

  """

  mass: float = ...

  """

  The mass of each vertex on the cloth material

  """

  pin_stiffness: float = ...

  """

  Pin (vertex target position) spring stiffness

  """

  pressure_factor: float = ...

  """

  Ambient pressure (kPa) that balances out between the inside and outside of the object when it has the target volume

  """

  quality: int = ...

  """

  Quality of the simulation in steps per frame (higher is better quality but slower)

  """

  rest_shape_key: ShapeKey = ...

  """

  Shape key to use the rest spring lengths from

  """

  sewing_force_max: float = ...

  """

  Maximum sewing force

  """

  shear_damping: float = ...

  """

  Amount of damping in shearing behavior

  """

  shear_stiffness: float = ...

  """

  How much the material resists shearing

  """

  shear_stiffness_max: float = ...

  """

  Maximum shear scaling value

  """

  shrink_max: float = ...

  """

  Max amount to shrink cloth by

  """

  shrink_min: float = ...

  """

  Factor by which to shrink cloth

  """

  target_volume: float = ...

  """

  The mesh volume where the inner/outer pressure will be the same. If set to zero the change in volume will not affect pressure

  """

  tension_damping: float = ...

  """

  Amount of damping in stretching behavior

  """

  tension_stiffness: float = ...

  """

  How much the material resists stretching

  """

  tension_stiffness_max: float = ...

  """

  Maximum tension stiffness value

  """

  time_scale: float = ...

  """

  Cloth speed is multiplied by this value

  """

  uniform_pressure_force: float = ...

  """

  The uniform pressure that is constantly applied to the mesh, in units of Pressure Scale. Can be negative

  """

  use_dynamic_mesh: bool = ...

  """

  Make simulation respect deformations in the base mesh

  """

  use_internal_springs: bool = ...

  """

  Simulate an internal volume structure by creating springs connecting the opposite sides of the mesh

  """

  use_pressure: bool = ...

  """

  Simulate pressure inside a closed cloth mesh

  """

  use_pressure_volume: bool = ...

  """

  Use the Target Volume parameter as the initial volume, instead of calculating it from the mesh itself

  """

  use_sewing_springs: bool = ...

  """

  Pulls loose edges together

  """

  vertex_group_bending: str = ...

  """

  Vertex group for fine control over bending stiffness

  """

  vertex_group_intern: str = ...

  """

  Vertex group for fine control over the internal spring stiffness

  """

  vertex_group_mass: str = ...

  """

  Vertex Group for pinning of vertices

  """

  vertex_group_pressure: str = ...

  """

  Vertex Group for where to apply pressure. Zero weight means no pressure while a weight of one means full pressure. Faces with a vertex that has zero weight will be excluded from the volume calculation

  """

  vertex_group_shear_stiffness: str = ...

  """

  Vertex group for fine control over shear stiffness

  """

  vertex_group_shrink: str = ...

  """

  Vertex Group for shrinking cloth

  """

  vertex_group_structural_stiffness: str = ...

  """

  Vertex group for fine control over structural stiffness

  """

  voxel_cell_size: float = ...

  """

  Size of the voxel grid cells for interaction effects

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ClothSolverResult(bpy_struct):

  """

  Result of cloth solver iteration

  """

  avg_error: float = ...

  """

  Average error during substeps

  """

  avg_iterations: float = ...

  """

  Average iterations during substeps

  """

  max_error: float = ...

  """

  Maximum error during substeps

  """

  max_iterations: int = ...

  """

  Maximum iterations during substeps

  """

  min_error: float = ...

  """

  Minimum error during substeps

  """

  min_iterations: int = ...

  """

  Minimum iterations during substeps

  """

  status: typing.Set[str] = ...

  """

  Status of the solver iteration

  * ``SUCCESS``
Success -- Computation was successful.

  * ``NUMERICAL_ISSUE``
Numerical Issue -- The provided data did not satisfy the prerequisites.

  * ``NO_CONVERGENCE``
No Convergence -- Iterative procedure did not converge.

  * ``INVALID_INPUT``
Invalid Input -- The inputs are invalid, or the algorithm has been improperly called.

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class CollectionChildren(bpy_struct):

  """

  Collection of child collections

  """

  def link(self, child: Collection) -> None:

    """

    Add this collection as child of this collection

    """

    ...

  def unlink(self, child: Collection) -> None:

    """

    Remove this child collection from a collection

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class CollectionObjects(bpy_struct):

  """

  Collection of collection objects

  """

  def link(self, object: Object) -> None:

    """

    Add this object to a collection

    """

    ...

  def unlink(self, object: Object) -> None:

    """

    Remove this object from a collection

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class CollisionSettings(bpy_struct):

  """

  Collision settings for object in physics simulation

  """

  absorption: float = ...

  """

  How much of effector force gets lost during collision with this object (in percent)

  """

  cloth_friction: float = ...

  """

  Friction for cloth collisions

  """

  damping: float = ...

  """

  Amount of damping during collision

  """

  damping_factor: float = ...

  """

  Amount of damping during particle collision

  """

  damping_random: float = ...

  """

  Random variation of damping

  """

  friction_factor: float = ...

  """

  Amount of friction during particle collision

  """

  friction_random: float = ...

  """

  Random variation of friction

  """

  permeability: float = ...

  """

  Chance that the particle will pass through the mesh

  """

  stickiness: float = ...

  """

  Amount of stickiness to surface collision

  """

  thickness_inner: float = ...

  """

  Inner face thickness (only used by softbodies)

  """

  thickness_outer: float = ...

  """

  Outer face thickness

  """

  use: bool = ...

  """

  Enable this objects as a collider for physics systems

  """

  use_culling: bool = ...

  """

  Cloth collision acts with respect to the collider normals (improves penetration recovery)

  """

  use_normal: bool = ...

  """

  Cloth collision impulses act in the direction of the collider normals (more reliable in some cases)

  """

  use_particle_kill: bool = ...

  """

  Kill collided particles

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ColorManagedDisplaySettings(bpy_struct):

  """

  Color management specific to display device

  """

  display_device: str = ...

  """

  Display device name

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ColorManagedInputColorspaceSettings(bpy_struct):

  """

  Input color space settings

  """

  is_data: bool = ...

  """

  Treat image as non-color data without color management, like normal or displacement maps

  """

  name: str = ...

  """

  Color space in the image file, to convert to and from when saving and loading the image

  * ``Filmic Log``
Filmic Log -- Log based filmic shaper with 16.5 stops of latitude, and 25 stops of dynamic range.

  * ``Linear``
Linear -- Rec. 709 (Full Range), Blender native linear space.

  * ``Linear ACES``
Linear ACES -- ACES linear space.

  * ``Non-Color``
Non-Color -- Color space used for images which contains non-color data (i,e, normal maps).

  * ``Raw``
Raw.

  * ``sRGB``
sRGB -- Standard RGB Display Space.

  * ``XYZ``
XYZ.

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ColorManagedSequencerColorspaceSettings(bpy_struct):

  """

  Input color space settings

  """

  name: str = ...

  """

  Color space that the sequencer operates in

  * ``Filmic Log``
Filmic Log -- Log based filmic shaper with 16.5 stops of latitude, and 25 stops of dynamic range.

  * ``Linear``
Linear -- Rec. 709 (Full Range), Blender native linear space.

  * ``Linear ACES``
Linear ACES -- ACES linear space.

  * ``Non-Color``
Non-Color -- Color space used for images which contains non-color data (i,e, normal maps).

  * ``Raw``
Raw.

  * ``sRGB``
sRGB -- Standard RGB Display Space.

  * ``XYZ``
XYZ.

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ColorManagedViewSettings(bpy_struct):

  """

  Color management settings used for displaying images on the display

  """

  curve_mapping: CurveMapping = ...

  """

  Color curve mapping applied before display transform

  """

  exposure: float = ...

  """

  Exposure (stops) applied before display transform

  """

  gamma: float = ...

  """

  Amount of gamma modification applied after display transform

  """

  look: str = ...

  """

  Additional transform applied before view transform for artistic needs

  * ``NONE``
None -- Do not modify image in an artistic manner.

  """

  use_curve_mapping: bool = ...

  """

  Use RGB curved for pre-display transformation

  """

  view_transform: str = ...

  """

  View used when converting image to a display space

  * ``NONE``
None -- Do not perform any color transform on display, use old non-color managed technique for display.

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ColorMapping(bpy_struct):

  """

  Color mapping settings

  """

  blend_color: typing.Tuple[float, float, float] = ...

  """

  Blend color to mix with texture output color

  """

  blend_factor: float = ...

  blend_type: str = ...

  """

  Mode used to mix with texture output color

  """

  brightness: float = ...

  """

  Adjust the brightness of the texture

  """

  color_ramp: ColorRamp = ...

  contrast: float = ...

  """

  Adjust the contrast of the texture

  """

  saturation: float = ...

  """

  Adjust the saturation of colors in the texture

  """

  use_color_ramp: bool = ...

  """

  Toggle color ramp operations

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ColorRamp(bpy_struct):

  """

  Color ramp mapping a scalar value to a color

  """

  color_mode: str = ...

  """

  Set color mode to use for interpolation

  """

  elements: typing.Union[ColorRampElements, typing.Sequence[ColorRampElement], typing.Mapping[str, ColorRampElement], bpy_prop_collection] = ...

  hue_interpolation: str = ...

  """

  Set color interpolation

  """

  interpolation: str = ...

  """

  Set interpolation between color stops

  """

  def evaluate(self, position: float) -> typing.Tuple[float, float, float, float]:

    """

    Evaluate ColorRamp

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ColorRampElement(bpy_struct):

  """

  Element defining a color at a position in the color ramp

  """

  alpha: float = ...

  """

  Set alpha of selected color stop

  """

  color: typing.Tuple[float, float, float, float] = ...

  """

  Set color of selected color stop

  """

  position: float = ...

  """

  Set position of selected color stop

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ColorRampElements(bpy_struct):

  """

  Collection of Color Ramp Elements

  """

  def new(self, position: float) -> ColorRampElement:

    """

    Add element to ColorRamp

    """

    ...

  def remove(self, element: ColorRampElement) -> None:

    """

    Delete element from ColorRamp

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class CompositorNodeOutputFileFileSlots(bpy_struct):

  """

  Collection of File Output node slots

  """

  def new(self, name: str) -> NodeSocket:

    """

    Add a file slot to this node

    """

    ...

  def remove(self, socket: NodeSocket) -> None:

    """

    Remove a file slot from this node

    """

    ...

  def clear(self) -> None:

    """

    Remove all file slots from this node

    """

    ...

  def move(self, from_index: int, to_index: int) -> None:

    """

    Move a file slot to another position

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class CompositorNodeOutputFileLayerSlots(bpy_struct):

  """

  Collection of File Output node slots

  """

  def new(self, name: str) -> NodeSocket:

    """

    Add a file slot to this node

    """

    ...

  def remove(self, socket: NodeSocket) -> None:

    """

    Remove a file slot from this node

    """

    ...

  def clear(self) -> None:

    """

    Remove all file slots from this node

    """

    ...

  def move(self, from_index: int, to_index: int) -> None:

    """

    Move a file slot to another position

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ConsoleLine(bpy_struct):

  """

  Input line for the interactive console

  """

  body: str = ...

  """

  Text in the line

  """

  current_character: int = ...

  type: str = ...

  """

  Console line type when used in scrollback

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Constraint(bpy_struct):

  """

  Constraint modifying the transformation of objects and bones

  """

  active: bool = ...

  """

  Constraint is the one being edited

  """

  enabled: bool = ...

  """

  Use the results of this constraint

  """

  error_location: float = ...

  """

  Amount of residual error in Blender space unit for constraints that work on position

  """

  error_rotation: float = ...

  """

  Amount of residual error in radians for constraints that work on orientation

  """

  influence: float = ...

  """

  Amount of influence constraint will have on the final solution

  """

  is_override_data: bool = ...

  """

  In a local override object, whether this constraint comes from the linked reference object, or is local to the override

  """

  is_proxy_local: bool = ...

  """

  Constraint was added in this proxy instance (i.e. did not belong to source Armature)

  """

  is_valid: bool = ...

  """

  Constraint has valid settings and can be evaluated

  """

  mute: bool = ...

  """

  Enable/Disable Constraint

  """

  name: str = ...

  """

  Constraint name

  """

  owner_space: str = ...

  """

  Space that owner is evaluated in

  * ``WORLD``
World Space -- The constraint is applied relative to the world coordinate system.

  * ``CUSTOM``
Custom Space -- The constraint is applied in local space of a custom object/bone/vertex group.

  * ``POSE``
Pose Space -- The constraint is applied in Pose Space, the object transformation is ignored.

  * ``LOCAL_WITH_PARENT``
Local With Parent -- The constraint is applied relative to the rest pose local coordinate system of the bone, thus including the parent-induced transformation.

  * ``LOCAL``
Local Space -- The constraint is applied relative to the local coordinate system of the object.

  """

  show_expanded: bool = ...

  """

  Constraint's panel is expanded in UI

  """

  space_object: Object = ...

  """

  Object for Custom Space

  """

  space_subtarget: str = ...

  """

  Armature bone, mesh or lattice vertex group, ...

  """

  target_space: str = ...

  """

  Space that target is evaluated in

  * ``WORLD``
World Space -- The transformation of the target is evaluated relative to the world coordinate system.

  * ``CUSTOM``
Custom Space -- The transformation of the target is evaluated relative to a custom object/bone/vertex group.

  * ``POSE``
Pose Space -- The transformation of the target is only evaluated in the Pose Space, the target armature object transformation is ignored.

  * ``LOCAL_WITH_PARENT``
Local With Parent -- The transformation of the target bone is evaluated relative to its rest pose local coordinate system, thus including the parent-induced transformation.

  * ``LOCAL``
Local Space -- The transformation of the target is evaluated relative to its local coordinate system.

  * ``LOCAL_OWNER_ORIENT``
Local Space (Owner Orientation) -- The transformation of the target bone is evaluated relative to its local coordinate system, followed by a correction for the difference in target and owner rest pose orientations. When applied as local transform to the owner produces the same global motion as the target if the parents are still in rest pose.

  """

  type: str = ...

  """

  * ``CAMERA_SOLVER``
Camera Solver.

  * ``FOLLOW_TRACK``
Follow Track.

  * ``OBJECT_SOLVER``
Object Solver.

  * ``COPY_LOCATION``
Copy Location -- Copy the location of a target (with an optional offset), so that they move together.

  * ``COPY_ROTATION``
Copy Rotation -- Copy the rotation of a target (with an optional offset), so that they rotate together.

  * ``COPY_SCALE``
Copy Scale -- Copy the scale factors of a target (with an optional offset), so that they are scaled by the same amount.

  * ``COPY_TRANSFORMS``
Copy Transforms -- Copy all the transformations of a target, so that they move together.

  * ``LIMIT_DISTANCE``
Limit Distance -- Restrict movements to within a certain distance of a target (at the time of constraint evaluation only).

  * ``LIMIT_LOCATION``
Limit Location -- Restrict movement along each axis within given ranges.

  * ``LIMIT_ROTATION``
Limit Rotation -- Restrict rotation along each axis within given ranges.

  * ``LIMIT_SCALE``
Limit Scale -- Restrict scaling along each axis with given ranges.

  * ``MAINTAIN_VOLUME``
Maintain Volume -- Compensate for scaling one axis by applying suitable scaling to the other two axes.

  * ``TRANSFORM``
Transformation -- Use one transform property from target to control another (or same) property on owner.

  * ``TRANSFORM_CACHE``
Transform Cache -- Look up the transformation matrix from an external file.

  * ``CLAMP_TO``
Clamp To -- Restrict movements to lie along a curve by remapping location along curve's longest axis.

  * ``DAMPED_TRACK``
Damped Track -- Point towards a target by performing the smallest rotation necessary.

  * ``IK``
Inverse Kinematics -- Control a chain of bones by specifying the endpoint target (Bones only).

  * ``LOCKED_TRACK``
Locked Track -- Rotate around the specified ('locked') axis to point towards a target.

  * ``SPLINE_IK``
Spline IK -- Align chain of bones along a curve (Bones only).

  * ``STRETCH_TO``
Stretch To -- Stretch along Y-Axis to point towards a target.

  * ``TRACK_TO``
Track To -- Legacy tracking constraint prone to twisting artifacts.

  * ``ACTION``
Action -- Use transform property of target to look up pose for owner from an Action.

  * ``ARMATURE``
Armature -- Apply weight-blended transformation from multiple bones like the Armature modifier.

  * ``CHILD_OF``
Child Of -- Make target the 'detachable' parent of owner.

  * ``FLOOR``
Floor -- Use position (and optionally rotation) of target to define a 'wall' or 'floor' that the owner can not cross.

  * ``FOLLOW_PATH``
Follow Path -- Use to animate an object/bone following a path.

  * ``PIVOT``
Pivot -- Change pivot point for transforms (buggy).

  * ``SHRINKWRAP``
Shrinkwrap -- Restrict movements to surface of target mesh.

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ConstraintTarget(bpy_struct):

  """

  Target object for multi-target constraints

  """

  subtarget: str = ...

  """

  Armature bone, mesh or lattice vertex group, ...

  """

  target: Object = ...

  """

  Target object

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ConstraintTargetBone(bpy_struct):

  """

  Target bone for multi-target constraints

  """

  subtarget: str = ...

  """

  Target armature bone

  """

  target: Object = ...

  """

  Target armature

  """

  weight: float = ...

  """

  Blending weight of this bone

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Context(bpy_struct):

  """

  Current windowmanager and data context

  """

  area: Area = ...

  asset_file_handle: FileSelectEntry = ...

  """

  The file of an active asset. Avoid using this, it will be replaced by a proper AssetHandle design

  """

  blend_data: BlendData = ...

  collection: Collection = ...

  engine: str = ...

  gizmo_group: GizmoGroup = ...

  layer_collection: LayerCollection = ...

  mode: str = ...

  preferences: Preferences = ...

  region: Region = ...

  region_data: RegionView3D = ...

  scene: Scene = ...

  screen: Screen = ...

  space_data: Space = ...

  tool_settings: ToolSettings = ...

  view_layer: ViewLayer = ...

  window: Window = ...

  window_manager: WindowManager = ...

  workspace: WorkSpace = ...

  def evaluated_depsgraph_get(self) -> Depsgraph:

    """

    Get the dependency graph for the current scene and view layer, to access to data-blocks with animation and modifiers applied. If any data-blocks have been edited, the dependency graph will be updated. This invalidates all references to evaluated data-blocks from the dependency graph.

    """

    ...

  def copy(self) -> None:

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class CryptomatteEntry(bpy_struct):

  encoded_hash: float = ...

  name: str = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class CurveMap(bpy_struct):

  """

  Curve in a curve mapping

  """

  points: typing.Union[CurveMapPoints, typing.Sequence[CurveMapPoint], typing.Mapping[str, CurveMapPoint], bpy_prop_collection] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class CurveMapping(bpy_struct):

  """

  Curve mapping to map color, vector and scalar values to other values using a user defined curve

  """

  black_level: typing.Tuple[float, float, float] = ...

  """

  For RGB curves, the color that black is mapped to

  """

  clip_max_x: float = ...

  clip_max_y: float = ...

  clip_min_x: float = ...

  clip_min_y: float = ...

  curves: typing.Union[typing.Sequence[CurveMap], typing.Mapping[str, CurveMap], bpy_prop_collection] = ...

  extend: str = ...

  """

  Extrapolate the curve or extend it horizontally

  """

  tone: str = ...

  """

  Tone of the curve

  """

  use_clip: bool = ...

  """

  Force the curve view to fit a defined boundary

  """

  white_level: typing.Tuple[float, float, float] = ...

  """

  For RGB curves, the color that white is mapped to

  """

  def update(self) -> None:

    """

    Update curve mapping after making changes

    """

    ...

  def reset_view(self) -> None:

    """

    Reset the curve mapping grid to its clipping size

    """

    ...

  def initialize(self) -> None:

    """

    Initialize curve

    """

    ...

  def evaluate(self, curve: CurveMap, position: float) -> float:

    """

    Evaluate curve at given location

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class CurveMapPoint(bpy_struct):

  """

  Point of a curve used for a curve mapping

  """

  handle_type: str = ...

  """

  Curve interpolation at this point: Bezier or vector

  """

  location: typing.Tuple[float, float] = ...

  """

  X/Y coordinates of the curve point

  """

  select: bool = ...

  """

  Selection state of the curve point

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class CurveMapPoints(bpy_struct):

  """

  Collection of Curve Map Points

  """

  def new(self, position: float, value: float) -> CurveMapPoint:

    """

    Add point to CurveMap

    """

    ...

  def remove(self, point: CurveMapPoint) -> None:

    """

    Delete point from CurveMap

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class CurvePaintSettings(bpy_struct):

  corner_angle: float = ...

  """

  Angles above this are considered corners

  """

  curve_type: str = ...

  """

  Type of curve to use for new strokes

  """

  depth_mode: str = ...

  """

  Method of projecting depth

  """

  error_threshold: int = ...

  """

  Allow deviation for a smoother, less precise line

  """

  fit_method: str = ...

  """

  Curve fitting method

  * ``REFIT``
Refit -- Incrementally refit the curve (high quality).

  * ``SPLIT``
Split -- Split the curve until the tolerance is met (fast).

  """

  radius_max: float = ...

  """

  Radius to use when the maximum pressure is applied (or when a tablet isn't used)

  """

  radius_min: float = ...

  """

  Minimum radius when the minimum pressure is applied (also the minimum when tapering)

  """

  radius_taper_end: float = ...

  """

  Taper factor for the radius of each point along the curve

  """

  radius_taper_start: float = ...

  """

  Taper factor for the radius of each point along the curve

  """

  surface_offset: float = ...

  """

  Offset the stroke from the surface

  """

  surface_plane: str = ...

  """

  Plane for projected stroke

  * ``NORMAL_VIEW``
Normal/View -- Display perpendicular to the surface.

  * ``NORMAL_SURFACE``
Normal/Surface -- Display aligned to the surface.

  * ``VIEW``
View -- Display aligned to the viewport.

  """

  use_corners_detect: bool = ...

  """

  Detect corners and use non-aligned handles

  """

  use_offset_absolute: bool = ...

  """

  Apply a fixed offset (don't scale by the radius)

  """

  use_pressure_radius: bool = ...

  """

  Map tablet pressure to curve radius

  """

  use_stroke_endpoints: bool = ...

  """

  Use the start of the stroke for the depth

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class CurveProfile(bpy_struct):

  """

  Profile Path editor used to build a profile path

  """

  points: typing.Union[CurveProfilePoints, typing.Sequence[CurveProfilePoint], typing.Mapping[str, CurveProfilePoint], bpy_prop_collection] = ...

  """

  Profile control points

  """

  preset: str = ...

  """

  * ``LINE``
Line -- Default.

  * ``SUPPORTS``
Support Loops -- Loops on each side of the profile.

  * ``CORNICE``
Cornice Molding.

  * ``CROWN``
Crown Molding.

  * ``STEPS``
Steps -- A number of steps defined by the segments.

  """

  segments: typing.Union[typing.Sequence[CurveProfilePoint], typing.Mapping[str, CurveProfilePoint], bpy_prop_collection] = ...

  """

  Segments sampled from control points

  """

  use_clip: bool = ...

  """

  Force the path view to fit a defined boundary

  """

  use_sample_even_lengths: bool = ...

  """

  Sample edges with even lengths

  """

  use_sample_straight_edges: bool = ...

  """

  Sample edges with vector handles

  """

  def update(self) -> None:

    """

    Refresh internal data, remove doubles and clip points

    """

    ...

  def reset_view(self) -> None:

    """

    Reset the curve profile grid to its clipping size

    """

    ...

  def initialize(self, totsegments: int) -> None:

    """

    Set the number of display segments and fill tables

    """

    ...

  def evaluate(self, length_portion: float) -> typing.Tuple[float, float]:

    """

    Evaluate the at the given portion of the path length

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class CurveProfilePoint(bpy_struct):

  """

  Point of a path used to define a profile

  """

  handle_type_1: str = ...

  """

  Path interpolation at this point

  """

  handle_type_2: str = ...

  """

  Path interpolation at this point

  """

  location: typing.Tuple[float, float] = ...

  """

  X/Y coordinates of the path point

  """

  select: bool = ...

  """

  Selection state of the path point

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class CurveProfilePoints(bpy_struct):

  """

  Collection of Profile Points

  """

  def add(self, x: float, y: float) -> CurveProfilePoint:

    """

    Add point to the profile

    """

    ...

  def remove(self, point: CurveProfilePoint) -> None:

    """

    Delete point from the profile

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class CurveSplines(bpy_struct):

  """

  Collection of curve splines

  """

  active: Spline = ...

  """

  Active curve spline

  """

  def new(self, type: str) -> Spline:

    """

    Add a new spline to the curve

    """

    ...

  def remove(self, spline: Spline) -> None:

    """

    Remove a spline from a curve

    """

    ...

  def clear(self) -> None:

    """

    Remove all splines from a curve

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class DashGpencilModifierSegment(bpy_struct):

  """

  Configuration for a single dash segment

  """

  dash: int = ...

  """

  The number of consecutive points from the original stroke to include in this segment

  """

  gap: int = ...

  """

  The number of points skipped after this segment

  """

  material_index: int = ...

  """

  Use this index on generated segment. -1 means using the existing material

  """

  name: str = ...

  """

  Name of the dash segment

  """

  opacity: float = ...

  """

  The factor to apply to the original point's opacity for the new points

  """

  radius: float = ...

  """

  The factor to apply to the original point's radius for the new points

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Depsgraph(bpy_struct):

  ids: typing.Union[typing.Sequence[ID], typing.Mapping[str, ID], bpy_prop_collection] = ...

  """

  All evaluated data-blocks

  """

  mode: str = ...

  """

  Evaluation mode

  * ``VIEWPORT``
Viewport -- Viewport non-rendered mode.

  * ``RENDER``
Render -- Render.

  """

  object_instances: typing.Union[typing.Sequence[DepsgraphObjectInstance], typing.Mapping[str, DepsgraphObjectInstance], bpy_prop_collection] = ...

  """

  All object instances to display or render (Warning: Only use this as an iterator, never as a sequence, and do not keep any references to its items)

  """

  objects: typing.Union[typing.Sequence[Object], typing.Mapping[str, Object], bpy_prop_collection] = ...

  """

  Evaluated objects in the dependency graph

  """

  scene: Scene = ...

  """

  Original scene dependency graph is built for

  """

  scene_eval: Scene = ...

  """

  Original scene dependency graph is built for

  """

  updates: typing.Union[typing.Sequence[DepsgraphUpdate], typing.Mapping[str, DepsgraphUpdate], bpy_prop_collection] = ...

  """

  Updates to data-blocks

  """

  view_layer: ViewLayer = ...

  """

  Original view layer dependency graph is built for

  """

  view_layer_eval: ViewLayer = ...

  """

  Original view layer dependency graph is built for

  """

  def debug_relations_graphviz(self, filename: str) -> None:

    """

    debug_relations_graphviz

    """

    ...

  def debug_stats_gnuplot(self, filename: str, output_filename: str) -> None:

    """

    debug_stats_gnuplot

    """

    ...

  def debug_tag_update(self) -> None:

    """

    debug_tag_update

    """

    ...

  def debug_stats(self) -> str:

    """

    Report the number of elements in the Dependency Graph

    """

    ...

  def update(self) -> None:

    """

    Re-evaluate any modified data-blocks, for example for animation or modifiers. This invalidates all references to evaluated data-blocks from this dependency graph.

    """

    ...

  def id_eval_get(self, id: ID) -> ID:

    """

    id_eval_get

    """

    ...

  def id_type_updated(self, id_type: str) -> bool:

    """

    id_type_updated

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class DepsgraphObjectInstance(bpy_struct):

  """

  Extended information about dependency graph object iterator (Warning: All data here is 'evaluated' one, not original .blend IDs)

  """

  instance_object: Object = ...

  """

  Evaluated object which is being instanced by this iterator

  """

  is_instance: bool = ...

  """

  Denotes if the object is generated by another object

  """

  matrix_world: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]] = ...

  """

  Generated transform matrix in world space

  """

  object: Object = ...

  """

  Evaluated object the iterator points to

  """

  orco: typing.Tuple[float, float, float] = ...

  """

  Generated coordinates in parent object space

  """

  parent: Object = ...

  """

  If the object is an instance, the parent object that generated it

  """

  particle_system: ParticleSystem = ...

  """

  Evaluated particle system that this object was instanced from

  """

  persistent_id: typing.Tuple[int, ...] = ...

  """

  Persistent identifier for inter-frame matching of objects with motion blur

  """

  random_id: int = ...

  """

  Random id for this instance, typically for randomized shading

  """

  show_particles: bool = ...

  """

  Particles part of the object should be visible in the render

  """

  show_self: bool = ...

  """

  The object geometry itself should be visible in the render

  """

  uv: typing.Tuple[float, float] = ...

  """

  UV coordinates in parent object space

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class DepsgraphUpdate(bpy_struct):

  """

  Information about ID that was updated

  """

  id: ID = ...

  """

  Updated data-block

  """

  is_updated_geometry: bool = ...

  """

  Object geometry is updated

  """

  is_updated_shading: bool = ...

  """

  Object shading is updated

  """

  is_updated_transform: bool = ...

  """

  Object transformation is updated

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class DisplaySafeAreas(bpy_struct):

  """

  Safe areas used in 3D view and the sequencer

  """

  action: typing.Tuple[float, float] = ...

  """

  Safe area for general elements

  """

  action_center: typing.Tuple[float, float] = ...

  """

  Safe area for general elements in a different aspect ratio

  """

  title: typing.Tuple[float, float] = ...

  """

  Safe area for text and graphics

  """

  title_center: typing.Tuple[float, float] = ...

  """

  Safe area for text and graphics in a different aspect ratio

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class DopeSheet(bpy_struct):

  """

  Settings for filtering the channels shown in animation editors

  """

  filter_collection: Collection = ...

  """

  Collection that included object should be a member of

  """

  filter_fcurve_name: str = ...

  """

  F-Curve live filtering string

  """

  filter_text: str = ...

  """

  Live filtering string

  """

  show_armatures: bool = ...

  """

  Include visualization of armature related animation data

  """

  show_cache_files: bool = ...

  """

  Include visualization of cache file related animation data

  """

  show_cameras: bool = ...

  """

  Include visualization of camera related animation data

  """

  show_curves: bool = ...

  """

  Include visualization of curve related animation data

  """

  show_datablock_filters: bool = ...

  """

  Show options for whether channels related to certain types of data are included

  """

  show_expanded_summary: bool = ...

  """

  Collapse summary when shown, so all other channels get hidden (Dope Sheet editors only)

  """

  show_gpencil: bool = ...

  """

  Include visualization of Grease Pencil related animation data and frames

  """

  show_hairs: bool = ...

  """

  Include visualization of hair related animation data

  """

  show_hidden: bool = ...

  """

  Include channels from objects/bone that are not visible

  """

  show_lattices: bool = ...

  """

  Include visualization of lattice related animation data

  """

  show_lights: bool = ...

  """

  Include visualization of light related animation data

  """

  show_linestyles: bool = ...

  """

  Include visualization of Line Style related Animation data

  """

  show_materials: bool = ...

  """

  Include visualization of material related animation data

  """

  show_meshes: bool = ...

  """

  Include visualization of mesh related animation data

  """

  show_metaballs: bool = ...

  """

  Include visualization of metaball related animation data

  """

  show_missing_nla: bool = ...

  """

  Include animation data-blocks with no NLA data (NLA editor only)

  """

  show_modifiers: bool = ...

  """

  Include visualization of animation data related to data-blocks linked to modifiers

  """

  show_movieclips: bool = ...

  """

  Include visualization of movie clip related animation data

  """

  show_nodes: bool = ...

  """

  Include visualization of node related animation data

  """

  show_only_errors: bool = ...

  """

  Only include F-Curves and drivers that are disabled or have errors

  """

  show_only_selected: bool = ...

  """

  Only include channels relating to selected objects and data

  """

  show_particles: bool = ...

  """

  Include visualization of particle related animation data

  """

  show_pointclouds: bool = ...

  """

  Include visualization of point cloud related animation data

  """

  show_scenes: bool = ...

  """

  Include visualization of scene related animation data

  """

  show_shapekeys: bool = ...

  """

  Include visualization of shape key related animation data

  """

  show_speakers: bool = ...

  """

  Include visualization of speaker related animation data

  """

  show_summary: bool = ...

  """

  Display an additional 'summary' line (Dope Sheet editors only)

  """

  show_textures: bool = ...

  """

  Include visualization of texture related animation data

  """

  show_transforms: bool = ...

  """

  Include visualization of object-level animation data (mostly transforms)

  """

  show_volumes: bool = ...

  """

  Include visualization of volume related animation data

  """

  show_worlds: bool = ...

  """

  Include visualization of world related animation data

  """

  source: ID = ...

  """

  ID-Block representing source data, usually ID_SCE (i.e. Scene)

  """

  use_datablock_sort: bool = ...

  """

  Alphabetically sorts data-blocks - mainly objects in the scene (disable to increase viewport speed)

  """

  use_filter_invert: bool = ...

  """

  Invert filter search

  """

  use_multi_word_filter: bool = ...

  """

  Perform fuzzy/multi-word matching.
Warning: May be slow

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Driver(bpy_struct):

  """

  Driver for the value of a setting based on an external value

  """

  expression: str = ...

  """

  Expression to use for Scripted Expression

  """

  is_simple_expression: bool = ...

  """

  The scripted expression can be evaluated without using the full python interpreter

  """

  is_valid: bool = ...

  """

  Driver could not be evaluated in past, so should be skipped

  """

  type: str = ...

  """

  Driver type

  """

  use_self: bool = ...

  """

  Include a 'self' variable in the name-space, so drivers can easily reference the data being modified (object, bone, etc...)

  """

  variables: typing.Union[ChannelDriverVariables, typing.Sequence[DriverVariable], typing.Mapping[str, DriverVariable], bpy_prop_collection] = ...

  """

  Properties acting as inputs for this driver

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class DriverTarget(bpy_struct):

  """

  Source of input values for driver variables

  """

  bone_target: str = ...

  """

  Name of PoseBone to use as target

  """

  data_path: str = ...

  """

  RNA Path (from ID-block) to property used

  """

  id: ID = ...

  """

  ID-block that the specific property used can be found from (id_type property must be set first)

  """

  id_type: str = ...

  """

  Type of ID-block that can be used

  """

  rotation_mode: str = ...

  """

  Mode for calculating rotation channel values

  * ``AUTO``
Auto Euler -- Euler using the rotation order of the target.

  * ``XYZ``
XYZ Euler -- Euler using the XYZ rotation order.

  * ``XZY``
XZY Euler -- Euler using the XZY rotation order.

  * ``YXZ``
YXZ Euler -- Euler using the YXZ rotation order.

  * ``YZX``
YZX Euler -- Euler using the YZX rotation order.

  * ``ZXY``
ZXY Euler -- Euler using the ZXY rotation order.

  * ``ZYX``
ZYX Euler -- Euler using the ZYX rotation order.

  * ``QUATERNION``
Quaternion -- Quaternion rotation.

  * ``SWING_TWIST_X``
Swing and X Twist -- Decompose into a swing rotation to aim the X axis, followed by twist around it.

  * ``SWING_TWIST_Y``
Swing and Y Twist -- Decompose into a swing rotation to aim the Y axis, followed by twist around it.

  * ``SWING_TWIST_Z``
Swing and Z Twist -- Decompose into a swing rotation to aim the Z axis, followed by twist around it.

  """

  transform_space: str = ...

  """

  Space in which transforms are used

  * ``WORLD_SPACE``
World Space -- Transforms include effects of parenting/restpose and constraints.

  * ``TRANSFORM_SPACE``
Transform Space -- Transforms don't include parenting/restpose or constraints.

  * ``LOCAL_SPACE``
Local Space -- Transforms include effects of constraints but not parenting/restpose.

  """

  transform_type: str = ...

  """

  Driver variable type

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class DriverVariable(bpy_struct):

  """

  Variable from some source/target for driver relationship

  """

  is_name_valid: bool = ...

  """

  Is this a valid name for a driver variable

  """

  name: str = ...

  """

  Name to use in scripted expressions/functions (no spaces or dots are allowed, and must start with a letter)

  """

  targets: typing.Union[typing.Sequence[DriverTarget], typing.Mapping[str, DriverTarget], bpy_prop_collection] = ...

  """

  Sources of input data for evaluating this variable

  """

  type: str = ...

  """

  Driver variable type

  * ``SINGLE_PROP``
Single Property -- Use the value from some RNA property (Default).

  * ``TRANSFORMS``
Transform Channel -- Final transformation value of object or bone.

  * ``ROTATION_DIFF``
Rotational Difference -- Use the angle between two bones.

  * ``LOC_DIFF``
Distance -- Distance between two bones or objects.

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class DynamicPaintBrushSettings(bpy_struct):

  """

  Brush settings

  """

  invert_proximity: bool = ...

  """

  Proximity falloff is applied inside the volume

  """

  paint_alpha: float = ...

  """

  Paint alpha

  """

  paint_color: typing.Tuple[float, float, float] = ...

  """

  Color of the paint

  """

  paint_distance: float = ...

  """

  Maximum distance from brush to mesh surface to affect paint

  """

  paint_ramp: ColorRamp = ...

  """

  Color ramp used to define proximity falloff

  """

  paint_source: str = ...

  paint_wetness: float = ...

  """

  Paint wetness, visible in wetmap (some effects only affect wet paint)

  """

  particle_system: ParticleSystem = ...

  """

  The particle system to paint with

  """

  proximity_falloff: str = ...

  """

  Proximity falloff type

  """

  ray_direction: str = ...

  """

  Ray direction to use for projection (if brush object is located in that direction it's painted)

  """

  smooth_radius: float = ...

  """

  Smooth falloff added after solid radius

  """

  smudge_strength: float = ...

  """

  Smudge effect strength

  """

  solid_radius: float = ...

  """

  Radius that will be painted solid

  """

  use_absolute_alpha: bool = ...

  """

  Only increase alpha value if paint alpha is higher than existing

  """

  use_negative_volume: bool = ...

  """

  Negate influence inside the volume

  """

  use_paint_erase: bool = ...

  """

  Erase / remove paint instead of adding it

  """

  use_particle_radius: bool = ...

  """

  Use radius from particle settings

  """

  use_proximity_project: bool = ...

  """

  Brush is projected to canvas from defined direction within brush proximity

  """

  use_proximity_ramp_alpha: bool = ...

  """

  Only read color ramp alpha

  """

  use_smudge: bool = ...

  """

  Make this brush to smudge existing paint as it moves

  """

  use_velocity_alpha: bool = ...

  """

  Multiply brush influence by velocity color ramp alpha

  """

  use_velocity_color: bool = ...

  """

  Replace brush color by velocity color ramp

  """

  use_velocity_depth: bool = ...

  """

  Multiply brush intersection depth (displace, waves) by velocity ramp alpha

  """

  velocity_max: float = ...

  """

  Velocity considered as maximum influence (Blender units per frame)

  """

  velocity_ramp: ColorRamp = ...

  """

  Color ramp used to define brush velocity effect

  """

  wave_clamp: float = ...

  """

  Maximum level of surface intersection used to influence waves (use 0.0 to disable)

  """

  wave_factor: float = ...

  """

  Multiplier for wave influence of this brush

  """

  wave_type: str = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class DynamicPaintCanvasSettings(bpy_struct):

  """

  Dynamic Paint canvas settings

  """

  canvas_surfaces: typing.Union[DynamicPaintSurfaces, typing.Sequence[DynamicPaintSurface], typing.Mapping[str, DynamicPaintSurface], bpy_prop_collection] = ...

  """

  Paint surface list

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class DynamicPaintSurface(bpy_struct):

  """

  A canvas surface layer

  """

  brush_collection: Collection = ...

  """

  Only use brush objects from this collection

  """

  brush_influence_scale: float = ...

  """

  Adjust influence brush objects have on this surface

  """

  brush_radius_scale: float = ...

  """

  Adjust radius of proximity brushes or particles for this surface

  """

  color_dry_threshold: float = ...

  """

  The wetness level when colors start to shift to the background

  """

  color_spread_speed: float = ...

  """

  How fast colors get mixed within wet paint

  """

  depth_clamp: float = ...

  """

  Maximum level of depth intersection in object space (use 0.0 to disable)

  """

  displace_factor: float = ...

  """

  Strength of displace when applied to the mesh

  """

  displace_type: str = ...

  dissolve_speed: int = ...

  """

  Approximately in how many frames should dissolve happen

  """

  drip_acceleration: float = ...

  """

  How much surface acceleration affects dripping

  """

  drip_velocity: float = ...

  """

  How much surface velocity affects dripping

  """

  dry_speed: int = ...

  """

  Approximately in how many frames should drying happen

  """

  effect_ui: str = ...

  effector_weights: EffectorWeights = ...

  frame_end: int = ...

  """

  Simulation end frame

  """

  frame_start: int = ...

  """

  Simulation start frame

  """

  frame_substeps: int = ...

  """

  Do extra frames between scene frames to ensure smooth motion

  """

  image_fileformat: str = ...

  image_output_path: str = ...

  """

  Directory to save the textures

  """

  image_resolution: int = ...

  """

  Output image resolution

  """

  init_color: typing.Tuple[float, float, float, float] = ...

  """

  Initial color of the surface

  """

  init_color_type: str = ...

  init_layername: str = ...

  init_texture: Texture = ...

  is_active: bool = ...

  """

  Toggle whether surface is processed or ignored

  """

  is_cache_user: bool = ...

  name: str = ...

  """

  Surface name

  """

  output_name_a: str = ...

  """

  Name used to save output from this surface

  """

  output_name_b: str = ...

  """

  Name used to save output from this surface

  """

  point_cache: PointCache = ...

  shrink_speed: float = ...

  """

  How fast shrink effect moves on the canvas surface

  """

  spread_speed: float = ...

  """

  How fast spread effect moves on the canvas surface

  """

  surface_format: str = ...

  """

  Surface Format

  """

  surface_type: str = ...

  """

  Surface Type

  """

  use_antialiasing: bool = ...

  """

  Use 5x multisampling to smooth paint edges

  """

  use_dissolve: bool = ...

  """

  Enable to make surface changes disappear over time

  """

  use_dissolve_log: bool = ...

  """

  Use logarithmic dissolve (makes high values to fade faster than low values)

  """

  use_drip: bool = ...

  """

  Process drip effect (drip wet paint to gravity direction)

  """

  use_dry_log: bool = ...

  """

  Use logarithmic drying (makes high values to dry faster than low values)

  """

  use_drying: bool = ...

  """

  Enable to make surface wetness dry over time

  """

  use_incremental_displace: bool = ...

  """

  New displace is added cumulatively on top of existing

  """

  use_output_a: bool = ...

  """

  Save this output layer

  """

  use_output_b: bool = ...

  """

  Save this output layer

  """

  use_premultiply: bool = ...

  """

  Multiply color by alpha (recommended for Blender input)

  """

  use_shrink: bool = ...

  """

  Process shrink effect (shrink paint areas)

  """

  use_spread: bool = ...

  """

  Process spread effect (spread wet paint around surface)

  """

  use_wave_open_border: bool = ...

  """

  Pass waves through mesh edges

  """

  uv_layer: str = ...

  """

  UV map name

  """

  wave_damping: float = ...

  """

  Wave damping factor

  """

  wave_smoothness: float = ...

  """

  Limit maximum steepness of wave slope between simulation points (use higher values for smoother waves at expense of reduced detail)

  """

  wave_speed: float = ...

  """

  Wave propagation speed

  """

  wave_spring: float = ...

  """

  Spring force that pulls water level back to zero

  """

  wave_timescale: float = ...

  """

  Wave time scaling factor

  """

  def output_exists(self, object: Object, index: int) -> bool:

    """

    Checks if surface output layer of given name exists

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class DynamicPaintSurfaces(bpy_struct):

  """

  Collection of Dynamic Paint Canvas surfaces

  """

  active: DynamicPaintSurface = ...

  """

  Active Dynamic Paint surface being displayed

  """

  active_index: int = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class EditBone(bpy_struct):

  """

  Edit mode bone in an armature data-block

  """

  bbone_curveinx: float = ...

  """

  X-axis handle offset for start of the B-Bone's curve, adjusts curvature

  """

  bbone_curveinz: float = ...

  """

  Z-axis handle offset for start of the B-Bone's curve, adjusts curvature

  """

  bbone_curveoutx: float = ...

  """

  X-axis handle offset for end of the B-Bone's curve, adjusts curvature

  """

  bbone_curveoutz: float = ...

  """

  Z-axis handle offset for end of the B-Bone's curve, adjusts curvature

  """

  bbone_custom_handle_end: EditBone = ...

  """

  Bone that serves as the end handle for the B-Bone curve

  """

  bbone_custom_handle_start: EditBone = ...

  """

  Bone that serves as the start handle for the B-Bone curve

  """

  bbone_easein: float = ...

  """

  Length of first Bezier Handle (for B-Bones only)

  """

  bbone_easeout: float = ...

  """

  Length of second Bezier Handle (for B-Bones only)

  """

  bbone_handle_type_end: str = ...

  """

  Selects how the end handle of the B-Bone is computed

  * ``AUTO``
Automatic -- Use connected parent and children to compute the handle.

  * ``ABSOLUTE``
Absolute -- Use the position of the specified bone to compute the handle.

  * ``RELATIVE``
Relative -- Use the offset of the specified bone from rest pose to compute the handle.

  * ``TANGENT``
Tangent -- Use the orientation of the specified bone to compute the handle, ignoring the location.

  """

  bbone_handle_type_start: str = ...

  """

  Selects how the start handle of the B-Bone is computed

  * ``AUTO``
Automatic -- Use connected parent and children to compute the handle.

  * ``ABSOLUTE``
Absolute -- Use the position of the specified bone to compute the handle.

  * ``RELATIVE``
Relative -- Use the offset of the specified bone from rest pose to compute the handle.

  * ``TANGENT``
Tangent -- Use the orientation of the specified bone to compute the handle, ignoring the location.

  """

  bbone_handle_use_ease_end: bool = ...

  """

  Multiply the B-Bone Ease Out channel by the local Y scale value of the end handle. This is done after the Scale Easing option and isn't affected by it

  """

  bbone_handle_use_ease_start: bool = ...

  """

  Multiply the B-Bone Ease In channel by the local Y scale value of the start handle. This is done after the Scale Easing option and isn't affected by it

  """

  bbone_handle_use_scale_end: typing.Tuple[bool, bool, bool] = ...

  """

  Multiply B-Bone Scale Out channels by the local scale values of the end handle. This is done after the Scale Easing option and isn't affected by it

  """

  bbone_handle_use_scale_start: typing.Tuple[bool, bool, bool] = ...

  """

  Multiply B-Bone Scale In channels by the local scale values of the start handle. This is done after the Scale Easing option and isn't affected by it

  """

  bbone_rollin: float = ...

  """

  Roll offset for the start of the B-Bone, adjusts twist

  """

  bbone_rollout: float = ...

  """

  Roll offset for the end of the B-Bone, adjusts twist

  """

  bbone_scalein: typing.Tuple[float, float, float] = ...

  """

  Scale factors for the start of the B-Bone, adjusts thickness (for tapering effects)

  """

  bbone_scaleout: typing.Tuple[float, float, float] = ...

  """

  Scale factors for the end of the B-Bone, adjusts thickness (for tapering effects)

  """

  bbone_segments: int = ...

  """

  Number of subdivisions of bone (for B-Bones only)

  """

  bbone_x: float = ...

  """

  B-Bone X size

  """

  bbone_z: float = ...

  """

  B-Bone Z size

  """

  envelope_distance: float = ...

  """

  Bone deformation distance (for Envelope deform only)

  """

  envelope_weight: float = ...

  """

  Bone deformation weight (for Envelope deform only)

  """

  head: typing.Tuple[float, float, float] = ...

  """

  Location of head end of the bone

  """

  head_radius: float = ...

  """

  Radius of head of bone (for Envelope deform only)

  """

  hide: bool = ...

  """

  Bone is not visible when in Edit Mode

  """

  hide_select: bool = ...

  """

  Bone is able to be selected

  """

  inherit_scale: str = ...

  """

  Specifies how the bone inherits scaling from the parent bone

  * ``FULL``
Full -- Inherit all effects of parent scaling.

  * ``FIX_SHEAR``
Fix Shear -- Inherit scaling, but remove shearing of the child in the rest orientation.

  * ``ALIGNED``
Aligned -- Rotate non-uniform parent scaling to align with the child, applying parent X scale to child X axis, and so forth.

  * ``AVERAGE``
Average -- Inherit uniform scaling representing the overall change in the volume of the parent.

  * ``NONE``
None -- Completely ignore parent scaling.

  * ``NONE_LEGACY``
None (Legacy) -- Ignore parent scaling without compensating for parent shear. Replicates the effect of disabling the original Inherit Scale checkbox.

  """

  layers: typing.Tuple[bool, ...] = ...

  """

  Layers bone exists in

  """

  length: float = ...

  """

  Length of the bone. Changing moves the tail end

  """

  lock: bool = ...

  """

  Bone is not able to be transformed when in Edit Mode

  """

  matrix: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]] = ...

  """

  Matrix combining location and rotation of the bone (head position, direction and roll), in armature space (does not include/support bone's length/size)

  """

  name: str = ...

  parent: EditBone = ...

  """

  Parent edit bone (in same Armature)

  """

  roll: float = ...

  """

  Bone rotation around head-tail axis

  """

  select: bool = ...

  select_head: bool = ...

  select_tail: bool = ...

  show_wire: bool = ...

  """

  Bone is always displayed in wireframe regardless of viewport shading mode (useful for non-obstructive custom bone shapes)

  """

  tail: typing.Tuple[float, float, float] = ...

  """

  Location of tail end of the bone

  """

  tail_radius: float = ...

  """

  Radius of tail of bone (for Envelope deform only)

  """

  use_connect: bool = ...

  """

  When bone has a parent, bone's head is stuck to the parent's tail

  """

  use_cyclic_offset: bool = ...

  """

  When bone doesn't have a parent, it receives cyclic offset effects (Deprecated)

  """

  use_deform: bool = ...

  """

  Enable Bone to deform geometry

  """

  use_endroll_as_inroll: bool = ...

  """

  Add Roll Out of the Start Handle bone to the Roll In value

  """

  use_envelope_multiply: bool = ...

  """

  When deforming bone, multiply effects of Vertex Group weights with Envelope influence

  """

  use_inherit_rotation: bool = ...

  """

  Bone inherits rotation or scale from parent bone

  """

  use_inherit_scale: bool = ...

  """

  DEPRECATED: Bone inherits scaling from parent bone

  """

  use_local_location: bool = ...

  """

  Bone location is set in local space

  """

  use_relative_parent: bool = ...

  """

  Object children will use relative transform, like deform

  """

  use_scale_easing: bool = ...

  """

  Multiply the final easing values by the Scale In/Out Y factors

  """

  basename: typing.Any = ...

  """

  The name of this bone before any '.' character

  (readonly)

  """

  center: typing.Any = ...

  """

  The midpoint between the head and the tail.

  (readonly)

  """

  children: typing.Any = ...

  """

  A list of all the bones children.

    Note: Takes ``O(len(bones))`` time.

  (readonly)

  """

  children_recursive: typing.Any = ...

  """

  A list of all children from this bone.

    Note: Takes ``O(len(bones)**2)`` time.

  (readonly)

  """

  children_recursive_basename: typing.Any = ...

  """

  Returns a chain of children with the same base name as this bone.
Only direct chains are supported, forks caused by multiple children
with matching base names will terminate the function
and not be returned.

  Note: Takes ``O(len(bones)**2)`` time.

  (readonly)

  """

  parent_recursive: typing.Any = ...

  """

  A list of parents, starting with the immediate parent

  (readonly)

  """

  vector: typing.Any = ...

  """

  The direction this bone is pointing.
Utility function for (tail - head)

  (readonly)

  """

  x_axis: typing.Any = ...

  """

  Vector pointing down the x-axis of the bone.

  (readonly)

  """

  y_axis: typing.Any = ...

  """

  Vector pointing down the y-axis of the bone.

  (readonly)

  """

  z_axis: typing.Any = ...

  """

  Vector pointing down the z-axis of the bone.

  (readonly)

  """

  def align_roll(self, vector: typing.Tuple[float, float, float]) -> None:

    """

    Align the bone to a localspace roll so the Z axis points in the direction of the vector given

    """

    ...

  def align_orientation(self, other: typing.Any) -> None:

    """

    Align this bone to another by moving its tail and settings its roll
the length of the other bone is not used.

    """

    ...

  def parent_index(self, parent_test: typing.Any) -> None:

    """

    The same as 'bone in other_bone.parent_recursive'
but saved generating a list.

    """

    ...

  def transform(self, matrix: mathutils.Matrix, *args, scale: bool = True, roll: bool = True) -> None:

    """

    Transform the the bones head, tail, roll and envelope
(when the matrix has a scale component).

    """

    ...

  def translate(self, vec: typing.Any) -> None:

    """

    Utility function to add *vec* to the head and tail of this bone

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class EffectorWeights(bpy_struct):

  """

  Effector weights for physics simulation

  """

  all: float = ...

  """

  All effector's weight

  """

  apply_to_hair_growing: bool = ...

  """

  Use force fields when growing hair

  """

  boid: float = ...

  """

  Boid effector weight

  """

  charge: float = ...

  """

  Charge effector weight

  """

  collection: Collection = ...

  """

  Limit effectors to this collection

  """

  curve_guide: float = ...

  """

  Curve guide effector weight

  """

  drag: float = ...

  """

  Drag effector weight

  """

  force: float = ...

  """

  Force effector weight

  """

  gravity: float = ...

  """

  Global gravity weight

  """

  harmonic: float = ...

  """

  Harmonic effector weight

  """

  lennardjones: float = ...

  """

  Lennard-Jones effector weight

  """

  magnetic: float = ...

  """

  Magnetic effector weight

  """

  smokeflow: float = ...

  """

  Fluid Flow effector weight

  """

  texture: float = ...

  """

  Texture effector weight

  """

  turbulence: float = ...

  """

  Turbulence effector weight

  """

  vortex: float = ...

  """

  Vortex effector weight

  """

  wind: float = ...

  """

  Wind effector weight

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class EnumPropertyItem(bpy_struct):

  """

  Definition of a choice in an RNA enum property

  """

  description: str = ...

  """

  Description of the item's purpose

  """

  icon: str = ...

  """

  Icon of the item

  """

  identifier: str = ...

  """

  Unique name used in the code and scripting

  """

  name: str = ...

  """

  Human readable name

  """

  value: int = ...

  """

  Value of the item

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Event(bpy_struct):

  """

  Window Manager Event

  """

  alt: bool = ...

  """

  True when the Alt/Option key is held

  """

  ascii: str = ...

  """

  Single ASCII character for this event

  """

  ctrl: bool = ...

  """

  True when the Ctrl key is held

  """

  is_mouse_absolute: bool = ...

  """

  The last motion event was an absolute input

  """

  is_repeat: bool = ...

  """

  The event is generated by holding a key down

  """

  is_tablet: bool = ...

  """

  The event has tablet data

  """

  mouse_prev_x: int = ...

  """

  The window relative horizontal location of the mouse

  """

  mouse_prev_y: int = ...

  """

  The window relative vertical location of the mouse

  """

  mouse_region_x: int = ...

  """

  The region relative horizontal location of the mouse

  """

  mouse_region_y: int = ...

  """

  The region relative vertical location of the mouse

  """

  mouse_x: int = ...

  """

  The window relative horizontal location of the mouse

  """

  mouse_y: int = ...

  """

  The window relative vertical location of the mouse

  """

  oskey: bool = ...

  """

  True when the Cmd key is held

  """

  pressure: float = ...

  """

  The pressure of the tablet or 1.0 if no tablet present

  """

  shift: bool = ...

  """

  True when the Shift key is held

  """

  tilt: typing.Tuple[float, float] = ...

  """

  The pressure of the tablet or zeroes if no tablet present

  """

  type: str = ...

  """

  * ``NONE``
Undocumented.

  * ``LEFTMOUSE``
Left Mouse -- LMB.

  * ``MIDDLEMOUSE``
Middle Mouse -- MMB.

  * ``RIGHTMOUSE``
Right Mouse -- RMB.

  * ``BUTTON4MOUSE``
Button4 Mouse -- MB4.

  * ``BUTTON5MOUSE``
Button5 Mouse -- MB5.

  * ``BUTTON6MOUSE``
Button6 Mouse -- MB6.

  * ``BUTTON7MOUSE``
Button7 Mouse -- MB7.

  * ``PEN``
Pen.

  * ``ERASER``
Eraser.

  * ``MOUSEMOVE``
Mouse Move -- MsMov.

  * ``INBETWEEN_MOUSEMOVE``
In-between Move -- MsSubMov.

  * ``TRACKPADPAN``
Mouse/Trackpad Pan -- MsPan.

  * ``TRACKPADZOOM``
Mouse/Trackpad Zoom -- MsZoom.

  * ``MOUSEROTATE``
Mouse/Trackpad Rotate -- MsRot.

  * ``MOUSESMARTZOOM``
Mouse/Trackpad Smart Zoom -- MsSmartZoom.

  * ``WHEELUPMOUSE``
Wheel Up -- WhUp.

  * ``WHEELDOWNMOUSE``
Wheel Down -- WhDown.

  * ``WHEELINMOUSE``
Wheel In -- WhIn.

  * ``WHEELOUTMOUSE``
Wheel Out -- WhOut.

  * ``EVT_TWEAK_L``
Tweak Left -- TwkL.

  * ``EVT_TWEAK_M``
Tweak Middle -- TwkM.

  * ``EVT_TWEAK_R``
Tweak Right -- TwkR.

  * ``A``
A.

  * ``B``
B.

  * ``C``
C.

  * ``D``
D.

  * ``E``
E.

  * ``F``
F.

  * ``G``
G.

  * ``H``
H.

  * ``I``
I.

  * ``J``
J.

  * ``K``
K.

  * ``L``
L.

  * ``M``
M.

  * ``N``
N.

  * ``O``
O.

  * ``P``
P.

  * ``Q``
Q.

  * ``R``
R.

  * ``S``
S.

  * ``T``
T.

  * ``U``
U.

  * ``V``
V.

  * ``W``
W.

  * ``X``
X.

  * ``Y``
Y.

  * ``Z``
Z.

  * ``ZERO``
0.

  * ``ONE``
1.

  * ``TWO``
2.

  * ``THREE``
3.

  * ``FOUR``
4.

  * ``FIVE``
5.

  * ``SIX``
6.

  * ``SEVEN``
7.

  * ``EIGHT``
8.

  * ``NINE``
9.

  * ``LEFT_CTRL``
Left Ctrl -- CtrlL.

  * ``LEFT_ALT``
Left Alt -- AltL.

  * ``LEFT_SHIFT``
Left Shift -- ShiftL.

  * ``RIGHT_ALT``
Right Alt -- AltR.

  * ``RIGHT_CTRL``
Right Ctrl -- CtrlR.

  * ``RIGHT_SHIFT``
Right Shift -- ShiftR.

  * ``OSKEY``
OS Key -- Cmd.

  * ``APP``
Application -- App.

  * ``GRLESS``
Grless.

  * ``ESC``
Esc.

  * ``TAB``
Tab.

  * ``RET``
Return -- Enter.

  * ``SPACE``
Spacebar -- Space.

  * ``LINE_FEED``
Line Feed.

  * ``BACK_SPACE``
Backspace -- BkSpace.

  * ``DEL``
Delete -- Del.

  * ``SEMI_COLON``
;.

  * ``PERIOD``
..

  * ``COMMA``
,.

  * ``QUOTE``
".

  * ``ACCENT_GRAVE``
`.

  * ``MINUS``
-.

  * ``PLUS``
+.

  * ``SLASH``
/.

  * ``BACK_SLASH``
\.

  * ``EQUAL``
=.

  * ``LEFT_BRACKET``
[.

  * ``RIGHT_BRACKET``
].

  * ``LEFT_ARROW``
Left Arrow -- ←.

  * ``DOWN_ARROW``
Down Arrow -- ↓.

  * ``RIGHT_ARROW``
Right Arrow -- →.

  * ``UP_ARROW``
Up Arrow -- ↑.

  * ``NUMPAD_2``
Numpad 2 -- Pad2.

  * ``NUMPAD_4``
Numpad 4 -- Pad4.

  * ``NUMPAD_6``
Numpad 6 -- Pad6.

  * ``NUMPAD_8``
Numpad 8 -- Pad8.

  * ``NUMPAD_1``
Numpad 1 -- Pad1.

  * ``NUMPAD_3``
Numpad 3 -- Pad3.

  * ``NUMPAD_5``
Numpad 5 -- Pad5.

  * ``NUMPAD_7``
Numpad 7 -- Pad7.

  * ``NUMPAD_9``
Numpad 9 -- Pad9.

  * ``NUMPAD_PERIOD``
Numpad . -- Pad..

  * ``NUMPAD_SLASH``
Numpad / -- Pad/.

  * ``NUMPAD_ASTERIX``
Numpad * -- Pad*.

  * ``NUMPAD_0``
Numpad 0 -- Pad0.

  * ``NUMPAD_MINUS``
Numpad - -- Pad-.

  * ``NUMPAD_ENTER``
Numpad Enter -- PadEnter.

  * ``NUMPAD_PLUS``
Numpad + -- Pad+.

  * ``F1``
F1.

  * ``F2``
F2.

  * ``F3``
F3.

  * ``F4``
F4.

  * ``F5``
F5.

  * ``F6``
F6.

  * ``F7``
F7.

  * ``F8``
F8.

  * ``F9``
F9.

  * ``F10``
F10.

  * ``F11``
F11.

  * ``F12``
F12.

  * ``F13``
F13.

  * ``F14``
F14.

  * ``F15``
F15.

  * ``F16``
F16.

  * ``F17``
F17.

  * ``F18``
F18.

  * ``F19``
F19.

  * ``F20``
F20.

  * ``F21``
F21.

  * ``F22``
F22.

  * ``F23``
F23.

  * ``F24``
F24.

  * ``PAUSE``
Pause.

  * ``INSERT``
Insert -- Ins.

  * ``HOME``
Home.

  * ``PAGE_UP``
Page Up -- PgUp.

  * ``PAGE_DOWN``
Page Down -- PgDown.

  * ``END``
End.

  * ``MEDIA_PLAY``
Media Play/Pause -- >/||.

  * ``MEDIA_STOP``
Media Stop -- Stop.

  * ``MEDIA_FIRST``
Media First -- |<<.

  * ``MEDIA_LAST``
Media Last -- >>|.

  * ``TEXTINPUT``
Text Input -- TxtIn.

  * ``WINDOW_DEACTIVATE``
Window Deactivate.

  * ``TIMER``
Timer -- Tmr.

  * ``TIMER0``
Timer 0 -- Tmr0.

  * ``TIMER1``
Timer 1 -- Tmr1.

  * ``TIMER2``
Timer 2 -- Tmr2.

  * ``TIMER_JOBS``
Timer Jobs -- TmrJob.

  * ``TIMER_AUTOSAVE``
Timer Autosave -- TmrSave.

  * ``TIMER_REPORT``
Timer Report -- TmrReport.

  * ``TIMERREGION``
Timer Region -- TmrReg.

  * ``NDOF_MOTION``
NDOF Motion -- NdofMov.

  * ``NDOF_BUTTON_MENU``
NDOF Menu -- NdofMenu.

  * ``NDOF_BUTTON_FIT``
NDOF Fit -- NdofFit.

  * ``NDOF_BUTTON_TOP``
NDOF Top -- Ndof↑.

  * ``NDOF_BUTTON_BOTTOM``
NDOF Bottom -- Ndof↓.

  * ``NDOF_BUTTON_LEFT``
NDOF Left -- Ndof←.

  * ``NDOF_BUTTON_RIGHT``
NDOF Right -- Ndof→.

  * ``NDOF_BUTTON_FRONT``
NDOF Front -- NdofFront.

  * ``NDOF_BUTTON_BACK``
NDOF Back -- NdofBack.

  * ``NDOF_BUTTON_ISO1``
NDOF Isometric 1 -- NdofIso1.

  * ``NDOF_BUTTON_ISO2``
NDOF Isometric 2 -- NdofIso2.

  * ``NDOF_BUTTON_ROLL_CW``
NDOF Roll CW -- NdofRCW.

  * ``NDOF_BUTTON_ROLL_CCW``
NDOF Roll CCW -- NdofRCCW.

  * ``NDOF_BUTTON_SPIN_CW``
NDOF Spin CW -- NdofSCW.

  * ``NDOF_BUTTON_SPIN_CCW``
NDOF Spin CCW -- NdofSCCW.

  * ``NDOF_BUTTON_TILT_CW``
NDOF Tilt CW -- NdofTCW.

  * ``NDOF_BUTTON_TILT_CCW``
NDOF Tilt CCW -- NdofTCCW.

  * ``NDOF_BUTTON_ROTATE``
NDOF Rotate -- NdofRot.

  * ``NDOF_BUTTON_PANZOOM``
NDOF Pan/Zoom -- NdofPanZoom.

  * ``NDOF_BUTTON_DOMINANT``
NDOF Dominant -- NdofDom.

  * ``NDOF_BUTTON_PLUS``
NDOF Plus -- Ndof+.

  * ``NDOF_BUTTON_MINUS``
NDOF Minus -- Ndof-.

  * ``NDOF_BUTTON_ESC``
NDOF Esc -- NdofEsc.

  * ``NDOF_BUTTON_ALT``
NDOF Alt -- NdofAlt.

  * ``NDOF_BUTTON_SHIFT``
NDOF Shift -- NdofShift.

  * ``NDOF_BUTTON_CTRL``
NDOF Ctrl -- NdofCtrl.

  * ``NDOF_BUTTON_1``
NDOF Button 1 -- NdofB1.

  * ``NDOF_BUTTON_2``
NDOF Button 2 -- NdofB2.

  * ``NDOF_BUTTON_3``
NDOF Button 3 -- NdofB3.

  * ``NDOF_BUTTON_4``
NDOF Button 4 -- NdofB4.

  * ``NDOF_BUTTON_5``
NDOF Button 5 -- NdofB5.

  * ``NDOF_BUTTON_6``
NDOF Button 6 -- NdofB6.

  * ``NDOF_BUTTON_7``
NDOF Button 7 -- NdofB7.

  * ``NDOF_BUTTON_8``
NDOF Button 8 -- NdofB8.

  * ``NDOF_BUTTON_9``
NDOF Button 9 -- NdofB9.

  * ``NDOF_BUTTON_10``
NDOF Button 10 -- NdofB10.

  * ``NDOF_BUTTON_A``
NDOF Button A -- NdofBA.

  * ``NDOF_BUTTON_B``
NDOF Button B -- NdofBB.

  * ``NDOF_BUTTON_C``
NDOF Button C -- NdofBC.

  * ``ACTIONZONE_AREA``
ActionZone Area -- AZone Area.

  * ``ACTIONZONE_REGION``
ActionZone Region -- AZone Region.

  * ``ACTIONZONE_FULLSCREEN``
ActionZone Fullscreen -- AZone FullScr.

  * ``XR_ACTION``
XR Action.

  """

  unicode: str = ...

  """

  Single unicode character for this event

  """

  value: str = ...

  """

  The type of event, only applies to some

  """

  xr: XrEventData = ...

  """

  XR event data

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FaceMap(bpy_struct):

  """

  Group of faces, each face can only be part of one map

  """

  index: int = ...

  """

  Index number of the face map

  """

  name: str = ...

  """

  Face map name

  """

  select: bool = ...

  """

  Face map selection state (for tools to use)

  """

  def add(self, index: typing.Tuple[int]) -> None:

    """

    Add faces to the face-map

    """

    ...

  def remove(self, index: typing.Tuple[int]) -> None:

    """

    Remove faces from the face-map

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FaceMaps(bpy_struct):

  """

  Collection of face maps

  """

  active: FaceMap = ...

  """

  Face maps of the object

  """

  active_index: int = ...

  """

  Active index in face map array

  """

  def new(self, name: str = 'Map') -> FaceMap:

    """

    Add face map to object

    """

    ...

  def remove(self, group: FaceMap) -> None:

    """

    Delete vertex group from object

    """

    ...

  def clear(self) -> None:

    """

    Delete all vertex groups from object

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FCurve(bpy_struct):

  """

  F-Curve defining values of a period of time

  """

  array_index: int = ...

  """

  Index to the specific property affected by F-Curve if applicable

  """

  auto_smoothing: str = ...

  """

  Algorithm used to compute automatic handles

  * ``NONE``
None -- Automatic handles only take immediately adjacent keys into account.

  * ``CONT_ACCEL``
Continuous Acceleration -- Automatic handles are adjusted to avoid jumps in acceleration, resulting in smoother curves. However, key changes may affect interpolation over a larger stretch of the curve.

  """

  color: typing.Tuple[float, float, float] = ...

  """

  Color of the F-Curve in the Graph Editor

  """

  color_mode: str = ...

  """

  Method used to determine color of F-Curve in Graph Editor

  * ``AUTO_RAINBOW``
Auto Rainbow -- Cycle through the rainbow, trying to give each curve a unique color.

  * ``AUTO_RGB``
Auto XYZ to RGB -- Use axis colors for transform and color properties, and auto-rainbow for the rest.

  * ``AUTO_YRGB``
Auto WXYZ to YRGB -- Use axis colors for XYZ parts of transform, and yellow for the 'W' channel.

  * ``CUSTOM``
User Defined -- Use custom hand-picked color for F-Curve.

  """

  data_path: str = ...

  """

  RNA Path to property affected by F-Curve

  """

  driver: Driver = ...

  """

  Channel Driver (only set for Driver F-Curves)

  """

  extrapolation: str = ...

  """

  Method used for evaluating value of F-Curve outside first and last keyframes

  * ``CONSTANT``
Constant -- Hold values of endpoint keyframes.

  * ``LINEAR``
Linear -- Use slope of curve leading in/out of endpoint keyframes.

  """

  group: ActionGroup = ...

  """

  Action Group that this F-Curve belongs to

  """

  hide: bool = ...

  """

  F-Curve and its keyframes are hidden in the Graph Editor graphs

  """

  is_empty: bool = ...

  """

  True if the curve contributes no animation due to lack of keyframes or useful modifiers, and should be deleted

  """

  is_valid: bool = ...

  """

  False when F-Curve could not be evaluated in past, so should be skipped when evaluating

  """

  keyframe_points: typing.Union[FCurveKeyframePoints, typing.Sequence[Keyframe], typing.Mapping[str, Keyframe], bpy_prop_collection] = ...

  """

  User-editable keyframes

  """

  lock: bool = ...

  """

  F-Curve's settings cannot be edited

  """

  modifiers: typing.Union[FCurveModifiers, typing.Sequence[FModifier], typing.Mapping[str, FModifier], bpy_prop_collection] = ...

  """

  Modifiers affecting the shape of the F-Curve

  """

  mute: bool = ...

  """

  Disable F-Curve evaluation

  """

  sampled_points: typing.Union[typing.Sequence[FCurveSample], typing.Mapping[str, FCurveSample], bpy_prop_collection] = ...

  """

  Sampled animation data

  """

  select: bool = ...

  """

  F-Curve is selected for editing

  """

  def evaluate(self, frame: float) -> float:

    """

    Evaluate F-Curve

    """

    ...

  def update(self) -> None:

    """

    Ensure keyframes are sorted in chronological order and handles are set correctly

    """

    ...

  def range(self) -> typing.Tuple[float, float]:

    """

    Get the time extents for F-Curve

    """

    ...

  def update_autoflags(self, data: typing.Any) -> None:

    """

    Update FCurve flags set automatically from affected property (currently, integer/discrete flags set when the property is not a float)

    """

    ...

  def convert_to_samples(self, start: int, end: int) -> None:

    """

    Convert current FCurve from keyframes to sample points, if necessary

    """

    ...

  def convert_to_keyframes(self, start: int, end: int) -> None:

    """

    Convert current FCurve from sample points to keyframes (linear interpolation), if necessary

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FCurveKeyframePoints(bpy_struct):

  """

  Collection of keyframe points

  """

  def insert(self, frame: float, value: float, options: typing.Set[str] = {}, keyframe_type: str = 'KEYFRAME') -> Keyframe:

    """

    Add a keyframe point to a F-Curve

    """

    ...

  def add(self, count: int) -> None:

    """

    Add a keyframe point to a F-Curve

    """

    ...

  def remove(self, keyframe: Keyframe, fast: bool = False) -> None:

    """

    Remove keyframe from an F-Curve

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FCurveModifiers(bpy_struct):

  """

  Collection of F-Curve Modifiers

  """

  active: FModifier = ...

  """

  Active F-Curve Modifier

  """

  def new(self, type: str) -> FModifier:

    """

    Add a constraint to this object

    """

    ...

  def remove(self, modifier: FModifier) -> None:

    """

    Remove a modifier from this F-Curve

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FCurveSample(bpy_struct):

  """

  Sample point for F-Curve

  """

  co: typing.Tuple[float, float] = ...

  """

  Point coordinates

  """

  select: bool = ...

  """

  Selection status

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FFmpegSettings(bpy_struct):

  """

  FFmpeg related settings for the scene

  """

  audio_bitrate: int = ...

  """

  Audio bitrate (kb/s)

  """

  audio_channels: str = ...

  """

  Audio channel count

  * ``MONO``
Mono -- Set audio channels to mono.

  * ``STEREO``
Stereo -- Set audio channels to stereo.

  * ``SURROUND4``
4 Channels -- Set audio channels to 4 channels.

  * ``SURROUND51``
5.1 Surround -- Set audio channels to 5.1 surround sound.

  * ``SURROUND71``
7.1 Surround -- Set audio channels to 7.1 surround sound.

  """

  audio_codec: str = ...

  """

  FFmpeg audio codec to use

  * ``NONE``
No Audio -- Disables audio output, for video-only renders.

  * ``AAC``
AAC.

  * ``AC3``
AC3.

  * ``FLAC``
FLAC.

  * ``MP2``
MP2.

  * ``MP3``
MP3.

  * ``OPUS``
Opus.

  * ``PCM``
PCM.

  * ``VORBIS``
Vorbis.

  """

  audio_mixrate: int = ...

  """

  Audio samplerate(samples/s)

  """

  audio_volume: float = ...

  """

  Audio volume

  """

  buffersize: int = ...

  """

  Rate control: buffer size (kb)

  """

  codec: str = ...

  """

  FFmpeg codec to use for video output

  * ``NONE``
No Video -- Disables video output, for audio-only renders.

  * ``DNXHD``
DNxHD.

  * ``DV``
DV.

  * ``FFV1``
FFmpeg video codec #1.

  * ``FLASH``
Flash Video.

  * ``H264``
H.264.

  * ``HUFFYUV``
HuffYUV.

  * ``MPEG1``
MPEG-1.

  * ``MPEG2``
MPEG-2.

  * ``MPEG4``
MPEG-4 (divx).

  * ``PNG``
PNG.

  * ``QTRLE``
QT rle / QT Animation.

  * ``THEORA``
Theora.

  * ``WEBM``
WEBM / VP9.

  """

  constant_rate_factor: str = ...

  """

  Constant Rate Factor (CRF); tradeoff between video quality and file size

  * ``NONE``
Constant Bitrate -- Configure constant bit rate, rather than constant output quality.

  * ``LOSSLESS``
Lossless.

  * ``PERC_LOSSLESS``
Perceptually Lossless.

  * ``HIGH``
High Quality.

  * ``MEDIUM``
Medium Quality.

  * ``LOW``
Low Quality.

  * ``VERYLOW``
Very Low Quality.

  * ``LOWEST``
Lowest Quality.

  """

  ffmpeg_preset: str = ...

  """

  Tradeoff between encoding speed and compression ratio

  * ``BEST``
Slowest -- Recommended if you have lots of time and want the best compression efficiency.

  * ``GOOD``
Good -- The default and recommended for most applications.

  * ``REALTIME``
Realtime -- Recommended for fast encoding.

  """

  format: str = ...

  """

  Output file container

  """

  gopsize: int = ...

  """

  Distance between key frames, also known as GOP size; influences file size and seekability

  """

  max_b_frames: int = ...

  """

  Maximum number of B-frames between non-B-frames; influences file size and seekability

  """

  maxrate: int = ...

  """

  Rate control: max rate (kbit/s)

  """

  minrate: int = ...

  """

  Rate control: min rate (kbit/s)

  """

  muxrate: int = ...

  """

  Mux rate (bits/second)

  """

  packetsize: int = ...

  """

  Mux packet size (byte)

  """

  use_autosplit: bool = ...

  """

  Autosplit output at 2GB boundary

  """

  use_lossless_output: bool = ...

  """

  Use lossless output for video streams

  """

  use_max_b_frames: bool = ...

  """

  Set a maximum number of B-frames

  """

  video_bitrate: int = ...

  """

  Video bitrate (kbit/s)

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FieldSettings(bpy_struct):

  """

  Field settings for an object in physics simulation

  """

  apply_to_location: bool = ...

  """

  Affect particle's location

  """

  apply_to_rotation: bool = ...

  """

  Affect particle's dynamic rotation

  """

  distance_max: float = ...

  """

  Maximum distance for the field to work

  """

  distance_min: float = ...

  """

  Minimum distance for the field's fall-off

  """

  falloff_power: float = ...

  """

  How quickly strength falls off with distance from the force field

  """

  falloff_type: str = ...

  flow: float = ...

  """

  Convert effector force into air flow velocity

  """

  guide_clump_amount: float = ...

  """

  Amount of clumping

  """

  guide_clump_shape: float = ...

  """

  Shape of clumping

  """

  guide_free: float = ...

  """

  Guide-free time from particle life's end

  """

  guide_kink_amplitude: float = ...

  """

  The amplitude of the offset

  """

  guide_kink_axis: str = ...

  """

  Which axis to use for offset

  """

  guide_kink_frequency: float = ...

  """

  The frequency of the offset (1/total length)

  """

  guide_kink_shape: float = ...

  """

  Adjust the offset to the beginning/end

  """

  guide_kink_type: str = ...

  """

  Type of periodic offset on the curve

  """

  guide_minimum: float = ...

  """

  The distance from which particles are affected fully

  """

  harmonic_damping: float = ...

  """

  Damping of the harmonic force

  """

  inflow: float = ...

  """

  Inwards component of the vortex force

  """

  linear_drag: float = ...

  """

  Drag component proportional to velocity

  """

  noise: float = ...

  """

  Amount of noise for the force strength

  """

  quadratic_drag: float = ...

  """

  Drag component proportional to the square of velocity

  """

  radial_falloff: float = ...

  """

  Radial falloff power (real gravitational falloff = 2)

  """

  radial_max: float = ...

  """

  Maximum radial distance for the field to work

  """

  radial_min: float = ...

  """

  Minimum radial distance for the field's fall-off

  """

  rest_length: float = ...

  """

  Rest length of the harmonic force

  """

  seed: int = ...

  """

  Seed of the noise

  """

  shape: str = ...

  """

  Which direction is used to calculate the effector force

  * ``POINT``
Point -- Field originates from the object center.

  * ``LINE``
Line -- Field originates from the local Z axis of the object.

  * ``PLANE``
Plane -- Field originates from the local XY plane of the object.

  * ``SURFACE``
Surface -- Field originates from the surface of the object.

  * ``POINTS``
Every Point -- Field originates from all of the vertices of the object.

  """

  size: float = ...

  """

  Size of the turbulence

  """

  source_object: Object = ...

  """

  Select domain object of the smoke simulation

  """

  strength: float = ...

  """

  Strength of force field

  """

  texture: Texture = ...

  """

  Texture to use as force

  """

  texture_mode: str = ...

  """

  How the texture effect is calculated (RGB and Curl need a RGB texture, else Gradient will be used instead)

  """

  texture_nabla: float = ...

  """

  Defines size of derivative offset used for calculating gradient and curl

  """

  type: str = ...

  """

  Type of field

  * ``NONE``
None.

  * ``FORCE``
Force -- Radial field toward the center of object.

  * ``WIND``
Wind -- Constant force along the force object's local Z axis.

  * ``VORTEX``
Vortex -- Spiraling force that twists the force object's local Z axis.

  * ``MAGNET``
Magnetic -- Forcefield depends on the speed of the particles.

  * ``HARMONIC``
Harmonic -- The source of this force field is the zero point of a harmonic oscillator.

  * ``CHARGE``
Charge -- Spherical forcefield based on the charge of particles, only influences other charge force fields.

  * ``LENNARDJ``
Lennard-Jones -- Forcefield based on the Lennard-Jones potential.

  * ``TEXTURE``
Texture -- Force field based on a texture.

  * ``GUIDE``
Curve Guide -- Create a force along a curve object.

  * ``BOID``
Boid -- Create a force that acts as a boid's predators or target.

  * ``TURBULENCE``
Turbulence -- Create turbulence with a noise field.

  * ``DRAG``
Drag -- Create a force that dampens motion.

  * ``FLUID_FLOW``
Fluid Flow -- Create a force based on fluid simulation velocities.

  """

  use_2d_force: bool = ...

  """

  Apply force only in 2D

  """

  use_absorption: bool = ...

  """

  Force gets absorbed by collision objects

  """

  use_global_coords: bool = ...

  """

  Use effector/global coordinates for turbulence

  """

  use_gravity_falloff: bool = ...

  """

  Multiply force by 1/distanceÂ²

  """

  use_guide_path_add: bool = ...

  """

  Based on distance/falloff it adds a portion of the entire path

  """

  use_guide_path_weight: bool = ...

  """

  Use curve weights to influence the particle influence along the curve

  """

  use_max_distance: bool = ...

  """

  Use a maximum distance for the field to work

  """

  use_min_distance: bool = ...

  """

  Use a minimum distance for the field's fall-off

  """

  use_multiple_springs: bool = ...

  """

  Every point is effected by multiple springs

  """

  use_object_coords: bool = ...

  """

  Use object/global coordinates for texture

  """

  use_radial_max: bool = ...

  """

  Use a maximum radial distance for the field to work

  """

  use_radial_min: bool = ...

  """

  Use a minimum radial distance for the field's fall-off

  """

  use_root_coords: bool = ...

  """

  Texture coordinates from root particle locations

  """

  use_smoke_density: bool = ...

  """

  Adjust force strength based on smoke density

  """

  wind_factor: float = ...

  """

  How much the force is reduced when acting parallel to a surface, e.g. cloth

  """

  z_direction: str = ...

  """

  Effect in full or only positive/negative Z direction

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FileAssetSelectIDFilter(bpy_struct):

  """

  Which asset types to show/hide, when browsing an asset library

  """

  experimental_filter_armature: bool = ...

  """

  Show Armature data-blocks

  """

  experimental_filter_brush: bool = ...

  """

  Show Brushes data-blocks

  """

  experimental_filter_cachefile: bool = ...

  """

  Show Cache File data-blocks

  """

  experimental_filter_camera: bool = ...

  """

  Show Camera data-blocks

  """

  experimental_filter_curve: bool = ...

  """

  Show Curve data-blocks

  """

  experimental_filter_font: bool = ...

  """

  Show Font data-blocks

  """

  experimental_filter_grease_pencil: bool = ...

  """

  Show Grease pencil data-blocks

  """

  experimental_filter_group: bool = ...

  """

  Show Collection data-blocks

  """

  experimental_filter_hair: bool = ...

  """

  Show/hide Hair data-blocks

  """

  experimental_filter_image: bool = ...

  """

  Show Image data-blocks

  """

  experimental_filter_lattice: bool = ...

  """

  Show Lattice data-blocks

  """

  experimental_filter_light: bool = ...

  """

  Show Light data-blocks

  """

  experimental_filter_light_probe: bool = ...

  """

  Show Light Probe data-blocks

  """

  experimental_filter_linestyle: bool = ...

  """

  Show Freestyle's Line Style data-blocks

  """

  experimental_filter_mask: bool = ...

  """

  Show Mask data-blocks

  """

  experimental_filter_mesh: bool = ...

  """

  Show Mesh data-blocks

  """

  experimental_filter_metaball: bool = ...

  """

  Show Metaball data-blocks

  """

  experimental_filter_movie_clip: bool = ...

  """

  Show Movie Clip data-blocks

  """

  experimental_filter_node_tree: bool = ...

  """

  Show Node Tree data-blocks

  """

  experimental_filter_paint_curve: bool = ...

  """

  Show Paint Curve data-blocks

  """

  experimental_filter_palette: bool = ...

  """

  Show Palette data-blocks

  """

  experimental_filter_particle_settings: bool = ...

  """

  Show Particle Settings data-blocks

  """

  experimental_filter_pointcloud: bool = ...

  """

  Show/hide Point Cloud data-blocks

  """

  experimental_filter_scene: bool = ...

  """

  Show Scene data-blocks

  """

  experimental_filter_simulation: bool = ...

  """

  Show Simulation data-blocks

  """

  experimental_filter_sound: bool = ...

  """

  Show Sound data-blocks

  """

  experimental_filter_speaker: bool = ...

  """

  Show Speaker data-blocks

  """

  experimental_filter_text: bool = ...

  """

  Show Text data-blocks

  """

  experimental_filter_texture: bool = ...

  """

  Show Texture data-blocks

  """

  experimental_filter_volume: bool = ...

  """

  Show/hide Volume data-blocks

  """

  experimental_filter_work_space: bool = ...

  """

  Show workspace data-blocks

  """

  filter_action: bool = ...

  """

  Show Action data-blocks

  """

  filter_material: bool = ...

  """

  Show Material data-blocks

  """

  filter_object: bool = ...

  """

  Show Object data-blocks

  """

  filter_world: bool = ...

  """

  Show World data-blocks

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FileBrowserFSMenuEntry(bpy_struct):

  """

  File Select Parameters

  """

  icon: int = ...

  is_valid: bool = ...

  """

  Whether this path is currently reachable

  """

  name: str = ...

  path: str = ...

  use_save: bool = ...

  """

  Whether this path is saved in bookmarks, or generated from OS

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FileSelectEntry(bpy_struct):

  """

  A file viewable in the File Browser

  """

  asset_data: AssetMetaData = ...

  """

  Asset data, valid if the file represents an asset

  """

  id_type: str = ...

  """

  The type of the data-block, if the file represents one ('NONE' otherwise)

  """

  local_id: ID = ...

  """

  The local data-block this file represents; only valid if that is a data-block in this file

  """

  name: str = ...

  preview_icon_id: int = ...

  """

  Unique integer identifying the preview of this file as an icon (zero means invalid)

  """

  relative_path: str = ...

  """

  Path relative to the directory currently displayed in the File Browser (includes the file name)

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FileSelectIDFilter(bpy_struct):

  """

  Which ID types to show/hide, when browsing a library

  """

  category_animation: bool = ...

  """

  Show animation data

  """

  category_environment: bool = ...

  """

  Show worlds, lights, cameras and speakers

  """

  category_geometry: bool = ...

  """

  Show meshes, curves, lattice, armatures and metaballs data

  """

  category_image: bool = ...

  """

  Show images, movie clips, sounds and masks

  """

  category_misc: bool = ...

  """

  Show other data types

  """

  category_object: bool = ...

  """

  Show objects and collections

  """

  category_scene: bool = ...

  """

  Show scenes

  """

  category_shading: bool = ...

  """

  Show materials, nodetrees, textures and Freestyle's linestyles

  """

  filter_action: bool = ...

  """

  Show Action data-blocks

  """

  filter_armature: bool = ...

  """

  Show Armature data-blocks

  """

  filter_brush: bool = ...

  """

  Show Brushes data-blocks

  """

  filter_cachefile: bool = ...

  """

  Show Cache File data-blocks

  """

  filter_camera: bool = ...

  """

  Show Camera data-blocks

  """

  filter_curve: bool = ...

  """

  Show Curve data-blocks

  """

  filter_font: bool = ...

  """

  Show Font data-blocks

  """

  filter_grease_pencil: bool = ...

  """

  Show Grease pencil data-blocks

  """

  filter_group: bool = ...

  """

  Show Collection data-blocks

  """

  filter_hair: bool = ...

  """

  Show/hide Hair data-blocks

  """

  filter_image: bool = ...

  """

  Show Image data-blocks

  """

  filter_lattice: bool = ...

  """

  Show Lattice data-blocks

  """

  filter_light: bool = ...

  """

  Show Light data-blocks

  """

  filter_light_probe: bool = ...

  """

  Show Light Probe data-blocks

  """

  filter_linestyle: bool = ...

  """

  Show Freestyle's Line Style data-blocks

  """

  filter_mask: bool = ...

  """

  Show Mask data-blocks

  """

  filter_material: bool = ...

  """

  Show Material data-blocks

  """

  filter_mesh: bool = ...

  """

  Show Mesh data-blocks

  """

  filter_metaball: bool = ...

  """

  Show Metaball data-blocks

  """

  filter_movie_clip: bool = ...

  """

  Show Movie Clip data-blocks

  """

  filter_node_tree: bool = ...

  """

  Show Node Tree data-blocks

  """

  filter_object: bool = ...

  """

  Show Object data-blocks

  """

  filter_paint_curve: bool = ...

  """

  Show Paint Curve data-blocks

  """

  filter_palette: bool = ...

  """

  Show Palette data-blocks

  """

  filter_particle_settings: bool = ...

  """

  Show Particle Settings data-blocks

  """

  filter_pointcloud: bool = ...

  """

  Show/hide Point Cloud data-blocks

  """

  filter_scene: bool = ...

  """

  Show Scene data-blocks

  """

  filter_simulation: bool = ...

  """

  Show Simulation data-blocks

  """

  filter_sound: bool = ...

  """

  Show Sound data-blocks

  """

  filter_speaker: bool = ...

  """

  Show Speaker data-blocks

  """

  filter_text: bool = ...

  """

  Show Text data-blocks

  """

  filter_texture: bool = ...

  """

  Show Texture data-blocks

  """

  filter_volume: bool = ...

  """

  Show/hide Volume data-blocks

  """

  filter_work_space: bool = ...

  """

  Show workspace data-blocks

  """

  filter_world: bool = ...

  """

  Show World data-blocks

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FileSelectParams(bpy_struct):

  """

  File Select Parameters

  """

  directory: str = ...

  """

  Directory displayed in the file browser

  """

  display_size: str = ...

  """

  Change the size of the display (width of columns or thumbnails size)

  """

  display_type: str = ...

  """

  Display mode for the file list

  * ``LIST_VERTICAL``
Vertical List -- Display files as a vertical list.

  * ``LIST_HORIZONTAL``
Horizontal List -- Display files as a horizontal list.

  * ``THUMBNAIL``
Thumbnails -- Display files as thumbnails.

  """

  filename: str = ...

  """

  Active file in the file browser

  """

  filter_glob: str = ...

  """

  UNIX shell-like filename patterns matching, supports wildcards ('*') and list of patterns separated by ';'

  """

  filter_id: FileSelectIDFilter = ...

  """

  Which ID types to show/hide, when browsing a library

  """

  filter_search: str = ...

  """

  Filter by name, supports '*' wildcard

  """

  recursion_level: str = ...

  """

  Numbers of dirtree levels to show simultaneously

  * ``NONE``
None -- Only list current directory's content, with no recursion.

  * ``BLEND``
Blend File -- List .blend files' content.

  * ``ALL_1``
One Level -- List all sub-directories' content, one level of recursion.

  * ``ALL_2``
Two Levels -- List all sub-directories' content, two levels of recursion.

  * ``ALL_3``
Three Levels -- List all sub-directories' content, three levels of recursion.

  """

  show_details_datetime: bool = ...

  """

  Show a column listing the date and time of modification for each file

  """

  show_details_size: bool = ...

  """

  Show a column listing the size of each file

  """

  show_hidden: bool = ...

  """

  Show hidden dot files

  """

  sort_method: str = ...

  """

  * ``FILE_SORT_ALPHA``
Name -- Sort the file list alphabetically.

  * ``FILE_SORT_EXTENSION``
Extension -- Sort the file list by extension/type.

  * ``FILE_SORT_TIME``
Modified Date -- Sort files by modification time.

  * ``FILE_SORT_SIZE``
Size -- Sort files by size.

  """

  title: str = ...

  """

  Title for the file browser

  """

  use_filter: bool = ...

  """

  Enable filtering of files

  """

  use_filter_asset_only: bool = ...

  """

  Hide .blend files items that are not data-blocks with asset metadata

  """

  use_filter_backup: bool = ...

  """

  Show .blend1, .blend2, etc. files

  """

  use_filter_blender: bool = ...

  """

  Show .blend files

  """

  use_filter_blendid: bool = ...

  """

  Show .blend files items (objects, materials, etc.)

  """

  use_filter_folder: bool = ...

  """

  Show folders

  """

  use_filter_font: bool = ...

  """

  Show font files

  """

  use_filter_image: bool = ...

  """

  Show image files

  """

  use_filter_movie: bool = ...

  """

  Show movie files

  """

  use_filter_script: bool = ...

  """

  Show script files

  """

  use_filter_sound: bool = ...

  """

  Show sound files

  """

  use_filter_text: bool = ...

  """

  Show text files

  """

  use_filter_volume: bool = ...

  """

  Show 3D volume files

  """

  use_library_browsing: bool = ...

  """

  Whether we may browse blender files' content or not

  """

  use_sort_invert: bool = ...

  """

  Sort items descending, from highest value to lowest

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Float2AttributeValue(bpy_struct):

  """

  2D Vector value in geometry attribute

  """

  vector: typing.Tuple[float, float] = ...

  """

  2D vector

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FloatAttributeValue(bpy_struct):

  """

  Floating-point value in geometry attribute

  """

  value: float = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FloatColorAttributeValue(bpy_struct):

  """

  Color value in geometry attribute

  """

  color: typing.Tuple[float, float, float, float] = ...

  """

  RGBA color in scene linear color space

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FloatVectorAttributeValue(bpy_struct):

  """

  Vector value in geometry attribute

  """

  vector: typing.Tuple[float, float, float] = ...

  """

  3D vector

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FluidDomainSettings(bpy_struct):

  """

  Fluid domain settings

  """

  adapt_margin: int = ...

  """

  Margin added around fluid to minimize boundary interference

  """

  adapt_threshold: float = ...

  """

  Minimum amount of fluid a cell can contain before it is considered empty

  """

  additional_res: int = ...

  """

  Maximum number of additional cells

  """

  alpha: float = ...

  """

  Buoyant force based on smoke density (higher value results in faster rising smoke)

  """

  beta: float = ...

  """

  Buoyant force based on smoke heat (higher value results in faster rising smoke)

  """

  burning_rate: float = ...

  """

  Speed of the burning reaction (higher value results in smaller flames)

  """

  cache_data_format: str = ...

  """

  Select the file format to be used for caching volumetric data

  """

  cache_directory: str = ...

  """

  Directory that contains fluid cache files

  """

  cache_frame_end: int = ...

  """

  Frame on which the simulation stops. This is the last frame that will be baked

  """

  cache_frame_offset: int = ...

  """

  Frame offset that is used when loading the simulation from the cache. It is not considered when baking the simulation, only when loading it

  """

  cache_frame_pause_data: int = ...

  cache_frame_pause_guide: int = ...

  cache_frame_pause_mesh: int = ...

  cache_frame_pause_noise: int = ...

  cache_frame_pause_particles: int = ...

  cache_frame_start: int = ...

  """

  Frame on which the simulation starts. This is the first frame that will be baked

  """

  cache_mesh_format: str = ...

  """

  Select the file format to be used for caching surface data

  """

  cache_noise_format: str = ...

  """

  Select the file format to be used for caching noise data

  """

  cache_particle_format: str = ...

  """

  Select the file format to be used for caching particle data

  """

  cache_resumable: bool = ...

  """

  Additional data will be saved so that the bake jobs can be resumed after pausing. Because more data will be written to disk it is recommended to avoid enabling this option when baking at high resolutions

  """

  cache_type: str = ...

  """

  Change the cache type of the simulation

  * ``REPLAY``
Replay -- Use the timeline to bake the scene.

  * ``MODULAR``
Modular -- Bake every stage of the simulation separately.

  * ``ALL``
All -- Bake all simulation settings at once.

  """

  cell_size: typing.Tuple[float, float, float] = ...

  """

  Cell Size

  """

  cfl_condition: float = ...

  """

  Maximal velocity per cell (higher value results in greater timesteps)

  """

  clipping: float = ...

  """

  Value under which voxels are considered empty space to optimize rendering

  """

  color_grid: typing.Tuple[float, ...] = ...

  """

  Smoke color grid

  """

  color_ramp: ColorRamp = ...

  color_ramp_field: str = ...

  """

  Simulation field to color map

  """

  color_ramp_field_scale: float = ...

  """

  Multiplier for scaling the selected field to color map

  """

  delete_in_obstacle: bool = ...

  """

  Delete fluid inside obstacles

  """

  density_grid: typing.Tuple[float, ...] = ...

  """

  Smoke density grid

  """

  display_interpolation: str = ...

  """

  Interpolation method to use for smoke/fire volumes in solid mode

  * ``LINEAR``
Linear -- Good smoothness and speed.

  * ``CUBIC``
Cubic -- Smoothed high quality interpolation, but slower.

  * ``CLOSEST``
Closest -- No interpolation.

  """

  display_thickness: float = ...

  """

  Thickness of smoke display in the viewport

  """

  dissolve_speed: int = ...

  """

  Determine how quickly the smoke dissolves (lower value makes smoke disappear faster)

  """

  domain_resolution: typing.Tuple[int, int, int] = ...

  """

  Smoke Grid Resolution

  """

  domain_type: str = ...

  """

  Change domain type of the simulation

  * ``GAS``
Gas -- Create domain for gases.

  * ``LIQUID``
Liquid -- Create domain for liquids.

  """

  effector_group: Collection = ...

  """

  Limit effectors to this collection

  """

  effector_weights: EffectorWeights = ...

  export_manta_script: bool = ...

  """

  Generate and export Mantaflow script from current domain settings during bake. This is only needed if you plan to analyze the cache (e.g. view grids, velocity vectors, particles) in Mantaflow directly (outside of Blender) after baking the simulation

  """

  flame_grid: typing.Tuple[float, ...] = ...

  """

  Smoke flame grid

  """

  flame_ignition: float = ...

  """

  Minimum temperature of the flames (higher value results in faster rising flames)

  """

  flame_max_temp: float = ...

  """

  Maximum temperature of the flames (higher value results in faster rising flames)

  """

  flame_smoke: float = ...

  """

  Amount of smoke created by burning fuel

  """

  flame_smoke_color: typing.Tuple[float, float, float] = ...

  """

  Color of smoke emitted from burning fuel

  """

  flame_vorticity: float = ...

  """

  Additional vorticity for the flames

  """

  flip_ratio: float = ...

  """

  PIC/FLIP Ratio. A value of 1.0 will result in a completely FLIP based simulation. Use a lower value for simulations which should produce smaller splashes

  """

  fluid_group: Collection = ...

  """

  Limit fluid objects to this collection

  """

  force_collection: Collection = ...

  """

  Limit forces to this collection

  """

  fractions_distance: float = ...

  """

  Determines how far apart fluid and obstacle are (higher values will result in fluid being further away from obstacles, smaller values will let fluid move towards the inside of obstacles)

  """

  fractions_threshold: float = ...

  """

  Determines how much fluid is allowed in an obstacle cell (higher values will tag a boundary cell as an obstacle easier and reduce the boundary smoothening effect)

  """

  gravity: typing.Tuple[float, float, float] = ...

  """

  Gravity in X, Y and Z direction

  """

  gridlines_cell_filter: str = ...

  """

  Cell type to be highlighted

  * ``NONE``
None -- Highlight the cells regardless of their type.

  * ``FLUID``
Fluid -- Highlight only the cells of type Fluid.

  * ``OBSTACLE``
Obstacle -- Highlight only the cells of type Obstacle.

  * ``EMPTY``
Empty -- Highlight only the cells of type Empty.

  * ``INFLOW``
Inflow -- Highlight only the cells of type Inflow.

  * ``OUTFLOW``
Outflow -- Highlight only the cells of type Outflow.

  """

  gridlines_color_field: str = ...

  """

  Simulation field to color map onto gridlines

  * ``NONE``
None -- None.

  * ``FLAGS``
Flags -- Flag grid of the fluid domain.

  * ``RANGE``
Highlight Range -- Highlight the voxels with values of the color mapped field within the range.

  """

  gridlines_lower_bound: float = ...

  """

  Lower bound of the highlighting range

  """

  gridlines_range_color: typing.Tuple[float, float, float, float] = ...

  """

  Color used to highlight the range

  """

  gridlines_upper_bound: float = ...

  """

  Upper bound of the highlighting range

  """

  guide_alpha: float = ...

  """

  Guiding weight (higher value results in greater lag)

  """

  guide_beta: int = ...

  """

  Guiding size (higher value results in larger vortices)

  """

  guide_parent: Object = ...

  """

  Use velocities from this object for the guiding effect (object needs to have fluid modifier and be of type domain))

  """

  guide_source: str = ...

  """

  Choose where to get guiding velocities from

  * ``DOMAIN``
Domain -- Use a fluid domain for guiding (domain needs to be baked already so that velocities can be extracted). Guiding domain can be of any type (i.e. gas or liquid).

  * ``EFFECTOR``
Effector -- Use guiding (effector) objects to create fluid guiding (guiding objects should be animated and baked once set up completely).

  """

  guide_vel_factor: float = ...

  """

  Guiding velocity factor (higher value results in greater guiding velocities)

  """

  has_cache_baked_any: bool = ...

  has_cache_baked_data: bool = ...

  has_cache_baked_guide: bool = ...

  has_cache_baked_mesh: bool = ...

  has_cache_baked_noise: bool = ...

  has_cache_baked_particles: bool = ...

  heat_grid: typing.Tuple[float, ...] = ...

  """

  Smoke heat grid

  """

  highres_sampling: str = ...

  """

  Method for sampling the high resolution flow

  """

  is_cache_baking_any: bool = ...

  is_cache_baking_data: bool = ...

  is_cache_baking_guide: bool = ...

  is_cache_baking_mesh: bool = ...

  is_cache_baking_noise: bool = ...

  is_cache_baking_particles: bool = ...

  mesh_concave_lower: float = ...

  """

  Lower mesh concavity bound (high values tend to smoothen and fill out concave regions)

  """

  mesh_concave_upper: float = ...

  """

  Upper mesh concavity bound (high values tend to smoothen and fill out concave regions)

  """

  mesh_generator: str = ...

  """

  Which particle level set generator to use

  * ``IMPROVED``
Final -- Use improved particle level set (slower but more precise and with mesh smoothening options).

  * ``UNION``
Preview -- Use union particle level set (faster but lower quality).

  """

  mesh_particle_radius: float = ...

  """

  Particle radius factor (higher value results in larger (meshed) particles). Needs to be adjusted after changing the mesh scale

  """

  mesh_scale: int = ...

  """

  The mesh simulation is scaled up by this factor (compared to the base resolution of the domain). For best meshing, it is recommended to adjust the mesh particle radius alongside this value

  """

  mesh_smoothen_neg: int = ...

  """

  Negative mesh smoothening

  """

  mesh_smoothen_pos: int = ...

  """

  Positive mesh smoothening

  """

  noise_pos_scale: float = ...

  """

  Scale of noise (higher value results in larger vortices)

  """

  noise_scale: int = ...

  """

  The noise simulation is scaled up by this factor (compared to the base resolution of the domain)

  """

  noise_strength: float = ...

  """

  Strength of noise

  """

  noise_time_anim: float = ...

  """

  Animation time of noise

  """

  openvdb_cache_compress_type: str = ...

  """

  Compression method to be used

  * ``ZIP``
Zip -- Effective but slow compression.

  * ``BLOSC``
Blosc -- Multithreaded compression, similar in size and quality as 'Zip'.

  * ``NONE``
None -- Do not use any compression.

  """

  openvdb_data_depth: str = ...

  """

  Bit depth for fluid particles and grids (lower bit values reduce file size)

  """

  particle_band_width: float = ...

  """

  Particle (narrow) band width (higher value results in thicker band and more particles)

  """

  particle_max: int = ...

  """

  Maximum number of particles per cell (ensures that each cell has at most this amount of particles)

  """

  particle_min: int = ...

  """

  Minimum number of particles per cell (ensures that each cell has at least this amount of particles)

  """

  particle_number: int = ...

  """

  Particle number factor (higher value results in more particles)

  """

  particle_radius: float = ...

  """

  Particle radius factor. Increase this value if the simulation appears to leak volume, decrease it if the simulation seems to gain volume

  """

  particle_randomness: float = ...

  """

  Randomness factor for particle sampling

  """

  particle_scale: int = ...

  """

  The particle simulation is scaled up by this factor (compared to the base resolution of the domain)

  """

  resolution_max: int = ...

  """

  Resolution used for the fluid domain. Value corresponds to the longest domain side (resolution for other domain sides is calculated automatically)

  """

  show_gridlines: bool = ...

  """

  Show gridlines

  """

  show_velocity: bool = ...

  """

  Visualize vector fields

  """

  simulation_method: str = ...

  """

  Change the underlying simulation method

  * ``FLIP``
FLIP -- Use FLIP as the simulation method (more splashy behavior).

  * ``APIC``
APIC -- Use APIC as the simulation method (more energetic and stable behavior).

  """

  slice_axis: str = ...

  """

  * ``AUTO``
Auto -- Adjust slice direction according to the view direction.

  * ``X``
X -- Slice along the X axis.

  * ``Y``
Y -- Slice along the Y axis.

  * ``Z``
Z -- Slice along the Z axis.

  """

  slice_depth: float = ...

  """

  Position of the slice

  """

  slice_per_voxel: float = ...

  """

  How many slices per voxel should be generated

  """

  sndparticle_boundary: str = ...

  """

  How particles that left the domain are treated

  * ``DELETE``
Delete -- Delete secondary particles that are inside obstacles or left the domain.

  * ``PUSHOUT``
Push Out -- Push secondary particles that left the domain back into the domain.

  """

  sndparticle_bubble_buoyancy: float = ...

  """

  Amount of buoyancy force that rises bubbles (high value results in bubble movement mainly upwards)

  """

  sndparticle_bubble_drag: float = ...

  """

  Amount of drag force that moves bubbles along with the fluid (high value results in bubble movement mainly along with the fluid)

  """

  sndparticle_combined_export: str = ...

  """

  Determines which particle systems are created from secondary particles

  * ``OFF``
Off -- Create a separate particle system for every secondary particle type.

  * ``SPRAY_FOAM``
Spray + Foam -- Spray and foam particles are saved in the same particle system.

  * ``SPRAY_BUBBLES``
Spray + Bubbles -- Spray and bubble particles are saved in the same particle system.

  * ``FOAM_BUBBLES``
Foam + Bubbles -- Foam and bubbles particles are saved in the same particle system.

  * ``SPRAY_FOAM_BUBBLES``
Spray + Foam + Bubbles -- Create one particle system that contains all three secondary particle types.

  """

  sndparticle_life_max: float = ...

  """

  Highest possible particle lifetime

  """

  sndparticle_life_min: float = ...

  """

  Lowest possible particle lifetime

  """

  sndparticle_potential_max_energy: float = ...

  """

  Upper clamping threshold that indicates the fluid speed where cells no longer emit more particles (higher value results in generally less particles)

  """

  sndparticle_potential_max_trappedair: float = ...

  """

  Upper clamping threshold for marking fluid cells where air is trapped (higher value results in less marked cells)

  """

  sndparticle_potential_max_wavecrest: float = ...

  """

  Upper clamping threshold for marking fluid cells as wave crests (higher value results in less marked cells)

  """

  sndparticle_potential_min_energy: float = ...

  """

  Lower clamping threshold that indicates the fluid speed where cells start to emit particles (lower values result in generally more particles)

  """

  sndparticle_potential_min_trappedair: float = ...

  """

  Lower clamping threshold for marking fluid cells where air is trapped (lower value results in more marked cells)

  """

  sndparticle_potential_min_wavecrest: float = ...

  """

  Lower clamping threshold for marking fluid cells as wave crests (lower value results in more marked cells)

  """

  sndparticle_potential_radius: int = ...

  """

  Radius to compute potential for each cell (higher values are slower but create smoother potential grids)

  """

  sndparticle_sampling_trappedair: int = ...

  """

  Maximum number of particles generated per trapped air cell per frame

  """

  sndparticle_sampling_wavecrest: int = ...

  """

  Maximum number of particles generated per wave crest cell per frame

  """

  sndparticle_update_radius: int = ...

  """

  Radius to compute position update for each particle (higher values are slower but particles move less chaotic)

  """

  start_point: typing.Tuple[float, float, float] = ...

  """

  Start point

  """

  surface_tension: float = ...

  """

  Surface tension of liquid (higher value results in greater hydrophobic behavior)

  """

  sys_particle_maximum: int = ...

  """

  Maximum number of fluid particles that are allowed in this simulation

  """

  temperature_grid: typing.Tuple[float, ...] = ...

  """

  Smoke temperature grid, range 0 to 1 represents 0 to 1000K

  """

  time_scale: float = ...

  """

  Adjust simulation speed

  """

  timesteps_max: int = ...

  """

  Maximum number of simulation steps to perform for one frame

  """

  timesteps_min: int = ...

  """

  Minimum number of simulation steps to perform for one frame

  """

  use_adaptive_domain: bool = ...

  """

  Adapt simulation resolution and size to fluid

  """

  use_adaptive_timesteps: bool = ...

  use_bubble_particles: bool = ...

  """

  Create bubble particle system

  """

  use_collision_border_back: bool = ...

  """

  Enable collisions with back domain border

  """

  use_collision_border_bottom: bool = ...

  """

  Enable collisions with bottom domain border

  """

  use_collision_border_front: bool = ...

  """

  Enable collisions with front domain border

  """

  use_collision_border_left: bool = ...

  """

  Enable collisions with left domain border

  """

  use_collision_border_right: bool = ...

  """

  Enable collisions with right domain border

  """

  use_collision_border_top: bool = ...

  """

  Enable collisions with top domain border

  """

  use_color_ramp: bool = ...

  """

  Render a simulation field while mapping its voxels values to the colors of a ramp or using a predefined color code

  """

  use_diffusion: bool = ...

  """

  Enable fluid diffusion settings (e.g. viscosity, surface tension)

  """

  use_dissolve_smoke: bool = ...

  """

  Let smoke disappear over time

  """

  use_dissolve_smoke_log: bool = ...

  """

  Dissolve smoke in a logarithmic fashion. Dissolves quickly at first, but lingers longer

  """

  use_flip_particles: bool = ...

  """

  Create liquid particle system

  """

  use_foam_particles: bool = ...

  """

  Create foam particle system

  """

  use_fractions: bool = ...

  """

  Fractional obstacles improve and smoothen the fluid-obstacle boundary

  """

  use_guide: bool = ...

  """

  Enable fluid guiding

  """

  use_mesh: bool = ...

  """

  Enable fluid mesh (using amplification)

  """

  use_noise: bool = ...

  """

  Enable fluid noise (using amplification)

  """

  use_slice: bool = ...

  """

  Perform a single slice of the domain object

  """

  use_speed_vectors: bool = ...

  """

  Caches velocities of mesh vertices. These will be used (automatically) when rendering with motion blur enabled

  """

  use_spray_particles: bool = ...

  """

  Create spray particle system

  """

  use_tracer_particles: bool = ...

  """

  Create tracer particle system

  """

  use_viscosity: bool = ...

  """

  Enable fluid viscosity settings

  """

  vector_display_type: str = ...

  """

  * ``NEEDLE``
Needle -- Display vectors as needles.

  * ``STREAMLINE``
Streamlines -- Display vectors as streamlines.

  * ``MAC``
MAC Grid -- Display vector field as MAC grid.

  """

  vector_field: str = ...

  """

  Vector field to be represented by the display vectors

  * ``FLUID_VELOCITY``
Fluid Velocity -- Velocity field of the fluid domain.

  * ``GUIDE_VELOCITY``
Guide Velocity -- Guide velocity field of the fluid domain.

  * ``FORCE``
Force -- Force field of the fluid domain.

  """

  vector_scale: float = ...

  """

  Multiplier for scaling the vectors

  """

  vector_scale_with_magnitude: bool = ...

  """

  Scale vectors with their magnitudes

  """

  vector_show_mac_x: bool = ...

  """

  Show X-component of MAC Grid

  """

  vector_show_mac_y: bool = ...

  """

  Show Y-component of MAC Grid

  """

  vector_show_mac_z: bool = ...

  """

  Show Z-component of MAC Grid

  """

  velocity_grid: typing.Tuple[float, ...] = ...

  """

  Smoke velocity grid

  """

  viscosity_base: float = ...

  """

  Viscosity setting: value that is multiplied by 10 to the power of (exponent*-1)

  """

  viscosity_exponent: int = ...

  """

  Negative exponent for the viscosity value (to simplify entering small values e.g. 5*10^-6)

  """

  viscosity_value: float = ...

  """

  Viscosity of liquid (higher values result in more viscous fluids, a value of 0 will still apply some viscosity)

  """

  vorticity: float = ...

  """

  Amount of turbulence and rotation in smoke

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FluidEffectorSettings(bpy_struct):

  """

  Smoke collision settings

  """

  effector_type: str = ...

  """

  Change type of effector in the simulation

  * ``COLLISION``
Collision -- Create collision object.

  * ``GUIDE``
Guide -- Create guide object.

  """

  guide_mode: str = ...

  """

  How to create guiding velocities

  * ``MAXIMUM``
Maximize -- Compare velocities from previous frame with new velocities from current frame and keep the maximum.

  * ``MINIMUM``
Minimize -- Compare velocities from previous frame with new velocities from current frame and keep the minimum.

  * ``OVERRIDE``
Override -- Always write new guide velocities for every frame (each frame only contains current velocities from guiding objects).

  * ``AVERAGED``
Averaged -- Take average of velocities from previous frame and new velocities from current frame.

  """

  subframes: int = ...

  """

  Number of additional samples to take between frames to improve quality of fast moving effector objects

  """

  surface_distance: float = ...

  """

  Additional distance around mesh surface to consider as effector

  """

  use_effector: bool = ...

  """

  Control when to apply the effector

  """

  use_plane_init: bool = ...

  """

  Treat this object as a planar, unclosed mesh

  """

  velocity_factor: float = ...

  """

  Multiplier of obstacle velocity

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FluidFlowSettings(bpy_struct):

  """

  Fluid flow settings

  """

  density: float = ...

  density_vertex_group: str = ...

  """

  Name of vertex group which determines surface emission rate

  """

  flow_behavior: str = ...

  """

  Change flow behavior in the simulation

  * ``INFLOW``
Inflow -- Add fluid to simulation.

  * ``OUTFLOW``
Outflow -- Delete fluid from simulation.

  * ``GEOMETRY``
Geometry -- Only use given geometry for fluid.

  """

  flow_source: str = ...

  """

  Change how fluid is emitted

  """

  flow_type: str = ...

  """

  Change type of fluid in the simulation

  * ``SMOKE``
Smoke -- Add smoke.

  * ``BOTH``
Fire + Smoke -- Add fire and smoke.

  * ``FIRE``
Fire -- Add fire.

  * ``LIQUID``
Liquid -- Add liquid.

  """

  fuel_amount: float = ...

  noise_texture: Texture = ...

  """

  Texture that controls emission strength

  """

  particle_size: float = ...

  """

  Particle size in simulation cells

  """

  particle_system: ParticleSystem = ...

  """

  Particle systems emitted from the object

  """

  smoke_color: typing.Tuple[float, float, float] = ...

  """

  Color of smoke

  """

  subframes: int = ...

  """

  Number of additional samples to take between frames to improve quality of fast moving flows

  """

  surface_distance: float = ...

  """

  Controls fluid emission from the mesh surface (higher value results in emission further away from the mesh surface

  """

  temperature: float = ...

  """

  Temperature difference to ambient temperature

  """

  texture_map_type: str = ...

  """

  Texture mapping type

  * ``AUTO``
Generated -- Generated coordinates centered to flow object.

  * ``UV``
UV -- Use UV layer for texture coordinates.

  """

  texture_offset: float = ...

  """

  Z-offset of texture mapping

  """

  texture_size: float = ...

  """

  Size of texture mapping

  """

  use_absolute: bool = ...

  """

  Only allow given density value in emitter area and will not add up

  """

  use_inflow: bool = ...

  """

  Control when to apply fluid flow

  """

  use_initial_velocity: bool = ...

  """

  Fluid has some initial velocity when it is emitted

  """

  use_particle_size: bool = ...

  """

  Set particle size in simulation cells or use nearest cell

  """

  use_plane_init: bool = ...

  """

  Treat this object as a planar and unclosed mesh. Fluid will only be emitted from the mesh surface and based on the surface emission value

  """

  use_texture: bool = ...

  """

  Use a texture to control emission strength

  """

  uv_layer: str = ...

  """

  UV map name

  """

  velocity_coord: typing.Tuple[float, float, float] = ...

  """

  Additional initial velocity in X, Y and Z direction (added to source velocity)

  """

  velocity_factor: float = ...

  """

  Multiplier of source velocity passed to fluid (source velocity is non-zero only if object is moving)

  """

  velocity_normal: float = ...

  """

  Amount of normal directional velocity

  """

  velocity_random: float = ...

  """

  Amount of random velocity

  """

  volume_density: float = ...

  """

  Controls fluid emission from within the mesh (higher value results in greater emissions from inside the mesh)

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FModifier(bpy_struct):

  """

  Modifier for values of F-Curve

  """

  active: bool = ...

  """

  F-Curve modifier will show settings in the editor

  """

  blend_in: float = ...

  """

  Number of frames from start frame for influence to take effect

  """

  blend_out: float = ...

  """

  Number of frames from end frame for influence to fade out

  """

  frame_end: float = ...

  """

  Frame that modifier's influence ends (if Restrict Frame Range is in use)

  """

  frame_start: float = ...

  """

  Frame that modifier's influence starts (if Restrict Frame Range is in use)

  """

  influence: float = ...

  """

  Amount of influence F-Curve Modifier will have when not fading in/out

  """

  is_valid: bool = ...

  """

  F-Curve Modifier has invalid settings and will not be evaluated

  """

  mute: bool = ...

  """

  Enable F-Curve modifier evaluation

  """

  show_expanded: bool = ...

  """

  F-Curve Modifier's panel is expanded in UI

  """

  type: str = ...

  """

  F-Curve Modifier Type

  * ``NULL``
Invalid.

  * ``GENERATOR``
Generator -- Generate a curve using a factorized or expanded polynomial.

  * ``FNGENERATOR``
Built-In Function -- Generate a curve using standard math functions such as sin and cos.

  * ``ENVELOPE``
Envelope -- Reshape F-Curve values, e.g. change amplitude of movements.

  * ``CYCLES``
Cycles -- Cyclic extend/repeat keyframe sequence.

  * ``NOISE``
Noise -- Add pseudo-random noise on top of F-Curves.

  * ``LIMITS``
Limits -- Restrict maximum and minimum values of F-Curve.

  * ``STEPPED``
Stepped Interpolation -- Snap values to nearest grid step, e.g. for a stop-motion look.

  """

  use_influence: bool = ...

  """

  F-Curve Modifier's effects will be tempered by a default factor

  """

  use_restricted_range: bool = ...

  """

  F-Curve Modifier is only applied for the specified frame range to help mask off effects in order to chain them

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FModifierEnvelopeControlPoint(bpy_struct):

  """

  Control point for envelope F-Modifier

  """

  frame: float = ...

  """

  Frame this control-point occurs on

  """

  max: float = ...

  """

  Upper bound of envelope at this control-point

  """

  min: float = ...

  """

  Lower bound of envelope at this control-point

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FModifierEnvelopeControlPoints(bpy_struct):

  """

  Control points defining the shape of the envelope

  """

  def add(self, frame: float) -> FModifierEnvelopeControlPoint:

    """

    Add a control point to a FModifierEnvelope

    """

    ...

  def remove(self, point: FModifierEnvelopeControlPoint) -> None:

    """

    Remove a control-point from an FModifierEnvelope

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FreestyleLineSet(bpy_struct):

  """

  Line set for associating lines and style parameters

  """

  collection: Collection = ...

  """

  A collection of objects based on which feature edges are selected

  """

  collection_negation: str = ...

  """

  Specify either inclusion or exclusion of feature edges belonging to a collection of objects

  * ``INCLUSIVE``
Inclusive -- Select feature edges belonging to some object in the group.

  * ``EXCLUSIVE``
Exclusive -- Select feature edges not belonging to any object in the group.

  """

  edge_type_combination: str = ...

  """

  Specify a logical combination of selection conditions on feature edge types

  * ``OR``
Logical OR -- Select feature edges satisfying at least one of edge type conditions.

  * ``AND``
Logical AND -- Select feature edges satisfying all edge type conditions.

  """

  edge_type_negation: str = ...

  """

  Specify either inclusion or exclusion of feature edges selected by edge types

  * ``INCLUSIVE``
Inclusive -- Select feature edges satisfying the given edge type conditions.

  * ``EXCLUSIVE``
Exclusive -- Select feature edges not satisfying the given edge type conditions.

  """

  exclude_border: bool = ...

  """

  Exclude border edges

  """

  exclude_contour: bool = ...

  """

  Exclude contours

  """

  exclude_crease: bool = ...

  """

  Exclude crease edges

  """

  exclude_edge_mark: bool = ...

  """

  Exclude edge marks

  """

  exclude_external_contour: bool = ...

  """

  Exclude external contours

  """

  exclude_material_boundary: bool = ...

  """

  Exclude edges at material boundaries

  """

  exclude_ridge_valley: bool = ...

  """

  Exclude ridges and valleys

  """

  exclude_silhouette: bool = ...

  """

  Exclude silhouette edges

  """

  exclude_suggestive_contour: bool = ...

  """

  Exclude suggestive contours

  """

  face_mark_condition: str = ...

  """

  Specify a feature edge selection condition based on face marks

  * ``ONE``
One Face -- Select a feature edge if either of its adjacent faces is marked.

  * ``BOTH``
Both Faces -- Select a feature edge if both of its adjacent faces are marked.

  """

  face_mark_negation: str = ...

  """

  Specify either inclusion or exclusion of feature edges selected by face marks

  * ``INCLUSIVE``
Inclusive -- Select feature edges satisfying the given face mark conditions.

  * ``EXCLUSIVE``
Exclusive -- Select feature edges not satisfying the given face mark conditions.

  """

  linestyle: FreestyleLineStyle = ...

  """

  Line style settings

  """

  name: str = ...

  """

  Line set name

  """

  qi_end: int = ...

  """

  Last QI value of the QI range

  """

  qi_start: int = ...

  """

  First QI value of the QI range

  """

  select_border: bool = ...

  """

  Select border edges (open mesh edges)

  """

  select_by_collection: bool = ...

  """

  Select feature edges based on a collection of objects

  """

  select_by_edge_types: bool = ...

  """

  Select feature edges based on edge types

  """

  select_by_face_marks: bool = ...

  """

  Select feature edges by face marks

  """

  select_by_image_border: bool = ...

  """

  Select feature edges by image border (less memory consumption)

  """

  select_by_visibility: bool = ...

  """

  Select feature edges based on visibility

  """

  select_contour: bool = ...

  """

  Select contours (outer silhouettes of each object)

  """

  select_crease: bool = ...

  """

  Select crease edges (those between two faces making an angle smaller than the Crease Angle)

  """

  select_edge_mark: bool = ...

  """

  Select edge marks (edges annotated by Freestyle edge marks)

  """

  select_external_contour: bool = ...

  """

  Select external contours (outer silhouettes of occluding and occluded objects)

  """

  select_material_boundary: bool = ...

  """

  Select edges at material boundaries

  """

  select_ridge_valley: bool = ...

  """

  Select ridges and valleys (boundary lines between convex and concave areas of surface)

  """

  select_silhouette: bool = ...

  """

  Select silhouettes (edges at the boundary of visible and hidden faces)

  """

  select_suggestive_contour: bool = ...

  """

  Select suggestive contours (almost silhouette/contour edges)

  """

  show_render: bool = ...

  """

  Enable or disable this line set during stroke rendering

  """

  visibility: str = ...

  """

  Determine how to use visibility for feature edge selection

  * ``VISIBLE``
Visible -- Select visible feature edges.

  * ``HIDDEN``
Hidden -- Select hidden feature edges.

  * ``RANGE``
Quantitative Invisibility -- Select feature edges within a range of quantitative invisibility (QI) values.

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FreestyleModules(bpy_struct):

  """

  A list of style modules (to be applied from top to bottom)

  """

  def new(self) -> FreestyleModuleSettings:

    """

    Add a style module to scene render layer Freestyle settings

    """

    ...

  def remove(self, module: FreestyleModuleSettings) -> None:

    """

    Remove a style module from scene render layer Freestyle settings

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FreestyleModuleSettings(bpy_struct):

  """

  Style module configuration for specifying a style module

  """

  script: Text = ...

  """

  Python script to define a style module

  """

  use: bool = ...

  """

  Enable or disable this style module during stroke rendering

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FreestyleSettings(bpy_struct):

  """

  Freestyle settings for a ViewLayer data-block

  """

  as_render_pass: bool = ...

  """

  Renders Freestyle output to a separate pass instead of overlaying it on the Combined pass

  """

  crease_angle: float = ...

  """

  Angular threshold for detecting crease edges

  """

  kr_derivative_epsilon: float = ...

  """

  Kr derivative epsilon for computing suggestive contours

  """

  linesets: typing.Union[Linesets, typing.Sequence[FreestyleLineSet], typing.Mapping[str, FreestyleLineSet], bpy_prop_collection] = ...

  mode: str = ...

  """

  Select the Freestyle control mode

  * ``SCRIPT``
Python Scripting -- Advanced mode for using style modules written in Python.

  * ``EDITOR``
Parameter Editor -- Basic mode for interactive style parameter editing.

  """

  modules: typing.Union[FreestyleModules, typing.Sequence[FreestyleModuleSettings], typing.Mapping[str, FreestyleModuleSettings], bpy_prop_collection] = ...

  """

  A list of style modules (to be applied from top to bottom)

  """

  sphere_radius: float = ...

  """

  Sphere radius for computing curvatures

  """

  use_culling: bool = ...

  """

  If enabled, out-of-view edges are ignored

  """

  use_material_boundaries: bool = ...

  """

  Enable material boundaries

  """

  use_ridges_and_valleys: bool = ...

  """

  Enable ridges and valleys

  """

  use_smoothness: bool = ...

  """

  Take face smoothness into account in view map calculation

  """

  use_suggestive_contours: bool = ...

  """

  Enable suggestive contours

  """

  use_view_map_cache: bool = ...

  """

  Keep the computed view map and avoid recalculating it if mesh geometry is unchanged

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Function(bpy_struct):

  """

  RNA function definition

  """

  description: str = ...

  """

  Description of the Function's purpose

  """

  identifier: str = ...

  """

  Unique name used in the code and scripting

  """

  is_registered: bool = ...

  """

  Function is registered as callback as part of type registration

  """

  is_registered_optional: bool = ...

  """

  Function is optionally registered as callback part of type registration

  """

  parameters: typing.Union[typing.Sequence[Property], typing.Mapping[str, Property], bpy_prop_collection] = ...

  """

  Parameters for the function

  """

  use_self: bool = ...

  """

  Function does not pass its self as an argument (becomes a static method in python)

  """

  use_self_type: bool = ...

  """

  Function passes its self type as an argument (becomes a class method in python if use_self is false)

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Gizmo(bpy_struct):

  """

  Collection of gizmos

  """

  alpha: float = ...

  alpha_highlight: float = ...

  bl_idname: str = ...

  color: typing.Tuple[float, float, float] = ...

  color_highlight: typing.Tuple[float, float, float] = ...

  group: GizmoGroup = ...

  """

  Gizmo group this gizmo is a member of

  """

  hide: bool = ...

  hide_keymap: bool = ...

  """

  Ignore the key-map for this gizmo

  """

  hide_select: bool = ...

  is_highlight: bool = ...

  is_modal: bool = ...

  line_width: float = ...

  matrix_basis: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]] = ...

  matrix_offset: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]] = ...

  matrix_space: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]] = ...

  matrix_world: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]] = ...

  properties: GizmoProperties = ...

  scale_basis: float = ...

  select: bool = ...

  select_bias: float = ...

  """

  Depth bias used for selection

  """

  use_draw_hover: bool = ...

  use_draw_modal: bool = ...

  """

  Show while dragging

  """

  use_draw_offset_scale: bool = ...

  """

  Scale the offset matrix (use to apply screen-space offset)

  """

  use_draw_scale: bool = ...

  """

  Use scale when calculating the matrix

  """

  use_draw_value: bool = ...

  """

  Show an indicator for the current value while dragging

  """

  use_event_handle_all: bool = ...

  """

  When highlighted, do not pass events through to be handled by other keymaps

  """

  use_grab_cursor: bool = ...

  use_operator_tool_properties: bool = ...

  """

  Merge active tool properties on activation (does not overwrite existing)

  """

  use_select_background: bool = ...

  """

  Don't write into the depth buffer

  """

  use_tooltip: bool = ...

  """

  Use tooltips when hovering over this gizmo

  """

  def draw(self, context: Context) -> None:

    ...

  def draw_select(self, context: Context, select_id: int = 0) -> None:

    ...

  def test_select(self, context: Context, location: typing.Tuple[int, int]) -> int:

    ...

  def modal(self, context: Context, event: Event, tweak: typing.Set[str]) -> typing.Set[str]:

    ...

  def setup(self) -> None:

    ...

  def invoke(self, context: Context, event: Event) -> typing.Set[str]:

    ...

  def exit(self, context: Context, cancel: bool) -> None:

    ...

  def select_refresh(self) -> None:

    ...

  def draw_preset_box(self, matrix: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]], select_id: int = -1) -> None:

    """

    Draw a box

    """

    ...

  def draw_preset_arrow(self, matrix: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]], axis: str = 'POS_Z', select_id: int = -1) -> None:

    """

    Draw a box

    """

    ...

  def draw_preset_circle(self, matrix: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]], axis: str = 'POS_Z', select_id: int = -1) -> None:

    """

    Draw a box

    """

    ...

  def draw_preset_facemap(self, object: Object, face_map: int, select_id: int = -1) -> None:

    """

    Draw the face-map of a mesh object

    """

    ...

  def target_set_prop(self, target: str, data: typing.Any, property: str, index: int = -1) -> None:

    ...

  def target_set_operator(self, operator: str, index: int = 0) -> OperatorProperties:

    """

    Operator to run when activating the gizmo (overrides property targets)

    """

    ...

  def target_is_valid(self, property: str) -> bool:

    ...

  def draw_custom_shape(self, shape: typing.Any, *args, matrix: mathutils.Matrix = None, select_id: typing.Any = None) -> None:

    """

    Draw a shape created form :class:`bpy.types.Gizmo.draw_custom_shape`.

    """

    ...

  @staticmethod

  def new_custom_shape(type: str, verts: typing.Sequence[typing.Any]) -> typing.Any:

    """

    Create a new shape that can be passed to :class:`bpy.types.Gizmo.draw_custom_shape`.

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

  def target_get_range(self, target: typing.Any) -> typing.Tuple[typing.Any, ...]:

    """

    Get the range for this target property.

    """

    ...

  def target_get_value(self, target: str) -> typing.Any:

    """

    Get the value of this target property.

    """

    ...

  def target_set_handler(self, target: typing.Any, get: typing.Callable, set: typing.Callable, range: typing.Callable = None) -> None:

    """

    Assigns callbacks to a gizmos property.

    """

    ...

  def target_set_value(self, target: str) -> None:

    """

    Set the value of this target property.

    """

    ...

class GizmoGroup(bpy_struct):

  """

  Storage of an operator being executed, or registered after execution

  """

  bl_idname: str = ...

  bl_label: str = ...

  bl_options: typing.Set[str] = ...

  """

  Options for this operator type

  * ``3D``
3D -- Use in 3D viewport.

  * ``SCALE``
Scale -- Scale to respect zoom (otherwise zoom independent display size).

  * ``DEPTH_3D``
Depth 3D -- Supports culled depth by other objects in the view.

  * ``SELECT``
Select -- Supports selection.

  * ``PERSISTENT``
Persistent.

  * ``SHOW_MODAL_ALL``
Show Modal All -- Show all while interacting, as well as this group when another is being interacted with.

  * ``EXCLUDE_MODAL``
Exclude Modal -- Show all except this group while interacting.

  * ``TOOL_INIT``
Tool Init -- Postpone running until tool operator run (when used with a tool).

  * ``VR_REDRAWS``
VR Redraws -- The gizmos are made for use with virtual reality sessions and require special redraw management.

  """

  bl_owner_id: str = ...

  bl_region_type: str = ...

  """

  The region where the panel is going to be used in

  """

  bl_space_type: str = ...

  """

  The space where the panel is going to be used in

  * ``EMPTY``
Empty.

  * ``VIEW_3D``
3D Viewport -- Manipulate objects in a 3D environment.

  * ``IMAGE_EDITOR``
UV/Image Editor -- View and edit images and UV Maps.

  * ``NODE_EDITOR``
Node Editor -- Editor for node-based shading and compositing tools.

  * ``SEQUENCE_EDITOR``
Video Sequencer -- Video editing tools.

  * ``CLIP_EDITOR``
Movie Clip Editor -- Motion tracking tools.

  * ``DOPESHEET_EDITOR``
Dope Sheet -- Adjust timing of keyframes.

  * ``GRAPH_EDITOR``
Graph Editor -- Edit drivers and keyframe interpolation.

  * ``NLA_EDITOR``
Nonlinear Animation -- Combine and layer Actions.

  * ``TEXT_EDITOR``
Text Editor -- Edit scripts and in-file documentation.

  * ``CONSOLE``
Python Console -- Interactive programmatic console for advanced editing and script development.

  * ``INFO``
Info -- Log of operations, warnings and error messages.

  * ``TOPBAR``
Top Bar -- Global bar at the top of the screen for global per-window settings.

  * ``STATUSBAR``
Status Bar -- Global bar at the bottom of the screen for general status information.

  * ``OUTLINER``
Outliner -- Overview of scene graph and all available data-blocks.

  * ``PROPERTIES``
Properties -- Edit properties of active object and related data-blocks.

  * ``FILE_BROWSER``
File Browser -- Browse for files and assets.

  * ``SPREADSHEET``
Spreadsheet -- Explore geometry data in a table.

  * ``PREFERENCES``
Preferences -- Edit persistent configuration settings.

  """

  gizmos: typing.Union[Gizmos, typing.Sequence[Gizmo], typing.Mapping[str, Gizmo], bpy_prop_collection] = ...

  """

  List of gizmos in the Gizmo Map

  """

  has_reports: bool = ...

  """

  GizmoGroup has a set of reports (warnings and errors) from last execution

  """

  name: str = ...

  @classmethod

  def poll(cls, context: Context) -> bool:

    """

    Test if the gizmo group can be called or not

    """

    ...

  @classmethod

  def setup_keymap(cls, keyconfig: KeyConfig) -> KeyMap:

    """

    Initialize keymaps for this gizmo group, use fallback keymap when not present

    """

    ...

  def setup(self, context: Context) -> None:

    """

    Create gizmos function for the gizmo group

    """

    ...

  def refresh(self, context: Context) -> None:

    """

    Refresh data (called on common state changes such as selection)

    """

    ...

  def draw_prepare(self, context: Context) -> None:

    """

    Run before each redraw

    """

    ...

  def invoke_prepare(self, context: Context, gizmo: Gizmo) -> None:

    """

    Run before invoke

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class GizmoGroupProperties(bpy_struct):

  """

  Input properties of a Gizmo Group

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class GizmoProperties(bpy_struct):

  """

  Input properties of an Gizmo

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Gizmos(bpy_struct):

  """

  Collection of gizmos

  """

  def new(self, type: str) -> Gizmo:

    """

    Add gizmo

    """

    ...

  def remove(self, gizmo: Gizmo) -> None:

    """

    Delete gizmo

    """

    ...

  def clear(self) -> None:

    """

    Delete all gizmos

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class GPencilEditCurve(bpy_struct):

  """

  Edition Curve

  """

  curve_points: typing.Union[typing.Sequence[GPencilEditCurvePoint], typing.Mapping[str, GPencilEditCurvePoint], bpy_prop_collection] = ...

  """

  Curve data points

  """

  select: bool = ...

  """

  Curve is selected for viewport editing

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class GPencilEditCurvePoint(bpy_struct):

  """

  Bezier curve point with two handles

  """

  co: typing.Tuple[float, float, float] = ...

  """

  Coordinates of the control point

  """

  handle_left: typing.Tuple[float, float, float] = ...

  """

  Coordinates of the first handle

  """

  handle_right: typing.Tuple[float, float, float] = ...

  """

  Coordinates of the second handle

  """

  hide: bool = ...

  """

  Visibility status

  """

  point_index: int = ...

  """

  Index of the corresponding grease pencil stroke point

  """

  pressure: float = ...

  """

  Pressure of the grease pencil stroke point

  """

  select_control_point: bool = ...

  """

  Control point selection status

  """

  select_left_handle: bool = ...

  """

  Handle 1 selection status

  """

  select_right_handle: bool = ...

  """

  Handle 2 selection status

  """

  strength: float = ...

  """

  Color intensity (alpha factor) of the grease pencil stroke point

  """

  uv_factor: float = ...

  """

  Internal UV factor

  """

  uv_rotation: float = ...

  """

  Internal UV factor for dot mode

  """

  vertex_color: typing.Tuple[float, float, float, float] = ...

  """

  Vertex color of the grease pencil stroke point

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class GPencilFrame(bpy_struct):

  """

  Collection of related sketches on a particular frame

  """

  frame_number: int = ...

  """

  The frame on which this sketch appears

  """

  is_edited: bool = ...

  """

  Frame is being edited (painted on)

  """

  keyframe_type: str = ...

  """

  Type of keyframe

  * ``KEYFRAME``
Keyframe -- Normal keyframe - e.g. for key poses.

  * ``BREAKDOWN``
Breakdown -- A breakdown pose - e.g. for transitions between key poses.

  * ``MOVING_HOLD``
Moving Hold -- A keyframe that is part of a moving hold.

  * ``EXTREME``
Extreme -- An 'extreme' pose, or some other purpose as needed.

  * ``JITTER``
Jitter -- A filler or baked keyframe for keying on ones, or some other purpose as needed.

  """

  select: bool = ...

  """

  Frame is selected for editing in the Dope Sheet

  """

  strokes: typing.Union[GPencilStrokes, typing.Sequence[GPencilStroke], typing.Mapping[str, GPencilStroke], bpy_prop_collection] = ...

  """

  Freehand curves defining the sketch on this frame

  """

  def clear(self) -> None:

    """

    Remove all the grease pencil frame data

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class GPencilFrames(bpy_struct):

  """

  Collection of grease pencil frames

  """

  def new(self, frame_number: int, active: bool = False) -> GPencilFrame:

    """

    Add a new grease pencil frame

    """

    ...

  def remove(self, frame: GPencilFrame) -> None:

    """

    Remove a grease pencil frame

    """

    ...

  def copy(self, source: GPencilFrame) -> GPencilFrame:

    """

    Copy a grease pencil frame

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class GPencilInterpolateSettings(bpy_struct):

  """

  Settings for Grease Pencil interpolation tools

  """

  interpolation_curve: CurveMapping = ...

  """

  Custom curve to control 'sequence' interpolation between Grease Pencil frames

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class GPencilLayer(bpy_struct):

  """

  Collection of related sketches

  """

  active_frame: GPencilFrame = ...

  """

  Frame currently being displayed for this layer

  """

  annotation_hide: bool = ...

  """

  Set annotation Visibility

  """

  annotation_onion_after_color: typing.Tuple[float, float, float] = ...

  """

  Base color for ghosts after the active frame

  """

  annotation_onion_after_range: int = ...

  """

  Maximum number of frames to show after current frame

  """

  annotation_onion_before_color: typing.Tuple[float, float, float] = ...

  """

  Base color for ghosts before the active frame

  """

  annotation_onion_before_range: int = ...

  """

  Maximum number of frames to show before current frame

  """

  annotation_opacity: float = ...

  """

  Annotation Layer Opacity

  """

  blend_mode: str = ...

  """

  Blend mode

  """

  channel_color: typing.Tuple[float, float, float] = ...

  """

  Custom color for animation channel in Dopesheet

  """

  color: typing.Tuple[float, float, float] = ...

  """

  Color for all strokes in this layer

  """

  frames: typing.Union[GPencilFrames, typing.Sequence[GPencilFrame], typing.Mapping[str, GPencilFrame], bpy_prop_collection] = ...

  """

  Sketches for this layer on different frames

  """

  hide: bool = ...

  """

  Set layer Visibility

  """

  info: str = ...

  """

  Layer name

  """

  is_parented: bool = ...

  """

  True when the layer parent object is set

  """

  is_ruler: bool = ...

  """

  This is a special ruler layer

  """

  line_change: int = ...

  """

  Thickness change to apply to current strokes (in pixels)

  """

  location: typing.Tuple[float, float, float] = ...

  """

  Values for change location

  """

  lock: bool = ...

  """

  Protect layer from further editing and/or frame changes

  """

  lock_frame: bool = ...

  """

  Lock current frame displayed by layer

  """

  lock_material: bool = ...

  """

  Avoids editing locked materials in the layer

  """

  mask_layers: typing.Union[GreasePencilMaskLayers, typing.Sequence[GPencilLayerMask], typing.Mapping[str, GPencilLayerMask], bpy_prop_collection] = ...

  """

  List of Masking Layers

  """

  matrix_inverse: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]] = ...

  """

  Parent inverse transformation matrix

  """

  matrix_inverse_layer: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]] = ...

  """

  Local Layer transformation inverse matrix

  """

  matrix_layer: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]] = ...

  """

  Local Layer transformation matrix

  """

  opacity: float = ...

  """

  Layer Opacity

  """

  parent: Object = ...

  """

  Parent object

  """

  parent_bone: str = ...

  """

  Name of parent bone in case of a bone parenting relation

  """

  parent_type: str = ...

  """

  Type of parent relation

  * ``OBJECT``
Object -- The layer is parented to an object.

  * ``ARMATURE``
Armature.

  * ``BONE``
Bone -- The layer is parented to a bone.

  """

  pass_index: int = ...

  """

  Index number for the "Layer Index" pass

  """

  rotation: typing.Tuple[float, float, float] = ...

  """

  Values for changes in rotation

  """

  scale: typing.Tuple[float, float, float] = ...

  """

  Values for changes in scale

  """

  select: bool = ...

  """

  Layer is selected for editing in the Dope Sheet

  """

  show_in_front: bool = ...

  """

  Make the layer display in front of objects

  """

  show_points: bool = ...

  """

  Show the points which make up the strokes (for debugging purposes)

  """

  thickness: int = ...

  """

  Thickness of annotation strokes

  """

  tint_color: typing.Tuple[float, float, float] = ...

  """

  Color for tinting stroke colors

  """

  tint_factor: float = ...

  """

  Factor of tinting color

  """

  use_annotation_onion_skinning: bool = ...

  """

  Display annotation onion skins before and after the current frame

  """

  use_lights: bool = ...

  """

  Enable the use of lights on stroke and fill materials

  """

  use_mask_layer: bool = ...

  """

  The visibility of drawings on this layer is affected by the layers in its masks list

  """

  use_onion_skinning: bool = ...

  """

  Display onion skins before and after the current frame

  """

  use_solo_mode: bool = ...

  """

  In Paint mode display only layers with keyframe in current frame

  """

  use_viewlayer_masks: bool = ...

  """

  Include the mask layers when rendering the view-layer

  """

  vertex_paint_opacity: float = ...

  """

  Vertex Paint mix factor

  """

  viewlayer_render: str = ...

  """

  Only include Layer in this View Layer render output (leave blank to include always)

  """

  def clear(self) -> None:

    """

    Remove all the grease pencil layer data

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class GPencilLayerMask(bpy_struct):

  """

  List of Mask Layers

  """

  hide: bool = ...

  """

  Set mask Visibility

  """

  invert: bool = ...

  """

  Invert mask

  """

  name: str = ...

  """

  Mask layer name

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class GpencilModifier(bpy_struct):

  """

  Modifier affecting the Grease Pencil object

  """

  is_override_data: bool = ...

  """

  In a local override object, whether this modifier comes from the linked reference object, or is local to the override

  """

  name: str = ...

  """

  Modifier name

  """

  show_expanded: bool = ...

  """

  Set modifier expanded in the user interface

  """

  show_in_editmode: bool = ...

  """

  Display modifier in Edit mode

  """

  show_render: bool = ...

  """

  Use modifier during render

  """

  show_viewport: bool = ...

  """

  Display modifier in viewport

  """

  type: str = ...

  """

  * ``GP_TEXTURE``
Texture Mapping -- Change stroke uv texture values.

  * ``GP_TIME``
Time Offset -- Offset keyframes.

  * ``GP_WEIGHT_ANGLE``
Vertex Weight Angle -- Generate Vertex Weights base on stroke angle.

  * ``GP_WEIGHT_PROXIMITY``
Vertex Weight Proximity -- Generate Vertex Weights base on distance to object.

  * ``GP_ARRAY``
Array -- Create array of duplicate instances.

  * ``GP_BUILD``
Build -- Create duplication of strokes.

  * ``GP_DASH``
Dot Dash -- Generate dot-dash styled strokes.

  * ``GP_LENGTH``
Length -- Extend or shrink strokes.

  * ``GP_LINEART``
Line Art -- Generate line art strokes from selected source.

  * ``GP_MIRROR``
Mirror -- Duplicate strokes like a mirror.

  * ``GP_MULTIPLY``
Multiple Strokes -- Produce multiple strokes along one stroke.

  * ``GP_SIMPLIFY``
Simplify -- Simplify stroke reducing number of points.

  * ``GP_SUBDIV``
Subdivide -- Subdivide stroke adding more control points.

  * ``GP_ARMATURE``
Armature -- Deform stroke points using armature object.

  * ``GP_HOOK``
Hook -- Deform stroke points using objects.

  * ``GP_LATTICE``
Lattice -- Deform strokes using lattice.

  * ``GP_NOISE``
Noise -- Add noise to strokes.

  * ``GP_OFFSET``
Offset -- Change stroke location, rotation or scale.

  * ``GP_SMOOTH``
Smooth -- Smooth stroke.

  * ``GP_THICK``
Thickness -- Change stroke thickness.

  * ``GP_COLOR``
Hue/Saturation -- Apply changes to stroke colors.

  * ``GP_OPACITY``
Opacity -- Opacity of the strokes.

  * ``GP_TINT``
Tint -- Tint strokes with new color.

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class GPencilSculptGuide(bpy_struct):

  """

  Guides for drawing

  """

  angle: float = ...

  """

  Direction of lines

  """

  angle_snap: float = ...

  """

  Angle snapping

  """

  location: typing.Tuple[float, float, float] = ...

  """

  Custom reference point for guides

  """

  reference_object: Object = ...

  """

  Object used for reference point

  """

  reference_point: str = ...

  """

  Type of speed guide

  * ``CURSOR``
Cursor -- Use cursor as reference point.

  * ``CUSTOM``
Custom -- Use custom reference point.

  * ``OBJECT``
Object -- Use object as reference point.

  """

  spacing: float = ...

  """

  Guide spacing

  """

  type: str = ...

  """

  Type of speed guide

  * ``CIRCULAR``
Circular -- Use single point to create rings.

  * ``RADIAL``
Radial -- Use single point as direction.

  * ``PARALLEL``
Parallel -- Parallel lines.

  * ``GRID``
Grid -- Grid allows horizontal and vertical lines.

  * ``ISO``
Isometric -- Grid allows isometric and vertical lines.

  """

  use_guide: bool = ...

  """

  Enable speed guides

  """

  use_snapping: bool = ...

  """

  Enable snapping to guides angle or spacing options

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class GPencilSculptSettings(bpy_struct):

  """

  General properties for Grease Pencil stroke sculpting tools

  """

  guide: GPencilSculptGuide = ...

  intersection_threshold: float = ...

  """

  Threshold for stroke intersections

  """

  lock_axis: str = ...

  """

  * ``VIEW``
View -- Align strokes to current view plane.

  * ``AXIS_Y``
Front (X-Z) -- Project strokes to plane locked to Y.

  * ``AXIS_X``
Side (Y-Z) -- Project strokes to plane locked to X.

  * ``AXIS_Z``
Top (X-Y) -- Project strokes to plane locked to Z.

  * ``CURSOR``
Cursor -- Align strokes to current 3D cursor orientation.

  """

  multiframe_falloff_curve: CurveMapping = ...

  """

  Custom curve to control falloff of brush effect by Grease Pencil frames

  """

  thickness_primitive_curve: CurveMapping = ...

  """

  Custom curve to control primitive thickness

  """

  use_multiframe_falloff: bool = ...

  """

  Use falloff effect when edit in multiframe mode to compute brush effect by frame

  """

  use_scale_thickness: bool = ...

  """

  Scale the stroke thickness when transforming strokes

  """

  use_thickness_curve: bool = ...

  """

  Use curve to define primitive stroke thickness

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class GPencilStroke(bpy_struct):

  """

  Freehand curve defining part of a sketch

  """

  aspect: typing.Tuple[float, float] = ...

  bound_box_max: typing.Tuple[float, float, float] = ...

  bound_box_min: typing.Tuple[float, float, float] = ...

  display_mode: str = ...

  """

  Coordinate space that stroke is in

  * ``SCREEN``
Screen -- Stroke is in screen-space.

  * ``3DSPACE``
3D Space -- Stroke is in 3D-space.

  * ``2DSPACE``
2D Space -- Stroke is in 2D-space.

  * ``2DIMAGE``
2D Image -- Stroke is in 2D-space (but with special 'image' scaling).

  """

  edit_curve: GPencilEditCurve = ...

  """

  Temporary data for Edit Curve

  """

  end_cap_mode: str = ...

  """

  Stroke end extreme cap style

  """

  hardness: float = ...

  """

  Amount of gradient along section of stroke

  """

  has_edit_curve: bool = ...

  """

  Stroke has Curve data to edit shape

  """

  is_nofill_stroke: bool = ...

  """

  Special stroke to use as boundary for filling areas

  """

  line_width: int = ...

  """

  Thickness of stroke (in pixels)

  """

  material_index: int = ...

  """

  Material slot index of this stroke

  """

  points: typing.Union[GPencilStrokePoints, typing.Sequence[GPencilStrokePoint], typing.Mapping[str, GPencilStrokePoint], bpy_prop_collection] = ...

  """

  Stroke data points

  """

  select: bool = ...

  """

  Stroke is selected for viewport editing

  """

  select_index: int = ...

  """

  Index of selection used for interpolation

  """

  start_cap_mode: str = ...

  """

  Stroke start extreme cap style

  """

  triangles: typing.Union[typing.Sequence[GPencilTriangle], typing.Mapping[str, GPencilTriangle], bpy_prop_collection] = ...

  """

  Triangulation data for HQ fill

  """

  use_cyclic: bool = ...

  """

  Enable cyclic drawing, closing the stroke

  """

  uv_rotation: float = ...

  """

  Rotation of the UV

  """

  uv_scale: float = ...

  """

  Scale of the UV

  """

  uv_translation: typing.Tuple[float, float] = ...

  """

  Translation of default UV position

  """

  vertex_color_fill: typing.Tuple[float, float, float, float] = ...

  """

  Color used to mix with fill color to get final color

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class GPencilStrokePoint(bpy_struct):

  """

  Data point for freehand stroke curve

  """

  co: typing.Tuple[float, float, float] = ...

  pressure: float = ...

  """

  Pressure of tablet at point when drawing it

  """

  select: bool = ...

  """

  Point is selected for viewport editing

  """

  strength: float = ...

  """

  Color intensity (alpha factor)

  """

  uv_factor: float = ...

  """

  Internal UV factor

  """

  uv_fill: typing.Tuple[float, float] = ...

  """

  Internal UV factor for filling

  """

  uv_rotation: float = ...

  """

  Internal UV factor for dot mode

  """

  vertex_color: typing.Tuple[float, float, float, float] = ...

  """

  Color used to mix with point color to get final color

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class GPencilStrokePoints(bpy_struct):

  """

  Collection of grease pencil stroke points

  """

  def add(self, count: int, pressure: float = 1.0, strength: float = 1.0) -> None:

    """

    Add a new grease pencil stroke point

    """

    ...

  def pop(self, index: int = -1) -> None:

    """

    Remove a grease pencil stroke point

    """

    ...

  def update(self) -> None:

    """

    Recalculate internal triangulation data

    """

    ...

  def weight_get(self, vertex_group_index: int = 0, point_index: int = 0) -> float:

    """

    Get vertex group point weight

    """

    ...

  def weight_set(self, vertex_group_index: int = 0, point_index: int = 0, weight: float = 0.0) -> None:

    """

    Set vertex group point weight

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class GPencilStrokes(bpy_struct):

  """

  Collection of grease pencil stroke

  """

  def new(self) -> GPencilStroke:

    """

    Add a new grease pencil stroke

    """

    ...

  def remove(self, stroke: GPencilStroke) -> None:

    """

    Remove a grease pencil stroke

    """

    ...

  def close(self, stroke: GPencilStroke) -> None:

    """

    Close a grease pencil stroke adding geometry

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class GPencilTriangle(bpy_struct):

  """

  Triangulation data for Grease Pencil fills

  """

  v1: int = ...

  """

  First triangle vertex index

  """

  v2: int = ...

  """

  Second triangle vertex index

  """

  v3: int = ...

  """

  Third triangle vertex index

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class GpencilVertexGroupElement(bpy_struct):

  """

  Weight value of a vertex in a vertex group

  """

  group: int = ...

  weight: float = ...

  """

  Vertex Weight

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class GreasePencilGrid(bpy_struct):

  """

  Settings for grid and canvas in 3D viewport

  """

  color: typing.Tuple[float, float, float] = ...

  """

  Color for grid lines

  """

  lines: int = ...

  """

  Number of subdivisions in each side of symmetry line

  """

  offset: typing.Tuple[float, float] = ...

  """

  Offset of the canvas

  """

  scale: typing.Tuple[float, float] = ...

  """

  Grid scale

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class GreasePencilLayers(bpy_struct):

  """

  Collection of grease pencil layers

  """

  active: GPencilLayer = ...

  """

  Active grease pencil layer

  """

  active_index: int = ...

  """

  Index of active grease pencil layer

  """

  active_note: str = ...

  """

  Note/Layer to add annotation strokes to

  """

  def new(self, name: str, set_active: bool = True) -> GPencilLayer:

    """

    Add a new grease pencil layer

    """

    ...

  def remove(self, layer: GPencilLayer) -> None:

    """

    Remove a grease pencil layer

    """

    ...

  def move(self, layer: GPencilLayer, type: str) -> None:

    """

    Move a grease pencil layer in the layer stack

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class GreasePencilMaskLayers(bpy_struct):

  """

  Collection of grease pencil masking layers

  """

  active_mask_index: int = ...

  """

  Active index in layer mask array

  """

  def add(self, layer: GPencilLayer) -> None:

    """

    Add a layer to mask list

    """

    ...

  def remove(self, mask: GPencilLayerMask) -> None:

    """

    Remove a layer from mask list

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Header(bpy_struct):

  """

  Editor header containing UI elements

  """

  bl_idname: str = ...

  """

  If this is set, the header gets a custom ID, otherwise it takes the name of the class used to define the panel; for example, if the class name is "OBJECT_HT_hello", and bl_idname is not set by the script, then bl_idname = "OBJECT_HT_hello"

  """

  bl_region_type: str = ...

  """

  The region where the header is going to be used in (defaults to header region)

  """

  bl_space_type: str = ...

  """

  The space where the header is going to be used in

  * ``EMPTY``
Empty.

  * ``VIEW_3D``
3D Viewport -- Manipulate objects in a 3D environment.

  * ``IMAGE_EDITOR``
UV/Image Editor -- View and edit images and UV Maps.

  * ``NODE_EDITOR``
Node Editor -- Editor for node-based shading and compositing tools.

  * ``SEQUENCE_EDITOR``
Video Sequencer -- Video editing tools.

  * ``CLIP_EDITOR``
Movie Clip Editor -- Motion tracking tools.

  * ``DOPESHEET_EDITOR``
Dope Sheet -- Adjust timing of keyframes.

  * ``GRAPH_EDITOR``
Graph Editor -- Edit drivers and keyframe interpolation.

  * ``NLA_EDITOR``
Nonlinear Animation -- Combine and layer Actions.

  * ``TEXT_EDITOR``
Text Editor -- Edit scripts and in-file documentation.

  * ``CONSOLE``
Python Console -- Interactive programmatic console for advanced editing and script development.

  * ``INFO``
Info -- Log of operations, warnings and error messages.

  * ``TOPBAR``
Top Bar -- Global bar at the top of the screen for global per-window settings.

  * ``STATUSBAR``
Status Bar -- Global bar at the bottom of the screen for general status information.

  * ``OUTLINER``
Outliner -- Overview of scene graph and all available data-blocks.

  * ``PROPERTIES``
Properties -- Edit properties of active object and related data-blocks.

  * ``FILE_BROWSER``
File Browser -- Browse for files and assets.

  * ``SPREADSHEET``
Spreadsheet -- Explore geometry data in a table.

  * ``PREFERENCES``
Preferences -- Edit persistent configuration settings.

  """

  layout: UILayout = ...

  """

  Structure of the header in the UI

  """

  def draw(self, context: Context) -> None:

    """

    Draw UI elements into the header UI layout

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Histogram(bpy_struct):

  """

  Statistical view of the levels of color in an image

  """

  mode: str = ...

  """

  Channels to display in the histogram

  * ``LUMA``
Luma -- Luma.

  * ``RGB``
RGB -- Red Green Blue.

  * ``R``
R -- Red.

  * ``G``
G -- Green.

  * ``B``
B -- Blue.

  * ``A``
A -- Alpha.

  """

  show_line: bool = ...

  """

  Display lines rather than filled shapes

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ID(bpy_struct):

  """

  Base type for data-blocks, defining a unique name, linking from other libraries and garbage collection

  """

  asset_data: AssetMetaData = ...

  """

  Additional data for an asset data-block

  """

  is_embedded_data: bool = ...

  """

  This data-block is not an independent one, but is actually a sub-data of another ID (typical example: root node trees or master collections)

  """

  is_evaluated: bool = ...

  """

  Whether this ID is runtime-only, evaluated data-block, or actual data from .blend file

  """

  is_library_indirect: bool = ...

  """

  Is this ID block linked indirectly

  """

  library: Library = ...

  """

  Library file the data-block is linked from

  """

  library_weak_reference: LibraryWeakReference = ...

  """

  Weak reference to a data-block in another library .blend file (used to re-use already appended data instead of appending new copies)

  """

  name: str = ...

  """

  Unique data-block ID name

  """

  name_full: str = ...

  """

  Unique data-block ID name, including library one is any

  """

  original: ID = ...

  """

  Actual data-block from .blend file (Main database) that generated that evaluated one

  """

  override_library: IDOverrideLibrary = ...

  """

  Library override data

  """

  preview: ImagePreview = ...

  """

  Preview image and icon of this data-block (always None if not supported for this type of data)

  """

  tag: bool = ...

  """

  Tools can use this to tag data for their own purposes (initial state is undefined)

  """

  use_fake_user: bool = ...

  """

  Save this data-block even if it has no users

  """

  users: int = ...

  """

  Number of times this data-block is referenced

  """

  def evaluated_get(self, depsgraph: Depsgraph) -> ID:

    """

    Get corresponding evaluated ID from the given dependency graph

    """

    ...

  def copy(self) -> ID:

    """

    Create a copy of this data-block (not supported for all data-blocks)

    """

    ...

  def asset_mark(self) -> None:

    """

    Enable easier reuse of the data-block through the Asset Browser, with the help of customizable metadata (like previews, descriptions and tags)

    """

    ...

  def asset_clear(self) -> None:

    """

    Delete all asset metadata and turn the asset data-block back into a normal data-block

    """

    ...

  def asset_generate_preview(self) -> None:

    """

    Generate preview image (might be scheduled in a background thread)

    """

    ...

  def override_create(self, remap_local_usages: bool = False) -> ID:

    """

    Create an overridden local copy of this linked data-block (not supported for all data-blocks)

    """

    ...

  def override_hierarchy_create(self, scene: Scene, view_layer: ViewLayer, reference: ID = None) -> ID:

    """

    Create an overridden local copy of this linked data-block, and most of its dependencies when it is a Collection or and Object

    """

    ...

  def override_template_create(self) -> None:

    """

    Create an override template for this ID

    """

    ...

  def user_clear(self) -> None:

    """

    Clear the user count of a data-block so its not saved, on reload the data will be removed

    This function is for advanced use only, misuse can crash blender since the user
count is used to prevent data being removed when it is used.

    .. code::

      # This example shows what _not_ to do, and will crash blender.
      import bpy

      # object which is in the scene.
      obj = bpy.data.objects["Cube"]

      # without this, removal would raise an error.
      obj.user_clear()

      # runs without an exception
      # but will crash on redraw.
      bpy.data.objects.remove(obj)

    """

    ...

  def user_remap(self, new_id: ID) -> None:

    """

    Replace all usage in the .blend file of this ID by new given one

    """

    ...

  def make_local(self, clear_proxy: bool = True) -> ID:

    """

    Make this datablock local, return local one (may be a copy of the original, in case it is also indirectly used)

    """

    ...

  def user_of_id(self, id: ID) -> int:

    """

    Count the number of times that ID uses/references given one

    """

    ...

  def animation_data_create(self) -> AnimData:

    """

    Create animation data to this ID, note that not all ID types support this

    """

    ...

  def animation_data_clear(self) -> None:

    """

    Clear animation on this this ID

    """

    ...

  def update_tag(self, refresh: typing.Set[str] = {}) -> None:

    """

    Tag the ID to update its display data, e.g. when calling :class:`bpy.types.Scene.update`

    """

    ...

  def preview_ensure(self) -> ImagePreview:

    """

    Ensure that this ID has preview data (if ID type supports it)

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class IDMaterials(bpy_struct):

  """

  Collection of materials

  """

  def append(self, material: Material) -> None:

    """

    Add a new material to the data-block

    """

    ...

  def pop(self, index: int = -1) -> Material:

    """

    Remove a material from the data-block

    """

    ...

  def clear(self) -> None:

    """

    Remove all materials from the data-block

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class IDOverrideLibrary(bpy_struct):

  """

  Struct gathering all data needed by overridden linked IDs

  """

  properties: typing.Union[IDOverrideLibraryProperties, typing.Sequence[IDOverrideLibraryProperty], typing.Mapping[str, IDOverrideLibraryProperty], bpy_prop_collection] = ...

  """

  List of overridden properties

  """

  reference: ID = ...

  """

  Linked ID used as reference by this override

  """

  def operations_update(self) -> None:

    """

    Update the library override operations based on the differences between this override ID and its reference

    """

    ...

  def reset(self, do_hierarchy: bool = True) -> None:

    """

    Reset this override to match again its linked reference ID

    """

    ...

  def destroy(self, do_hierarchy: bool = True) -> None:

    """

    Delete this override ID and remap its usages to its linked reference ID instead

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class IDOverrideLibraryProperties(bpy_struct):

  """

  Collection of override properties

  """

  def add(self, rna_path: str) -> IDOverrideLibraryProperty:

    """

    Add a property to the override library when it doesn't exist yet

    """

    ...

  def remove(self, property: IDOverrideLibraryProperty) -> None:

    """

    Remove and delete a property

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class IDOverrideLibraryProperty(bpy_struct):

  """

  Description of an overridden property

  """

  operations: typing.Union[IDOverrideLibraryPropertyOperations, typing.Sequence[IDOverrideLibraryPropertyOperation], typing.Mapping[str, IDOverrideLibraryPropertyOperation], bpy_prop_collection] = ...

  """

  List of overriding operations for a property

  """

  rna_path: str = ...

  """

  RNA path leading to that property, from owning ID

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class IDOverrideLibraryPropertyOperation(bpy_struct):

  """

  Description of an override operation over an overridden property

  """

  flag: str = ...

  """

  Optional flags (NOT USED)

  * ``MANDATORY``
Mandatory -- For templates, prevents the user from removing predefined operation (NOT USED).

  * ``LOCKED``
Locked -- Prevents the user from modifying that override operation (NOT USED).

  """

  operation: str = ...

  """

  What override operation is performed

  * ``NOOP``
No-Op -- Does nothing, prevents adding actual overrides (NOT USED).

  * ``REPLACE``
Replace -- Replace value of reference by overriding one.

  * ``DIFF_ADD``
Differential -- Stores and apply difference between reference and local value (NOT USED).

  * ``DIFF_SUB``
Differential -- Stores and apply difference between reference and local value (NOT USED).

  * ``FACT_MULTIPLY``
Factor -- Stores and apply multiplication factor between reference and local value (NOT USED).

  * ``INSERT_AFTER``
Insert After -- Insert a new item into collection after the one referenced in subitem_reference_name or _index.

  * ``INSERT_BEFORE``
Insert Before -- Insert a new item into collection after the one referenced in subitem_reference_name or _index (NOT USED).

  """

  subitem_local_index: int = ...

  """

  Used to handle insertions into collection

  """

  subitem_local_name: str = ...

  """

  Used to handle insertions into collection

  """

  subitem_reference_index: int = ...

  """

  Used to handle insertions into collection

  """

  subitem_reference_name: str = ...

  """

  Used to handle insertions into collection

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class IDOverrideLibraryPropertyOperations(bpy_struct):

  """

  Collection of override operations

  """

  def add(self, operation: str, subitem_reference_name: str = '', subitem_local_name: str = '', subitem_reference_index: int = -1, subitem_local_index: int = -1) -> IDOverrideLibraryPropertyOperation:

    """

    Add a new operation

    """

    ...

  def remove(self, operation: IDOverrideLibraryPropertyOperation) -> None:

    """

    Remove and delete an operation

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class IDPropertyWrapPtr(bpy_struct):

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class IKParam(bpy_struct):

  """

  Base type for IK solver parameters

  """

  ik_solver: str = ...

  """

  IK solver for which these parameters are defined

  * ``LEGACY``
Standard -- Original IK solver.

  * ``ITASC``
iTaSC -- Multi constraint, stateful IK solver.

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ImageFormatSettings(bpy_struct):

  """

  Settings for image formats

  """

  cineon_black: int = ...

  """

  Log conversion reference blackpoint

  """

  cineon_gamma: float = ...

  """

  Log conversion gamma

  """

  cineon_white: int = ...

  """

  Log conversion reference whitepoint

  """

  color_depth: str = ...

  """

  Bit depth per channel

  * ``8``
8 -- 8-bit color channels.

  * ``10``
10 -- 10-bit color channels.

  * ``12``
12 -- 12-bit color channels.

  * ``16``
16 -- 16-bit color channels.

  * ``32``
32 -- 32-bit color channels.

  """

  color_mode: str = ...

  """

  Choose BW for saving grayscale images, RGB for saving red, green and blue channels, and RGBA for saving red, green, blue and alpha channels

  * ``BW``
BW -- Images get saved in 8-bit grayscale (only PNG, JPEG, TGA, TIF).

  * ``RGB``
RGB -- Images are saved with RGB (color) data.

  * ``RGBA``
RGBA -- Images are saved with RGB and Alpha data (if supported).

  """

  compression: int = ...

  """

  Amount of time to determine best compression: 0 = no compression with fast file output, 100 = maximum lossless compression with slow file output

  """

  display_settings: ColorManagedDisplaySettings = ...

  """

  Settings of device saved image would be displayed on

  """

  exr_codec: str = ...

  """

  Codec settings for OpenEXR

  """

  file_format: str = ...

  """

  File format to save the rendered images as

  * ``BMP``
BMP -- Output image in bitmap format.

  * ``IRIS``
Iris -- Output image in SGI IRIS format.

  * ``PNG``
PNG -- Output image in PNG format.

  * ``JPEG``
JPEG -- Output image in JPEG format.

  * ``JPEG2000``
JPEG 2000 -- Output image in JPEG 2000 format.

  * ``TARGA``
Targa -- Output image in Targa format.

  * ``TARGA_RAW``
Targa Raw -- Output image in uncompressed Targa format.

  * ``CINEON``
Cineon -- Output image in Cineon format.

  * ``DPX``
DPX -- Output image in DPX format.

  * ``OPEN_EXR_MULTILAYER``
OpenEXR MultiLayer -- Output image in multilayer OpenEXR format.

  * ``OPEN_EXR``
OpenEXR -- Output image in OpenEXR format.

  * ``HDR``
Radiance HDR -- Output image in Radiance HDR format.

  * ``TIFF``
TIFF -- Output image in TIFF format.

  * ``AVI_JPEG``
AVI JPEG -- Output video in AVI JPEG format.

  * ``AVI_RAW``
AVI Raw -- Output video in AVI Raw format.

  * ``FFMPEG``
FFmpeg Video -- The most versatile way to output video files.

  """

  jpeg2k_codec: str = ...

  """

  Codec settings for Jpeg2000

  """

  quality: int = ...

  """

  Quality for image formats that support lossy compression

  """

  stereo_3d_format: Stereo3dFormat = ...

  """

  Settings for stereo 3D

  """

  tiff_codec: str = ...

  """

  Compression mode for TIFF

  """

  use_cineon_log: bool = ...

  """

  Convert to logarithmic color space

  """

  use_jpeg2k_cinema_48: bool = ...

  """

  Use Openjpeg Cinema Preset (48fps)

  """

  use_jpeg2k_cinema_preset: bool = ...

  """

  Use Openjpeg Cinema Preset

  """

  use_jpeg2k_ycc: bool = ...

  """

  Save luminance-chrominance-chrominance channels instead of RGB colors

  """

  use_preview: bool = ...

  """

  When rendering animations, save JPG preview images in same directory

  """

  use_zbuffer: bool = ...

  """

  Save the z-depth per pixel (32-bit unsigned integer z-buffer)

  """

  view_settings: ColorManagedViewSettings = ...

  """

  Color management settings applied on image before saving

  """

  views_format: str = ...

  """

  Format of multiview media

  * ``INDIVIDUAL``
Individual -- Individual files for each view with the prefix as defined by the scene views.

  * ``STEREO_3D``
Stereo 3D -- Single file with an encoded stereo pair.

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ImagePackedFile(bpy_struct):

  filepath: str = ...

  packed_file: PackedFile = ...

  def save(self) -> None:

    """

    Save the packed file to its filepath

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ImagePreview(bpy_struct):

  """

  Preview image and icon

  """

  icon_id: int = ...

  """

  Unique integer identifying this preview as an icon (zero means invalid)

  """

  icon_pixels: int = ...

  """

  Icon pixels, as bytes (always 32-bit RGBA)

  """

  icon_pixels_float: float = ...

  """

  Icon pixels components, as floats (RGBA concatenated values)

  """

  icon_size: typing.Tuple[int, int] = ...

  """

  Width and height in pixels

  """

  image_pixels: int = ...

  """

  Image pixels, as bytes (always 32-bit RGBA)

  """

  image_pixels_float: float = ...

  """

  Image pixels components, as floats (RGBA concatenated values)

  """

  image_size: typing.Tuple[int, int] = ...

  """

  Width and height in pixels

  """

  is_icon_custom: bool = ...

  """

  True if this preview icon has been modified by py script,and is no more auto-generated by Blender

  """

  is_image_custom: bool = ...

  """

  True if this preview image has been modified by py script,and is no more auto-generated by Blender

  """

  def reload(self) -> None:

    """

    Reload the preview from its source path

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ImageUser(bpy_struct):

  """

  Parameters defining how an Image data-block is used by another data-block

  """

  frame_current: int = ...

  """

  Current frame number in image sequence or movie

  """

  frame_duration: int = ...

  """

  Number of images of a movie to use

  """

  frame_offset: int = ...

  """

  Offset the number of the frame to use in the animation

  """

  frame_start: int = ...

  """

  Global starting frame of the movie/sequence, assuming first picture has a #1

  """

  multilayer_layer: int = ...

  """

  Layer in multilayer image

  """

  multilayer_pass: int = ...

  """

  Pass in multilayer image

  """

  multilayer_view: int = ...

  """

  View in multilayer image

  """

  tile: int = ...

  """

  Tile in tiled image

  """

  use_auto_refresh: bool = ...

  """

  Always refresh image on frame changes

  """

  use_cyclic: bool = ...

  """

  Cycle the images in the movie

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class IntAttributeValue(bpy_struct):

  """

  Integer value in geometry attribute

  """

  value: int = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class KeyConfig(bpy_struct):

  """

  Input configuration, including keymaps

  """

  is_user_defined: bool = ...

  """

  Indicates that a keyconfig was defined by the user

  """

  keymaps: typing.Union[KeyMaps, typing.Sequence[KeyMap], typing.Mapping[str, KeyMap], bpy_prop_collection] = ...

  """

  Key maps configured as part of this configuration

  """

  name: str = ...

  """

  Name of the key configuration

  """

  preferences: KeyConfigPreferences = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class KeyConfigPreferences(bpy_struct):

  bl_idname: str = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class KeyConfigurations(bpy_struct):

  """

  Collection of KeyConfigs

  """

  active: KeyConfig = ...

  """

  Active key configuration (preset)

  """

  addon: KeyConfig = ...

  """

  Key configuration that can be extended by add-ons, and is added to the active configuration when handling events

  """

  default: KeyConfig = ...

  """

  Default builtin key configuration

  """

  user: KeyConfig = ...

  """

  Final key configuration that combines keymaps from the active and add-on configurations, and can be edited by the user

  """

  def new(self, name: str) -> KeyConfig:

    """

    new

    """

    ...

  def remove(self, keyconfig: KeyConfig) -> None:

    """

    remove

    """

    ...

  def find_item_from_operator(self, idname: str, context: str = 'INVOKE_DEFAULT', properties: OperatorProperties = None, include: typing.Set[str] = {'ACTIONZONE', 'KEYBOARD', 'MOUSE', 'NDOF', 'TWEAK'}, exclude: typing.Set[str] = {}) -> None:

    """

    find_item_from_operator

    """

    ...

  def update(self) -> None:

    """

    update

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Keyframe(bpy_struct):

  """

  Bezier curve point with two handles defining a Keyframe on an F-Curve

  """

  amplitude: float = ...

  """

  Amount to boost elastic bounces for 'elastic' easing

  """

  back: float = ...

  """

  Amount of overshoot for 'back' easing

  """

  co: typing.Tuple[float, float] = ...

  """

  Coordinates of the control point

  """

  co_ui: typing.Tuple[float, float] = ...

  """

  Coordinates of the control point. Note: Changing this value also updates the handles similar to using the graph editor transform operator

  """

  easing: str = ...

  """

  Which ends of the segment between this and the next keyframe easing interpolation is applied to

  * ``AUTO``
Automatic Easing -- Easing type is chosen automatically based on what the type of interpolation used (e.g. Ease In for transitional types, and Ease Out for dynamic effects).

  * ``EASE_IN``
Ease In -- Only on the end closest to the next keyframe.

  * ``EASE_OUT``
Ease Out -- Only on the end closest to the first keyframe.

  * ``EASE_IN_OUT``
Ease In and Out -- Segment between both keyframes.

  """

  handle_left: typing.Tuple[float, float] = ...

  """

  Coordinates of the left handle (before the control point)

  """

  handle_left_type: str = ...

  """

  Handle types

  * ``FREE``
Free -- Completely independent manually set handle.

  * ``ALIGNED``
Aligned -- Manually set handle with rotation locked together with its pair.

  * ``VECTOR``
Vector -- Automatic handles that create straight lines.

  * ``AUTO``
Automatic -- Automatic handles that create smooth curves.

  * ``AUTO_CLAMPED``
Auto Clamped -- Automatic handles that create smooth curves which only change direction at keyframes.

  """

  handle_right: typing.Tuple[float, float] = ...

  """

  Coordinates of the right handle (after the control point)

  """

  handle_right_type: str = ...

  """

  Handle types

  * ``FREE``
Free -- Completely independent manually set handle.

  * ``ALIGNED``
Aligned -- Manually set handle with rotation locked together with its pair.

  * ``VECTOR``
Vector -- Automatic handles that create straight lines.

  * ``AUTO``
Automatic -- Automatic handles that create smooth curves.

  * ``AUTO_CLAMPED``
Auto Clamped -- Automatic handles that create smooth curves which only change direction at keyframes.

  """

  interpolation: str = ...

  """

  Interpolation method to use for segment of the F-Curve from this Keyframe until the next Keyframe

  * ``CONSTANT``
Constant -- No interpolation, value of A gets held until B is encountered.

  * ``LINEAR``
Linear -- Straight-line interpolation between A and B (i.e. no ease in/out).

  * ``BEZIER``
Bezier -- Smooth interpolation between A and B, with some control over curve shape.

  * ``SINE``
Sinusoidal -- Sinusoidal easing (weakest, almost linear but with a slight curvature).

  * ``QUAD``
Quadratic -- Quadratic easing.

  * ``CUBIC``
Cubic -- Cubic easing.

  * ``QUART``
Quartic -- Quartic easing.

  * ``QUINT``
Quintic -- Quintic easing.

  * ``EXPO``
Exponential -- Exponential easing (dramatic).

  * ``CIRC``
Circular -- Circular easing (strongest and most dynamic).

  * ``BACK``
Back -- Cubic easing with overshoot and settle.

  * ``BOUNCE``
Bounce -- Exponentially decaying parabolic bounce, like when objects collide.

  * ``ELASTIC``
Elastic -- Exponentially decaying sine wave, like an elastic band.

  """

  period: float = ...

  """

  Time between bounces for elastic easing

  """

  select_control_point: bool = ...

  """

  Control point selection status

  """

  select_left_handle: bool = ...

  """

  Left handle selection status

  """

  select_right_handle: bool = ...

  """

  Right handle selection status

  """

  type: str = ...

  """

  Type of keyframe (for visual purposes only)

  * ``KEYFRAME``
Keyframe -- Normal keyframe, e.g. for key poses.

  * ``BREAKDOWN``
Breakdown -- A breakdown pose, e.g. for transitions between key poses.

  * ``MOVING_HOLD``
Moving Hold -- A keyframe that is part of a moving hold.

  * ``EXTREME``
Extreme -- An "extreme" pose, or some other purpose as needed.

  * ``JITTER``
Jitter -- A filler or baked keyframe for keying on ones, or some other purpose as needed.

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class KeyingSet(bpy_struct):

  """

  Settings that should be keyframed together

  """

  bl_description: str = ...

  """

  A short description of the keying set

  """

  bl_idname: str = ...

  """

  If this is set, the Keying Set gets a custom ID, otherwise it takes the name of the class used to define the Keying Set (for example, if the class name is "BUILTIN_KSI_location", and bl_idname is not set by the script, then bl_idname = "BUILTIN_KSI_location")

  """

  bl_label: str = ...

  is_path_absolute: bool = ...

  """

  Keying Set defines specific paths/settings to be keyframed (i.e. is not reliant on context info)

  """

  paths: typing.Union[KeyingSetPaths, typing.Sequence[KeyingSetPath], typing.Mapping[str, KeyingSetPath], bpy_prop_collection] = ...

  """

  Keying Set Paths to define settings that get keyframed together

  """

  type_info: KeyingSetInfo = ...

  """

  Callback function defines for built-in Keying Sets

  """

  use_insertkey_needed: bool = ...

  """

  Only insert keyframes where they're needed in the relevant F-Curves

  """

  use_insertkey_override_needed: bool = ...

  """

  Override default setting to only insert keyframes where they're needed in the relevant F-Curves

  """

  use_insertkey_override_visual: bool = ...

  """

  Override default setting to insert keyframes based on 'visual transforms'

  """

  use_insertkey_override_xyz_to_rgb: bool = ...

  """

  Override default setting to set color for newly added transformation F-Curves (Location, Rotation, Scale) to be based on the transform axis

  """

  use_insertkey_visual: bool = ...

  """

  Insert keyframes based on 'visual transforms'

  """

  use_insertkey_xyz_to_rgb: bool = ...

  """

  Color for newly added transformation F-Curves (Location, Rotation, Scale) is based on the transform axis

  """

  def refresh(self) -> None:

    """

    Refresh Keying Set to ensure that it is valid for the current context (call before each use of one)

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class KeyingSetInfo(bpy_struct):

  """

  Callback function defines for builtin Keying Sets

  """

  bl_description: str = ...

  """

  A short description of the keying set

  """

  bl_idname: str = ...

  """

  If this is set, the Keying Set gets a custom ID, otherwise it takes the name of the class used to define the Keying Set (for example, if the class name is "BUILTIN_KSI_location", and bl_idname is not set by the script, then bl_idname = "BUILTIN_KSI_location")

  """

  bl_label: str = ...

  bl_options: typing.Set[str] = ...

  """

  Keying Set options to use when inserting keyframes

  * ``INSERTKEY_NEEDED``
Only Needed -- Only insert keyframes where they're needed in the relevant F-Curves.

  * ``INSERTKEY_VISUAL``
Visual Keying -- Insert keyframes based on 'visual transforms'.

  * ``INSERTKEY_XYZ_TO_RGB``
XYZ=RGB Colors -- Color for newly added transformation F-Curves (Location, Rotation, Scale) and also Color is based on the transform axis.

  """

  def poll(self, context: Context) -> bool:

    """

    Test if Keying Set can be used or not

    """

    ...

  def iterator(self, context: Context, ks: KeyingSet) -> None:

    """

    Call generate() on the structs which have properties to be keyframed

    """

    ...

  def generate(self, context: Context, ks: KeyingSet, data: typing.Any) -> None:

    """

    Add Paths to the Keying Set to keyframe the properties of the given data

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class KeyingSetPath(bpy_struct):

  """

  Path to a setting for use in a Keying Set

  """

  array_index: int = ...

  """

  Index to the specific setting if applicable

  """

  data_path: str = ...

  """

  Path to property setting

  """

  group: str = ...

  """

  Name of Action Group to assign setting(s) for this path to

  """

  group_method: str = ...

  """

  Method used to define which Group-name to use

  """

  id: ID = ...

  """

  ID-Block that keyframes for Keying Set should be added to (for Absolute Keying Sets only)

  """

  id_type: str = ...

  """

  Type of ID-block that can be used

  """

  use_entire_array: bool = ...

  """

  When an 'array/vector' type is chosen (Location, Rotation, Color, etc.), entire array is to be used

  """

  use_insertkey_needed: bool = ...

  """

  Only insert keyframes where they're needed in the relevant F-Curves

  """

  use_insertkey_override_needed: bool = ...

  """

  Override default setting to only insert keyframes where they're needed in the relevant F-Curves

  """

  use_insertkey_override_visual: bool = ...

  """

  Override default setting to insert keyframes based on 'visual transforms'

  """

  use_insertkey_override_xyz_to_rgb: bool = ...

  """

  Override default setting to set color for newly added transformation F-Curves (Location, Rotation, Scale) to be based on the transform axis

  """

  use_insertkey_visual: bool = ...

  """

  Insert keyframes based on 'visual transforms'

  """

  use_insertkey_xyz_to_rgb: bool = ...

  """

  Color for newly added transformation F-Curves (Location, Rotation, Scale) is based on the transform axis

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class KeyingSetPaths(bpy_struct):

  """

  Collection of keying set paths

  """

  active: KeyingSetPath = ...

  """

  Active Keying Set used to insert/delete keyframes

  """

  active_index: int = ...

  """

  Current Keying Set index

  """

  def add(self, target_id: ID, data_path: str, index: int = -1, group_method: str = 'KEYINGSET', group_name: str = '') -> KeyingSetPath:

    """

    Add a new path for the Keying Set

    """

    ...

  def remove(self, path: KeyingSetPath) -> None:

    """

    Remove the given path from the Keying Set

    """

    ...

  def clear(self) -> None:

    """

    Remove all the paths from the Keying Set

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class KeyingSets(bpy_struct):

  """

  Scene keying sets

  """

  active: KeyingSet = ...

  """

  Active Keying Set used to insert/delete keyframes

  """

  active_index: int = ...

  """

  Current Keying Set index (negative for 'builtin' and positive for 'absolute')

  """

  def new(self, idname: str = 'KeyingSet', name: str = 'KeyingSet') -> KeyingSet:

    """

    Add a new Keying Set to Scene

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class KeyingSetsAll(bpy_struct):

  """

  All available keying sets

  """

  active: KeyingSet = ...

  """

  Active Keying Set used to insert/delete keyframes

  """

  active_index: int = ...

  """

  Current Keying Set index (negative for 'builtin' and positive for 'absolute')

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class KeyMap(bpy_struct):

  """

  Input configuration, including keymaps

  """

  bl_owner_id: str = ...

  """

  Internal owner

  """

  is_modal: bool = ...

  """

  Indicates that a keymap is used for translate modal events for an operator

  """

  is_user_modified: bool = ...

  """

  Keymap is defined by the user

  """

  keymap_items: typing.Union[KeyMapItems, typing.Sequence[KeyMapItem], typing.Mapping[str, KeyMapItem], bpy_prop_collection] = ...

  """

  Items in the keymap, linking an operator to an input event

  """

  name: str = ...

  """

  Name of the key map

  """

  region_type: str = ...

  """

  Optional region type keymap is associated with

  """

  show_expanded_children: bool = ...

  """

  Children expanded in the user interface

  """

  show_expanded_items: bool = ...

  """

  Expanded in the user interface

  """

  space_type: str = ...

  """

  Optional space type keymap is associated with

  * ``EMPTY``
Empty.

  * ``VIEW_3D``
3D Viewport -- Manipulate objects in a 3D environment.

  * ``IMAGE_EDITOR``
UV/Image Editor -- View and edit images and UV Maps.

  * ``NODE_EDITOR``
Node Editor -- Editor for node-based shading and compositing tools.

  * ``SEQUENCE_EDITOR``
Video Sequencer -- Video editing tools.

  * ``CLIP_EDITOR``
Movie Clip Editor -- Motion tracking tools.

  * ``DOPESHEET_EDITOR``
Dope Sheet -- Adjust timing of keyframes.

  * ``GRAPH_EDITOR``
Graph Editor -- Edit drivers and keyframe interpolation.

  * ``NLA_EDITOR``
Nonlinear Animation -- Combine and layer Actions.

  * ``TEXT_EDITOR``
Text Editor -- Edit scripts and in-file documentation.

  * ``CONSOLE``
Python Console -- Interactive programmatic console for advanced editing and script development.

  * ``INFO``
Info -- Log of operations, warnings and error messages.

  * ``TOPBAR``
Top Bar -- Global bar at the top of the screen for global per-window settings.

  * ``STATUSBAR``
Status Bar -- Global bar at the bottom of the screen for general status information.

  * ``OUTLINER``
Outliner -- Overview of scene graph and all available data-blocks.

  * ``PROPERTIES``
Properties -- Edit properties of active object and related data-blocks.

  * ``FILE_BROWSER``
File Browser -- Browse for files and assets.

  * ``SPREADSHEET``
Spreadsheet -- Explore geometry data in a table.

  * ``PREFERENCES``
Preferences -- Edit persistent configuration settings.

  """

  def active(self) -> KeyMap:

    """

    active

    """

    ...

  def restore_to_default(self) -> None:

    """

    restore_to_default

    """

    ...

  def restore_item_to_default(self, item: KeyMapItem) -> None:

    """

    restore_item_to_default

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class KeyMapItem(bpy_struct):

  """

  Item in a Key Map

  """

  active: bool = ...

  """

  Activate or deactivate item

  """

  alt: int = ...

  """

  Alt key pressed, -1 for any state

  """

  alt_ui: bool = ...

  """

  Alt key pressed

  """

  any: bool = ...

  """

  Any modifier keys pressed

  """

  ctrl: int = ...

  """

  Control key pressed, -1 for any state

  """

  ctrl_ui: bool = ...

  """

  Control key pressed

  """

  id: int = ...

  """

  ID of the item

  """

  idname: str = ...

  """

  Identifier of operator to call on input event

  """

  is_user_defined: bool = ...

  """

  Is this keymap item user defined (doesn't just replace a builtin item)

  """

  is_user_modified: bool = ...

  """

  Is this keymap item modified by the user

  """

  key_modifier: str = ...

  """

  Regular key pressed as a modifier

  * ``NONE``
Undocumented.

  * ``LEFTMOUSE``
Left Mouse -- LMB.

  * ``MIDDLEMOUSE``
Middle Mouse -- MMB.

  * ``RIGHTMOUSE``
Right Mouse -- RMB.

  * ``BUTTON4MOUSE``
Button4 Mouse -- MB4.

  * ``BUTTON5MOUSE``
Button5 Mouse -- MB5.

  * ``BUTTON6MOUSE``
Button6 Mouse -- MB6.

  * ``BUTTON7MOUSE``
Button7 Mouse -- MB7.

  * ``PEN``
Pen.

  * ``ERASER``
Eraser.

  * ``MOUSEMOVE``
Mouse Move -- MsMov.

  * ``INBETWEEN_MOUSEMOVE``
In-between Move -- MsSubMov.

  * ``TRACKPADPAN``
Mouse/Trackpad Pan -- MsPan.

  * ``TRACKPADZOOM``
Mouse/Trackpad Zoom -- MsZoom.

  * ``MOUSEROTATE``
Mouse/Trackpad Rotate -- MsRot.

  * ``MOUSESMARTZOOM``
Mouse/Trackpad Smart Zoom -- MsSmartZoom.

  * ``WHEELUPMOUSE``
Wheel Up -- WhUp.

  * ``WHEELDOWNMOUSE``
Wheel Down -- WhDown.

  * ``WHEELINMOUSE``
Wheel In -- WhIn.

  * ``WHEELOUTMOUSE``
Wheel Out -- WhOut.

  * ``EVT_TWEAK_L``
Tweak Left -- TwkL.

  * ``EVT_TWEAK_M``
Tweak Middle -- TwkM.

  * ``EVT_TWEAK_R``
Tweak Right -- TwkR.

  * ``A``
A.

  * ``B``
B.

  * ``C``
C.

  * ``D``
D.

  * ``E``
E.

  * ``F``
F.

  * ``G``
G.

  * ``H``
H.

  * ``I``
I.

  * ``J``
J.

  * ``K``
K.

  * ``L``
L.

  * ``M``
M.

  * ``N``
N.

  * ``O``
O.

  * ``P``
P.

  * ``Q``
Q.

  * ``R``
R.

  * ``S``
S.

  * ``T``
T.

  * ``U``
U.

  * ``V``
V.

  * ``W``
W.

  * ``X``
X.

  * ``Y``
Y.

  * ``Z``
Z.

  * ``ZERO``
0.

  * ``ONE``
1.

  * ``TWO``
2.

  * ``THREE``
3.

  * ``FOUR``
4.

  * ``FIVE``
5.

  * ``SIX``
6.

  * ``SEVEN``
7.

  * ``EIGHT``
8.

  * ``NINE``
9.

  * ``LEFT_CTRL``
Left Ctrl -- CtrlL.

  * ``LEFT_ALT``
Left Alt -- AltL.

  * ``LEFT_SHIFT``
Left Shift -- ShiftL.

  * ``RIGHT_ALT``
Right Alt -- AltR.

  * ``RIGHT_CTRL``
Right Ctrl -- CtrlR.

  * ``RIGHT_SHIFT``
Right Shift -- ShiftR.

  * ``OSKEY``
OS Key -- Cmd.

  * ``APP``
Application -- App.

  * ``GRLESS``
Grless.

  * ``ESC``
Esc.

  * ``TAB``
Tab.

  * ``RET``
Return -- Enter.

  * ``SPACE``
Spacebar -- Space.

  * ``LINE_FEED``
Line Feed.

  * ``BACK_SPACE``
Backspace -- BkSpace.

  * ``DEL``
Delete -- Del.

  * ``SEMI_COLON``
;.

  * ``PERIOD``
..

  * ``COMMA``
,.

  * ``QUOTE``
".

  * ``ACCENT_GRAVE``
`.

  * ``MINUS``
-.

  * ``PLUS``
+.

  * ``SLASH``
/.

  * ``BACK_SLASH``
\.

  * ``EQUAL``
=.

  * ``LEFT_BRACKET``
[.

  * ``RIGHT_BRACKET``
].

  * ``LEFT_ARROW``
Left Arrow -- ←.

  * ``DOWN_ARROW``
Down Arrow -- ↓.

  * ``RIGHT_ARROW``
Right Arrow -- →.

  * ``UP_ARROW``
Up Arrow -- ↑.

  * ``NUMPAD_2``
Numpad 2 -- Pad2.

  * ``NUMPAD_4``
Numpad 4 -- Pad4.

  * ``NUMPAD_6``
Numpad 6 -- Pad6.

  * ``NUMPAD_8``
Numpad 8 -- Pad8.

  * ``NUMPAD_1``
Numpad 1 -- Pad1.

  * ``NUMPAD_3``
Numpad 3 -- Pad3.

  * ``NUMPAD_5``
Numpad 5 -- Pad5.

  * ``NUMPAD_7``
Numpad 7 -- Pad7.

  * ``NUMPAD_9``
Numpad 9 -- Pad9.

  * ``NUMPAD_PERIOD``
Numpad . -- Pad..

  * ``NUMPAD_SLASH``
Numpad / -- Pad/.

  * ``NUMPAD_ASTERIX``
Numpad * -- Pad*.

  * ``NUMPAD_0``
Numpad 0 -- Pad0.

  * ``NUMPAD_MINUS``
Numpad - -- Pad-.

  * ``NUMPAD_ENTER``
Numpad Enter -- PadEnter.

  * ``NUMPAD_PLUS``
Numpad + -- Pad+.

  * ``F1``
F1.

  * ``F2``
F2.

  * ``F3``
F3.

  * ``F4``
F4.

  * ``F5``
F5.

  * ``F6``
F6.

  * ``F7``
F7.

  * ``F8``
F8.

  * ``F9``
F9.

  * ``F10``
F10.

  * ``F11``
F11.

  * ``F12``
F12.

  * ``F13``
F13.

  * ``F14``
F14.

  * ``F15``
F15.

  * ``F16``
F16.

  * ``F17``
F17.

  * ``F18``
F18.

  * ``F19``
F19.

  * ``F20``
F20.

  * ``F21``
F21.

  * ``F22``
F22.

  * ``F23``
F23.

  * ``F24``
F24.

  * ``PAUSE``
Pause.

  * ``INSERT``
Insert -- Ins.

  * ``HOME``
Home.

  * ``PAGE_UP``
Page Up -- PgUp.

  * ``PAGE_DOWN``
Page Down -- PgDown.

  * ``END``
End.

  * ``MEDIA_PLAY``
Media Play/Pause -- >/||.

  * ``MEDIA_STOP``
Media Stop -- Stop.

  * ``MEDIA_FIRST``
Media First -- |<<.

  * ``MEDIA_LAST``
Media Last -- >>|.

  * ``TEXTINPUT``
Text Input -- TxtIn.

  * ``WINDOW_DEACTIVATE``
Window Deactivate.

  * ``TIMER``
Timer -- Tmr.

  * ``TIMER0``
Timer 0 -- Tmr0.

  * ``TIMER1``
Timer 1 -- Tmr1.

  * ``TIMER2``
Timer 2 -- Tmr2.

  * ``TIMER_JOBS``
Timer Jobs -- TmrJob.

  * ``TIMER_AUTOSAVE``
Timer Autosave -- TmrSave.

  * ``TIMER_REPORT``
Timer Report -- TmrReport.

  * ``TIMERREGION``
Timer Region -- TmrReg.

  * ``NDOF_MOTION``
NDOF Motion -- NdofMov.

  * ``NDOF_BUTTON_MENU``
NDOF Menu -- NdofMenu.

  * ``NDOF_BUTTON_FIT``
NDOF Fit -- NdofFit.

  * ``NDOF_BUTTON_TOP``
NDOF Top -- Ndof↑.

  * ``NDOF_BUTTON_BOTTOM``
NDOF Bottom -- Ndof↓.

  * ``NDOF_BUTTON_LEFT``
NDOF Left -- Ndof←.

  * ``NDOF_BUTTON_RIGHT``
NDOF Right -- Ndof→.

  * ``NDOF_BUTTON_FRONT``
NDOF Front -- NdofFront.

  * ``NDOF_BUTTON_BACK``
NDOF Back -- NdofBack.

  * ``NDOF_BUTTON_ISO1``
NDOF Isometric 1 -- NdofIso1.

  * ``NDOF_BUTTON_ISO2``
NDOF Isometric 2 -- NdofIso2.

  * ``NDOF_BUTTON_ROLL_CW``
NDOF Roll CW -- NdofRCW.

  * ``NDOF_BUTTON_ROLL_CCW``
NDOF Roll CCW -- NdofRCCW.

  * ``NDOF_BUTTON_SPIN_CW``
NDOF Spin CW -- NdofSCW.

  * ``NDOF_BUTTON_SPIN_CCW``
NDOF Spin CCW -- NdofSCCW.

  * ``NDOF_BUTTON_TILT_CW``
NDOF Tilt CW -- NdofTCW.

  * ``NDOF_BUTTON_TILT_CCW``
NDOF Tilt CCW -- NdofTCCW.

  * ``NDOF_BUTTON_ROTATE``
NDOF Rotate -- NdofRot.

  * ``NDOF_BUTTON_PANZOOM``
NDOF Pan/Zoom -- NdofPanZoom.

  * ``NDOF_BUTTON_DOMINANT``
NDOF Dominant -- NdofDom.

  * ``NDOF_BUTTON_PLUS``
NDOF Plus -- Ndof+.

  * ``NDOF_BUTTON_MINUS``
NDOF Minus -- Ndof-.

  * ``NDOF_BUTTON_ESC``
NDOF Esc -- NdofEsc.

  * ``NDOF_BUTTON_ALT``
NDOF Alt -- NdofAlt.

  * ``NDOF_BUTTON_SHIFT``
NDOF Shift -- NdofShift.

  * ``NDOF_BUTTON_CTRL``
NDOF Ctrl -- NdofCtrl.

  * ``NDOF_BUTTON_1``
NDOF Button 1 -- NdofB1.

  * ``NDOF_BUTTON_2``
NDOF Button 2 -- NdofB2.

  * ``NDOF_BUTTON_3``
NDOF Button 3 -- NdofB3.

  * ``NDOF_BUTTON_4``
NDOF Button 4 -- NdofB4.

  * ``NDOF_BUTTON_5``
NDOF Button 5 -- NdofB5.

  * ``NDOF_BUTTON_6``
NDOF Button 6 -- NdofB6.

  * ``NDOF_BUTTON_7``
NDOF Button 7 -- NdofB7.

  * ``NDOF_BUTTON_8``
NDOF Button 8 -- NdofB8.

  * ``NDOF_BUTTON_9``
NDOF Button 9 -- NdofB9.

  * ``NDOF_BUTTON_10``
NDOF Button 10 -- NdofB10.

  * ``NDOF_BUTTON_A``
NDOF Button A -- NdofBA.

  * ``NDOF_BUTTON_B``
NDOF Button B -- NdofBB.

  * ``NDOF_BUTTON_C``
NDOF Button C -- NdofBC.

  * ``ACTIONZONE_AREA``
ActionZone Area -- AZone Area.

  * ``ACTIONZONE_REGION``
ActionZone Region -- AZone Region.

  * ``ACTIONZONE_FULLSCREEN``
ActionZone Fullscreen -- AZone FullScr.

  * ``XR_ACTION``
XR Action.

  """

  map_type: str = ...

  """

  Type of event mapping

  """

  name: str = ...

  """

  Name of operator (translated) to call on input event

  """

  oskey: int = ...

  """

  Operating system key pressed, -1 for any state

  """

  oskey_ui: bool = ...

  """

  Operating system key pressed

  """

  properties: OperatorProperties = ...

  """

  Properties to set when the operator is called

  """

  propvalue: str = ...

  """

  The value this event translates to in a modal keymap

  """

  repeat: bool = ...

  """

  Active on key-repeat events (when a key is held)

  """

  shift: int = ...

  """

  Shift key pressed, -1 for any state

  """

  shift_ui: bool = ...

  """

  Shift key pressed

  """

  show_expanded: bool = ...

  """

  Show key map event and property details in the user interface

  """

  type: str = ...

  """

  Type of event

  * ``NONE``
Undocumented.

  * ``LEFTMOUSE``
Left Mouse -- LMB.

  * ``MIDDLEMOUSE``
Middle Mouse -- MMB.

  * ``RIGHTMOUSE``
Right Mouse -- RMB.

  * ``BUTTON4MOUSE``
Button4 Mouse -- MB4.

  * ``BUTTON5MOUSE``
Button5 Mouse -- MB5.

  * ``BUTTON6MOUSE``
Button6 Mouse -- MB6.

  * ``BUTTON7MOUSE``
Button7 Mouse -- MB7.

  * ``PEN``
Pen.

  * ``ERASER``
Eraser.

  * ``MOUSEMOVE``
Mouse Move -- MsMov.

  * ``INBETWEEN_MOUSEMOVE``
In-between Move -- MsSubMov.

  * ``TRACKPADPAN``
Mouse/Trackpad Pan -- MsPan.

  * ``TRACKPADZOOM``
Mouse/Trackpad Zoom -- MsZoom.

  * ``MOUSEROTATE``
Mouse/Trackpad Rotate -- MsRot.

  * ``MOUSESMARTZOOM``
Mouse/Trackpad Smart Zoom -- MsSmartZoom.

  * ``WHEELUPMOUSE``
Wheel Up -- WhUp.

  * ``WHEELDOWNMOUSE``
Wheel Down -- WhDown.

  * ``WHEELINMOUSE``
Wheel In -- WhIn.

  * ``WHEELOUTMOUSE``
Wheel Out -- WhOut.

  * ``EVT_TWEAK_L``
Tweak Left -- TwkL.

  * ``EVT_TWEAK_M``
Tweak Middle -- TwkM.

  * ``EVT_TWEAK_R``
Tweak Right -- TwkR.

  * ``A``
A.

  * ``B``
B.

  * ``C``
C.

  * ``D``
D.

  * ``E``
E.

  * ``F``
F.

  * ``G``
G.

  * ``H``
H.

  * ``I``
I.

  * ``J``
J.

  * ``K``
K.

  * ``L``
L.

  * ``M``
M.

  * ``N``
N.

  * ``O``
O.

  * ``P``
P.

  * ``Q``
Q.

  * ``R``
R.

  * ``S``
S.

  * ``T``
T.

  * ``U``
U.

  * ``V``
V.

  * ``W``
W.

  * ``X``
X.

  * ``Y``
Y.

  * ``Z``
Z.

  * ``ZERO``
0.

  * ``ONE``
1.

  * ``TWO``
2.

  * ``THREE``
3.

  * ``FOUR``
4.

  * ``FIVE``
5.

  * ``SIX``
6.

  * ``SEVEN``
7.

  * ``EIGHT``
8.

  * ``NINE``
9.

  * ``LEFT_CTRL``
Left Ctrl -- CtrlL.

  * ``LEFT_ALT``
Left Alt -- AltL.

  * ``LEFT_SHIFT``
Left Shift -- ShiftL.

  * ``RIGHT_ALT``
Right Alt -- AltR.

  * ``RIGHT_CTRL``
Right Ctrl -- CtrlR.

  * ``RIGHT_SHIFT``
Right Shift -- ShiftR.

  * ``OSKEY``
OS Key -- Cmd.

  * ``APP``
Application -- App.

  * ``GRLESS``
Grless.

  * ``ESC``
Esc.

  * ``TAB``
Tab.

  * ``RET``
Return -- Enter.

  * ``SPACE``
Spacebar -- Space.

  * ``LINE_FEED``
Line Feed.

  * ``BACK_SPACE``
Backspace -- BkSpace.

  * ``DEL``
Delete -- Del.

  * ``SEMI_COLON``
;.

  * ``PERIOD``
..

  * ``COMMA``
,.

  * ``QUOTE``
".

  * ``ACCENT_GRAVE``
`.

  * ``MINUS``
-.

  * ``PLUS``
+.

  * ``SLASH``
/.

  * ``BACK_SLASH``
\.

  * ``EQUAL``
=.

  * ``LEFT_BRACKET``
[.

  * ``RIGHT_BRACKET``
].

  * ``LEFT_ARROW``
Left Arrow -- ←.

  * ``DOWN_ARROW``
Down Arrow -- ↓.

  * ``RIGHT_ARROW``
Right Arrow -- →.

  * ``UP_ARROW``
Up Arrow -- ↑.

  * ``NUMPAD_2``
Numpad 2 -- Pad2.

  * ``NUMPAD_4``
Numpad 4 -- Pad4.

  * ``NUMPAD_6``
Numpad 6 -- Pad6.

  * ``NUMPAD_8``
Numpad 8 -- Pad8.

  * ``NUMPAD_1``
Numpad 1 -- Pad1.

  * ``NUMPAD_3``
Numpad 3 -- Pad3.

  * ``NUMPAD_5``
Numpad 5 -- Pad5.

  * ``NUMPAD_7``
Numpad 7 -- Pad7.

  * ``NUMPAD_9``
Numpad 9 -- Pad9.

  * ``NUMPAD_PERIOD``
Numpad . -- Pad..

  * ``NUMPAD_SLASH``
Numpad / -- Pad/.

  * ``NUMPAD_ASTERIX``
Numpad * -- Pad*.

  * ``NUMPAD_0``
Numpad 0 -- Pad0.

  * ``NUMPAD_MINUS``
Numpad - -- Pad-.

  * ``NUMPAD_ENTER``
Numpad Enter -- PadEnter.

  * ``NUMPAD_PLUS``
Numpad + -- Pad+.

  * ``F1``
F1.

  * ``F2``
F2.

  * ``F3``
F3.

  * ``F4``
F4.

  * ``F5``
F5.

  * ``F6``
F6.

  * ``F7``
F7.

  * ``F8``
F8.

  * ``F9``
F9.

  * ``F10``
F10.

  * ``F11``
F11.

  * ``F12``
F12.

  * ``F13``
F13.

  * ``F14``
F14.

  * ``F15``
F15.

  * ``F16``
F16.

  * ``F17``
F17.

  * ``F18``
F18.

  * ``F19``
F19.

  * ``F20``
F20.

  * ``F21``
F21.

  * ``F22``
F22.

  * ``F23``
F23.

  * ``F24``
F24.

  * ``PAUSE``
Pause.

  * ``INSERT``
Insert -- Ins.

  * ``HOME``
Home.

  * ``PAGE_UP``
Page Up -- PgUp.

  * ``PAGE_DOWN``
Page Down -- PgDown.

  * ``END``
End.

  * ``MEDIA_PLAY``
Media Play/Pause -- >/||.

  * ``MEDIA_STOP``
Media Stop -- Stop.

  * ``MEDIA_FIRST``
Media First -- |<<.

  * ``MEDIA_LAST``
Media Last -- >>|.

  * ``TEXTINPUT``
Text Input -- TxtIn.

  * ``WINDOW_DEACTIVATE``
Window Deactivate.

  * ``TIMER``
Timer -- Tmr.

  * ``TIMER0``
Timer 0 -- Tmr0.

  * ``TIMER1``
Timer 1 -- Tmr1.

  * ``TIMER2``
Timer 2 -- Tmr2.

  * ``TIMER_JOBS``
Timer Jobs -- TmrJob.

  * ``TIMER_AUTOSAVE``
Timer Autosave -- TmrSave.

  * ``TIMER_REPORT``
Timer Report -- TmrReport.

  * ``TIMERREGION``
Timer Region -- TmrReg.

  * ``NDOF_MOTION``
NDOF Motion -- NdofMov.

  * ``NDOF_BUTTON_MENU``
NDOF Menu -- NdofMenu.

  * ``NDOF_BUTTON_FIT``
NDOF Fit -- NdofFit.

  * ``NDOF_BUTTON_TOP``
NDOF Top -- Ndof↑.

  * ``NDOF_BUTTON_BOTTOM``
NDOF Bottom -- Ndof↓.

  * ``NDOF_BUTTON_LEFT``
NDOF Left -- Ndof←.

  * ``NDOF_BUTTON_RIGHT``
NDOF Right -- Ndof→.

  * ``NDOF_BUTTON_FRONT``
NDOF Front -- NdofFront.

  * ``NDOF_BUTTON_BACK``
NDOF Back -- NdofBack.

  * ``NDOF_BUTTON_ISO1``
NDOF Isometric 1 -- NdofIso1.

  * ``NDOF_BUTTON_ISO2``
NDOF Isometric 2 -- NdofIso2.

  * ``NDOF_BUTTON_ROLL_CW``
NDOF Roll CW -- NdofRCW.

  * ``NDOF_BUTTON_ROLL_CCW``
NDOF Roll CCW -- NdofRCCW.

  * ``NDOF_BUTTON_SPIN_CW``
NDOF Spin CW -- NdofSCW.

  * ``NDOF_BUTTON_SPIN_CCW``
NDOF Spin CCW -- NdofSCCW.

  * ``NDOF_BUTTON_TILT_CW``
NDOF Tilt CW -- NdofTCW.

  * ``NDOF_BUTTON_TILT_CCW``
NDOF Tilt CCW -- NdofTCCW.

  * ``NDOF_BUTTON_ROTATE``
NDOF Rotate -- NdofRot.

  * ``NDOF_BUTTON_PANZOOM``
NDOF Pan/Zoom -- NdofPanZoom.

  * ``NDOF_BUTTON_DOMINANT``
NDOF Dominant -- NdofDom.

  * ``NDOF_BUTTON_PLUS``
NDOF Plus -- Ndof+.

  * ``NDOF_BUTTON_MINUS``
NDOF Minus -- Ndof-.

  * ``NDOF_BUTTON_ESC``
NDOF Esc -- NdofEsc.

  * ``NDOF_BUTTON_ALT``
NDOF Alt -- NdofAlt.

  * ``NDOF_BUTTON_SHIFT``
NDOF Shift -- NdofShift.

  * ``NDOF_BUTTON_CTRL``
NDOF Ctrl -- NdofCtrl.

  * ``NDOF_BUTTON_1``
NDOF Button 1 -- NdofB1.

  * ``NDOF_BUTTON_2``
NDOF Button 2 -- NdofB2.

  * ``NDOF_BUTTON_3``
NDOF Button 3 -- NdofB3.

  * ``NDOF_BUTTON_4``
NDOF Button 4 -- NdofB4.

  * ``NDOF_BUTTON_5``
NDOF Button 5 -- NdofB5.

  * ``NDOF_BUTTON_6``
NDOF Button 6 -- NdofB6.

  * ``NDOF_BUTTON_7``
NDOF Button 7 -- NdofB7.

  * ``NDOF_BUTTON_8``
NDOF Button 8 -- NdofB8.

  * ``NDOF_BUTTON_9``
NDOF Button 9 -- NdofB9.

  * ``NDOF_BUTTON_10``
NDOF Button 10 -- NdofB10.

  * ``NDOF_BUTTON_A``
NDOF Button A -- NdofBA.

  * ``NDOF_BUTTON_B``
NDOF Button B -- NdofBB.

  * ``NDOF_BUTTON_C``
NDOF Button C -- NdofBC.

  * ``ACTIONZONE_AREA``
ActionZone Area -- AZone Area.

  * ``ACTIONZONE_REGION``
ActionZone Region -- AZone Region.

  * ``ACTIONZONE_FULLSCREEN``
ActionZone Fullscreen -- AZone FullScr.

  * ``XR_ACTION``
XR Action.

  """

  value: str = ...

  def compare(self, item: KeyMapItem) -> bool:

    """

    compare

    """

    ...

  def to_string(self, compact: bool = False) -> str:

    """

    to_string

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class KeyMapItems(bpy_struct):

  """

  Collection of keymap items

  """

  def new(self, idname: str, type: str, value: str, any: bool = False, shift: int = 0, ctrl: int = 0, alt: int = 0, oskey: int = 0, key_modifier: str = 'NONE', repeat: bool = False, head: bool = False) -> KeyMapItem:

    """

    new

    """

    ...

  def new_modal(self, propvalue: str, type: str, value: str, any: bool = False, shift: int = 0, ctrl: int = 0, alt: int = 0, oskey: int = 0, key_modifier: str = 'NONE', repeat: bool = False) -> KeyMapItem:

    """

    new_modal

    """

    ...

  def new_from_item(self, item: KeyMapItem, head: bool = False) -> KeyMapItem:

    """

    new_from_item

    """

    ...

  def remove(self, item: KeyMapItem) -> None:

    """

    remove

    """

    ...

  def from_id(self, id: int) -> KeyMapItem:

    """

    from_id

    """

    ...

  def find_from_operator(self, idname: str, properties: OperatorProperties = None, include: typing.Set[str] = {'ACTIONZONE', 'KEYBOARD', 'MOUSE', 'NDOF', 'TWEAK'}, exclude: typing.Set[str] = {}) -> KeyMapItem:

    """

    find_from_operator

    """

    ...

  def match_event(self, event: Event) -> KeyMapItem:

    """

    match_event

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class KeyMaps(bpy_struct):

  """

  Collection of keymaps

  """

  def new(self, name: str, space_type: str = 'EMPTY', region_type: str = 'WINDOW', modal: bool = False, tool: bool = False) -> KeyMap:

    """

    Ensure the keymap exists. This will return the one with the given name/space type/region type, or create a new one if it does not exist yet.

    """

    ...

  def remove(self, keymap: KeyMap) -> None:

    """

    remove

    """

    ...

  def find(self, name: str, space_type: str = 'EMPTY', region_type: str = 'WINDOW') -> KeyMap:

    """

    find

    """

    ...

  def find_modal(self, name: str) -> KeyMap:

    """

    find_modal

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class LatticePoint(bpy_struct):

  """

  Point in the lattice grid

  """

  co: typing.Tuple[float, float, float] = ...

  """

  Original undeformed location used to calculate the strength of the deform effect (edit/animate the Deformed Location instead)

  """

  co_deform: typing.Tuple[float, float, float] = ...

  groups: typing.Union[typing.Sequence[VertexGroupElement], typing.Mapping[str, VertexGroupElement], bpy_prop_collection] = ...

  """

  Weights for the vertex groups this point is member of

  """

  select: bool = ...

  """

  Selection status

  """

  weight_softbody: float = ...

  """

  Softbody goal weight

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class LayerCollection(bpy_struct):

  """

  Layer collection

  """

  children: typing.Union[typing.Sequence[LayerCollection], typing.Mapping[str, LayerCollection], bpy_prop_collection] = ...

  """

  Child layer collections

  """

  collection: Collection = ...

  """

  Collection this layer collection is wrapping

  """

  exclude: bool = ...

  """

  Exclude from view layer

  """

  hide_viewport: bool = ...

  """

  Temporarily hide in viewport

  """

  holdout: bool = ...

  """

  Mask out objects in collection from view layer

  """

  indirect_only: bool = ...

  """

  Objects in collection only contribute indirectly (through shadows and reflections) in the view layer

  """

  is_visible: bool = ...

  """

  Whether this collection is visible for the view layer, take into account the collection parent

  """

  name: str = ...

  """

  Name of this view layer (same as its collection one)

  """

  def visible_get(self) -> bool:

    """

    Whether this collection is visible, take into account the collection parent and the viewport

    """

    ...

  def has_objects(self) -> bool:

    ...

  def has_selected_objects(self, view_layer: ViewLayer) -> bool:

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class LayerObjects(bpy_struct):

  """

  Collections of objects

  """

  active: Object = ...

  """

  Active object for this layer

  """

  selected: typing.Union[typing.Sequence[Object], typing.Mapping[str, Object], bpy_prop_collection] = ...

  """

  All the selected objects of this layer

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class LibraryWeakReference(bpy_struct):

  """

  Read-only external reference to a linked data-block and its library file

  """

  filepath: str = ...

  """

  Path to the library .blend file

  """

  id_name: str = ...

  """

  Full ID name in the library .blend file (including the two leading 'id type' chars)

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Linesets(bpy_struct):

  """

  Line sets for associating lines and style parameters

  """

  active: FreestyleLineSet = ...

  """

  Active line set being displayed

  """

  active_index: int = ...

  """

  Index of active line set slot

  """

  def new(self, name: str) -> FreestyleLineSet:

    """

    Add a line set to scene render layer Freestyle settings

    """

    ...

  def remove(self, lineset: FreestyleLineSet) -> None:

    """

    Remove a line set from scene render layer Freestyle settings

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class LineStyleAlphaModifiers(bpy_struct):

  """

  Alpha modifiers for changing line alphas

  """

  def new(self, name: str, type: str) -> LineStyleAlphaModifier:

    """

    Add a alpha modifier to line style

    """

    ...

  def remove(self, modifier: LineStyleAlphaModifier) -> None:

    """

    Remove a alpha modifier from line style

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class LineStyleColorModifiers(bpy_struct):

  """

  Color modifiers for changing line colors

  """

  def new(self, name: str, type: str) -> LineStyleColorModifier:

    """

    Add a color modifier to line style

    """

    ...

  def remove(self, modifier: LineStyleColorModifier) -> None:

    """

    Remove a color modifier from line style

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class LineStyleGeometryModifiers(bpy_struct):

  """

  Geometry modifiers for changing line geometries

  """

  def new(self, name: str, type: str) -> LineStyleGeometryModifier:

    """

    Add a geometry modifier to line style

    """

    ...

  def remove(self, modifier: LineStyleGeometryModifier) -> None:

    """

    Remove a geometry modifier from line style

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class LineStyleModifier(bpy_struct):

  """

  Base type to define modifiers

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class LineStyleTextureSlots(bpy_struct):

  """

  Collection of texture slots

  """

  @classmethod

  def add(cls) -> LineStyleTextureSlot:

    """

    add

    """

    ...

  @classmethod

  def create(cls, index: int) -> LineStyleTextureSlot:

    """

    create

    """

    ...

  @classmethod

  def clear(cls, index: int) -> None:

    """

    clear

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class LineStyleThicknessModifiers(bpy_struct):

  """

  Thickness modifiers for changing line thickness

  """

  def new(self, name: str, type: str) -> LineStyleThicknessModifier:

    """

    Add a thickness modifier to line style

    """

    ...

  def remove(self, modifier: LineStyleThicknessModifier) -> None:

    """

    Remove a thickness modifier from line style

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class LoopColors(bpy_struct):

  """

  Collection of vertex colors

  """

  active: MeshLoopColorLayer = ...

  """

  Active vertex color layer

  """

  active_index: int = ...

  """

  Active vertex color index

  """

  def new(self, name: str = 'Col', do_init: bool = True) -> MeshLoopColorLayer:

    """

    Add a vertex color layer to Mesh

    """

    ...

  def remove(self, layer: MeshLoopColorLayer) -> None:

    """

    Remove a vertex color layer

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Macro(bpy_struct):

  """

  Storage of a macro operator being executed, or registered after execution

  """

  bl_cursor_pending: str = ...

  """

  Cursor to use when waiting for the user to select a location to activate the operator (when ``bl_options`` has ``DEPENDS_ON_CURSOR`` set)

  """

  bl_description: str = ...

  bl_idname: str = ...

  bl_label: str = ...

  bl_options: typing.Set[str] = ...

  """

  Options for this operator type

  * ``REGISTER``
Register -- Display in the info window and support the redo toolbar panel.

  * ``UNDO``
Undo -- Push an undo event (needed for operator redo).

  * ``UNDO_GROUPED``
Grouped Undo -- Push a single undo event for repeated instances of this operator.

  * ``BLOCKING``
Blocking -- Block anything else from using the cursor.

  * ``MACRO``
Macro -- Use to check if an operator is a macro.

  * ``GRAB_CURSOR``
Grab Pointer -- Use so the operator grabs the mouse focus, enables wrapping when continuous grab is enabled.

  * ``GRAB_CURSOR_X``
Grab Pointer X -- Grab, only warping the X axis.

  * ``GRAB_CURSOR_Y``
Grab Pointer Y -- Grab, only warping the Y axis.

  * ``DEPENDS_ON_CURSOR``
Depends on Cursor -- The initial cursor location is used, when running from a menus or buttons the user is prompted to place the cursor before beginning the operation.

  * ``PRESET``
Preset -- Display a preset button with the operators settings.

  * ``INTERNAL``
Internal -- Removes the operator from search results.

  """

  bl_translation_context: str = ...

  bl_undo_group: str = ...

  has_reports: bool = ...

  """

  Operator has a set of reports (warnings and errors) from last execution

  """

  name: str = ...

  properties: OperatorProperties = ...

  def report(self, type: typing.Set[str], message: str) -> None:

    """

    report

    """

    ...

  @classmethod

  def poll(cls, context: Context) -> bool:

    """

    Test if the operator can be called or not

    """

    ...

  def draw(self, context: Context) -> None:

    """

    Draw function for the operator

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MaskLayer(bpy_struct):

  """

  Single layer used for masking pixels

  """

  alpha: float = ...

  """

  Render Opacity

  """

  blend: str = ...

  """

  Method of blending mask layers

  """

  falloff: str = ...

  """

  Falloff type the feather

  * ``SMOOTH``
Smooth -- Smooth falloff.

  * ``SPHERE``
Sphere -- Spherical falloff.

  * ``ROOT``
Root -- Root falloff.

  * ``INVERSE_SQUARE``
Inverse Square -- Inverse Square falloff.

  * ``SHARP``
Sharp -- Sharp falloff.

  * ``LINEAR``
Linear -- Linear falloff.

  """

  hide: bool = ...

  """

  Restrict visibility in the viewport

  """

  hide_render: bool = ...

  """

  Restrict renderability

  """

  hide_select: bool = ...

  """

  Restrict selection in the viewport

  """

  invert: bool = ...

  """

  Invert the mask black/white

  """

  name: str = ...

  """

  Unique name of layer

  """

  select: bool = ...

  """

  Layer is selected for editing in the Dope Sheet

  """

  splines: typing.Union[MaskSplines, typing.Sequence[MaskSpline], typing.Mapping[str, MaskSpline], bpy_prop_collection] = ...

  """

  Collection of splines which defines this layer

  """

  use_fill_holes: bool = ...

  """

  Calculate holes when filling overlapping curves

  """

  use_fill_overlap: bool = ...

  """

  Calculate self intersections and overlap before filling

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MaskLayers(bpy_struct):

  """

  Collection of layers used by mask

  """

  active: MaskLayer = ...

  """

  Active layer in this mask

  """

  def new(self, name: str = '') -> MaskLayer:

    """

    Add layer to this mask

    """

    ...

  def remove(self, layer: MaskLayer) -> None:

    """

    Remove layer from this mask

    """

    ...

  def clear(self) -> None:

    """

    Remove all mask layers

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MaskParent(bpy_struct):

  """

  Parenting settings for masking element

  """

  id: ID = ...

  """

  ID-block to which masking element would be parented to or to its property

  """

  id_type: str = ...

  """

  Type of ID-block that can be used

  """

  parent: str = ...

  """

  Name of parent object in specified data-block to which parenting happens

  """

  sub_parent: str = ...

  """

  Name of parent sub-object in specified data-block to which parenting happens

  """

  type: str = ...

  """

  Parent Type

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MaskSpline(bpy_struct):

  """

  Single spline used for defining mask shape

  """

  offset_mode: str = ...

  """

  The method used for calculating the feather offset

  * ``EVEN``
Even -- Calculate even feather offset.

  * ``SMOOTH``
Smooth -- Calculate feather offset as a second curve.

  """

  points: typing.Union[MaskSplinePoints, typing.Sequence[MaskSplinePoint], typing.Mapping[str, MaskSplinePoint], bpy_prop_collection] = ...

  """

  Collection of points

  """

  use_cyclic: bool = ...

  """

  Make this spline a closed loop

  """

  use_fill: bool = ...

  """

  Make this spline filled

  """

  use_self_intersection_check: bool = ...

  """

  Prevent feather from self-intersections

  """

  weight_interpolation: str = ...

  """

  The type of weight interpolation for spline

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MaskSplinePoint(bpy_struct):

  """

  Single point in spline used for defining mask

  """

  co: typing.Tuple[float, float] = ...

  """

  Coordinates of the control point

  """

  feather_points: typing.Union[typing.Sequence[MaskSplinePointUW], typing.Mapping[str, MaskSplinePointUW], bpy_prop_collection] = ...

  """

  Points defining feather

  """

  handle_left: typing.Tuple[float, float] = ...

  """

  Coordinates of the first handle

  """

  handle_left_type: str = ...

  """

  Handle type

  """

  handle_right: typing.Tuple[float, float] = ...

  """

  Coordinates of the second handle

  """

  handle_right_type: str = ...

  """

  Handle type

  """

  handle_type: str = ...

  """

  Handle type

  """

  parent: MaskParent = ...

  select: bool = ...

  """

  Selection status

  """

  weight: float = ...

  """

  Weight of the point

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MaskSplinePoints(bpy_struct):

  """

  Collection of masking spline points

  """

  def add(self, count: int) -> None:

    """

    Add a number of point to this spline

    """

    ...

  def remove(self, point: MaskSplinePoint) -> None:

    """

    Remove a point from a spline

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MaskSplinePointUW(bpy_struct):

  """

  Single point in spline segment defining feather

  """

  select: bool = ...

  """

  Selection status

  """

  u: float = ...

  """

  U coordinate of point along spline segment

  """

  weight: float = ...

  """

  Weight of feather point

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MaskSplines(bpy_struct):

  """

  Collection of masking splines

  """

  active: MaskSpline = ...

  """

  Active spline of masking layer

  """

  active_point: MaskSplinePoint = ...

  """

  Active spline of masking layer

  """

  def new(self) -> MaskSpline:

    """

    Add a new spline to the layer

    """

    ...

  def remove(self, spline: MaskSpline) -> None:

    """

    Remove a spline from a layer

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MaterialGPencilStyle(bpy_struct):

  alignment_mode: str = ...

  """

  Defines how align Dots and Boxes with drawing path and object rotation

  * ``PATH``
Path -- Follow stroke drawing path and object rotation.

  * ``OBJECT``
Object -- Follow object rotation only.

  * ``FIXED``
Fixed -- Do not follow drawing path or object rotation and keeps aligned with viewport.

  """

  alignment_rotation: float = ...

  """

  Additional rotation applied to dots and square texture of strokes. Only applies in texture shading mode

  """

  color: typing.Tuple[float, float, float, float] = ...

  fill_color: typing.Tuple[float, float, float, float] = ...

  """

  Color for filling region bounded by each stroke

  """

  fill_image: Image = ...

  fill_style: str = ...

  """

  Select style used to fill strokes

  * ``SOLID``
Solid -- Fill area with solid color.

  * ``GRADIENT``
Gradient -- Fill area with gradient color.

  * ``TEXTURE``
Texture -- Fill area with image texture.

  """

  flip: bool = ...

  """

  Flip filling colors

  """

  ghost: bool = ...

  """

  Display strokes using this color when showing onion skins

  """

  gradient_type: str = ...

  """

  Select type of gradient used to fill strokes

  * ``LINEAR``
Linear -- Fill area with gradient color.

  * ``RADIAL``
Radial -- Fill area with radial gradient.

  """

  hide: bool = ...

  """

  Set color Visibility

  """

  is_fill_visible: bool = ...

  """

  True when opacity of fill is set high enough to be visible

  """

  is_stroke_visible: bool = ...

  """

  True when opacity of stroke is set high enough to be visible

  """

  lock: bool = ...

  """

  Protect color from further editing and/or frame changes

  """

  mix_color: typing.Tuple[float, float, float, float] = ...

  """

  Color for mixing with primary filling color

  """

  mix_factor: float = ...

  """

  Mix Factor

  """

  mix_stroke_factor: float = ...

  """

  Mix Stroke Factor

  """

  mode: str = ...

  """

  Select line type for strokes

  * ``LINE``
Line -- Draw strokes using a continuous line.

  * ``DOTS``
Dots -- Draw strokes using separated dots.

  * ``BOX``
Squares -- Draw strokes using separated squares.

  """

  pass_index: int = ...

  """

  Index number for the "Color Index" pass

  """

  pixel_size: float = ...

  """

  Texture Pixel Size factor along the stroke

  """

  show_fill: bool = ...

  """

  Show stroke fills of this material

  """

  show_stroke: bool = ...

  """

  Show stroke lines of this material

  """

  stroke_image: Image = ...

  stroke_style: str = ...

  """

  Select style used to draw strokes

  * ``SOLID``
Solid -- Draw strokes with solid color.

  * ``TEXTURE``
Texture -- Draw strokes using texture.

  """

  texture_angle: float = ...

  """

  Texture Orientation Angle

  """

  texture_clamp: bool = ...

  """

  Do not repeat texture and clamp to one instance only

  """

  texture_offset: typing.Tuple[float, float] = ...

  """

  Shift Texture in 2d Space

  """

  texture_scale: typing.Tuple[float, float] = ...

  """

  Scale Factor for Texture

  """

  use_fill_holdout: bool = ...

  """

  Remove the color from underneath this stroke by using it as a mask

  """

  use_overlap_strokes: bool = ...

  """

  Disable stencil and overlap self intersections with alpha materials

  """

  use_stroke_holdout: bool = ...

  """

  Remove the color from underneath this stroke by using it as a mask

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MaterialLineArt(bpy_struct):

  mat_occlusion: int = ...

  """

  Faces with this material will behave as if it has set number of layers in occlusion

  """

  use_material_mask: bool = ...

  """

  Use material masks to filter out occluded strokes

  """

  use_material_mask_bits: typing.Tuple[bool, ...] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MaterialSlot(bpy_struct):

  """

  Material slot in an object

  """

  link: str = ...

  """

  Link material to object or the object's data

  """

  material: Material = ...

  """

  Material data-block used by this material slot

  """

  name: str = ...

  """

  Material slot name

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Menu(bpy_struct):

  """

  Editor menu containing buttons

  """

  bl_description: str = ...

  bl_idname: str = ...

  """

  If this is set, the menu gets a custom ID, otherwise it takes the name of the class used to define the menu (for example, if the class name is "OBJECT_MT_hello", and bl_idname is not set by the script, then bl_idname = "OBJECT_MT_hello")

  """

  bl_label: str = ...

  """

  The menu label

  """

  bl_owner_id: str = ...

  bl_translation_context: str = ...

  layout: UILayout = ...

  """

  Defines the structure of the menu in the UI

  """

  @classmethod

  def poll(cls, context: Context) -> bool:

    """

    If this method returns a non-null output, then the menu can be drawn

    """

    ...

  def draw(self, context: Context) -> None:

    """

    Draw UI elements into the menu UI layout

    """

    ...

  def draw_preset(self, _context: typing.Any) -> None:

    """

    Define these on the subclass:
- preset_operator (string)
- preset_subdir (string)

    Optionally:
- preset_add_operator (string)
- preset_extensions (set of strings)
- preset_operator_defaults (dict of keyword args)

    """

    ...

  def path_menu(self, searchpaths: typing.Sequence[str], operator: str, *args, props_default: typing.Dict[str, typing.Any] = None, prop_filepath: str = 'filepath', filter_ext: typing.Callable = None, filter_path: typing.Any = None, display_name: typing.Callable = None, add_operator: typing.Any = None) -> None:

    """

    Populate a menu from a list of paths.

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshEdge(bpy_struct):

  """

  Edge in a Mesh data-block

  """

  bevel_weight: float = ...

  """

  Weight used by the Bevel modifier

  """

  crease: float = ...

  """

  Weight used by the Subdivision Surface modifier for creasing

  """

  hide: bool = ...

  index: int = ...

  """

  Index of this edge

  """

  is_loose: bool = ...

  """

  Loose edge

  """

  select: bool = ...

  use_edge_sharp: bool = ...

  """

  Sharp edge for the Edge Split modifier

  """

  use_freestyle_mark: bool = ...

  """

  Edge mark for Freestyle line rendering

  """

  use_seam: bool = ...

  """

  Seam edge for UV unwrapping

  """

  vertices: typing.Tuple[int, int] = ...

  """

  Vertex indices

  """

  key: typing.Any = ...

  """

  (readonly)

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshEdges(bpy_struct):

  """

  Collection of mesh edges

  """

  def add(self, count: int) -> None:

    """

    add

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshFaceMap(bpy_struct):

  value: int = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshFaceMapLayer(bpy_struct):

  """

  Per-face map index

  """

  data: typing.Union[typing.Sequence[MeshFaceMap], typing.Mapping[str, MeshFaceMap], bpy_prop_collection] = ...

  name: str = ...

  """

  Name of face map layer

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshFaceMapLayers(bpy_struct):

  """

  Collection of mesh face maps

  """

  active: MeshFaceMapLayer = ...

  def new(self, name: str = 'Face Map') -> MeshFaceMapLayer:

    """

    Add a float property layer to Mesh

    """

    ...

  def remove(self, layer: MeshFaceMapLayer) -> None:

    """

    Remove a face map layer

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshLoop(bpy_struct):

  """

  Loop in a Mesh data-block

  """

  bitangent: typing.Tuple[float, float, float] = ...

  """

  Bitangent vector of this vertex for this polygon (must be computed beforehand using calc_tangents, use it only if really needed, slower access than bitangent_sign)

  """

  bitangent_sign: float = ...

  """

  Sign of the bitangent vector of this vertex for this polygon (must be computed beforehand using calc_tangents, bitangent = bitangent_sign * cross(normal, tangent))

  """

  edge_index: int = ...

  """

  Edge index

  """

  index: int = ...

  """

  Index of this loop

  """

  normal: typing.Tuple[float, float, float] = ...

  """

  Local space unit length split normal vector of this vertex for this polygon (must be computed beforehand using calc_normals_split or calc_tangents)

  """

  tangent: typing.Tuple[float, float, float] = ...

  """

  Local space unit length tangent vector of this vertex for this polygon (must be computed beforehand using calc_tangents)

  """

  vertex_index: int = ...

  """

  Vertex index

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshLoopColor(bpy_struct):

  """

  Vertex loop colors in a Mesh

  """

  color: typing.Tuple[float, float, float, float] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshLoopColorLayer(bpy_struct):

  """

  Layer of vertex colors in a Mesh data-block

  """

  active: bool = ...

  """

  Sets the layer as active for display and editing

  """

  active_render: bool = ...

  """

  Sets the layer as active for rendering

  """

  data: typing.Union[typing.Sequence[MeshLoopColor], typing.Mapping[str, MeshLoopColor], bpy_prop_collection] = ...

  name: str = ...

  """

  Name of Vertex color layer

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshLoops(bpy_struct):

  """

  Collection of mesh loops

  """

  def add(self, count: int) -> None:

    """

    add

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshLoopTriangle(bpy_struct):

  """

  Tessellated triangle in a Mesh data-block

  """

  area: float = ...

  """

  Area of this triangle

  """

  index: int = ...

  """

  Index of this loop triangle

  """

  loops: typing.Tuple[int, int, int] = ...

  """

  Indices of mesh loops that make up the triangle

  """

  material_index: int = ...

  """

  Material slot index of this triangle

  """

  normal: typing.Tuple[float, float, float] = ...

  """

  Local space unit length normal vector for this triangle

  """

  polygon_index: int = ...

  """

  Index of mesh polygon that the triangle is a part of

  """

  split_normals: typing.Tuple[typing.Tuple[float, float, float], typing.Tuple[float, float, float], typing.Tuple[float, float, float]] = ...

  """

  Local space unit length split normals vectors of the vertices of this triangle (must be computed beforehand using calc_normals_split or calc_tangents)

  """

  use_smooth: bool = ...

  vertices: typing.Tuple[int, int, int] = ...

  """

  Indices of triangle vertices

  """

  center: typing.Any = ...

  """

  The midpoint of the face.

  (readonly)

  """

  edge_keys: typing.Any = ...

  """

  (readonly)

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshLoopTriangles(bpy_struct):

  """

  Tessellation of mesh polygons into triangles

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshPaintMaskLayer(bpy_struct):

  """

  Per-vertex paint mask data

  """

  data: typing.Union[typing.Sequence[MeshPaintMaskProperty], typing.Mapping[str, MeshPaintMaskProperty], bpy_prop_collection] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshPaintMaskProperty(bpy_struct):

  """

  Floating-point paint mask value

  """

  value: float = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshPolygon(bpy_struct):

  """

  Polygon in a Mesh data-block

  """

  area: float = ...

  """

  Read only area of this polygon

  """

  center: typing.Tuple[float, float, float] = ...

  """

  Center of this polygon

  """

  hide: bool = ...

  index: int = ...

  """

  Index of this polygon

  """

  loop_start: int = ...

  """

  Index of the first loop of this polygon

  """

  loop_total: int = ...

  """

  Number of loops used by this polygon

  """

  material_index: int = ...

  """

  Material slot index of this polygon

  """

  normal: typing.Tuple[float, float, float] = ...

  """

  Local space unit length normal vector for this polygon

  """

  select: bool = ...

  use_freestyle_mark: bool = ...

  """

  Face mark for Freestyle line rendering

  """

  use_smooth: bool = ...

  vertices: typing.Tuple[int, int, int] = ...

  """

  Vertex indices

  """

  edge_keys: typing.Any = ...

  """

  (readonly)

  """

  loop_indices: typing.Any = ...

  """

  (readonly)

  """

  def flip(self) -> None:

    """

    Invert winding of this polygon (flip its normal)

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshPolygonFloatProperty(bpy_struct):

  """

  User defined floating-point number value in a float properties layer

  """

  value: float = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshPolygonFloatPropertyLayer(bpy_struct):

  """

  User defined layer of floating-point number values

  """

  data: typing.Union[typing.Sequence[MeshPolygonFloatProperty], typing.Mapping[str, MeshPolygonFloatProperty], bpy_prop_collection] = ...

  name: str = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshPolygonIntProperty(bpy_struct):

  """

  User defined integer number value in an integer properties layer

  """

  value: int = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshPolygonIntPropertyLayer(bpy_struct):

  """

  User defined layer of integer number values

  """

  data: typing.Union[typing.Sequence[MeshPolygonIntProperty], typing.Mapping[str, MeshPolygonIntProperty], bpy_prop_collection] = ...

  name: str = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshPolygons(bpy_struct):

  """

  Collection of mesh polygons

  """

  active: int = ...

  """

  The active polygon for this mesh

  """

  def add(self, count: int) -> None:

    """

    add

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshPolygonStringProperty(bpy_struct):

  """

  User defined string text value in a string properties layer

  """

  value: str = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshPolygonStringPropertyLayer(bpy_struct):

  """

  User defined layer of string text values

  """

  data: typing.Union[typing.Sequence[MeshPolygonStringProperty], typing.Mapping[str, MeshPolygonStringProperty], bpy_prop_collection] = ...

  name: str = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshSkinVertex(bpy_struct):

  """

  Per-vertex skin data for use with the Skin modifier

  """

  radius: typing.Tuple[float, float] = ...

  """

  Radius of the skin

  """

  use_loose: bool = ...

  """

  If vertex has multiple adjacent edges, it is hulled to them directly

  """

  use_root: bool = ...

  """

  Vertex is a root for rotation calculations and armature generation, setting this flag does not clear other roots in the same mesh island

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshSkinVertexLayer(bpy_struct):

  """

  Per-vertex skin data for use with the Skin modifier

  """

  data: typing.Union[typing.Sequence[MeshSkinVertex], typing.Mapping[str, MeshSkinVertex], bpy_prop_collection] = ...

  name: str = ...

  """

  Name of skin layer

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshStatVis(bpy_struct):

  distort_max: float = ...

  """

  Maximum angle to display

  """

  distort_min: float = ...

  """

  Minimum angle to display

  """

  overhang_axis: str = ...

  overhang_max: float = ...

  """

  Maximum angle to display

  """

  overhang_min: float = ...

  """

  Minimum angle to display

  """

  sharp_max: float = ...

  """

  Maximum angle to display

  """

  sharp_min: float = ...

  """

  Minimum angle to display

  """

  thickness_max: float = ...

  """

  Maximum for measuring thickness

  """

  thickness_min: float = ...

  """

  Minimum for measuring thickness

  """

  thickness_samples: int = ...

  """

  Number of samples to test per face

  """

  type: str = ...

  """

  Type of data to visualize/check

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshUVLoop(bpy_struct):

  pin_uv: bool = ...

  select: bool = ...

  uv: typing.Tuple[float, float] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshUVLoopLayer(bpy_struct):

  active: bool = ...

  """

  Set the map as active for display and editing

  """

  active_clone: bool = ...

  """

  Set the map as active for cloning

  """

  active_render: bool = ...

  """

  Set the map as active for rendering

  """

  data: typing.Union[typing.Sequence[MeshUVLoop], typing.Mapping[str, MeshUVLoop], bpy_prop_collection] = ...

  name: str = ...

  """

  Name of UV map

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshVertColor(bpy_struct):

  """

  Vertex colors in a Mesh

  """

  color: typing.Tuple[float, float, float, float] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshVertColorLayer(bpy_struct):

  """

  Layer of sculpt vertex colors in a Mesh data-block

  """

  active: bool = ...

  """

  Sets the sculpt vertex color layer as active for display and editing

  """

  active_render: bool = ...

  """

  Sets the sculpt vertex color layer as active for rendering

  """

  data: typing.Union[typing.Sequence[MeshVertColor], typing.Mapping[str, MeshVertColor], bpy_prop_collection] = ...

  name: str = ...

  """

  Name of Sculpt Vertex color layer

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshVertex(bpy_struct):

  """

  Vertex in a Mesh data-block

  """

  bevel_weight: float = ...

  """

  Weight used by the Bevel modifier 'Only Vertices' option

  """

  co: typing.Tuple[float, float, float] = ...

  groups: typing.Union[typing.Sequence[VertexGroupElement], typing.Mapping[str, VertexGroupElement], bpy_prop_collection] = ...

  """

  Weights for the vertex groups this vertex is member of

  """

  hide: bool = ...

  index: int = ...

  """

  Index of this vertex

  """

  normal: typing.Tuple[float, float, float] = ...

  """

  Vertex Normal

  """

  select: bool = ...

  undeformed_co: typing.Tuple[float, float, float] = ...

  """

  For meshes with modifiers applied, the coordinate of the vertex with no deforming modifiers applied, as used for generated texture coordinates

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshVertexFloatProperty(bpy_struct):

  """

  User defined floating-point number value in a float properties layer

  """

  value: float = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshVertexFloatPropertyLayer(bpy_struct):

  """

  User defined layer of floating-point number values

  """

  data: typing.Union[typing.Sequence[MeshVertexFloatProperty], typing.Mapping[str, MeshVertexFloatProperty], bpy_prop_collection] = ...

  name: str = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshVertexIntProperty(bpy_struct):

  """

  User defined integer number value in an integer properties layer

  """

  value: int = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshVertexIntPropertyLayer(bpy_struct):

  """

  User defined layer of integer number values

  """

  data: typing.Union[typing.Sequence[MeshVertexIntProperty], typing.Mapping[str, MeshVertexIntProperty], bpy_prop_collection] = ...

  name: str = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshVertexStringProperty(bpy_struct):

  """

  User defined string text value in a string properties layer

  """

  value: str = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshVertexStringPropertyLayer(bpy_struct):

  """

  User defined layer of string text values

  """

  data: typing.Union[typing.Sequence[MeshVertexStringProperty], typing.Mapping[str, MeshVertexStringProperty], bpy_prop_collection] = ...

  name: str = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MeshVertices(bpy_struct):

  """

  Collection of mesh vertices

  """

  def add(self, count: int) -> None:

    """

    add

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MetaBallElements(bpy_struct):

  """

  Collection of metaball elements

  """

  active: MetaElement = ...

  """

  Last selected element

  """

  def new(self, type: str = 'BALL') -> MetaElement:

    """

    Add a new element to the metaball

    """

    ...

  def remove(self, element: MetaElement) -> None:

    """

    Remove an element from the metaball

    """

    ...

  def clear(self) -> None:

    """

    Remove all elements from the metaball

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MetaElement(bpy_struct):

  """

  Blobby element in a metaball data-block

  """

  co: typing.Tuple[float, float, float] = ...

  hide: bool = ...

  """

  Hide element

  """

  radius: float = ...

  rotation: typing.Tuple[float, float, float, float] = ...

  """

  Normalized quaternion rotation

  """

  select: bool = ...

  """

  Select element

  """

  size_x: float = ...

  """

  Size of element, use of components depends on element type

  """

  size_y: float = ...

  """

  Size of element, use of components depends on element type

  """

  size_z: float = ...

  """

  Size of element, use of components depends on element type

  """

  stiffness: float = ...

  """

  Stiffness defines how much of the element to fill

  """

  type: str = ...

  """

  Metaball types

  """

  use_negative: bool = ...

  """

  Set metaball as negative one

  """

  use_scale_stiffness: bool = ...

  """

  Scale stiffness instead of radius

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Modifier(bpy_struct):

  """

  Modifier affecting the geometry data of an object

  """

  is_active: bool = ...

  """

  The active modifier in the list

  """

  is_override_data: bool = ...

  """

  In a local override object, whether this modifier comes from the linked reference object, or is local to the override

  """

  name: str = ...

  """

  Modifier name

  """

  show_expanded: bool = ...

  """

  Set modifier expanded in the user interface

  """

  show_in_editmode: bool = ...

  """

  Display modifier in Edit mode

  """

  show_on_cage: bool = ...

  """

  Adjust edit cage to modifier result

  """

  show_render: bool = ...

  """

  Use modifier during render

  """

  show_viewport: bool = ...

  """

  Display modifier in viewport

  """

  type: str = ...

  """

  * ``DATA_TRANSFER``
Data Transfer -- Transfer several types of data (vertex groups, UV maps, vertex colors, custom normals) from one mesh to another.

  * ``MESH_CACHE``
Mesh Cache -- Deform the mesh using an external frame-by-frame vertex transform cache.

  * ``MESH_SEQUENCE_CACHE``
Mesh Sequence Cache -- Deform the mesh or curve using an external mesh cache in Alembic format.

  * ``NORMAL_EDIT``
Normal Edit -- Modify the direction of the surface normals.

  * ``WEIGHTED_NORMAL``
Weighted Normal -- Modify the direction of the surface normals using a weighting method.

  * ``UV_PROJECT``
UV Project -- Project the UV map coordinates from the negative Z axis of another object.

  * ``UV_WARP``
UV Warp -- Transform the UV map using the difference between two objects.

  * ``VERTEX_WEIGHT_EDIT``
Vertex Weight Edit -- Modify of the weights of a vertex group.

  * ``VERTEX_WEIGHT_MIX``
Vertex Weight Mix -- Mix the weights of two vertex groups.

  * ``VERTEX_WEIGHT_PROXIMITY``
Vertex Weight Proximity -- Set the vertex group weights based on the distance to another target object.

  * ``ARRAY``
Array -- Create copies of the shape with offsets.

  * ``BEVEL``
Bevel -- Generate sloped corners by adding geometry to the mesh's edges or vertices.

  * ``BOOLEAN``
Boolean -- Use another shape to cut, combine or perform a difference operation.

  * ``BUILD``
Build -- Cause the faces of the mesh object to appear or disappear one after the other over time.

  * ``DECIMATE``
Decimate -- Reduce the geometry density.

  * ``EDGE_SPLIT``
Edge Split -- Split away joined faces at the edges.

  * ``NODES``
Geometry Nodes.

  * ``MASK``
Mask -- Dynamically hide vertices based on a vertex group or armature.

  * ``MIRROR``
Mirror -- Mirror along the local X, Y and/or Z axes, over the object origin.

  * ``MESH_TO_VOLUME``
Mesh to Volume.

  * ``MULTIRES``
Multiresolution -- Subdivide the mesh in a way that allows editing the higher subdivision levels.

  * ``REMESH``
Remesh -- Generate new mesh topology based on the current shape.

  * ``SCREW``
Screw -- Lathe around an axis, treating the input mesh as a profile.

  * ``SKIN``
Skin -- Create a solid shape from vertices and edges, using the vertex radius to define the thickness.

  * ``SOLIDIFY``
Solidify -- Make the surface thick.

  * ``SUBSURF``
Subdivision Surface -- Split the faces into smaller parts, giving it a smoother appearance.

  * ``TRIANGULATE``
Triangulate -- Convert all polygons to triangles.

  * ``VOLUME_TO_MESH``
Volume to Mesh.

  * ``WELD``
Weld -- Find groups of vertices closer than dist and merge them together.

  * ``WIREFRAME``
Wireframe -- Convert faces into thickened edges.

  * ``ARMATURE``
Armature -- Deform the shape using an armature object.

  * ``CAST``
Cast -- Shift the shape towards a predefined primitive.

  * ``CURVE``
Curve -- Bend the mesh using a curve object.

  * ``DISPLACE``
Displace -- Offset vertices based on a texture.

  * ``HOOK``
Hook -- Deform specific points using another object.

  * ``LAPLACIANDEFORM``
Laplacian Deform -- Deform based a series of anchor points.

  * ``LATTICE``
Lattice -- Deform using the shape of a lattice object.

  * ``MESH_DEFORM``
Mesh Deform -- Deform using a different mesh, which acts as a deformation cage.

  * ``SHRINKWRAP``
Shrinkwrap -- Project the shape onto another object.

  * ``SIMPLE_DEFORM``
Simple Deform -- Deform the shape by twisting, bending, tapering or stretching.

  * ``SMOOTH``
Smooth -- Smooth the mesh by flattening the angles between adjacent faces.

  * ``CORRECTIVE_SMOOTH``
Smooth Corrective -- Smooth the mesh while still preserving the volume.

  * ``LAPLACIANSMOOTH``
Smooth Laplacian -- Reduce the noise on a mesh surface with minimal changes to its shape.

  * ``SURFACE_DEFORM``
Surface Deform -- Transfer motion from another mesh.

  * ``WARP``
Warp -- Warp parts of a mesh to a new location in a very flexible way thanks to 2 specified objects.

  * ``WAVE``
Wave -- Adds a ripple-like motion to an object's geometry.

  * ``VOLUME_DISPLACE``
Volume Displace -- Deform volume based on noise or other vector fields.

  * ``CLOTH``
Cloth.

  * ``COLLISION``
Collision.

  * ``DYNAMIC_PAINT``
Dynamic Paint.

  * ``EXPLODE``
Explode -- Break apart the mesh faces and let them follow particles.

  * ``FLUID``
Fluid.

  * ``OCEAN``
Ocean -- Generate a moving ocean surface.

  * ``PARTICLE_INSTANCE``
Particle Instance.

  * ``PARTICLE_SYSTEM``
Particle System -- Spawn particles from the shape.

  * ``SOFT_BODY``
Soft Body.

  * ``SURFACE``
Surface.

  """

  use_apply_on_spline: bool = ...

  """

  Apply this and all preceding deformation modifiers on splines' points rather than on filled curve/surface

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MotionPath(bpy_struct):

  """

  Cache of the worldspace positions of an element over a frame range

  """

  color: typing.Tuple[float, float, float] = ...

  """

  Custom color for motion path

  """

  frame_end: int = ...

  """

  End frame of the stored range

  """

  frame_start: int = ...

  """

  Starting frame of the stored range

  """

  is_modified: bool = ...

  """

  Path is being edited

  """

  length: int = ...

  """

  Number of frames cached

  """

  line_thickness: int = ...

  """

  Line thickness for motion path

  """

  lines: bool = ...

  """

  Use straight lines between keyframe points

  """

  points: typing.Union[typing.Sequence[MotionPathVert], typing.Mapping[str, MotionPathVert], bpy_prop_collection] = ...

  """

  Cached positions per frame

  """

  use_bone_head: bool = ...

  """

  For PoseBone paths, use the bone head location when calculating this path

  """

  use_custom_color: bool = ...

  """

  Use custom color for this motion path

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MotionPathVert(bpy_struct):

  """

  Cached location on path

  """

  co: typing.Tuple[float, float, float] = ...

  select: bool = ...

  """

  Path point is selected for editing

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MovieClipProxy(bpy_struct):

  """

  Proxy parameters for a movie clip

  """

  build_100: bool = ...

  """

  Build proxy resolution 100% of the original footage dimension

  """

  build_25: bool = ...

  """

  Build proxy resolution 25% of the original footage dimension

  """

  build_50: bool = ...

  """

  Build proxy resolution 50% of the original footage dimension

  """

  build_75: bool = ...

  """

  Build proxy resolution 75% of the original footage dimension

  """

  build_free_run: bool = ...

  """

  Build free run time code index

  """

  build_free_run_rec_date: bool = ...

  """

  Build free run time code index using Record Date/Time

  """

  build_record_run: bool = ...

  """

  Build record run time code index

  """

  build_undistorted_100: bool = ...

  """

  Build proxy resolution 100% of the original undistorted footage dimension

  """

  build_undistorted_25: bool = ...

  """

  Build proxy resolution 25% of the original undistorted footage dimension

  """

  build_undistorted_50: bool = ...

  """

  Build proxy resolution 50% of the original undistorted footage dimension

  """

  build_undistorted_75: bool = ...

  """

  Build proxy resolution 75% of the original undistorted footage dimension

  """

  directory: str = ...

  """

  Location to store the proxy files

  """

  quality: int = ...

  """

  JPEG quality of proxy images

  """

  timecode: str = ...

  """

  * ``NONE``
None.

  * ``RECORD_RUN``
Record Run -- Use images in the order they are recorded.

  * ``FREE_RUN``
Free Run -- Use global timestamp written by recording device.

  * ``FREE_RUN_REC_DATE``
Free Run (rec date) -- Interpolate a global timestamp using the record date and time written by recording device.

  * ``FREE_RUN_NO_GAPS``
Free Run No Gaps -- Record run, but ignore timecode, changes in framerate or dropouts.

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MovieClipScopes(bpy_struct):

  """

  Scopes for statistical view of a movie clip

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MovieClipUser(bpy_struct):

  """

  Parameters defining how a MovieClip data-block is used by another data-block

  """

  frame_current: int = ...

  """

  Current frame number in movie or image sequence

  """

  proxy_render_size: str = ...

  """

  Display preview using full resolution or different proxy resolutions

  """

  use_render_undistorted: bool = ...

  """

  Render preview using undistorted proxy

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MovieReconstructedCamera(bpy_struct):

  """

  Match-moving reconstructed camera data from tracker

  """

  average_error: float = ...

  """

  Average error of reconstruction

  """

  frame: int = ...

  """

  Frame number marker is keyframed on

  """

  matrix: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]] = ...

  """

  Worldspace transformation matrix

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MovieTracking(bpy_struct):

  """

  Match-moving data for tracking

  """

  active_object_index: int = ...

  """

  Index of active object

  """

  camera: MovieTrackingCamera = ...

  dopesheet: MovieTrackingDopesheet = ...

  objects: typing.Union[MovieTrackingObjects, typing.Sequence[MovieTrackingObject], typing.Mapping[str, MovieTrackingObject], bpy_prop_collection] = ...

  """

  Collection of objects in this tracking data object

  """

  plane_tracks: typing.Union[MovieTrackingPlaneTracks, typing.Sequence[MovieTrackingPlaneTrack], typing.Mapping[str, MovieTrackingPlaneTrack], bpy_prop_collection] = ...

  """

  Collection of plane tracks in this tracking data object

  """

  reconstruction: MovieTrackingReconstruction = ...

  settings: MovieTrackingSettings = ...

  stabilization: MovieTrackingStabilization = ...

  tracks: typing.Union[MovieTrackingTracks, typing.Sequence[MovieTrackingTrack], typing.Mapping[str, MovieTrackingTrack], bpy_prop_collection] = ...

  """

  Collection of tracks in this tracking data object

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MovieTrackingCamera(bpy_struct):

  """

  Match-moving camera data for tracking

  """

  brown_k1: float = ...

  """

  First coefficient of fourth order Brown-Conrady radial distortion

  """

  brown_k2: float = ...

  """

  Second coefficient of fourth order Brown-Conrady radial distortion

  """

  brown_k3: float = ...

  """

  Third coefficient of fourth order Brown-Conrady radial distortion

  """

  brown_k4: float = ...

  """

  Fourth coefficient of fourth order Brown-Conrady radial distortion

  """

  brown_p1: float = ...

  """

  First coefficient of second order Brown-Conrady tangential distortion

  """

  brown_p2: float = ...

  """

  Second coefficient of second order Brown-Conrady tangential distortion

  """

  distortion_model: str = ...

  """

  Distortion model used for camera lenses

  * ``POLYNOMIAL``
Polynomial -- Radial distortion model which fits common cameras.

  * ``DIVISION``
Divisions -- Division distortion model which better represents wide-angle cameras.

  * ``NUKE``
Nuke -- Nuke distortion model.

  * ``BROWN``
Brown -- Brown-Conrady distortion model.

  """

  division_k1: float = ...

  """

  First coefficient of second order division distortion

  """

  division_k2: float = ...

  """

  Second coefficient of second order division distortion

  """

  focal_length: float = ...

  """

  Camera's focal length

  """

  focal_length_pixels: float = ...

  """

  Camera's focal length

  """

  k1: float = ...

  """

  First coefficient of third order polynomial radial distortion

  """

  k2: float = ...

  """

  Second coefficient of third order polynomial radial distortion

  """

  k3: float = ...

  """

  Third coefficient of third order polynomial radial distortion

  """

  nuke_k1: float = ...

  """

  First coefficient of second order Nuke distortion

  """

  nuke_k2: float = ...

  """

  Second coefficient of second order Nuke distortion

  """

  pixel_aspect: float = ...

  """

  Pixel aspect ratio

  """

  principal: typing.Tuple[float, float] = ...

  """

  Optical center of lens

  """

  sensor_width: float = ...

  """

  Width of CCD sensor in millimeters

  """

  units: str = ...

  """

  Units used for camera focal length

  * ``PIXELS``
px -- Use pixels for units of focal length.

  * ``MILLIMETERS``
mm -- Use millimeters for units of focal length.

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MovieTrackingDopesheet(bpy_struct):

  """

  Match-moving dopesheet data

  """

  show_hidden: bool = ...

  """

  Include channels from objects/bone that aren't visible

  """

  show_only_selected: bool = ...

  """

  Only include channels relating to selected objects and data

  """

  sort_method: str = ...

  """

  Method to be used to sort channels in dopesheet view

  * ``NAME``
Name -- Sort channels by their names.

  * ``LONGEST``
Longest -- Sort channels by longest tracked segment.

  * ``TOTAL``
Total -- Sort channels by overall amount of tracked segments.

  * ``AVERAGE_ERROR``
Average Error -- Sort channels by average reprojection error of tracks after solve.

  * ``START``
Start Frame -- Sort channels by first frame number.

  * ``END``
End Frame -- Sort channels by last frame number.

  """

  use_invert_sort: bool = ...

  """

  Invert sort order of dopesheet channels

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MovieTrackingMarker(bpy_struct):

  """

  Match-moving marker data for tracking

  """

  co: typing.Tuple[float, float] = ...

  """

  Marker position at frame in normalized coordinates

  """

  frame: int = ...

  """

  Frame number marker is keyframed on

  """

  is_keyed: bool = ...

  """

  Whether the position of the marker is keyframed or tracked

  """

  mute: bool = ...

  """

  Is marker muted for current frame

  """

  pattern_bound_box: typing.Tuple[typing.Tuple[float, float], typing.Tuple[float, float]] = ...

  """

  Pattern area bounding box in normalized coordinates

  """

  pattern_corners: typing.Tuple[typing.Tuple[float, float], typing.Tuple[float, float], typing.Tuple[float, float], typing.Tuple[float, float]] = ...

  """

  Array of coordinates which represents pattern's corners in normalized coordinates relative to marker position

  """

  search_max: typing.Tuple[float, float] = ...

  """

  Right-bottom corner of search area in normalized coordinates relative to marker position

  """

  search_min: typing.Tuple[float, float] = ...

  """

  Left-bottom corner of search area in normalized coordinates relative to marker position

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MovieTrackingMarkers(bpy_struct):

  """

  Collection of markers for movie tracking track

  """

  def find_frame(self, frame: int, exact: bool = True) -> MovieTrackingMarker:

    """

    Get marker for specified frame

    """

    ...

  def insert_frame(self, frame: int, co: typing.Tuple[float, float] = (0.0, 0.0)) -> MovieTrackingMarker:

    """

    Insert a new marker at the specified frame

    """

    ...

  def delete_frame(self, frame: int) -> None:

    """

    Delete marker at specified frame

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MovieTrackingObject(bpy_struct):

  """

  Match-moving object tracking and reconstruction data

  """

  is_camera: bool = ...

  """

  Object is used for camera tracking

  """

  keyframe_a: int = ...

  """

  First keyframe used for reconstruction initialization

  """

  keyframe_b: int = ...

  """

  Second keyframe used for reconstruction initialization

  """

  name: str = ...

  """

  Unique name of object

  """

  plane_tracks: typing.Union[MovieTrackingObjectPlaneTracks, typing.Sequence[MovieTrackingPlaneTrack], typing.Mapping[str, MovieTrackingPlaneTrack], bpy_prop_collection] = ...

  """

  Collection of plane tracks in this tracking data object

  """

  reconstruction: MovieTrackingReconstruction = ...

  scale: float = ...

  """

  Scale of object solution in camera space

  """

  tracks: typing.Union[MovieTrackingObjectTracks, typing.Sequence[MovieTrackingTrack], typing.Mapping[str, MovieTrackingTrack], bpy_prop_collection] = ...

  """

  Collection of tracks in this tracking data object

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MovieTrackingObjectPlaneTracks(bpy_struct):

  """

  Collection of tracking plane tracks

  """

  active: MovieTrackingTrack = ...

  """

  Active track in this tracking data object

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MovieTrackingObjects(bpy_struct):

  """

  Collection of movie tracking objects

  """

  active: MovieTrackingObject = ...

  """

  Active object in this tracking data object

  """

  def new(self, name: str) -> MovieTrackingObject:

    """

    Add tracking object to this movie clip

    """

    ...

  def remove(self, object: MovieTrackingObject) -> None:

    """

    Remove tracking object from this movie clip

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MovieTrackingObjectTracks(bpy_struct):

  """

  Collection of movie tracking tracks

  """

  active: MovieTrackingTrack = ...

  """

  Active track in this tracking data object

  """

  def new(self, name: str = '', frame: int = 1) -> MovieTrackingTrack:

    """

    create new motion track in this movie clip

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MovieTrackingPlaneMarker(bpy_struct):

  """

  Match-moving plane marker data for tracking

  """

  corners: typing.Tuple[typing.Tuple[float, float], typing.Tuple[float, float], typing.Tuple[float, float], typing.Tuple[float, float]] = ...

  """

  Array of coordinates which represents UI rectangle corners in frame normalized coordinates

  """

  frame: int = ...

  """

  Frame number marker is keyframed on

  """

  mute: bool = ...

  """

  Is marker muted for current frame

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MovieTrackingPlaneMarkers(bpy_struct):

  """

  Collection of markers for movie tracking plane track

  """

  def find_frame(self, frame: int, exact: bool = True) -> MovieTrackingPlaneMarker:

    """

    Get plane marker for specified frame

    """

    ...

  def insert_frame(self, frame: int) -> MovieTrackingPlaneMarker:

    """

    Insert a new plane marker at the specified frame

    """

    ...

  def delete_frame(self, frame: int) -> None:

    """

    Delete plane marker at specified frame

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MovieTrackingPlaneTrack(bpy_struct):

  """

  Match-moving plane track data for tracking

  """

  image: Image = ...

  """

  Image displayed in the track during editing in clip editor

  """

  image_opacity: float = ...

  """

  Opacity of the image

  """

  markers: typing.Union[MovieTrackingPlaneMarkers, typing.Sequence[MovieTrackingPlaneMarker], typing.Mapping[str, MovieTrackingPlaneMarker], bpy_prop_collection] = ...

  """

  Collection of markers in track

  """

  name: str = ...

  """

  Unique name of track

  """

  select: bool = ...

  """

  Plane track is selected

  """

  use_auto_keying: bool = ...

  """

  Automatic keyframe insertion when moving plane corners

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MovieTrackingPlaneTracks(bpy_struct):

  """

  Collection of movie tracking plane tracks

  """

  active: MovieTrackingPlaneTrack = ...

  """

  Active plane track in this tracking data object

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MovieTrackingReconstructedCameras(bpy_struct):

  """

  Collection of solved cameras

  """

  def find_frame(self, frame: int = 1) -> MovieReconstructedCamera:

    """

    Find a reconstructed camera for a give frame number

    """

    ...

  def matrix_from_frame(self, frame: int = 1) -> typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]]:

    """

    Return interpolated camera matrix for a given frame

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MovieTrackingReconstruction(bpy_struct):

  """

  Match-moving reconstruction data from tracker

  """

  average_error: float = ...

  """

  Average error of reconstruction

  """

  cameras: typing.Union[MovieTrackingReconstructedCameras, typing.Sequence[MovieReconstructedCamera], typing.Mapping[str, MovieReconstructedCamera], bpy_prop_collection] = ...

  """

  Collection of solved cameras

  """

  is_valid: bool = ...

  """

  Is tracking data contains valid reconstruction information

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MovieTrackingSettings(bpy_struct):

  """

  Match moving settings

  """

  clean_action: str = ...

  """

  Cleanup action to execute

  * ``SELECT``
Select -- Select unclean tracks.

  * ``DELETE_TRACK``
Delete Track -- Delete unclean tracks.

  * ``DELETE_SEGMENTS``
Delete Segments -- Delete unclean segments of tracks.

  """

  clean_error: float = ...

  """

  Effect on tracks which have a larger re-projection error

  """

  clean_frames: int = ...

  """

  Effect on tracks which are tracked less than the specified amount of frames

  """

  default_correlation_min: float = ...

  """

  Default minimum value of correlation between matched pattern and reference that is still treated as successful tracking

  """

  default_frames_limit: int = ...

  """

  Every tracking cycle, this number of frames are tracked

  """

  default_margin: int = ...

  """

  Default distance from image boundary at which marker stops tracking

  """

  default_motion_model: str = ...

  """

  Default motion model to use for tracking

  * ``Perspective``
Perspective -- Search for markers that are perspectively deformed (homography) between frames.

  * ``Affine``
Affine -- Search for markers that are affine-deformed (t, r, k, and skew) between frames.

  * ``LocRotScale``
Location, Rotation & Scale -- Search for markers that are translated, rotated, and scaled between frames.

  * ``LocScale``
Location & Scale -- Search for markers that are translated and scaled between frames.

  * ``LocRot``
Location & Rotation -- Search for markers that are translated and rotated between frames.

  * ``Loc``
Location -- Search for markers that are translated between frames.

  """

  default_pattern_match: str = ...

  """

  Track pattern from given frame when tracking marker to next frame

  * ``KEYFRAME``
Keyframe -- Track pattern from keyframe to next frame.

  * ``PREV_FRAME``
Previous frame -- Track pattern from current frame to next frame.

  """

  default_pattern_size: int = ...

  """

  Size of pattern area for newly created tracks

  """

  default_search_size: int = ...

  """

  Size of search area for newly created tracks

  """

  default_weight: float = ...

  """

  Influence of newly created track on a final solution

  """

  distance: float = ...

  """

  Distance between two bundles used for scene scaling

  """

  object_distance: float = ...

  """

  Distance between two bundles used for object scaling

  """

  refine_intrinsics_focal_length: bool = ...

  """

  Refine focal length during camera solving

  """

  refine_intrinsics_principal_point: bool = ...

  """

  Refine principal point during camera solving

  """

  refine_intrinsics_radial_distortion: bool = ...

  """

  Refine radial coefficients of distortion model during camera solving

  """

  refine_intrinsics_tangential_distortion: bool = ...

  """

  Refine tangential coefficients of distortion model during camera solving

  """

  speed: str = ...

  """

  Limit speed of tracking to make visual feedback easier (this does not affect the tracking quality)

  * ``FASTEST``
Fastest -- Track as fast as it's possible.

  * ``DOUBLE``
Double -- Track with double speed.

  * ``REALTIME``
Realtime -- Track with realtime speed.

  * ``HALF``
Half -- Track with half of realtime speed.

  * ``QUARTER``
Quarter -- Track with quarter of realtime speed.

  """

  use_default_blue_channel: bool = ...

  """

  Use blue channel from footage for tracking

  """

  use_default_brute: bool = ...

  """

  Use a brute-force translation-only initialization when tracking

  """

  use_default_green_channel: bool = ...

  """

  Use green channel from footage for tracking

  """

  use_default_mask: bool = ...

  """

  Use a grease pencil data-block as a mask to use only specified areas of pattern when tracking

  """

  use_default_normalization: bool = ...

  """

  Normalize light intensities while tracking (slower)

  """

  use_default_red_channel: bool = ...

  """

  Use red channel from footage for tracking

  """

  use_keyframe_selection: bool = ...

  """

  Automatically select keyframes when solving camera/object motion

  """

  use_tripod_solver: bool = ...

  """

  Use special solver to track a stable camera position, such as a tripod

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MovieTrackingStabilization(bpy_struct):

  """

  2D stabilization based on tracking markers

  """

  active_rotation_track_index: int = ...

  """

  Index of active track in rotation stabilization tracks list

  """

  active_track_index: int = ...

  """

  Index of active track in translation stabilization tracks list

  """

  anchor_frame: int = ...

  """

  Reference point to anchor stabilization (other frames will be adjusted relative to this frame's position)

  """

  filter_type: str = ...

  """

  Interpolation to use for sub-pixel shifts and rotations due to stabilization

  * ``NEAREST``
Nearest -- No interpolation, use nearest neighbor pixel.

  * ``BILINEAR``
Bilinear -- Simple interpolation between adjacent pixels.

  * ``BICUBIC``
Bicubic -- High quality pixel interpolation.

  """

  influence_location: float = ...

  """

  Influence of stabilization algorithm on footage location

  """

  influence_rotation: float = ...

  """

  Influence of stabilization algorithm on footage rotation

  """

  influence_scale: float = ...

  """

  Influence of stabilization algorithm on footage scale

  """

  rotation_tracks: typing.Union[typing.Sequence[MovieTrackingTrack], typing.Mapping[str, MovieTrackingTrack], bpy_prop_collection] = ...

  """

  Collection of tracks used for 2D stabilization (translation)

  """

  scale_max: float = ...

  """

  Limit the amount of automatic scaling

  """

  show_tracks_expanded: bool = ...

  """

  Show UI list of tracks participating in stabilization

  """

  target_position: typing.Tuple[float, float] = ...

  """

  Known relative offset of original shot, will be subtracted (e.g. for panning shot, can be animated)

  """

  target_rotation: float = ...

  """

  Rotation present on original shot, will be compensated (e.g. for deliberate tilting)

  """

  target_scale: float = ...

  """

  Explicitly scale resulting frame to compensate zoom of original shot

  """

  tracks: typing.Union[typing.Sequence[MovieTrackingTrack], typing.Mapping[str, MovieTrackingTrack], bpy_prop_collection] = ...

  """

  Collection of tracks used for 2D stabilization (translation)

  """

  use_2d_stabilization: bool = ...

  """

  Use 2D stabilization for footage

  """

  use_autoscale: bool = ...

  """

  Automatically scale footage to cover unfilled areas when stabilizing

  """

  use_stabilize_rotation: bool = ...

  """

  Stabilize detected rotation around center of frame

  """

  use_stabilize_scale: bool = ...

  """

  Compensate any scale changes relative to center of rotation

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MovieTrackingTrack(bpy_struct):

  """

  Match-moving track data for tracking

  """

  average_error: float = ...

  """

  Average error of re-projection

  """

  bundle: typing.Tuple[float, float, float] = ...

  """

  Position of bundle reconstructed from this track

  """

  color: typing.Tuple[float, float, float] = ...

  """

  Color of the track in the Movie Clip Editor and the 3D viewport after a solve

  """

  correlation_min: float = ...

  """

  Minimal value of correlation between matched pattern and reference that is still treated as successful tracking

  """

  frames_limit: int = ...

  """

  Every tracking cycle, this number of frames are tracked

  """

  grease_pencil: GreasePencil = ...

  """

  Grease pencil data for this track

  """

  has_bundle: bool = ...

  """

  True if track has a valid bundle

  """

  hide: bool = ...

  """

  Track is hidden

  """

  lock: bool = ...

  """

  Track is locked and all changes to it are disabled

  """

  margin: int = ...

  """

  Distance from image boundary at which marker stops tracking

  """

  markers: typing.Union[MovieTrackingMarkers, typing.Sequence[MovieTrackingMarker], typing.Mapping[str, MovieTrackingMarker], bpy_prop_collection] = ...

  """

  Collection of markers in track

  """

  motion_model: str = ...

  """

  Default motion model to use for tracking

  * ``Perspective``
Perspective -- Search for markers that are perspectively deformed (homography) between frames.

  * ``Affine``
Affine -- Search for markers that are affine-deformed (t, r, k, and skew) between frames.

  * ``LocRotScale``
Location, Rotation & Scale -- Search for markers that are translated, rotated, and scaled between frames.

  * ``LocScale``
Location & Scale -- Search for markers that are translated and scaled between frames.

  * ``LocRot``
Location & Rotation -- Search for markers that are translated and rotated between frames.

  * ``Loc``
Location -- Search for markers that are translated between frames.

  """

  name: str = ...

  """

  Unique name of track

  """

  offset: typing.Tuple[float, float] = ...

  """

  Offset of track from the parenting point

  """

  pattern_match: str = ...

  """

  Track pattern from given frame when tracking marker to next frame

  * ``KEYFRAME``
Keyframe -- Track pattern from keyframe to next frame.

  * ``PREV_FRAME``
Previous frame -- Track pattern from current frame to next frame.

  """

  select: bool = ...

  """

  Track is selected

  """

  select_anchor: bool = ...

  """

  Track's anchor point is selected

  """

  select_pattern: bool = ...

  """

  Track's pattern area is selected

  """

  select_search: bool = ...

  """

  Track's search area is selected

  """

  use_alpha_preview: bool = ...

  """

  Apply track's mask on displaying preview

  """

  use_blue_channel: bool = ...

  """

  Use blue channel from footage for tracking

  """

  use_brute: bool = ...

  """

  Use a brute-force translation only pre-track before refinement

  """

  use_custom_color: bool = ...

  """

  Use custom color instead of theme-defined

  """

  use_grayscale_preview: bool = ...

  """

  Display what the tracking algorithm sees in the preview

  """

  use_green_channel: bool = ...

  """

  Use green channel from footage for tracking

  """

  use_mask: bool = ...

  """

  Use a grease pencil data-block as a mask to use only specified areas of pattern when tracking

  """

  use_normalization: bool = ...

  """

  Normalize light intensities while tracking. Slower

  """

  use_red_channel: bool = ...

  """

  Use red channel from footage for tracking

  """

  weight: float = ...

  """

  Influence of this track on a final solution

  """

  weight_stab: float = ...

  """

  Influence of this track on 2D stabilization

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MovieTrackingTracks(bpy_struct):

  """

  Collection of movie tracking tracks

  """

  active: MovieTrackingTrack = ...

  """

  Active track in this tracking data object

  """

  def new(self, name: str = '', frame: int = 1) -> MovieTrackingTrack:

    """

    Create new motion track in this movie clip

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class NlaStrip(bpy_struct):

  """

  A container referencing an existing Action

  """

  action: Action = ...

  """

  Action referenced by this strip

  """

  action_frame_end: float = ...

  """

  Last frame from action to use

  """

  action_frame_start: float = ...

  """

  First frame from action to use

  """

  active: bool = ...

  """

  NLA Strip is active

  """

  blend_in: float = ...

  """

  Number of frames at start of strip to fade in influence

  """

  blend_out: float = ...

  blend_type: str = ...

  """

  Method used for combining strip's result with accumulated result

  * ``REPLACE``
Replace -- The strip values replace the accumulated results by amount specified by influence.

  * ``COMBINE``
Combine -- The strip values are combined with accumulated results by appropriately using addition, multiplication, or quaternion math, based on channel type.

  * ``ADD``
Add -- Weighted result of strip is added to the accumulated results.

  * ``SUBTRACT``
Subtract -- Weighted result of strip is removed from the accumulated results.

  * ``MULTIPLY``
Multiply -- Weighted result of strip is multiplied with the accumulated results.

  """

  extrapolation: str = ...

  """

  Action to take for gaps past the strip extents

  * ``NOTHING``
Nothing -- Strip has no influence past its extents.

  * ``HOLD``
Hold -- Hold the first frame if no previous strips in track, and always hold last frame.

  * ``HOLD_FORWARD``
Hold Forward -- Only hold last frame.

  """

  fcurves: typing.Union[NlaStripFCurves, typing.Sequence[FCurve], typing.Mapping[str, FCurve], bpy_prop_collection] = ...

  """

  F-Curves for controlling the strip's influence and timing

  """

  frame_end: float = ...

  frame_start: float = ...

  influence: float = ...

  """

  Amount the strip contributes to the current result

  """

  modifiers: typing.Union[typing.Sequence[FModifier], typing.Mapping[str, FModifier], bpy_prop_collection] = ...

  """

  Modifiers affecting all the F-Curves in the referenced Action

  """

  mute: bool = ...

  """

  Disable NLA Strip evaluation

  """

  name: str = ...

  repeat: float = ...

  """

  Number of times to repeat the action range

  """

  scale: float = ...

  """

  Scaling factor for action

  """

  select: bool = ...

  """

  NLA Strip is selected

  """

  strip_time: float = ...

  """

  Frame of referenced Action to evaluate

  """

  strips: typing.Union[typing.Sequence[NlaStrip], typing.Mapping[str, NlaStrip], bpy_prop_collection] = ...

  """

  NLA Strips that this strip acts as a container for (if it is of type Meta)

  """

  type: str = ...

  """

  Type of NLA Strip

  * ``CLIP``
Action Clip -- NLA Strip references some Action.

  * ``TRANSITION``
Transition -- NLA Strip 'transitions' between adjacent strips.

  * ``META``
Meta -- NLA Strip acts as a container for adjacent strips.

  * ``SOUND``
Sound Clip -- NLA Strip representing a sound event for speakers.

  """

  use_animated_influence: bool = ...

  """

  Influence setting is controlled by an F-Curve rather than automatically determined

  """

  use_animated_time: bool = ...

  """

  Strip time is controlled by an F-Curve rather than automatically determined

  """

  use_animated_time_cyclic: bool = ...

  """

  Cycle the animated time within the action start and end

  """

  use_auto_blend: bool = ...

  """

  Number of frames for Blending In/Out is automatically determined from overlapping strips

  """

  use_reverse: bool = ...

  """

  NLA Strip is played back in reverse order (only when timing is automatically determined)

  """

  use_sync_length: bool = ...

  """

  Update range of frames referenced from action after tweaking strip and its keyframes

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class NlaStripFCurves(bpy_struct):

  """

  Collection of NLA strip F-Curves

  """

  def find(self, data_path: str, index: int = 0) -> FCurve:

    """

    Find an F-Curve. Note that this function performs a linear scan of all F-Curves in the NLA strip.

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class NlaStrips(bpy_struct):

  """

  Collection of Nla Strips

  """

  def new(self, name: str, start: int, action: Action) -> NlaStrip:

    """

    Add a new Action-Clip strip to the track

    """

    ...

  def remove(self, strip: NlaStrip) -> None:

    """

    Remove a NLA Strip

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class NlaTrack(bpy_struct):

  """

  A animation layer containing Actions referenced as NLA strips

  """

  active: bool = ...

  """

  NLA Track is active

  """

  is_override_data: bool = ...

  """

  In a local override data, whether this NLA track comes from the linked reference data, or is local to the override

  """

  is_solo: bool = ...

  """

  NLA Track is evaluated itself (i.e. active Action and all other NLA Tracks in the same AnimData block are disabled)

  """

  lock: bool = ...

  """

  NLA Track is locked

  """

  mute: bool = ...

  """

  Disable NLA Track evaluation

  """

  name: str = ...

  select: bool = ...

  """

  NLA Track is selected

  """

  strips: typing.Union[NlaStrips, typing.Sequence[NlaStrip], typing.Mapping[str, NlaStrip], bpy_prop_collection] = ...

  """

  NLA Strips on this NLA-track

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class NlaTracks(bpy_struct):

  """

  Collection of NLA Tracks

  """

  active: NlaTrack = ...

  """

  Active NLA Track

  """

  def new(self, prev: NlaTrack = None) -> NlaTrack:

    """

    Add a new NLA Track

    """

    ...

  def remove(self, track: NlaTrack) -> None:

    """

    Remove a NLA Track

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Node(bpy_struct):

  """

  Node in a node tree

  """

  bl_description: str = ...

  bl_height_default: float = ...

  bl_height_max: float = ...

  bl_height_min: float = ...

  bl_icon: str = ...

  """

  The node icon

  """

  bl_idname: str = ...

  bl_label: str = ...

  """

  The node label

  """

  bl_static_type: str = ...

  """

  Node type (deprecated, use with care)

  * ``CUSTOM``
Custom -- Custom Node.

  """

  bl_width_default: float = ...

  bl_width_max: float = ...

  bl_width_min: float = ...

  color: typing.Tuple[float, float, float] = ...

  """

  Custom color of the node body

  """

  dimensions: typing.Tuple[float, float] = ...

  """

  Absolute bounding box dimensions of the node

  """

  height: float = ...

  """

  Height of the node

  """

  hide: bool = ...

  inputs: typing.Union[NodeInputs, typing.Sequence[NodeSocket], typing.Mapping[str, NodeSocket], bpy_prop_collection] = ...

  internal_links: typing.Union[typing.Sequence[NodeLink], typing.Mapping[str, NodeLink], bpy_prop_collection] = ...

  """

  Internal input-to-output connections for muting

  """

  label: str = ...

  """

  Optional custom node label

  """

  location: typing.Tuple[float, float] = ...

  mute: bool = ...

  name: str = ...

  """

  Unique node identifier

  """

  outputs: typing.Union[NodeOutputs, typing.Sequence[NodeSocket], typing.Mapping[str, NodeSocket], bpy_prop_collection] = ...

  parent: Node = ...

  """

  Parent this node is attached to

  """

  select: bool = ...

  """

  Node selection state

  """

  show_options: bool = ...

  show_preview: bool = ...

  show_texture: bool = ...

  """

  Display node in viewport textured shading mode

  """

  type: str = ...

  """

  Node type (deprecated, use bl_static_type or bl_idname for the actual identifier string)

  * ``CUSTOM``
Custom -- Custom Node.

  """

  use_custom_color: bool = ...

  """

  Use custom color for the node

  """

  width: float = ...

  """

  Width of the node

  """

  width_hidden: float = ...

  """

  Width of the node in hidden state

  """

  def socket_value_update(self, context: Context) -> None:

    """

    Update after property changes

    """

    ...

  @classmethod

  def is_registered_node_type(cls) -> bool:

    """

    True if a registered node type

    """

    ...

  @classmethod

  def poll(cls, node_tree: NodeTree) -> bool:

    """

    If non-null output is returned, the node type can be added to the tree

    """

    ...

  def poll_instance(self, node_tree: NodeTree) -> bool:

    """

    If non-null output is returned, the node can be added to the tree

    """

    ...

  def update(self) -> None:

    """

    Update on node graph topology changes (adding or removing nodes and links)

    """

    ...

  def insert_link(self, link: NodeLink) -> None:

    """

    Handle creation of a link to or from the node

    """

    ...

  def init(self, context: Context) -> None:

    """

    Initialize a new instance of this node

    """

    ...

  def copy(self, node: Node) -> None:

    """

    Initialize a new instance of this node from an existing node

    """

    ...

  def free(self) -> None:

    """

    Clean up node on removal

    """

    ...

  def draw_buttons(self, context: Context, layout: UILayout) -> None:

    """

    Draw node buttons

    """

    ...

  def draw_buttons_ext(self, context: Context, layout: UILayout) -> None:

    """

    Draw node buttons in the sidebar

    """

    ...

  def draw_label(self) -> str:

    """

    Returns a dynamic label string

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class NodeInputs(bpy_struct):

  """

  Collection of Node Sockets

  """

  def new(self, type: str, name: str, identifier: str = '') -> NodeSocket:

    """

    Add a socket to this node

    """

    ...

  def remove(self, socket: NodeSocket) -> None:

    """

    Remove a socket from this node

    """

    ...

  def clear(self) -> None:

    """

    Remove all sockets from this node

    """

    ...

  def move(self, from_index: int, to_index: int) -> None:

    """

    Move a socket to another position

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class NodeInstanceHash(bpy_struct):

  """

  Hash table containing node instance data

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class NodeInternalSocketTemplate(bpy_struct):

  """

  Type and default value of a node socket

  """

  identifier: str = ...

  """

  Identifier of the socket

  """

  name: str = ...

  """

  Name of the socket

  """

  type: str = ...

  """

  Data type of the socket

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class NodeLink(bpy_struct):

  """

  Link is muted and can be ignored

  """

  from_node: Node = ...

  from_socket: NodeSocket = ...

  is_hidden: bool = ...

  """

  Link is hidden due to invisible sockets

  """

  is_muted: bool = ...

  is_valid: bool = ...

  to_node: Node = ...

  to_socket: NodeSocket = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class NodeLinks(bpy_struct):

  """

  Collection of Node Links

  """

  def new(self, input: NodeSocket, output: NodeSocket, verify_limits: bool = True) -> NodeLink:

    """

    Add a node link to this node tree

    """

    ...

  def remove(self, link: NodeLink) -> None:

    """

    remove a node link from the node tree

    """

    ...

  def clear(self) -> None:

    """

    remove all node links from the node tree

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class NodeOutputFileSlotFile(bpy_struct):

  """

  Single layer file slot of the file output node

  """

  format: ImageFormatSettings = ...

  path: str = ...

  """

  Subpath used for this slot

  """

  save_as_render: bool = ...

  """

  Apply render part of display transform when saving byte image

  """

  use_node_format: bool = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class NodeOutputFileSlotLayer(bpy_struct):

  """

  Multilayer slot of the file output node

  """

  name: str = ...

  """

  OpenEXR layer name used for this slot

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class NodeOutputs(bpy_struct):

  """

  Collection of Node Sockets

  """

  def new(self, type: str, name: str, identifier: str = '') -> NodeSocket:

    """

    Add a socket to this node

    """

    ...

  def remove(self, socket: NodeSocket) -> None:

    """

    Remove a socket from this node

    """

    ...

  def clear(self) -> None:

    """

    Remove all sockets from this node

    """

    ...

  def move(self, from_index: int, to_index: int) -> None:

    """

    Move a socket to another position

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Nodes(bpy_struct):

  """

  Collection of Nodes

  """

  active: Node = ...

  """

  Active node in this tree

  """

  def new(self, type: str) -> Node:

    """

    Add a node to this node tree

    """

    ...

  def remove(self, node: Node) -> None:

    """

    Remove a node from this node tree

    """

    ...

  def clear(self) -> None:

    """

    Remove all nodes from this node tree

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class NodeSocket(bpy_struct):

  """

  Input or output socket of a node

  """

  bl_idname: str = ...

  bl_label: str = ...

  """

  Label to display for the socket type in the UI

  """

  description: str = ...

  """

  Socket tooltip

  """

  display_shape: str = ...

  """

  Socket shape

  """

  enabled: bool = ...

  """

  Enable the socket

  """

  hide: bool = ...

  """

  Hide the socket

  """

  hide_value: bool = ...

  """

  Hide the socket input value

  """

  identifier: str = ...

  """

  Unique identifier for mapping sockets

  """

  is_linked: bool = ...

  """

  True if the socket is connected

  """

  is_multi_input: bool = ...

  """

  True if the socket can accept multiple ordered input links

  """

  is_output: bool = ...

  """

  True if the socket is an output, otherwise input

  """

  label: str = ...

  """

  Custom dynamic defined socket label

  """

  link_limit: int = ...

  """

  Max number of links allowed for this socket

  """

  name: str = ...

  """

  Socket name

  """

  node: Node = ...

  """

  Node owning this socket

  """

  show_expanded: bool = ...

  """

  Socket links are expanded in the user interface

  """

  type: str = ...

  """

  Data type

  """

  links: typing.Any = ...

  """

  List of node links from or to this socket.

  Note: Takes ``O(len(nodetree.links))`` time.

  (readonly)

  """

  def draw(self, context: Context, layout: UILayout, node: Node, text: str) -> None:

    """

    Draw socket

    """

    ...

  def draw_color(self, context: Context, node: Node) -> typing.Tuple[float, float, float, float]:

    """

    Color of the socket icon

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class NodeSocketInterface(bpy_struct):

  """

  Parameters to define node sockets

  """

  attribute_domain: str = ...

  """

  Attribute domain used by the geometry nodes modifier to create an attribute output

  * ``POINT``
Point -- Attribute on point.

  * ``EDGE``
Edge -- Attribute on mesh edge.

  * ``FACE``
Face -- Attribute on mesh faces.

  * ``CORNER``
Face Corner -- Attribute on mesh face corner.

  * ``CURVE``
Spline -- Attribute on spline.

  """

  bl_label: str = ...

  """

  Label to display for the socket type in the UI

  """

  bl_socket_idname: str = ...

  description: str = ...

  """

  Socket tooltip

  """

  hide_value: bool = ...

  """

  Hide the socket input value even when the socket is not connected

  """

  identifier: str = ...

  """

  Unique identifier for mapping sockets

  """

  is_output: bool = ...

  """

  True if the socket is an output, otherwise input

  """

  name: str = ...

  """

  Socket name

  """

  def draw(self, context: Context, layout: UILayout) -> None:

    """

    Draw template settings

    """

    ...

  def draw_color(self, context: Context) -> typing.Tuple[float, float, float, float]:

    """

    Color of the socket icon

    """

    ...

  def register_properties(self, data_rna_type: Struct) -> None:

    """

    Define RNA properties of a socket

    """

    ...

  def init_socket(self, node: Node, socket: NodeSocket, data_path: str) -> None:

    """

    Initialize a node socket instance

    """

    ...

  def from_socket(self, node: Node, socket: NodeSocket) -> None:

    """

    Setup template parameters from an existing socket

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class NodeTreeInputs(bpy_struct):

  """

  Collection of Node Tree Sockets

  """

  def new(self, type: str, name: str) -> NodeSocketInterface:

    """

    Add a socket to this node tree

    """

    ...

  def remove(self, socket: NodeSocketInterface) -> None:

    """

    Remove a socket from this node tree

    """

    ...

  def clear(self) -> None:

    """

    Remove all sockets from this node tree

    """

    ...

  def move(self, from_index: int, to_index: int) -> None:

    """

    Move a socket to another position

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class NodeTreeOutputs(bpy_struct):

  """

  Collection of Node Tree Sockets

  """

  def new(self, type: str, name: str) -> NodeSocketInterface:

    """

    Add a socket to this node tree

    """

    ...

  def remove(self, socket: NodeSocketInterface) -> None:

    """

    Remove a socket from this node tree

    """

    ...

  def clear(self) -> None:

    """

    Remove all sockets from this node tree

    """

    ...

  def move(self, from_index: int, to_index: int) -> None:

    """

    Move a socket to another position

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class NodeTreePath(bpy_struct):

  """

  Element of the node space tree path

  """

  node_tree: NodeTree = ...

  """

  Base node tree from context

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ObjectBase(bpy_struct):

  """

  An object instance in a render layer

  """

  hide_viewport: bool = ...

  """

  Temporarily hide in viewport

  """

  object: Object = ...

  """

  Object this base links to

  """

  select: bool = ...

  """

  Object base selection state

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ObjectConstraints(bpy_struct):

  """

  Collection of object constraints

  """

  active: Constraint = ...

  """

  Active Object constraint

  """

  def new(self, type: str) -> Constraint:

    """

    Add a new constraint to this object

    """

    ...

  def remove(self, constraint: Constraint) -> None:

    """

    Remove a constraint from this object

    """

    ...

  def clear(self) -> None:

    """

    Remove all constraint from this object

    """

    ...

  def move(self, from_index: int, to_index: int) -> None:

    """

    Move a constraint to a different position

    """

    ...

  def copy(self, constraint: Constraint) -> Constraint:

    """

    Add a new constraint that is a copy of the given one

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ObjectDisplay(bpy_struct):

  """

  Object display settings for 3D viewport

  """

  show_shadows: bool = ...

  """

  Object cast shadows in the 3D viewport

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ObjectGpencilModifiers(bpy_struct):

  """

  Collection of object grease pencil modifiers

  """

  def new(self, name: str, type: str) -> GpencilModifier:

    """

    Add a new greasepencil_modifier

    """

    ...

  def remove(self, greasepencil_modifier: GpencilModifier) -> None:

    """

    Remove an existing greasepencil_modifier from the object

    """

    ...

  def clear(self) -> None:

    """

    Remove all grease pencil modifiers from the object

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ObjectLineArt(bpy_struct):

  """

  Object line art settings

  """

  crease_threshold: float = ...

  """

  Angles smaller than this will be treated as creases

  """

  usage: str = ...

  """

  How to use this object in line art calculation

  * ``INHERIT``
Inherit -- Use settings from the parent collection.

  * ``INCLUDE``
Include -- Generate feature lines for this object's data.

  * ``OCCLUSION_ONLY``
Occlusion Only -- Only use the object data to produce occlusion.

  * ``EXCLUDE``
Exclude -- Don't use this object for Line Art rendering.

  * ``INTERSECTION_ONLY``
Intersection Only -- Only generate intersection lines for this collection.

  * ``NO_INTERSECTION``
No Intersection -- Include this object but do not generate intersection lines.

  """

  use_crease_override: bool = ...

  """

  Use this object's crease setting to overwrite scene global

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ObjectModifiers(bpy_struct):

  """

  Collection of object modifiers

  """

  active: Modifier = ...

  """

  The active modifier in the list

  """

  def new(self, name: str, type: str) -> Modifier:

    """

    Add a new modifier

    """

    ...

  def remove(self, modifier: Modifier) -> None:

    """

    Remove an existing modifier from the object

    """

    ...

  def clear(self) -> None:

    """

    Remove all modifiers from the object

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ObjectShaderFx(bpy_struct):

  """

  Collection of object effects

  """

  def new(self, name: str, type: str) -> ShaderFx:

    """

    Add a new shader fx

    """

    ...

  def remove(self, shader_fx: ShaderFx) -> None:

    """

    Remove an existing effect from the object

    """

    ...

  def clear(self) -> None:

    """

    Remove all effects from the object

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Operator(bpy_struct):

  """

  Storage of an operator being executed, or registered after execution

  """

  bl_cursor_pending: str = ...

  """

  Cursor to use when waiting for the user to select a location to activate the operator (when ``bl_options`` has ``DEPENDS_ON_CURSOR`` set)

  """

  bl_description: str = ...

  bl_idname: str = ...

  bl_label: str = ...

  bl_options: typing.Set[str] = ...

  """

  Options for this operator type

  * ``REGISTER``
Register -- Display in the info window and support the redo toolbar panel.

  * ``UNDO``
Undo -- Push an undo event (needed for operator redo).

  * ``UNDO_GROUPED``
Grouped Undo -- Push a single undo event for repeated instances of this operator.

  * ``BLOCKING``
Blocking -- Block anything else from using the cursor.

  * ``MACRO``
Macro -- Use to check if an operator is a macro.

  * ``GRAB_CURSOR``
Grab Pointer -- Use so the operator grabs the mouse focus, enables wrapping when continuous grab is enabled.

  * ``GRAB_CURSOR_X``
Grab Pointer X -- Grab, only warping the X axis.

  * ``GRAB_CURSOR_Y``
Grab Pointer Y -- Grab, only warping the Y axis.

  * ``DEPENDS_ON_CURSOR``
Depends on Cursor -- The initial cursor location is used, when running from a menus or buttons the user is prompted to place the cursor before beginning the operation.

  * ``PRESET``
Preset -- Display a preset button with the operators settings.

  * ``INTERNAL``
Internal -- Removes the operator from search results.

  """

  bl_translation_context: str = ...

  bl_undo_group: str = ...

  has_reports: bool = ...

  """

  Operator has a set of reports (warnings and errors) from last execution

  """

  layout: UILayout = ...

  macros: typing.Union[typing.Sequence[Macro], typing.Mapping[str, Macro], bpy_prop_collection] = ...

  name: str = ...

  options: OperatorOptions = ...

  """

  Runtime options

  """

  properties: OperatorProperties = ...

  bl_property: typing.Any = ...

  """

  The name of a property to use as this operators primary property.
Currently this is only used to select the default property when
expanding an operator into a menu.
:type: string

  """

  def report(self, type: typing.Set[str], message: str) -> None:

    """

    report

    """

    ...

  def is_repeat(self) -> bool:

    """

    is_repeat

    """

    ...

  @classmethod

  def poll(cls, context: Context) -> bool:

    """

    Test if the operator can be called or not

    """

    ...

  def execute(self, context: Context) -> typing.Set[str]:

    """

    Execute the operator

    """

    ...

  def check(self, context: Context) -> bool:

    """

    Check the operator settings, return True to signal a change to redraw

    """

    ...

  def invoke(self, context: Context, event: Event) -> typing.Set[str]:

    """

    Invoke the operator

    """

    ...

  def modal(self, context: Context, event: Event) -> typing.Set[str]:

    """

    Modal operator function

    """

    ...

  def draw(self, context: Context) -> None:

    """

    Draw function for the operator

    """

    ...

  def cancel(self, context: Context) -> None:

    """

    Called when the operator is canceled

    """

    ...

  @classmethod

  def description(cls, context: Context, properties: OperatorProperties) -> str:

    """

    Compute a description string that depends on parameters

    """

    ...

  def as_keywords(self, *args, ignore: typing.Any = ()) -> None:

    """

    Return a copy of the properties as a dictionary

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

  def poll_message_set(self, message: str, *args) -> None:

    """

    Set the message to show in the tool-tip when poll fails.

    When message is callable, additional user defined positional arguments are passed to the message function.

    """

    ...

class OperatorMacro(bpy_struct):

  """

  Storage of a sub operator in a macro after it has been added

  """

  properties: OperatorProperties = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class OperatorOptions(bpy_struct):

  """

  Runtime options

  """

  is_grab_cursor: bool = ...

  """

  True when the cursor is grabbed

  """

  is_invoke: bool = ...

  """

  True when invoked (even if only the execute callbacks available)

  """

  is_repeat: bool = ...

  """

  True when run from the 'Adjust Last Operation' panel

  """

  is_repeat_last: bool = ...

  """

  True when run from the operator 'Repeat Last'

  """

  use_cursor_region: bool = ...

  """

  Enable to use the region under the cursor for modal execution

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class OperatorProperties(bpy_struct):

  """

  Input properties of an operator

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class PackedFile(bpy_struct):

  """

  External file packed into the .blend file

  """

  data: str = ...

  """

  Raw data (bytes, exact content of the embedded file)

  """

  size: int = ...

  """

  Size of packed file in bytes

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Paint(bpy_struct):

  brush: Brush = ...

  """

  Active Brush

  """

  cavity_curve: CurveMapping = ...

  """

  Editable cavity curve

  """

  input_samples: int = ...

  """

  Average multiple input samples together to smooth the brush stroke

  """

  palette: Palette = ...

  """

  Active Palette

  """

  show_brush: bool = ...

  show_brush_on_surface: bool = ...

  show_low_resolution: bool = ...

  """

  For multires, show low resolution while navigating the view

  """

  tile_offset: typing.Tuple[float, float, float] = ...

  """

  Stride at which tiled strokes are copied

  """

  tile_x: bool = ...

  """

  Tile along X axis

  """

  tile_y: bool = ...

  """

  Tile along Y axis

  """

  tile_z: bool = ...

  """

  Tile along Z axis

  """

  tool_slots: typing.Union[typing.Sequence[PaintToolSlot], typing.Mapping[str, PaintToolSlot], bpy_prop_collection] = ...

  use_cavity: bool = ...

  """

  Mask painting according to mesh geometry cavity

  """

  use_sculpt_delay_updates: bool = ...

  """

  Update the geometry when it enters the view, providing faster view navigation

  """

  use_symmetry_feather: bool = ...

  """

  Reduce the strength of the brush where it overlaps symmetrical daubs

  """

  use_symmetry_x: bool = ...

  """

  Mirror brush across the X axis

  """

  use_symmetry_y: bool = ...

  """

  Mirror brush across the Y axis

  """

  use_symmetry_z: bool = ...

  """

  Mirror brush across the Z axis

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class PaintToolSlot(bpy_struct):

  brush: Brush = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class PaletteColor(bpy_struct):

  color: typing.Tuple[float, float, float] = ...

  strength: float = ...

  weight: float = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class PaletteColors(bpy_struct):

  """

  Collection of palette colors

  """

  active: PaletteColor = ...

  def new(self) -> PaletteColor:

    """

    Add a new color to the palette

    """

    ...

  def remove(self, color: PaletteColor) -> None:

    """

    Remove a color from the palette

    """

    ...

  def clear(self) -> None:

    """

    Remove all colors from the palette

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Panel(bpy_struct):

  """

  Panel containing UI elements

  """

  bl_category: str = ...

  """

  The category (tab) in which the panel will be displayed, when applicable

  """

  bl_context: str = ...

  """

  The context in which the panel belongs to. (TODO: explain the possible combinations bl_context/bl_region_type/bl_space_type)

  """

  bl_description: str = ...

  """

  The panel tooltip

  """

  bl_idname: str = ...

  """

  If this is set, the panel gets a custom ID, otherwise it takes the name of the class used to define the panel. For example, if the class name is "OBJECT_PT_hello", and bl_idname is not set by the script, then bl_idname = "OBJECT_PT_hello"

  """

  bl_label: str = ...

  """

  The panel label, shows up in the panel header at the right of the triangle used to collapse the panel

  """

  bl_options: typing.Set[str] = ...

  """

  Options for this panel type

  * ``DEFAULT_CLOSED``
Default Closed -- Defines if the panel has to be open or collapsed at the time of its creation.

  * ``HIDE_HEADER``
Hide Header -- If set to False, the panel shows a header, which contains a clickable arrow to collapse the panel and the label (see bl_label).

  * ``INSTANCED``
Instanced Panel -- Multiple panels with this type can be used as part of a list depending on data external to the UI. Used to create panels for the modifiers and other stacks.

  * ``HEADER_LAYOUT_EXPAND``
Expand Header Layout -- Allow buttons in the header to stretch and shrink to fill the entire layout width.

  """

  bl_order: int = ...

  """

  Panels with lower numbers are default ordered before panels with higher numbers

  """

  bl_owner_id: str = ...

  """

  The ID owning the data displayed in the panel, if any

  """

  bl_parent_id: str = ...

  """

  If this is set, the panel becomes a sub-panel

  """

  bl_region_type: str = ...

  """

  The region where the panel is going to be used in

  """

  bl_space_type: str = ...

  """

  The space where the panel is going to be used in

  * ``EMPTY``
Empty.

  * ``VIEW_3D``
3D Viewport -- Manipulate objects in a 3D environment.

  * ``IMAGE_EDITOR``
UV/Image Editor -- View and edit images and UV Maps.

  * ``NODE_EDITOR``
Node Editor -- Editor for node-based shading and compositing tools.

  * ``SEQUENCE_EDITOR``
Video Sequencer -- Video editing tools.

  * ``CLIP_EDITOR``
Movie Clip Editor -- Motion tracking tools.

  * ``DOPESHEET_EDITOR``
Dope Sheet -- Adjust timing of keyframes.

  * ``GRAPH_EDITOR``
Graph Editor -- Edit drivers and keyframe interpolation.

  * ``NLA_EDITOR``
Nonlinear Animation -- Combine and layer Actions.

  * ``TEXT_EDITOR``
Text Editor -- Edit scripts and in-file documentation.

  * ``CONSOLE``
Python Console -- Interactive programmatic console for advanced editing and script development.

  * ``INFO``
Info -- Log of operations, warnings and error messages.

  * ``TOPBAR``
Top Bar -- Global bar at the top of the screen for global per-window settings.

  * ``STATUSBAR``
Status Bar -- Global bar at the bottom of the screen for general status information.

  * ``OUTLINER``
Outliner -- Overview of scene graph and all available data-blocks.

  * ``PROPERTIES``
Properties -- Edit properties of active object and related data-blocks.

  * ``FILE_BROWSER``
File Browser -- Browse for files and assets.

  * ``SPREADSHEET``
Spreadsheet -- Explore geometry data in a table.

  * ``PREFERENCES``
Preferences -- Edit persistent configuration settings.

  """

  bl_translation_context: str = ...

  """

  Specific translation context, only define when the label needs to be disambiguated from others using the exact same label

  """

  bl_ui_units_x: int = ...

  """

  When set, defines popup panel width

  """

  custom_data: Constraint = ...

  """

  Panel data

  """

  is_popover: bool = ...

  layout: UILayout = ...

  """

  Defines the structure of the panel in the UI

  """

  text: str = ...

  """

  XXX todo

  """

  use_pin: bool = ...

  """

  Show the panel on all tabs

  """

  @classmethod

  def poll(cls, context: Context) -> bool:

    """

    If this method returns a non-null output, then the panel can be drawn

    """

    ...

  def draw(self, context: Context) -> None:

    """

    Draw UI elements into the panel UI layout

    """

    ...

  def draw_header(self, context: Context) -> None:

    """

    Draw UI elements into the panel's header UI layout

    """

    ...

  def draw_header_preset(self, context: Context) -> None:

    """

    Draw UI elements for presets in the panel's header

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Particle(bpy_struct):

  """

  Particle in a particle system

  """

  alive_state: str = ...

  angular_velocity: typing.Tuple[float, float, float] = ...

  birth_time: float = ...

  die_time: float = ...

  hair_keys: typing.Union[typing.Sequence[ParticleHairKey], typing.Mapping[str, ParticleHairKey], bpy_prop_collection] = ...

  is_exist: bool = ...

  is_visible: bool = ...

  lifetime: float = ...

  location: typing.Tuple[float, float, float] = ...

  particle_keys: typing.Union[typing.Sequence[ParticleKey], typing.Mapping[str, ParticleKey], bpy_prop_collection] = ...

  prev_angular_velocity: typing.Tuple[float, float, float] = ...

  prev_location: typing.Tuple[float, float, float] = ...

  prev_rotation: typing.Tuple[float, float, float, float] = ...

  prev_velocity: typing.Tuple[float, float, float] = ...

  rotation: typing.Tuple[float, float, float, float] = ...

  size: float = ...

  velocity: typing.Tuple[float, float, float] = ...

  def uv_on_emitter(self, modifier: ParticleSystemModifier) -> typing.Tuple[float, float]:

    """

    Obtain UV coordinates for a particle on an evaluated mesh.

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ParticleBrush(bpy_struct):

  """

  Particle editing brush

  """

  count: int = ...

  """

  Particle count

  """

  curve: CurveMapping = ...

  length_mode: str = ...

  """

  * ``GROW``
Grow -- Make hairs longer.

  * ``SHRINK``
Shrink -- Make hairs shorter.

  """

  puff_mode: str = ...

  """

  * ``ADD``
Add -- Make hairs more puffy.

  * ``SUB``
Sub -- Make hairs less puffy.

  """

  size: int = ...

  """

  Radius of the brush in pixels

  """

  steps: int = ...

  """

  Brush steps

  """

  strength: float = ...

  """

  Brush strength

  """

  use_puff_volume: bool = ...

  """

  Apply puff to unselected end-points (helps maintain hair volume when puffing root)

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ParticleDupliWeight(bpy_struct):

  """

  Weight of a particle instance object in a collection

  """

  count: int = ...

  """

  The number of times this object is repeated with respect to other objects

  """

  name: str = ...

  """

  Particle instance object name

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ParticleEdit(bpy_struct):

  """

  Properties of particle editing mode

  """

  brush: ParticleBrush = ...

  default_key_count: int = ...

  """

  How many keys to make new particles with

  """

  display_step: int = ...

  """

  How many steps to display the path with

  """

  emitter_distance: float = ...

  """

  Distance to keep particles away from the emitter

  """

  fade_frames: int = ...

  """

  How many frames to fade

  """

  is_editable: bool = ...

  """

  A valid edit mode exists

  """

  is_hair: bool = ...

  """

  Editing hair

  """

  object: Object = ...

  """

  The edited object

  """

  select_mode: str = ...

  """

  Particle select and display mode

  * ``PATH``
Path -- Path edit mode.

  * ``POINT``
Point -- Point select mode.

  * ``TIP``
Tip -- Tip select mode.

  """

  shape_object: Object = ...

  """

  Outer shape to use for tools

  """

  show_particles: bool = ...

  """

  Display actual particles

  """

  tool: str = ...

  """

  * ``COMB``
Comb -- Comb hairs.

  * ``SMOOTH``
Smooth -- Smooth hairs.

  * ``ADD``
Add -- Add hairs.

  * ``LENGTH``
Length -- Make hairs longer or shorter.

  * ``PUFF``
Puff -- Make hairs stand up.

  * ``CUT``
Cut -- Cut hairs.

  * ``WEIGHT``
Weight -- Weight hair particles.

  """

  type: str = ...

  use_auto_velocity: bool = ...

  """

  Calculate point velocities automatically

  """

  use_default_interpolate: bool = ...

  """

  Interpolate new particles from the existing ones

  """

  use_emitter_deflect: bool = ...

  """

  Keep paths from intersecting the emitter

  """

  use_fade_time: bool = ...

  """

  Fade paths and keys further away from current frame

  """

  use_preserve_length: bool = ...

  """

  Keep path lengths constant

  """

  use_preserve_root: bool = ...

  """

  Keep root keys unmodified

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ParticleHairKey(bpy_struct):

  """

  Particle key for hair particle system

  """

  co: typing.Tuple[float, float, float] = ...

  """

  Location of the hair key in object space

  """

  co_local: typing.Tuple[float, float, float] = ...

  """

  Location of the hair key in its local coordinate system, relative to the emitting face

  """

  time: float = ...

  """

  Relative time of key over hair length

  """

  weight: float = ...

  """

  Weight for cloth simulation

  """

  def co_object(self, object: Object, modifier: ParticleSystemModifier, particle: Particle) -> typing.Tuple[float, float, float]:

    """

    Obtain hairkey location with particle and modifier data

    """

    ...

  def co_object_set(self, object: Object, modifier: ParticleSystemModifier, particle: Particle, co: typing.Tuple[float, float, float]) -> None:

    """

    Set hairkey location with particle and modifier data

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ParticleKey(bpy_struct):

  """

  Key location for a particle over time

  """

  angular_velocity: typing.Tuple[float, float, float] = ...

  """

  Key angular velocity

  """

  location: typing.Tuple[float, float, float] = ...

  """

  Key location

  """

  rotation: typing.Tuple[float, float, float, float] = ...

  """

  Key rotation quaternion

  """

  time: float = ...

  """

  Time of key over the simulation

  """

  velocity: typing.Tuple[float, float, float] = ...

  """

  Key velocity

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ParticleSettingsTextureSlots(bpy_struct):

  """

  Collection of texture slots

  """

  @classmethod

  def add(cls) -> ParticleSettingsTextureSlot:

    """

    add

    """

    ...

  @classmethod

  def create(cls, index: int) -> ParticleSettingsTextureSlot:

    """

    create

    """

    ...

  @classmethod

  def clear(cls, index: int) -> None:

    """

    clear

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ParticleSystem(bpy_struct):

  """

  Particle system in an object

  """

  active_particle_target: ParticleTarget = ...

  active_particle_target_index: int = ...

  child_particles: typing.Union[typing.Sequence[ChildParticle], typing.Mapping[str, ChildParticle], bpy_prop_collection] = ...

  """

  Child particles generated by the particle system

  """

  child_seed: int = ...

  """

  Offset in the random number table for child particles, to get a different randomized result

  """

  cloth: ClothModifier = ...

  """

  Cloth dynamics for hair

  """

  dt_frac: float = ...

  """

  The current simulation time step size, as a fraction of a frame

  """

  has_multiple_caches: bool = ...

  """

  Particle system has multiple point caches

  """

  invert_vertex_group_clump: bool = ...

  """

  Negate the effect of the clump vertex group

  """

  invert_vertex_group_density: bool = ...

  """

  Negate the effect of the density vertex group

  """

  invert_vertex_group_field: bool = ...

  """

  Negate the effect of the field vertex group

  """

  invert_vertex_group_kink: bool = ...

  """

  Negate the effect of the kink vertex group

  """

  invert_vertex_group_length: bool = ...

  """

  Negate the effect of the length vertex group

  """

  invert_vertex_group_rotation: bool = ...

  """

  Negate the effect of the rotation vertex group

  """

  invert_vertex_group_roughness_1: bool = ...

  """

  Negate the effect of the roughness 1 vertex group

  """

  invert_vertex_group_roughness_2: bool = ...

  """

  Negate the effect of the roughness 2 vertex group

  """

  invert_vertex_group_roughness_end: bool = ...

  """

  Negate the effect of the roughness end vertex group

  """

  invert_vertex_group_size: bool = ...

  """

  Negate the effect of the size vertex group

  """

  invert_vertex_group_tangent: bool = ...

  """

  Negate the effect of the tangent vertex group

  """

  invert_vertex_group_twist: bool = ...

  """

  Negate the effect of the twist vertex group

  """

  invert_vertex_group_velocity: bool = ...

  """

  Negate the effect of the velocity vertex group

  """

  is_editable: bool = ...

  """

  Particle system can be edited in particle mode

  """

  is_edited: bool = ...

  """

  Particle system has been edited in particle mode

  """

  is_global_hair: bool = ...

  """

  Hair keys are in global coordinate space

  """

  name: str = ...

  """

  Particle system name

  """

  parent: Object = ...

  """

  Use this object's coordinate system instead of global coordinate system

  """

  particles: typing.Union[typing.Sequence[Particle], typing.Mapping[str, Particle], bpy_prop_collection] = ...

  """

  Particles generated by the particle system

  """

  point_cache: PointCache = ...

  reactor_target_object: Object = ...

  """

  For reactor systems, the object that has the target particle system (empty if same object)

  """

  reactor_target_particle_system: int = ...

  """

  For reactor systems, index of particle system on the target object

  """

  seed: int = ...

  """

  Offset in the random number table, to get a different randomized result

  """

  settings: ParticleSettings = ...

  """

  Particle system settings

  """

  targets: typing.Union[typing.Sequence[ParticleTarget], typing.Mapping[str, ParticleTarget], bpy_prop_collection] = ...

  """

  Target particle systems

  """

  use_hair_dynamics: bool = ...

  """

  Enable hair dynamics using cloth simulation

  """

  use_keyed_timing: bool = ...

  """

  Use key times

  """

  vertex_group_clump: str = ...

  """

  Vertex group to control clump

  """

  vertex_group_density: str = ...

  """

  Vertex group to control density

  """

  vertex_group_field: str = ...

  """

  Vertex group to control field

  """

  vertex_group_kink: str = ...

  """

  Vertex group to control kink

  """

  vertex_group_length: str = ...

  """

  Vertex group to control length

  """

  vertex_group_rotation: str = ...

  """

  Vertex group to control rotation

  """

  vertex_group_roughness_1: str = ...

  """

  Vertex group to control roughness 1

  """

  vertex_group_roughness_2: str = ...

  """

  Vertex group to control roughness 2

  """

  vertex_group_roughness_end: str = ...

  """

  Vertex group to control roughness end

  """

  vertex_group_size: str = ...

  """

  Vertex group to control size

  """

  vertex_group_tangent: str = ...

  """

  Vertex group to control tangent

  """

  vertex_group_twist: str = ...

  """

  Vertex group to control twist

  """

  vertex_group_velocity: str = ...

  """

  Vertex group to control velocity

  """

  def co_hair(self, object: Object, particle_no: int = 0, step: int = 0) -> typing.Tuple[float, float, float]:

    """

    Obtain cache hair data

    """

    ...

  def uv_on_emitter(self, modifier: ParticleSystemModifier, particle: Particle, particle_no: int = 0, uv_no: int = 0) -> typing.Tuple[float, float]:

    """

    Obtain uv for all particles

    """

    ...

  def mcol_on_emitter(self, modifier: ParticleSystemModifier, particle: Particle, particle_no: int = 0, vcol_no: int = 0) -> typing.Tuple[float, float, float]:

    """

    Obtain mcol for all particles

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ParticleSystems(bpy_struct):

  """

  Collection of particle systems

  """

  active: ParticleSystem = ...

  """

  Active particle system being displayed

  """

  active_index: int = ...

  """

  Index of active particle system slot

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ParticleTarget(bpy_struct):

  """

  Target particle system

  """

  alliance: str = ...

  duration: float = ...

  is_valid: bool = ...

  """

  Keyed particles target is valid

  """

  name: str = ...

  """

  Particle target name

  """

  object: Object = ...

  """

  The object that has the target particle system (empty if same object)

  """

  system: int = ...

  """

  The index of particle system on the target object

  """

  time: float = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class PathCompare(bpy_struct):

  """

  Match paths against this value

  """

  path: str = ...

  use_glob: bool = ...

  """

  Enable wildcard globbing

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class PathCompareCollection(bpy_struct):

  """

  Collection of paths

  """

  @classmethod

  def new(cls) -> PathCompare:

    """

    Add a new path

    """

    ...

  @classmethod

  def remove(cls, pathcmp: PathCompare) -> None:

    """

    Remove path

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class PointCache(bpy_struct):

  """

  Active point cache for physics simulations

  """

  compression: str = ...

  """

  Compression method to be used

  * ``NO``
None -- No compression.

  * ``LIGHT``
Lite -- Fast but not so effective compression.

  * ``HEAVY``
Heavy -- Effective but slow compression.

  """

  filepath: str = ...

  """

  Cache file path

  """

  frame_end: int = ...

  """

  Frame on which the simulation stops

  """

  frame_start: int = ...

  """

  Frame on which the simulation starts

  """

  frame_step: int = ...

  """

  Number of frames between cached frames

  """

  index: int = ...

  """

  Index number of cache files

  """

  info: str = ...

  """

  Info on current cache status

  """

  is_baked: bool = ...

  """

  The cache is baked

  """

  is_baking: bool = ...

  """

  The cache is being baked

  """

  is_frame_skip: bool = ...

  """

  Some frames were skipped while baking/saving that cache

  """

  is_outdated: bool = ...

  name: str = ...

  """

  Cache name

  """

  point_caches: typing.Union[PointCaches, typing.Sequence[PointCacheItem], typing.Mapping[str, PointCacheItem], bpy_prop_collection] = ...

  use_disk_cache: bool = ...

  """

  Save cache files to disk (.blend file must be saved first)

  """

  use_external: bool = ...

  """

  Read cache from an external location

  """

  use_library_path: bool = ...

  """

  Use this file's path for the disk cache when library linked into another file (for local bakes per scene file, disable this option)

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class PointCacheItem(bpy_struct):

  """

  Point cache for physics simulations

  """

  compression: str = ...

  """

  Compression method to be used

  * ``NO``
None -- No compression.

  * ``LIGHT``
Lite -- Fast but not so effective compression.

  * ``HEAVY``
Heavy -- Effective but slow compression.

  """

  filepath: str = ...

  """

  Cache file path

  """

  frame_end: int = ...

  """

  Frame on which the simulation stops

  """

  frame_start: int = ...

  """

  Frame on which the simulation starts

  """

  frame_step: int = ...

  """

  Number of frames between cached frames

  """

  index: int = ...

  """

  Index number of cache files

  """

  info: str = ...

  """

  Info on current cache status

  """

  is_baked: bool = ...

  """

  The cache is baked

  """

  is_baking: bool = ...

  """

  The cache is being baked

  """

  is_frame_skip: bool = ...

  """

  Some frames were skipped while baking/saving that cache

  """

  is_outdated: bool = ...

  name: str = ...

  """

  Cache name

  """

  use_disk_cache: bool = ...

  """

  Save cache files to disk (.blend file must be saved first)

  """

  use_external: bool = ...

  """

  Read cache from an external location

  """

  use_library_path: bool = ...

  """

  Use this file's path for the disk cache when library linked into another file (for local bakes per scene file, disable this option)

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class PointCaches(bpy_struct):

  """

  Collection of point caches

  """

  active_index: int = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class PolygonFloatProperties(bpy_struct):

  """

  Collection of float properties

  """

  def new(self, name: str = 'Float Prop') -> MeshPolygonFloatPropertyLayer:

    """

    Add a float property layer to Mesh

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class PolygonIntProperties(bpy_struct):

  """

  Collection of int properties

  """

  def new(self, name: str = 'Int Prop') -> MeshPolygonIntPropertyLayer:

    """

    Add a integer property layer to Mesh

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class PolygonStringProperties(bpy_struct):

  """

  Collection of string properties

  """

  def new(self, name: str = 'String Prop') -> MeshPolygonStringPropertyLayer:

    """

    Add a string property layer to Mesh

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Pose(bpy_struct):

  """

  A collection of pose channels, including settings for animating bones

  """

  animation_visualization: AnimViz = ...

  """

  Animation data for this data-block

  """

  bone_groups: typing.Union[BoneGroups, typing.Sequence[BoneGroup], typing.Mapping[str, BoneGroup], bpy_prop_collection] = ...

  """

  Groups of the bones

  """

  bones: typing.Union[typing.Sequence[PoseBone], typing.Mapping[str, PoseBone], bpy_prop_collection] = ...

  """

  Individual pose bones for the armature

  """

  ik_param: IKParam = ...

  """

  Parameters for IK solver

  """

  ik_solver: str = ...

  """

  Selection of IK solver for IK chain

  * ``LEGACY``
Standard -- Original IK solver.

  * ``ITASC``
iTaSC -- Multi constraint, stateful IK solver.

  """

  use_auto_ik: bool = ...

  """

  Add temporary IK constraints while grabbing bones in Pose Mode

  """

  use_mirror_relative: bool = ...

  """

  Apply relative transformations in X-mirror mode (not supported with Auto IK)

  """

  use_mirror_x: bool = ...

  """

  Apply changes to matching bone on opposite side of X-Axis

  """

  @classmethod

  def apply_pose_from_action(cls, action: Action, evaluation_time: float = 0.0) -> None:

    """

    Apply the given action to this pose by evaluating it at a specific time. Only updates the pose of selected bones, or all bones if none are selected.

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class PoseBone(bpy_struct):

  """

  Channel defining pose data for a bone in a Pose

  """

  bbone_curveinx: float = ...

  """

  X-axis handle offset for start of the B-Bone's curve, adjusts curvature

  """

  bbone_curveinz: float = ...

  """

  Z-axis handle offset for start of the B-Bone's curve, adjusts curvature

  """

  bbone_curveoutx: float = ...

  """

  X-axis handle offset for end of the B-Bone's curve, adjusts curvature

  """

  bbone_curveoutz: float = ...

  """

  Z-axis handle offset for end of the B-Bone's curve, adjusts curvature

  """

  bbone_custom_handle_end: PoseBone = ...

  """

  Bone that serves as the end handle for the B-Bone curve

  """

  bbone_custom_handle_start: PoseBone = ...

  """

  Bone that serves as the start handle for the B-Bone curve

  """

  bbone_easein: float = ...

  """

  Length of first Bezier Handle (for B-Bones only)

  """

  bbone_easeout: float = ...

  """

  Length of second Bezier Handle (for B-Bones only)

  """

  bbone_rollin: float = ...

  """

  Roll offset for the start of the B-Bone, adjusts twist

  """

  bbone_rollout: float = ...

  """

  Roll offset for the end of the B-Bone, adjusts twist

  """

  bbone_scalein: typing.Tuple[float, float, float] = ...

  """

  Scale factors for the start of the B-Bone, adjusts thickness (for tapering effects)

  """

  bbone_scaleout: typing.Tuple[float, float, float] = ...

  """

  Scale factors for the end of the B-Bone, adjusts thickness (for tapering effects)

  """

  bone: Bone = ...

  """

  Bone associated with this PoseBone

  """

  bone_group: BoneGroup = ...

  """

  Bone group this pose channel belongs to

  """

  bone_group_index: int = ...

  """

  Bone group this pose channel belongs to (0 means no group)

  """

  child: PoseBone = ...

  """

  Child of this pose bone

  """

  constraints: typing.Union[PoseBoneConstraints, typing.Sequence[Constraint], typing.Mapping[str, Constraint], bpy_prop_collection] = ...

  """

  Constraints that act on this pose channel

  """

  custom_shape: Object = ...

  """

  Object that defines custom display shape for this bone

  """

  custom_shape_rotation_euler: typing.Tuple[float, float, float] = ...

  """

  Adjust the rotation of the custom shape

  """

  custom_shape_scale_xyz: typing.Tuple[float, float, float] = ...

  """

  Adjust the size of the custom shape

  """

  custom_shape_transform: PoseBone = ...

  """

  Bone that defines the display transform of this custom shape

  """

  custom_shape_translation: typing.Tuple[float, float, float] = ...

  """

  Adjust the location of the custom shape

  """

  head: typing.Tuple[float, float, float] = ...

  """

  Location of head of the channel's bone

  """

  ik_linear_weight: float = ...

  """

  Weight of scale constraint for IK

  """

  ik_max_x: float = ...

  """

  Maximum angles for IK Limit

  """

  ik_max_y: float = ...

  """

  Maximum angles for IK Limit

  """

  ik_max_z: float = ...

  """

  Maximum angles for IK Limit

  """

  ik_min_x: float = ...

  """

  Minimum angles for IK Limit

  """

  ik_min_y: float = ...

  """

  Minimum angles for IK Limit

  """

  ik_min_z: float = ...

  """

  Minimum angles for IK Limit

  """

  ik_rotation_weight: float = ...

  """

  Weight of rotation constraint for IK

  """

  ik_stiffness_x: float = ...

  """

  IK stiffness around the X axis

  """

  ik_stiffness_y: float = ...

  """

  IK stiffness around the Y axis

  """

  ik_stiffness_z: float = ...

  """

  IK stiffness around the Z axis

  """

  ik_stretch: float = ...

  """

  Allow scaling of the bone for IK

  """

  is_in_ik_chain: bool = ...

  """

  Is part of an IK chain

  """

  length: float = ...

  """

  Length of the bone

  """

  location: typing.Tuple[float, float, float] = ...

  lock_ik_x: bool = ...

  """

  Disallow movement around the X axis

  """

  lock_ik_y: bool = ...

  """

  Disallow movement around the Y axis

  """

  lock_ik_z: bool = ...

  """

  Disallow movement around the Z axis

  """

  lock_location: typing.Tuple[bool, bool, bool] = ...

  """

  Lock editing of location when transforming

  """

  lock_rotation: typing.Tuple[bool, bool, bool] = ...

  """

  Lock editing of rotation when transforming

  """

  lock_rotation_w: bool = ...

  """

  Lock editing of 'angle' component of four-component rotations when transforming

  """

  lock_rotations_4d: bool = ...

  """

  Lock editing of four component rotations by components (instead of as Eulers)

  """

  lock_scale: typing.Tuple[bool, bool, bool] = ...

  """

  Lock editing of scale when transforming

  """

  matrix: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]] = ...

  """

  Final 4x4 matrix after constraints and drivers are applied (object space)

  """

  matrix_basis: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]] = ...

  """

  Alternative access to location/scale/rotation relative to the parent and own rest bone

  """

  matrix_channel: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]] = ...

  """

  4x4 matrix, before constraints

  """

  motion_path: MotionPath = ...

  """

  Motion Path for this element

  """

  name: str = ...

  parent: PoseBone = ...

  """

  Parent of this pose bone

  """

  rotation_axis_angle: typing.Tuple[float, float, float, float] = ...

  """

  Angle of Rotation for Axis-Angle rotation representation

  """

  rotation_euler: typing.Tuple[float, float, float] = ...

  """

  Rotation in Eulers

  """

  rotation_mode: str = ...

  """

  * ``QUATERNION``
Quaternion (WXYZ) -- No Gimbal Lock.

  * ``XYZ``
XYZ Euler -- XYZ Rotation Order - prone to Gimbal Lock (default).

  * ``XZY``
XZY Euler -- XZY Rotation Order - prone to Gimbal Lock.

  * ``YXZ``
YXZ Euler -- YXZ Rotation Order - prone to Gimbal Lock.

  * ``YZX``
YZX Euler -- YZX Rotation Order - prone to Gimbal Lock.

  * ``ZXY``
ZXY Euler -- ZXY Rotation Order - prone to Gimbal Lock.

  * ``ZYX``
ZYX Euler -- ZYX Rotation Order - prone to Gimbal Lock.

  * ``AXIS_ANGLE``
Axis Angle -- Axis Angle (W+XYZ), defines a rotation around some axis defined by 3D-Vector.

  """

  rotation_quaternion: typing.Tuple[float, float, float, float] = ...

  """

  Rotation in Quaternions

  """

  scale: typing.Tuple[float, float, float] = ...

  tail: typing.Tuple[float, float, float] = ...

  """

  Location of tail of the channel's bone

  """

  use_custom_shape_bone_size: bool = ...

  """

  Scale the custom object by the bone length

  """

  use_ik_limit_x: bool = ...

  """

  Limit movement around the X axis

  """

  use_ik_limit_y: bool = ...

  """

  Limit movement around the Y axis

  """

  use_ik_limit_z: bool = ...

  """

  Limit movement around the Z axis

  """

  use_ik_linear_control: bool = ...

  """

  Apply channel size as IK constraint if stretching is enabled

  """

  use_ik_rotation_control: bool = ...

  """

  Apply channel rotation as IK constraint

  """

  basename: typing.Any = ...

  """

  The name of this bone before any '.' character

  (readonly)

  """

  center: typing.Any = ...

  """

  The midpoint between the head and the tail.

  (readonly)

  """

  children: typing.Any = ...

  """

  (readonly)

  """

  children_recursive: typing.Any = ...

  """

  A list of all children from this bone.

    Note: Takes ``O(len(bones)**2)`` time.

  (readonly)

  """

  children_recursive_basename: typing.Any = ...

  """

  Returns a chain of children with the same base name as this bone.
Only direct chains are supported, forks caused by multiple children
with matching base names will terminate the function
and not be returned.

  Note: Takes ``O(len(bones)**2)`` time.

  (readonly)

  """

  parent_recursive: typing.Any = ...

  """

  A list of parents, starting with the immediate parent

  (readonly)

  """

  vector: typing.Any = ...

  """

  The direction this bone is pointing.
Utility function for (tail - head)

  (readonly)

  """

  x_axis: typing.Any = ...

  """

  Vector pointing down the x-axis of the bone.

  (readonly)

  """

  y_axis: typing.Any = ...

  """

  Vector pointing down the y-axis of the bone.

  (readonly)

  """

  z_axis: typing.Any = ...

  """

  Vector pointing down the z-axis of the bone.

  (readonly)

  """

  def evaluate_envelope(self, point: typing.Tuple[float, float, float]) -> float:

    """

    Calculate bone envelope at given point

    """

    ...

  def bbone_segment_matrix(self, index: int, rest: bool = False) -> typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]]:

    """

    Retrieve the matrix of the joint between B-Bone segments if available

    """

    ...

  def compute_bbone_handles(self, rest: bool = False, ease: bool = False, offsets: bool = False) -> None:

    """

    Retrieve the vectors and rolls coming from B-Bone custom handles

    """

    ...

  def parent_index(self, parent_test: typing.Any) -> None:

    """

    The same as 'bone in other_bone.parent_recursive'
but saved generating a list.

    """

    ...

  def translate(self, vec: typing.Any) -> None:

    """

    Utility function to add *vec* to the head and tail of this bone

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class PoseBoneConstraints(bpy_struct):

  """

  Collection of pose bone constraints

  """

  active: Constraint = ...

  """

  Active PoseChannel constraint

  """

  def new(self, type: str) -> Constraint:

    """

    Add a constraint to this object

    """

    ...

  def remove(self, constraint: Constraint) -> None:

    """

    Remove a constraint from this object

    """

    ...

  def move(self, from_index: int, to_index: int) -> None:

    """

    Move a constraint to a different position

    """

    ...

  def copy(self, constraint: Constraint) -> Constraint:

    """

    Add a new constraint that is a copy of the given one

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Preferences(bpy_struct):

  """

  Global preferences

  """

  active_section: str = ...

  """

  Active section of the preferences shown in the user interface

  """

  addons: typing.Union[Addons, typing.Sequence[Addon], typing.Mapping[str, Addon], bpy_prop_collection] = ...

  app_template: str = ...

  apps: PreferencesApps = ...

  """

  Preferences that work only for apps

  """

  autoexec_paths: typing.Union[PathCompareCollection, typing.Sequence[PathCompare], typing.Mapping[str, PathCompare], bpy_prop_collection] = ...

  edit: PreferencesEdit = ...

  """

  Settings for interacting with Blender data

  """

  experimental: PreferencesExperimental = ...

  """

  Settings for features that are still early in their development stage

  """

  filepaths: PreferencesFilePaths = ...

  """

  Default paths for external files

  """

  inputs: PreferencesInput = ...

  """

  Settings for input devices

  """

  is_dirty: bool = ...

  """

  Preferences have changed

  """

  keymap: PreferencesKeymap = ...

  """

  Shortcut setup for keyboards and other input devices

  """

  studio_lights: typing.Union[StudioLights, typing.Sequence[StudioLight], typing.Mapping[str, StudioLight], bpy_prop_collection] = ...

  system: PreferencesSystem = ...

  """

  Graphics driver and operating system settings

  """

  themes: typing.Union[typing.Sequence[Theme], typing.Mapping[str, Theme], bpy_prop_collection] = ...

  ui_styles: typing.Union[typing.Sequence[ThemeStyle], typing.Mapping[str, ThemeStyle], bpy_prop_collection] = ...

  use_preferences_save: bool = ...

  """

  Save preferences on exit when modified (unless factory settings have been loaded)

  """

  version: typing.Tuple[int, int, int] = ...

  """

  Version of Blender the userpref.blend was saved with

  """

  view: PreferencesView = ...

  """

  Preferences related to viewing data

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class PreferencesApps(bpy_struct):

  """

  Preferences that work only for apps

  """

  show_corner_split: bool = ...

  """

  Split and join editors by dragging from corners

  """

  show_edge_resize: bool = ...

  """

  Resize editors by dragging from the edges

  """

  show_regions_visibility_toggle: bool = ...

  """

  Header and side bars visibility toggles

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class PreferencesEdit(bpy_struct):

  """

  Settings for interacting with Blender data

  """

  auto_keying_mode: str = ...

  """

  Mode of automatic keyframe insertion for Objects and Bones (default setting used for new Scenes)

  """

  collection_instance_empty_size: float = ...

  """

  Display size of the empty when new collection instances are created

  """

  fcurve_new_auto_smoothing: str = ...

  """

  Auto Handle Smoothing mode used for newly added F-Curves

  * ``NONE``
None -- Automatic handles only take immediately adjacent keys into account.

  * ``CONT_ACCEL``
Continuous Acceleration -- Automatic handles are adjusted to avoid jumps in acceleration, resulting in smoother curves. However, key changes may affect interpolation over a larger stretch of the curve.

  """

  fcurve_unselected_alpha: float = ...

  """

  The opacity of unselected F-Curves against the background of the Graph Editor

  """

  grease_pencil_default_color: typing.Tuple[float, float, float, float] = ...

  """

  Color of new annotation layers

  """

  grease_pencil_eraser_radius: int = ...

  """

  Radius of eraser 'brush'

  """

  grease_pencil_euclidean_distance: int = ...

  """

  Distance moved by mouse when drawing stroke to include

  """

  grease_pencil_manhattan_distance: int = ...

  """

  Pixels moved by mouse per axis when drawing stroke

  """

  keyframe_new_handle_type: str = ...

  """

  Handle type for handles of new keyframes

  * ``FREE``
Free -- Completely independent manually set handle.

  * ``ALIGNED``
Aligned -- Manually set handle with rotation locked together with its pair.

  * ``VECTOR``
Vector -- Automatic handles that create straight lines.

  * ``AUTO``
Automatic -- Automatic handles that create smooth curves.

  * ``AUTO_CLAMPED``
Auto Clamped -- Automatic handles that create smooth curves which only change direction at keyframes.

  """

  keyframe_new_interpolation_type: str = ...

  """

  Interpolation mode used for first keyframe on newly added F-Curves (subsequent keyframes take interpolation from preceding keyframe)

  * ``CONSTANT``
Constant -- No interpolation, value of A gets held until B is encountered.

  * ``LINEAR``
Linear -- Straight-line interpolation between A and B (i.e. no ease in/out).

  * ``BEZIER``
Bezier -- Smooth interpolation between A and B, with some control over curve shape.

  * ``SINE``
Sinusoidal -- Sinusoidal easing (weakest, almost linear but with a slight curvature).

  * ``QUAD``
Quadratic -- Quadratic easing.

  * ``CUBIC``
Cubic -- Cubic easing.

  * ``QUART``
Quartic -- Quartic easing.

  * ``QUINT``
Quintic -- Quintic easing.

  * ``EXPO``
Exponential -- Exponential easing (dramatic).

  * ``CIRC``
Circular -- Circular easing (strongest and most dynamic).

  * ``BACK``
Back -- Cubic easing with overshoot and settle.

  * ``BOUNCE``
Bounce -- Exponentially decaying parabolic bounce, like when objects collide.

  * ``ELASTIC``
Elastic -- Exponentially decaying sine wave, like an elastic band.

  """

  material_link: str = ...

  """

  Toggle whether the material is linked to object data or the object block

  * ``OBDATA``
Object Data -- Toggle whether the material is linked to object data or the object block.

  * ``OBJECT``
Object -- Toggle whether the material is linked to object data or the object block.

  """

  node_margin: int = ...

  """

  Minimum distance between nodes for Auto-offsetting nodes

  """

  object_align: str = ...

  """

  When adding objects from a 3D View menu, either align them with that view or with the world

  * ``WORLD``
World -- Align newly added objects to the world coordinate system.

  * ``VIEW``
View -- Align newly added objects to the active 3D View direction.

  * ``CURSOR``
3D Cursor -- Align newly added objects to the 3D Cursor's rotation.

  """

  sculpt_paint_overlay_color: typing.Tuple[float, float, float] = ...

  """

  Color of texture overlay

  """

  undo_memory_limit: int = ...

  """

  Maximum memory usage in megabytes (0 means unlimited)

  """

  undo_steps: int = ...

  """

  Number of undo steps available (smaller values conserve memory)

  """

  use_anim_channel_group_colors: bool = ...

  """

  Use animation channel group colors; generally this is used to show bone group colors

  """

  use_auto_keying: bool = ...

  """

  Automatic keyframe insertion for Objects and Bones (default setting used for new Scenes)

  """

  use_auto_keying_warning: bool = ...

  """

  Show warning indicators when transforming objects and bones if auto keying is enabled

  """

  use_cursor_lock_adjust: bool = ...

  """

  Place the cursor without 'jumping' to the new location (when lock-to-cursor is used)

  """

  use_duplicate_action: bool = ...

  """

  Causes actions to be duplicated with the data-blocks

  """

  use_duplicate_armature: bool = ...

  """

  Causes armature data to be duplicated with the object

  """

  use_duplicate_camera: bool = ...

  """

  Causes camera data to be duplicated with the object

  """

  use_duplicate_curve: bool = ...

  """

  Causes curve data to be duplicated with the object

  """

  use_duplicate_grease_pencil: bool = ...

  """

  Causes grease pencil data to be duplicated with the object

  """

  use_duplicate_hair: bool = ...

  """

  Causes hair data to be duplicated with the object

  """

  use_duplicate_lattice: bool = ...

  """

  Causes lattice data to be duplicated with the object

  """

  use_duplicate_light: bool = ...

  """

  Causes light data to be duplicated with the object

  """

  use_duplicate_lightprobe: bool = ...

  """

  Causes light probe data to be duplicated with the object

  """

  use_duplicate_material: bool = ...

  """

  Causes material data to be duplicated with the object

  """

  use_duplicate_mesh: bool = ...

  """

  Causes mesh data to be duplicated with the object

  """

  use_duplicate_metaball: bool = ...

  """

  Causes metaball data to be duplicated with the object

  """

  use_duplicate_particle: bool = ...

  """

  Causes particle systems to be duplicated with the object

  """

  use_duplicate_pointcloud: bool = ...

  """

  Causes point cloud data to be duplicated with the object

  """

  use_duplicate_speaker: bool = ...

  """

  Causes speaker data to be duplicated with the object

  """

  use_duplicate_surface: bool = ...

  """

  Causes surface data to be duplicated with the object

  """

  use_duplicate_text: bool = ...

  """

  Causes text data to be duplicated with the object

  """

  use_duplicate_volume: bool = ...

  """

  Causes volume data to be duplicated with the object

  """

  use_enter_edit_mode: bool = ...

  """

  Enter Edit Mode automatically after adding a new object

  """

  use_global_undo: bool = ...

  """

  Global undo works by keeping a full copy of the file itself in memory, so takes extra memory

  """

  use_insertkey_xyz_to_rgb: bool = ...

  """

  Color for newly added transformation F-Curves (Location, Rotation, Scale) and also Color is based on the transform axis

  """

  use_keyframe_insert_available: bool = ...

  """

  Automatic keyframe insertion in available F-Curves

  """

  use_keyframe_insert_needed: bool = ...

  """

  Keyframe insertion only when keyframe needed

  """

  use_mouse_depth_cursor: bool = ...

  """

  Use the surface depth for cursor placement

  """

  use_negative_frames: bool = ...

  """

  Current frame number can be manually set to a negative value

  """

  use_visual_keying: bool = ...

  """

  Use Visual keying automatically for constrained objects

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class PreferencesExperimental(bpy_struct):

  """

  Experimental features

  """

  override_auto_resync: bool = ...

  """

  Enable library overrides automatic resync detection and process on file load. Disable when dealing with older .blend files that need manual Resync (Enforce) handling

  """

  proxy_to_override_auto_conversion: bool = ...

  """

  Enable automatic conversion of proxies to library overrides on file load

  """

  show_asset_debug_info: bool = ...

  """

  Enable some extra fields in the Asset Browser to aid in debugging

  """

  use_cycles_debug: bool = ...

  """

  Enable Cycles debugging options for developers

  """

  use_extended_asset_browser: bool = ...

  """

  Enable Asset Browser editor and operators to manage regular data-blocks as assets, not just poses

  """

  use_full_frame_compositor: bool = ...

  """

  Enable compositor full frame execution mode option (no tiling, reduces execution time and memory usage)

  """

  use_geometry_nodes_legacy: bool = ...

  """

  Enable legacy geometry nodes in the menu

  """

  use_new_hair_type: bool = ...

  """

  Enable the new hair type in the ui

  """

  use_new_point_cloud_type: bool = ...

  """

  Enable the new point cloud type in the ui

  """

  use_override_templates: bool = ...

  """

  Enable library override template in the python API

  """

  use_sculpt_tools_tilt: bool = ...

  """

  Support for pen tablet tilt events in Sculpt Mode

  """

  use_sculpt_vertex_colors: bool = ...

  """

  Use the new Vertex Painting system

  """

  use_undo_legacy: bool = ...

  """

  Use legacy undo (slower than the new default one, but may be more stable in some cases)

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class PreferencesFilePaths(bpy_struct):

  """

  Default paths for external files

  """

  animation_player: str = ...

  """

  Path to a custom animation/frame sequence player

  """

  animation_player_preset: str = ...

  """

  Preset configs for external animation players

  * ``INTERNAL``
Internal -- Built-in animation player.

  * ``DJV``
DJV -- Open source frame player.

  * ``FRAMECYCLER``
FrameCycler -- Frame player from IRIDAS.

  * ``RV``
RV -- Frame player from Tweak Software.

  * ``MPLAYER``
MPlayer -- Media player for video and PNG/JPEG/SGI image sequences.

  * ``CUSTOM``
Custom -- Custom animation player executable path.

  """

  asset_libraries: typing.Union[typing.Sequence[UserAssetLibrary], typing.Mapping[str, UserAssetLibrary], bpy_prop_collection] = ...

  auto_save_time: int = ...

  """

  The time (in minutes) to wait between automatic temporary saves

  """

  file_preview_type: str = ...

  """

  What type of blend preview to create

  * ``NONE``
None -- Do not create blend previews.

  * ``AUTO``
Auto -- Automatically select best preview type.

  * ``SCREENSHOT``
Screenshot -- Capture the entire window.

  * ``CAMERA``
Camera View -- Workbench render of scene.

  """

  font_directory: str = ...

  """

  The default directory to search for loading fonts

  """

  i18n_branches_directory: str = ...

  """

  The path to the '/branches' directory of your local svn-translation copy, to allow translating from the UI

  """

  image_editor: str = ...

  """

  Path to an image editor

  """

  recent_files: int = ...

  """

  Maximum number of recently opened files to remember

  """

  render_cache_directory: str = ...

  """

  Where to cache raw render results

  """

  render_output_directory: str = ...

  """

  The default directory for rendering output, for new scenes

  """

  save_version: int = ...

  """

  The number of old versions to maintain in the current directory, when manually saving

  """

  script_directory: str = ...

  """

  Alternate script path, matching the default layout with subdirectories: startup, add-ons, modules, and presets (requires restart)

  """

  show_hidden_files_datablocks: bool = ...

  """

  Show files and data-blocks that are normally hidden

  """

  show_recent_locations: bool = ...

  """

  Show Recent locations list in the File Browser

  """

  show_system_bookmarks: bool = ...

  """

  Show System locations list in the File Browser

  """

  sound_directory: str = ...

  """

  The default directory to search for sounds

  """

  temporary_directory: str = ...

  """

  The directory for storing temporary save files

  """

  texture_directory: str = ...

  """

  The default directory to search for textures

  """

  use_auto_save_temporary_files: bool = ...

  """

  Automatic saving of temporary files in temp directory, uses process ID.
Warning: Sculpt and edit mode data won't be saved

  """

  use_file_compression: bool = ...

  """

  Enable file compression when saving .blend files

  """

  use_filter_files: bool = ...

  """

  Enable filtering of files in the File Browser

  """

  use_load_ui: bool = ...

  """

  Load user interface setup when loading .blend files

  """

  use_relative_paths: bool = ...

  """

  Default relative path option for the file selector, when no path is defined yet

  """

  use_scripts_auto_execute: bool = ...

  """

  Allow any .blend file to run scripts automatically (unsafe with blend files from an untrusted source)

  """

  use_tabs_as_spaces: bool = ...

  """

  Automatically convert all new tabs into spaces for new and loaded text files

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class PreferencesInput(bpy_struct):

  """

  Settings for input devices

  """

  drag_threshold: int = ...

  """

  Number of pixels to drag before a drag event is triggered for keyboard and other non mouse/tablet input (otherwise click events are detected)

  """

  drag_threshold_mouse: int = ...

  """

  Number of pixels to drag before a tweak/drag event is triggered for mouse/trackpad input (otherwise click events are detected)

  """

  drag_threshold_tablet: int = ...

  """

  Number of pixels to drag before a tweak/drag event is triggered for tablet input (otherwise click events are detected)

  """

  invert_mouse_zoom: bool = ...

  """

  Invert the axis of mouse movement for zooming

  """

  invert_zoom_wheel: bool = ...

  """

  Swap the Mouse Wheel zoom direction

  """

  mouse_double_click_time: int = ...

  """

  Time/delay (in ms) for a double click

  """

  mouse_emulate_3_button_modifier: str = ...

  """

  Hold this modifier to emulate the middle mouse button

  """

  move_threshold: int = ...

  """

  Number of pixels to before the cursor is considered to have moved (used for cycling selected items on successive clicks)

  """

  navigation_mode: str = ...

  """

  Which method to use for viewport navigation

  * ``WALK``
Walk -- Interactively walk or free navigate around the scene.

  * ``FLY``
Fly -- Use fly dynamics to navigate the scene.

  """

  ndof_deadzone: float = ...

  """

  Threshold of initial movement needed from the device's rest position

  """

  ndof_fly_helicopter: bool = ...

  """

  Device up/down directly controls the Z position of the 3D viewport

  """

  ndof_lock_horizon: bool = ...

  """

  Keep horizon level while flying with 3D Mouse

  """

  ndof_orbit_sensitivity: float = ...

  """

  Overall sensitivity of the 3D Mouse for orbiting

  """

  ndof_pan_yz_swap_axis: bool = ...

  """

  Pan using up/down on the device (otherwise forward/backward)

  """

  ndof_panx_invert_axis: bool = ...

  ndof_pany_invert_axis: bool = ...

  ndof_panz_invert_axis: bool = ...

  ndof_rotx_invert_axis: bool = ...

  ndof_roty_invert_axis: bool = ...

  ndof_rotz_invert_axis: bool = ...

  ndof_sensitivity: float = ...

  """

  Overall sensitivity of the 3D Mouse for panning

  """

  ndof_show_guide: bool = ...

  """

  Display the center and axis during rotation

  """

  ndof_view_navigate_method: str = ...

  """

  Navigation style in the viewport

  * ``FREE``
Free -- Use full 6 degrees of freedom by default.

  * ``ORBIT``
Orbit -- Orbit about the view center by default.

  """

  ndof_view_rotate_method: str = ...

  """

  Rotation style in the viewport

  * ``TURNTABLE``
Turntable -- Use turntable style rotation in the viewport.

  * ``TRACKBALL``
Trackball -- Use trackball style rotation in the viewport.

  """

  ndof_zoom_invert: bool = ...

  """

  Zoom using opposite direction

  """

  pressure_softness: float = ...

  """

  Adjusts softness of the low pressure response onset using a gamma curve

  """

  pressure_threshold_max: float = ...

  """

  Raw input pressure value that is interpreted as 100% by Blender

  """

  tablet_api: str = ...

  """

  Select the tablet API to use for pressure sensitivity (may require restarting Blender for changes to take effect)

  * ``AUTOMATIC``
Automatic -- Automatically choose Wintab or Windows Ink depending on the device.

  * ``WINDOWS_INK``
Windows Ink -- Use native Windows Ink API, for modern tablet and pen devices. Requires Windows 8 or newer.

  * ``WINTAB``
Wintab -- Use Wintab driver for older tablets and Windows versions.

  """

  use_auto_perspective: bool = ...

  """

  Automatically switch between orthographic and perspective when changing from top/front/side views

  """

  use_drag_immediately: bool = ...

  """

  Moving things with a mouse drag confirms when releasing the button

  """

  use_emulate_numpad: bool = ...

  """

  Main 1 to 0 keys act as the numpad ones (useful for laptops)

  """

  use_mouse_continuous: bool = ...

  """

  Let the mouse wrap around the view boundaries so mouse movements are not limited by the screen size (used by transform, dragging of UI controls, etc.)

  """

  use_mouse_depth_navigate: bool = ...

  """

  Use the depth under the mouse to improve view pan/rotate/zoom functionality

  """

  use_mouse_emulate_3_button: bool = ...

  """

  Emulate Middle Mouse with Alt+Left Mouse

  """

  use_ndof: bool = ...

  use_numeric_input_advanced: bool = ...

  """

  When entering numbers while transforming, default to advanced mode for full math expression evaluation

  """

  use_rotate_around_active: bool = ...

  """

  Use selection as the pivot point

  """

  use_zoom_to_mouse: bool = ...

  """

  Zoom in towards the mouse pointer's position in the 3D view, rather than the 2D window center

  """

  view_rotate_method: str = ...

  """

  Orbit method in the viewport

  * ``TURNTABLE``
Turntable -- Turntable keeps the Z-axis upright while orbiting.

  * ``TRACKBALL``
Trackball -- Trackball allows you to tumble your view at any angle.

  """

  view_rotate_sensitivity_trackball: float = ...

  """

  Scale trackball orbit sensitivity

  """

  view_rotate_sensitivity_turntable: float = ...

  """

  Rotation amount per pixel to control how fast the viewport orbits

  """

  view_zoom_axis: str = ...

  """

  Axis of mouse movement to zoom in or out on

  * ``VERTICAL``
Vertical -- Zoom in and out based on vertical mouse movement.

  * ``HORIZONTAL``
Horizontal -- Zoom in and out based on horizontal mouse movement.

  """

  view_zoom_method: str = ...

  """

  Which style to use for viewport scaling

  * ``CONTINUE``
Continue -- Continuous zooming. The zoom direction and speed depends on how far along the set Zoom Axis the mouse has moved.

  * ``DOLLY``
Dolly -- Zoom in and out based on mouse movement along the set Zoom Axis.

  * ``SCALE``
Scale -- Zoom in and out as if you are scaling the view, mouse movements relative to center.

  """

  walk_navigation: WalkNavigation = ...

  """

  Settings for walk navigation mode

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class PreferencesKeymap(bpy_struct):

  """

  Shortcut setup for keyboards and other input devices

  """

  active_keyconfig: str = ...

  """

  The name of the active key configuration

  """

  show_ui_keyconfig: bool = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class PreferencesSystem(bpy_struct):

  """

  Graphics driver and operating system settings

  """

  anisotropic_filter: str = ...

  """

  Quality of the anisotropic filtering (values greater than 1.0 enable anisotropic filtering)

  """

  audio_channels: str = ...

  """

  Audio channel count

  * ``MONO``
Mono -- Set audio channels to mono.

  * ``STEREO``
Stereo -- Set audio channels to stereo.

  * ``SURROUND4``
4 Channels -- Set audio channels to 4 channels.

  * ``SURROUND51``
5.1 Surround -- Set audio channels to 5.1 surround sound.

  * ``SURROUND71``
7.1 Surround -- Set audio channels to 7.1 surround sound.

  """

  audio_device: str = ...

  """

  Audio output device

  * ``None``
None -- No device - there will be no audio output.

  """

  audio_mixing_buffer: str = ...

  """

  Number of samples used by the audio mixing buffer

  * ``SAMPLES_256``
256 Samples -- Set audio mixing buffer size to 256 samples.

  * ``SAMPLES_512``
512 Samples -- Set audio mixing buffer size to 512 samples.

  * ``SAMPLES_1024``
1024 Samples -- Set audio mixing buffer size to 1024 samples.

  * ``SAMPLES_2048``
2048 Samples -- Set audio mixing buffer size to 2048 samples.

  * ``SAMPLES_4096``
4096 Samples -- Set audio mixing buffer size to 4096 samples.

  * ``SAMPLES_8192``
8192 Samples -- Set audio mixing buffer size to 8192 samples.

  * ``SAMPLES_16384``
16384 Samples -- Set audio mixing buffer size to 16384 samples.

  * ``SAMPLES_32768``
32768 Samples -- Set audio mixing buffer size to 32768 samples.

  """

  audio_sample_format: str = ...

  """

  Audio sample format

  * ``U8``
8-bit Unsigned -- Set audio sample format to 8-bit unsigned integer.

  * ``S16``
16-bit Signed -- Set audio sample format to 16-bit signed integer.

  * ``S24``
24-bit Signed -- Set audio sample format to 24-bit signed integer.

  * ``S32``
32-bit Signed -- Set audio sample format to 32-bit signed integer.

  * ``FLOAT``
32-bit Float -- Set audio sample format to 32-bit float.

  * ``DOUBLE``
64-bit Float -- Set audio sample format to 64-bit float.

  """

  audio_sample_rate: str = ...

  """

  Audio sample rate

  * ``RATE_44100``
44.1 kHz -- Set audio sampling rate to 44100 samples per second.

  * ``RATE_48000``
48 kHz -- Set audio sampling rate to 48000 samples per second.

  * ``RATE_96000``
96 kHz -- Set audio sampling rate to 96000 samples per second.

  * ``RATE_192000``
192 kHz -- Set audio sampling rate to 192000 samples per second.

  """

  dpi: int = ...

  gl_clip_alpha: float = ...

  """

  Clip alpha below this threshold in the 3D textured view

  """

  gl_texture_limit: str = ...

  """

  Limit the texture size to save graphics memory

  """

  image_draw_method: str = ...

  """

  Method used for displaying images on the screen

  * ``AUTO``
Automatic -- Automatically choose method based on GPU and image.

  * ``2DTEXTURE``
2D Texture -- Use CPU for display transform and display image with 2D texture.

  * ``GLSL``
GLSL -- Use GLSL shaders for display transform and display image with 2D texture.

  """

  legacy_compute_device_type: int = ...

  """

  For backwards compatibility only

  """

  light_ambient: typing.Tuple[float, float, float] = ...

  """

  Color of the ambient light that uniformly lit the scene

  """

  memory_cache_limit: int = ...

  """

  Memory cache limit (in megabytes)

  """

  opensubdiv_compute_type: str = ...

  """

  Type of computer back-end used with OpenSubdiv

  """

  pixel_size: float = ...

  scrollback: int = ...

  """

  Maximum number of lines to store for the console buffer

  """

  sequencer_disk_cache_compression: str = ...

  """

  Smaller compression will result in larger files, but less decoding overhead

  * ``NONE``
None -- Requires fast storage, but uses minimum CPU resources.

  * ``LOW``
Low -- Doesn't require fast storage and uses less CPU resources.

  * ``HIGH``
High -- Works on slower storage devices and uses most CPU resources.

  """

  sequencer_disk_cache_dir: str = ...

  """

  Override default directory

  """

  sequencer_disk_cache_size_limit: int = ...

  """

  Disk cache limit (in gigabytes)

  """

  sequencer_proxy_setup: str = ...

  """

  When and how proxies are created

  * ``MANUAL``
Manual -- Set up proxies manually.

  * ``AUTOMATIC``
Automatic -- Build proxies for added movie and image strips in each preview size.

  """

  solid_lights: typing.Union[typing.Sequence[UserSolidLight], typing.Mapping[str, UserSolidLight], bpy_prop_collection] = ...

  """

  Lights used to display objects in solid shading mode

  """

  texture_collection_rate: int = ...

  """

  Number of seconds between each run of the GL texture garbage collector

  """

  texture_time_out: int = ...

  """

  Time since last access of a GL texture in seconds after which it is freed (set to 0 to keep textures allocated)

  """

  ui_line_width: float = ...

  """

  Suggested line thickness and point size in pixels, for add-ons displaying custom user interface elements, based on operating system settings and Blender UI scale

  """

  ui_scale: float = ...

  """

  Size multiplier to use when displaying custom user interface elements, so that they are scaled correctly on screens with different DPI. This value is based on operating system DPI settings and Blender display scale

  """

  use_edit_mode_smooth_wire: bool = ...

  """

  Enable Edit-Mode edge smoothing, reducing aliasing, requires restart

  """

  use_overlay_smooth_wire: bool = ...

  """

  Enable overlay smooth wires, reducing aliasing

  """

  use_region_overlap: bool = ...

  """

  Display tool/property regions over the main region

  """

  use_select_pick_depth: bool = ...

  """

  Use the depth buffer for picking 3D View selection (without this the front most object may not be selected first)

  """

  use_sequencer_disk_cache: bool = ...

  """

  Store cached images to disk

  """

  use_studio_light_edit: bool = ...

  """

  View the result of the studio light editor in the viewport

  """

  vbo_collection_rate: int = ...

  """

  Number of seconds between each run of the GL Vertex buffer object garbage collector

  """

  vbo_time_out: int = ...

  """

  Time since last access of a GL Vertex buffer object in seconds after which it is freed (set to 0 to keep vbo allocated)

  """

  viewport_aa: str = ...

  """

  Method of anti-aliasing in 3d viewport

  * ``OFF``
No Anti-Aliasing -- Scene will be rendering without any anti-aliasing.

  * ``FXAA``
Single Pass Anti-Aliasing -- Scene will be rendered using a single pass anti-aliasing method (FXAA).

  * ``5``
5 Samples -- Scene will be rendered using 5 anti-aliasing samples.

  * ``8``
8 Samples -- Scene will be rendered using 8 anti-aliasing samples.

  * ``11``
11 Samples -- Scene will be rendered using 11 anti-aliasing samples.

  * ``16``
16 Samples -- Scene will be rendered using 16 anti-aliasing samples.

  * ``32``
32 Samples -- Scene will be rendered using 32 anti-aliasing samples.

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class PreferencesView(bpy_struct):

  """

  Preferences related to viewing data

  """

  color_picker_type: str = ...

  """

  Different styles of displaying the color picker widget

  * ``CIRCLE_HSV``
Circle (HSV) -- A circular Hue/Saturation color wheel, with Value slider.

  * ``CIRCLE_HSL``
Circle (HSL) -- A circular Hue/Saturation color wheel, with Lightness slider.

  * ``SQUARE_SV``
Square (SV + H) -- A square showing Saturation/Value, with Hue slider.

  * ``SQUARE_HS``
Square (HS + V) -- A square showing Hue/Saturation, with Value slider.

  * ``SQUARE_HV``
Square (HV + S) -- A square showing Hue/Value, with Saturation slider.

  """

  factor_display_type: str = ...

  """

  How factor values are displayed

  * ``FACTOR``
Factor -- Display factors as values between 0 and 1.

  * ``PERCENTAGE``
Percentage -- Display factors as percentages.

  """

  filebrowser_display_type: str = ...

  """

  Default location where the File Editor will be displayed in

  * ``SCREEN``
Maximized Area -- Open the temporary editor in a maximized screen.

  * ``WINDOW``
New Window -- Open the temporary editor in a new window.

  """

  font_path_ui: str = ...

  """

  Path to interface font

  """

  font_path_ui_mono: str = ...

  """

  Path to interface monospaced Font

  """

  gizmo_size: int = ...

  """

  Diameter of the gizmo

  """

  gizmo_size_navigate_v3d: int = ...

  """

  The Navigate Gizmo size

  """

  header_align: str = ...

  """

  Default header position for new space-types

  * ``NONE``
Keep Existing -- Keep existing header alignment.

  * ``TOP``
Top -- Top aligned on load.

  * ``BOTTOM``
Bottom -- Bottom align on load (except for property editors).

  """

  language: str = ...

  """

  Language used for translation

  * ``DEFAULT``
Automatic (Automatic) -- Automatically choose system's defined language if available, or fall-back to English.

  """

  lookdev_sphere_size: int = ...

  """

  Diameter of the HDRI preview spheres

  """

  mini_axis_brightness: int = ...

  """

  Brightness of the icon

  """

  mini_axis_size: int = ...

  """

  The axes icon's size

  """

  mini_axis_type: str = ...

  """

  Show a small rotating 3D axes in the top right corner of the 3D View

  """

  open_sublevel_delay: int = ...

  """

  Time delay in 1/10 seconds before automatically opening sub level menus

  """

  open_toplevel_delay: int = ...

  """

  Time delay in 1/10 seconds before automatically opening top level menus

  """

  pie_animation_timeout: int = ...

  """

  Time needed to fully animate the pie to unfolded state (in 1/100ths of sec)

  """

  pie_initial_timeout: int = ...

  """

  Pie menus will use the initial mouse position as center for this amount of time (in 1/100ths of sec)

  """

  pie_menu_confirm: int = ...

  """

  Distance threshold after which selection is made (zero to disable)

  """

  pie_menu_radius: int = ...

  """

  Pie menu size in pixels

  """

  pie_menu_threshold: int = ...

  """

  Distance from center needed before a selection can be made

  """

  pie_tap_timeout: int = ...

  """

  Pie menu button held longer than this will dismiss menu on release.(in 1/100ths of sec)

  """

  render_display_type: str = ...

  """

  Default location where rendered images will be displayed in

  * ``NONE``
Keep User Interface -- Images are rendered without changing the user interface.

  * ``SCREEN``
Maximized Area -- Images are rendered in a maximized Image Editor.

  * ``AREA``
Image Editor -- Images are rendered in an Image Editor.

  * ``WINDOW``
New Window -- Images are rendered in a new window.

  """

  rotation_angle: float = ...

  """

  Rotation step for numerical pad keys (2 4 6 8)

  """

  show_addons_enabled_only: bool = ...

  """

  Only show enabled add-ons. Un-check to see all installed add-ons

  """

  show_column_layout: bool = ...

  """

  Use a column layout for toolbox

  """

  show_developer_ui: bool = ...

  """

  Show options for developers (edit source in context menu, geometry indices)

  """

  show_gizmo: bool = ...

  """

  Use transform gizmos by default

  """

  show_navigate_ui: bool = ...

  """

  Show navigation controls in 2D and 3D views which do not have scroll bars

  """

  show_object_info: bool = ...

  """

  Display objects name and frame number in 3D view

  """

  show_playback_fps: bool = ...

  """

  Show the frames per second screen refresh rate, while animation is played back

  """

  show_splash: bool = ...

  """

  Display splash screen on startup

  """

  show_statusbar_memory: bool = ...

  """

  Show Blender memory usage

  """

  show_statusbar_stats: bool = ...

  """

  Show scene statistics

  """

  show_statusbar_version: bool = ...

  """

  Show Blender version string

  """

  show_statusbar_vram: bool = ...

  """

  Show GPU video memory usage

  """

  show_tooltips: bool = ...

  """

  Display tooltips (when off hold Alt to force display)

  """

  show_tooltips_python: bool = ...

  """

  Show Python references in tooltips

  """

  show_view_name: bool = ...

  """

  Show the name of the view's direction in each 3D View

  """

  smooth_view: int = ...

  """

  Time to animate the view in milliseconds, zero to disable

  """

  text_hinting: str = ...

  """

  Method for making user interface text render sharp

  """

  timecode_style: str = ...

  """

  Format of Time Codes displayed when not displaying timing in terms of frames

  * ``MINIMAL``
Minimal Info -- Most compact representation, uses '+' as separator for sub-second frame numbers, with left and right truncation of the timecode as necessary.

  * ``SMPTE``
SMPTE (Full) -- Full SMPTE timecode (format is HH:MM:SS:FF).

  * ``SMPTE_COMPACT``
SMPTE (Compact) -- SMPTE timecode showing minutes, seconds, and frames only - hours are also shown if necessary, but not by default.

  * ``MILLISECONDS``
Compact with Milliseconds -- Similar to SMPTE (Compact), except that instead of frames, milliseconds are shown instead.

  * ``SECONDS_ONLY``
Only Seconds -- Direct conversion of frame numbers to seconds.

  """

  ui_line_width: str = ...

  """

  Changes the thickness of widget outlines, lines and dots in the interface

  * ``THIN``
Thin -- Thinner lines than the default.

  * ``AUTO``
Default -- Automatic line width based on UI scale.

  * ``THICK``
Thick -- Thicker lines than the default.

  """

  ui_scale: float = ...

  """

  Changes the size of the fonts and widgets in the interface

  """

  use_directional_menus: bool = ...

  """

  Otherwise menus, etc will always be top to bottom, left to right, no matter opening direction

  """

  use_mouse_over_open: bool = ...

  """

  Open menu buttons and pulldowns automatically when the mouse is hovering

  """

  use_save_prompt: bool = ...

  """

  Ask for confirmation when quitting with unsaved changes

  """

  use_text_antialiasing: bool = ...

  """

  Smooth jagged edges of user interface text

  """

  use_translate_interface: bool = ...

  """

  Translate all labels in menus, buttons and panels (note that this might make it hard to follow tutorials or the manual)

  """

  use_translate_new_dataname: bool = ...

  """

  Translate the names of new data-blocks (objects, materials...)

  """

  use_translate_tooltips: bool = ...

  """

  Translate the descriptions when hovering UI elements (recommended)

  """

  use_weight_color_range: bool = ...

  """

  Enable color range used for weight visualization in weight painting mode

  """

  view2d_grid_spacing_min: int = ...

  """

  Minimum number of pixels between each gridline in 2D Viewports

  """

  view_frame_keyframes: int = ...

  """

  Keyframes around cursor that we zoom around

  """

  view_frame_seconds: float = ...

  """

  Seconds around cursor that we zoom around

  """

  view_frame_type: str = ...

  """

  How zooming to frame focuses around current frame

  """

  weight_color_range: ColorRamp = ...

  """

  Color range used for weight visualization in weight painting mode

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Property(bpy_struct):

  """

  RNA property definition

  """

  description: str = ...

  """

  Description of the property for tooltips

  """

  icon: str = ...

  """

  Icon of the item

  """

  identifier: str = ...

  """

  Unique name used in the code and scripting

  """

  is_animatable: bool = ...

  """

  Property is animatable through RNA

  """

  is_argument_optional: bool = ...

  """

  True when the property is optional in a Python function implementing an RNA function

  """

  is_enum_flag: bool = ...

  """

  True when multiple enums

  """

  is_hidden: bool = ...

  """

  True when the property is hidden

  """

  is_library_editable: bool = ...

  """

  Property is editable from linked instances (changes not saved)

  """

  is_never_none: bool = ...

  """

  True when this value can't be set to None

  """

  is_output: bool = ...

  """

  True when this property is an output value from an RNA function

  """

  is_overridable: bool = ...

  """

  Property is overridable through RNA

  """

  is_readonly: bool = ...

  """

  Property is editable through RNA

  """

  is_registered: bool = ...

  """

  Property is registered as part of type registration

  """

  is_registered_optional: bool = ...

  """

  Property is optionally registered as part of type registration

  """

  is_required: bool = ...

  """

  False when this property is an optional argument in an RNA function

  """

  is_runtime: bool = ...

  """

  Property has been dynamically created at runtime

  """

  is_skip_save: bool = ...

  """

  True when the property is not saved in presets

  """

  name: str = ...

  """

  Human readable name

  """

  srna: Struct = ...

  """

  Struct definition used for properties assigned to this item

  """

  subtype: str = ...

  """

  Semantic interpretation of the property

  * ``NONE``
None.

  * ``FILEPATH``
File Path.

  * ``DIRPATH``
Directory Path.

  * ``FILENAME``
File Name.

  * ``BYTESTRING``
Byte String.

  * ``PASSWORD``
Password -- A string that is displayed hidden ('********').

  * ``PIXEL``
Pixel.

  * ``UNSIGNED``
Unsigned.

  * ``PERCENTAGE``
Percentage.

  * ``FACTOR``
Factor.

  * ``ANGLE``
Angle.

  * ``TIME``
Time (Scene Relative) -- Time specified in frames, converted to seconds based on scene frame rate.

  * ``TIME_ABSOLUTE``
Time (Absolute) -- Time specified in seconds, independent of the scene.

  * ``DISTANCE``
Distance.

  * ``DISTANCE_CAMERA``
Camera Distance.

  * ``POWER``
Power.

  * ``TEMPERATURE``
Temperature.

  * ``COLOR``
Color.

  * ``TRANSLATION``
Translation.

  * ``DIRECTION``
Direction.

  * ``VELOCITY``
Velocity.

  * ``ACCELERATION``
Acceleration.

  * ``MATRIX``
Matrix.

  * ``EULER``
Euler Angles.

  * ``QUATERNION``
Quaternion.

  * ``AXISANGLE``
Axis-Angle.

  * ``XYZ``
XYZ.

  * ``XYZ_LENGTH``
XYZ Length.

  * ``COLOR_GAMMA``
Color.

  * ``COORDS``
Coordinates.

  * ``LAYER``
Layer.

  * ``LAYER_MEMBER``
Layer Member.

  """

  tags: typing.Set[str] = ...

  """

  Subset of tags (defined in parent struct) that are set for this property

  """

  translation_context: str = ...

  """

  Translation context of the property's name

  """

  type: str = ...

  """

  Data type of the property

  """

  unit: str = ...

  """

  Type of units for this property

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class PropertyGroup(bpy_struct):

  """

  Group of ID properties

  """

  name: str = ...

  """

  Unique name used in the code and scripting

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class PropertyGroupItem(bpy_struct):

  """

  Property that stores arbitrary, user defined properties

  """

  collection: typing.Union[typing.Sequence[PropertyGroup], typing.Mapping[str, PropertyGroup], bpy_prop_collection] = ...

  double: float = ...

  double_array: typing.Tuple[float] = ...

  float: float = ...

  float_array: typing.Tuple[float] = ...

  group: PropertyGroup = ...

  id: ID = ...

  idp_array: typing.Union[typing.Sequence[PropertyGroup], typing.Mapping[str, PropertyGroup], bpy_prop_collection] = ...

  int: int = ...

  int_array: typing.Tuple[int] = ...

  string: str = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Region(bpy_struct):

  """

  Region in a subdivided screen area

  """

  alignment: str = ...

  """

  Alignment of the region within the area

  * ``NONE``
None -- Don't use any fixed alignment, fill available space.

  * ``TOP``
Top.

  * ``BOTTOM``
Bottom.

  * ``LEFT``
Left.

  * ``RIGHT``
Right.

  * ``HORIZONTAL_SPLIT``
Horizontal Split.

  * ``VERTICAL_SPLIT``
Vertical Split.

  * ``FLOAT``
Float -- Region floats on screen, doesn't use any fixed alignment.

  * ``QUAD_SPLIT``
Quad Split -- Region is split horizontally and vertically.

  """

  data: typing.Any = ...

  """

  Region specific data (the type depends on the region type)

  """

  height: int = ...

  """

  Region height

  """

  type: str = ...

  """

  Type of this region

  """

  view2d: View2D = ...

  """

  2D view of the region

  """

  width: int = ...

  """

  Region width

  """

  x: int = ...

  """

  The window relative vertical location of the region

  """

  y: int = ...

  """

  The window relative horizontal location of the region

  """

  def tag_redraw(self) -> None:

    """

    tag_redraw

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class RegionView3D(bpy_struct):

  """

  3D View region data

  """

  clip_planes: typing.Tuple[typing.Tuple[float, float, float, float], ...] = ...

  is_orthographic_side_view: bool = ...

  """

  Is current view an orthographic side view

  """

  is_perspective: bool = ...

  lock_rotation: bool = ...

  """

  Lock view rotation of side views to Top/Front/Right

  """

  perspective_matrix: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]] = ...

  """

  Current perspective matrix (``window_matrix * view_matrix``)

  """

  show_sync_view: bool = ...

  """

  Sync view position between side views

  """

  use_box_clip: bool = ...

  """

  Clip view contents based on what is visible in other side views

  """

  use_clip_planes: bool = ...

  view_camera_offset: typing.Tuple[float, float] = ...

  """

  View shift in camera view

  """

  view_camera_zoom: float = ...

  """

  Zoom factor in camera view

  """

  view_distance: float = ...

  """

  Distance to the view location

  """

  view_location: typing.Tuple[float, float, float] = ...

  """

  View pivot location

  """

  view_matrix: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]] = ...

  """

  Current view matrix

  """

  view_perspective: str = ...

  """

  View Perspective

  """

  view_rotation: typing.Tuple[float, float, float, float] = ...

  """

  Rotation in quaternions (keep normalized)

  """

  window_matrix: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]] = ...

  """

  Current window matrix

  """

  def update(self) -> None:

    """

    Recalculate the view matrices

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class RenderEngine(bpy_struct):

  """

  Render engine

  """

  bl_idname: str = ...

  bl_label: str = ...

  bl_use_alembic_procedural: bool = ...

  """

  Support loading Alembic data at render time

  """

  bl_use_custom_freestyle: bool = ...

  """

  Handles freestyle rendering on its own, instead of delegating it to EEVEE

  """

  bl_use_eevee_viewport: bool = ...

  """

  Uses Eevee for viewport shading in LookDev shading mode

  """

  bl_use_gpu_context: bool = ...

  """

  Enable OpenGL context for the render method, for engines that render using OpenGL

  """

  bl_use_image_save: bool = ...

  """

  Save images/movie to disk while rendering an animation. Disabling image saving is only supported when bl_use_postprocess is also disabled

  """

  bl_use_postprocess: bool = ...

  """

  Apply compositing on render results

  """

  bl_use_preview: bool = ...

  """

  Render engine supports being used for rendering previews of materials, lights and worlds

  """

  bl_use_shading_nodes_custom: bool = ...

  """

  Don't expose Cycles and Eevee shading nodes in the node editor user interface, so own nodes can be used instead

  """

  bl_use_spherical_stereo: bool = ...

  """

  Support spherical stereo camera models

  """

  bl_use_stereo_viewport: bool = ...

  """

  Support rendering stereo 3D viewport

  """

  camera_override: Object = ...

  is_animation: bool = ...

  is_preview: bool = ...

  layer_override: typing.Tuple[bool, ...] = ...

  render: RenderSettings = ...

  resolution_x: int = ...

  resolution_y: int = ...

  use_highlight_tiles: bool = ...

  def update(self, data: BlendData = None, depsgraph: Depsgraph = None) -> None:

    """

    Export scene data for render

    """

    ...

  def render(self, depsgraph: Depsgraph) -> None:

    """

    Render scene into an image

    """

    ...

  def render_frame_finish(self) -> None:

    """

    Perform finishing operations after all view layers in a frame were rendered

    """

    ...

  def draw(self, context: Context, depsgraph: Depsgraph) -> None:

    """

    Draw render image

    """

    ...

  def bake(self, depsgraph: Depsgraph, object: Object, pass_type: str, pass_filter: int, width: int, height: int) -> None:

    """

    Bake passes

    """

    ...

  def view_update(self, context: Context, depsgraph: Depsgraph) -> None:

    """

    Update on data changes for viewport render

    """

    ...

  def view_draw(self, context: Context, depsgraph: Depsgraph) -> None:

    """

    Draw viewport render

    """

    ...

  def update_script_node(self, node: Node = None) -> None:

    """

    Compile shader script node

    """

    ...

  def update_render_passes(self, scene: Scene = None, renderlayer: ViewLayer = None) -> None:

    """

    Update the render passes that will be generated

    """

    ...

  def tag_redraw(self) -> None:

    """

    Request redraw for viewport rendering

    """

    ...

  def tag_update(self) -> None:

    """

    Request update call for viewport rendering

    """

    ...

  def begin_result(self, x: int, y: int, w: int, h: int, layer: str = '', view: str = '') -> RenderResult:

    """

    Create render result to write linear floating-point render layers and passes

    """

    ...

  def update_result(self, result: RenderResult) -> None:

    """

    Signal that pixels have been updated and can be redrawn in the user interface

    """

    ...

  def end_result(self, result: RenderResult, cancel: bool = False, highlight: bool = False, do_merge_results: bool = False) -> None:

    """

    All pixels in the render result have been set and are final

    """

    ...

  def add_pass(self, name: str, channels: int, chan_id: str, layer: str = '') -> None:

    """

    Add a pass to the render layer

    """

    ...

  def get_result(self) -> RenderResult:

    """

    Get final result for non-pixel operations

    """

    ...

  def test_break(self) -> bool:

    """

    Test if the render operation should been canceled, this is a fast call that should be used regularly for responsiveness

    """

    ...

  def pass_by_index_get(self, layer: str, index: int) -> RenderPass:

    """

    pass_by_index_get

    """

    ...

  def active_view_get(self) -> str:

    """

    active_view_get

    """

    ...

  def active_view_set(self, view: str) -> None:

    """

    active_view_set

    """

    ...

  def camera_shift_x(self, camera: Object, use_spherical_stereo: bool = False) -> float:

    """

    camera_shift_x

    """

    ...

  def camera_model_matrix(self, camera: Object, use_spherical_stereo: bool = False) -> typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]]:

    """

    camera_model_matrix

    """

    ...

  def use_spherical_stereo(self, camera: Object) -> bool:

    """

    use_spherical_stereo

    """

    ...

  def update_stats(self, stats: str, info: str) -> None:

    """

    Update and signal to redraw render status text

    """

    ...

  def frame_set(self, frame: int, subframe: float) -> None:

    """

    Evaluate scene at a different frame (for motion blur)

    """

    ...

  def update_progress(self, progress: float) -> None:

    """

    Update progress percentage of render

    """

    ...

  def update_memory_stats(self, memory_used: float = 0.0, memory_peak: float = 0.0) -> None:

    """

    Update memory usage statistics

    """

    ...

  def report(self, type: typing.Set[str], message: str) -> None:

    """

    Report info, warning or error messages

    """

    ...

  def error_set(self, message: str) -> None:

    """

    Set error message displaying after the render is finished

    """

    ...

  def bind_display_space_shader(self, scene: Scene) -> None:

    """

    Bind GLSL fragment shader that converts linear colors to display space colors using scene color management settings

    """

    ...

  def unbind_display_space_shader(self) -> None:

    """

    Unbind GLSL display space shader, must always be called after binding the shader

    """

    ...

  def support_display_space_shader(self, scene: Scene) -> bool:

    """

    Test if GLSL display space shader is supported for the combination of graphics card and scene settings

    """

    ...

  def get_preview_pixel_size(self, scene: Scene) -> int:

    """

    Get the pixel size that should be used for preview rendering

    """

    ...

  def free_blender_memory(self) -> None:

    """

    Free Blender side memory of render engine

    """

    ...

  def tile_highlight_set(self, x: int, y: int, width: int, height: int, highlight: bool) -> None:

    """

    Set highlighted state of the given tile

    """

    ...

  def tile_highlight_clear_all(self) -> None:

    """

    Clear highlight from all tiles

    """

    ...

  def register_pass(self, scene: Scene, view_layer: ViewLayer, name: str, channels: int, chanid: str, type: str) -> None:

    """

    Register a render pass that will be part of the render with the current settings

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class RenderLayer(bpy_struct):

  name: str = ...

  """

  View layer name

  """

  passes: typing.Union[RenderPasses, typing.Sequence[RenderPass], typing.Mapping[str, RenderPass], bpy_prop_collection] = ...

  use_ao: bool = ...

  """

  Render Ambient Occlusion in this Layer

  """

  use_motion_blur: bool = ...

  """

  Render motion blur in this Layer, if enabled in the scene

  """

  use_pass_ambient_occlusion: bool = ...

  """

  Deliver Ambient Occlusion pass

  """

  use_pass_combined: bool = ...

  """

  Deliver full combined RGBA buffer

  """

  use_pass_diffuse_color: bool = ...

  """

  Deliver diffuse color pass

  """

  use_pass_diffuse_direct: bool = ...

  """

  Deliver diffuse direct pass

  """

  use_pass_diffuse_indirect: bool = ...

  """

  Deliver diffuse indirect pass

  """

  use_pass_emit: bool = ...

  """

  Deliver emission pass

  """

  use_pass_environment: bool = ...

  """

  Deliver environment lighting pass

  """

  use_pass_glossy_color: bool = ...

  """

  Deliver glossy color pass

  """

  use_pass_glossy_direct: bool = ...

  """

  Deliver glossy direct pass

  """

  use_pass_glossy_indirect: bool = ...

  """

  Deliver glossy indirect pass

  """

  use_pass_material_index: bool = ...

  """

  Deliver material index pass

  """

  use_pass_mist: bool = ...

  """

  Deliver mist factor pass (0.0 to 1.0)

  """

  use_pass_normal: bool = ...

  """

  Deliver normal pass

  """

  use_pass_object_index: bool = ...

  """

  Deliver object index pass

  """

  use_pass_position: bool = ...

  """

  Deliver position pass

  """

  use_pass_shadow: bool = ...

  """

  Deliver shadow pass

  """

  use_pass_subsurface_color: bool = ...

  """

  Deliver subsurface color pass

  """

  use_pass_subsurface_direct: bool = ...

  """

  Deliver subsurface direct pass

  """

  use_pass_subsurface_indirect: bool = ...

  """

  Deliver subsurface indirect pass

  """

  use_pass_transmission_color: bool = ...

  """

  Deliver transmission color pass

  """

  use_pass_transmission_direct: bool = ...

  """

  Deliver transmission direct pass

  """

  use_pass_transmission_indirect: bool = ...

  """

  Deliver transmission indirect pass

  """

  use_pass_uv: bool = ...

  """

  Deliver texture UV pass

  """

  use_pass_vector: bool = ...

  """

  Deliver speed vector pass

  """

  use_pass_z: bool = ...

  """

  Deliver Z values pass

  """

  use_sky: bool = ...

  """

  Render Sky in this Layer

  """

  use_solid: bool = ...

  """

  Render Solid faces in this Layer

  """

  use_strand: bool = ...

  """

  Render Strands in this Layer

  """

  use_volumes: bool = ...

  """

  Render volumes in this Layer

  """

  def load_from_file(self, filename: str, x: int = 0, y: int = 0) -> None:

    """

    Copies the pixels of this renderlayer from an image file

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class RenderPass(bpy_struct):

  channel_id: str = ...

  channels: int = ...

  fullname: str = ...

  name: str = ...

  rect: float = ...

  view_id: int = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class RenderPasses(bpy_struct):

  """

  Collection of render passes

  """

  def find_by_type(self, pass_type: str, view: str) -> RenderPass:

    """

    Get the render pass for a given type and view

    """

    ...

  def find_by_name(self, name: str, view: str) -> RenderPass:

    """

    Get the render pass for a given name and view

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class RenderResult(bpy_struct):

  """

  Result of rendering, including all layers and passes

  """

  layers: typing.Union[typing.Sequence[RenderLayer], typing.Mapping[str, RenderLayer], bpy_prop_collection] = ...

  resolution_x: int = ...

  resolution_y: int = ...

  views: typing.Union[typing.Sequence[RenderView], typing.Mapping[str, RenderView], bpy_prop_collection] = ...

  def load_from_file(self, filename: str) -> None:

    """

    Copies the pixels of this render result from an image file

    """

    ...

  def stamp_data_add_field(self, field: str, value: str) -> None:

    """

    Add engine-specific stamp data to the result

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class RenderSettings(bpy_struct):

  """

  Rendering settings for a Scene data-block

  """

  bake: BakeSettings = ...

  bake_bias: float = ...

  """

  Bias towards faces further away from the object (in blender units)

  """

  bake_margin: int = ...

  """

  Extends the baked result as a post process filter

  """

  bake_samples: int = ...

  """

  Number of samples used for ambient occlusion baking from multires

  """

  bake_type: str = ...

  """

  Choose shading information to bake into the image

  * ``NORMALS``
Normals -- Bake normals.

  * ``DISPLACEMENT``
Displacement -- Bake displacement.

  """

  bake_user_scale: float = ...

  """

  Instead of automatically normalizing to the range 0 to 1, apply a user scale to the derivative map

  """

  border_max_x: float = ...

  """

  Maximum X value for the render region

  """

  border_max_y: float = ...

  """

  Maximum Y value for the render region

  """

  border_min_x: float = ...

  """

  Minimum X value for the render region

  """

  border_min_y: float = ...

  """

  Minimum Y value for the render region

  """

  dither_intensity: float = ...

  """

  Amount of dithering noise added to the rendered image to break up banding

  """

  engine: str = ...

  """

  Engine to use for rendering

  """

  ffmpeg: FFmpegSettings = ...

  """

  FFmpeg related settings for the scene

  """

  file_extension: str = ...

  """

  The file extension used for saving renders

  """

  filepath: str = ...

  """

  Directory/name to save animations, # characters defines the position and length of frame numbers

  """

  film_transparent: bool = ...

  """

  World background is transparent, for compositing the render over another background

  """

  filter_size: float = ...

  """

  Width over which the reconstruction filter combines samples

  """

  fps: int = ...

  """

  Framerate, expressed in frames per second

  """

  fps_base: float = ...

  """

  Framerate base

  """

  frame_map_new: int = ...

  """

  How many frames the Map Old will last

  """

  frame_map_old: int = ...

  """

  Old mapping value in frames

  """

  hair_subdiv: int = ...

  """

  Additional subdivision along the hair

  """

  hair_type: str = ...

  """

  Hair shape type

  """

  has_multiple_engines: bool = ...

  """

  More than one rendering engine is available

  """

  image_settings: ImageFormatSettings = ...

  is_movie_format: bool = ...

  """

  When true the format is a movie

  """

  line_thickness: float = ...

  """

  Line thickness in pixels

  """

  line_thickness_mode: str = ...

  """

  Line thickness mode for Freestyle line drawing

  * ``ABSOLUTE``
Absolute -- Specify unit line thickness in pixels.

  * ``RELATIVE``
Relative -- Unit line thickness is scaled by the proportion of the present vertical image resolution to 480 pixels.

  """

  metadata_input: str = ...

  """

  Where to take the metadata from

  * ``SCENE``
Scene -- Use metadata from the current scene.

  * ``STRIPS``
Sequencer Strips -- Use metadata from the strips in the sequencer.

  """

  motion_blur_shutter: float = ...

  """

  Time taken in frames between shutter open and close

  """

  motion_blur_shutter_curve: CurveMapping = ...

  """

  Curve defining the shutter's openness over time

  """

  pixel_aspect_x: float = ...

  """

  Horizontal aspect ratio - for anamorphic or non-square pixel output

  """

  pixel_aspect_y: float = ...

  """

  Vertical aspect ratio - for anamorphic or non-square pixel output

  """

  preview_pixel_size: str = ...

  """

  Pixel size for viewport rendering

  * ``AUTO``
Automatic -- Automatic pixel size, depends on the user interface scale.

  * ``1``
1x -- Render at full resolution.

  * ``2``
2x -- Render at 50% resolution.

  * ``4``
4x -- Render at 25% resolution.

  * ``8``
8x -- Render at 12.5% resolution.

  """

  resolution_percentage: int = ...

  """

  Percentage scale for render resolution

  """

  resolution_x: int = ...

  """

  Number of horizontal pixels in the rendered image

  """

  resolution_y: int = ...

  """

  Number of vertical pixels in the rendered image

  """

  sequencer_gl_preview: str = ...

  """

  Display method used in the sequencer view

  * ``WIREFRAME``
Wireframe -- Display the object as wire edges.

  * ``SOLID``
Solid -- Display in solid mode.

  * ``MATERIAL``
Material Preview -- Display in Material Preview mode.

  * ``RENDERED``
Rendered -- Display render preview.

  """

  simplify_child_particles: float = ...

  """

  Global child particles percentage

  """

  simplify_child_particles_render: float = ...

  """

  Global child particles percentage during rendering

  """

  simplify_gpencil: bool = ...

  """

  Simplify Grease Pencil drawing

  """

  simplify_gpencil_antialiasing: bool = ...

  """

  Use Antialiasing to smooth stroke edges

  """

  simplify_gpencil_modifier: bool = ...

  """

  Display modifiers

  """

  simplify_gpencil_onplay: bool = ...

  """

  Simplify Grease Pencil only during animation playback

  """

  simplify_gpencil_shader_fx: bool = ...

  """

  Display Shader Effects

  """

  simplify_gpencil_tint: bool = ...

  """

  Display layer tint

  """

  simplify_gpencil_view_fill: bool = ...

  """

  Display fill strokes in the viewport

  """

  simplify_subdivision: int = ...

  """

  Global maximum subdivision level

  """

  simplify_subdivision_render: int = ...

  """

  Global maximum subdivision level during rendering

  """

  simplify_volumes: float = ...

  """

  Resolution percentage of volume objects in viewport

  """

  stamp_background: typing.Tuple[float, float, float, float] = ...

  """

  Color to use behind stamp text

  """

  stamp_font_size: int = ...

  """

  Size of the font used when rendering stamp text

  """

  stamp_foreground: typing.Tuple[float, float, float, float] = ...

  """

  Color to use for stamp text

  """

  stamp_note_text: str = ...

  """

  Custom text to appear in the stamp note

  """

  stereo_views: typing.Union[typing.Sequence[SceneRenderView], typing.Mapping[str, SceneRenderView], bpy_prop_collection] = ...

  threads: int = ...

  """

  Maximum number of CPU cores to use simultaneously while rendering (for multi-core/CPU systems)

  """

  threads_mode: str = ...

  """

  Determine the amount of render threads used

  * ``AUTO``
Auto-Detect -- Automatically determine the number of threads, based on CPUs.

  * ``FIXED``
Fixed -- Manually determine the number of threads.

  """

  use_bake_clear: bool = ...

  """

  Clear Images before baking

  """

  use_bake_lores_mesh: bool = ...

  """

  Calculate heights against unsubdivided low resolution mesh

  """

  use_bake_multires: bool = ...

  """

  Bake directly from multires object

  """

  use_bake_selected_to_active: bool = ...

  """

  Bake shading on the surface of selected objects to the active object

  """

  use_bake_user_scale: bool = ...

  """

  Use a user scale for the derivative map

  """

  use_border: bool = ...

  """

  Render a user-defined render region, within the frame size

  """

  use_compositing: bool = ...

  """

  Process the render result through the compositing pipeline, if compositing nodes are enabled

  """

  use_crop_to_border: bool = ...

  """

  Crop the rendered frame to the defined render region size

  """

  use_file_extension: bool = ...

  """

  Add the file format extensions to the rendered file name (eg: filename + .jpg)

  """

  use_freestyle: bool = ...

  """

  Draw stylized strokes using Freestyle

  """

  use_high_quality_normals: bool = ...

  """

  Use high quality tangent space at the cost of lower performance

  """

  use_lock_interface: bool = ...

  """

  Lock interface during rendering in favor of giving more memory to the renderer

  """

  use_motion_blur: bool = ...

  """

  Use multi-sampled 3D scene motion blur

  """

  use_multiview: bool = ...

  """

  Use multiple views in the scene

  """

  use_overwrite: bool = ...

  """

  Overwrite existing files while rendering

  """

  use_persistent_data: bool = ...

  """

  Keep render data around for faster re-renders and animation renders, at the cost of increased memory usage

  """

  use_placeholder: bool = ...

  """

  Create empty placeholder files while rendering frames (similar to Unix 'touch')

  """

  use_render_cache: bool = ...

  """

  Save render cache to EXR files (useful for heavy compositing, Note: affects indirectly rendered scenes)

  """

  use_sequencer: bool = ...

  """

  Process the render (and composited) result through the video sequence editor pipeline, if sequencer strips exist

  """

  use_sequencer_override_scene_strip: bool = ...

  """

  Use workbench render settings from the sequencer scene, instead of each individual scene used in the strip

  """

  use_simplify: bool = ...

  """

  Enable simplification of scene for quicker preview renders

  """

  use_single_layer: bool = ...

  """

  Only render the active layer. Only affects rendering from the interface, ignored for rendering from command line

  """

  use_spherical_stereo: bool = ...

  """

  Active render engine supports spherical stereo rendering

  """

  use_stamp: bool = ...

  """

  Render the stamp info text in the rendered image

  """

  use_stamp_camera: bool = ...

  """

  Include the name of the active camera in image metadata

  """

  use_stamp_date: bool = ...

  """

  Include the current date in image/video metadata

  """

  use_stamp_filename: bool = ...

  """

  Include the .blend filename in image/video metadata

  """

  use_stamp_frame: bool = ...

  """

  Include the frame number in image metadata

  """

  use_stamp_frame_range: bool = ...

  """

  Include the rendered frame range in image/video metadata

  """

  use_stamp_hostname: bool = ...

  """

  Include the hostname of the machine that rendered the frame

  """

  use_stamp_labels: bool = ...

  """

  Display stamp labels ("Camera" in front of camera name, etc.)

  """

  use_stamp_lens: bool = ...

  """

  Include the active camera's lens in image metadata

  """

  use_stamp_marker: bool = ...

  """

  Include the name of the last marker in image metadata

  """

  use_stamp_memory: bool = ...

  """

  Include the peak memory usage in image metadata

  """

  use_stamp_note: bool = ...

  """

  Include a custom note in image/video metadata

  """

  use_stamp_render_time: bool = ...

  """

  Include the render time in image metadata

  """

  use_stamp_scene: bool = ...

  """

  Include the name of the active scene in image/video metadata

  """

  use_stamp_sequencer_strip: bool = ...

  """

  Include the name of the foreground sequence strip in image metadata

  """

  use_stamp_time: bool = ...

  """

  Include the rendered frame timecode as HH:MM:SS.FF in image metadata

  """

  views: typing.Union[RenderViews, typing.Sequence[SceneRenderView], typing.Mapping[str, SceneRenderView], bpy_prop_collection] = ...

  views_format: str = ...

  """

  * ``STEREO_3D``
Stereo 3D -- Single stereo camera system, adjust the stereo settings in the camera panel.

  * ``MULTIVIEW``
Multi-View -- Multi camera system, adjust the cameras individually.

  """

  def frame_path(self, frame: int = -2147483648, preview: bool = False, view: str = '') -> str:

    """

    Return the absolute path to the filename to be written for a given frame

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class RenderSlot(bpy_struct):

  """

  Parameters defining the render slot

  """

  name: str = ...

  """

  Render slot name

  """

  def clear(self, iuser: ImageUser) -> None:

    """

    Clear the render slot

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class RenderSlots(bpy_struct):

  """

  Collection of render layers

  """

  active: RenderSlot = ...

  """

  Active render slot of the image

  """

  active_index: int = ...

  """

  Active render slot of the image

  """

  def new(self, name: str = '') -> RenderSlot:

    """

    Add a render slot to the image

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class RenderView(bpy_struct):

  name: str = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class RenderViews(bpy_struct):

  """

  Collection of render views

  """

  active: SceneRenderView = ...

  """

  Active Render View

  """

  active_index: int = ...

  """

  Active index in render view array

  """

  def new(self, name: str) -> SceneRenderView:

    """

    Add a render view to scene

    """

    ...

  def remove(self, view: SceneRenderView) -> None:

    """

    Remove a render view

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class RigidBodyConstraint(bpy_struct):

  """

  Constraint influencing Objects inside Rigid Body Simulation

  """

  breaking_threshold: float = ...

  """

  Impulse threshold that must be reached for the constraint to break

  """

  disable_collisions: bool = ...

  """

  Disable collisions between constrained rigid bodies

  """

  enabled: bool = ...

  """

  Enable this constraint

  """

  limit_ang_x_lower: float = ...

  """

  Lower limit of X axis rotation

  """

  limit_ang_x_upper: float = ...

  """

  Upper limit of X axis rotation

  """

  limit_ang_y_lower: float = ...

  """

  Lower limit of Y axis rotation

  """

  limit_ang_y_upper: float = ...

  """

  Upper limit of Y axis rotation

  """

  limit_ang_z_lower: float = ...

  """

  Lower limit of Z axis rotation

  """

  limit_ang_z_upper: float = ...

  """

  Upper limit of Z axis rotation

  """

  limit_lin_x_lower: float = ...

  """

  Lower limit of X axis translation

  """

  limit_lin_x_upper: float = ...

  """

  Upper limit of X axis translation

  """

  limit_lin_y_lower: float = ...

  """

  Lower limit of Y axis translation

  """

  limit_lin_y_upper: float = ...

  """

  Upper limit of Y axis translation

  """

  limit_lin_z_lower: float = ...

  """

  Lower limit of Z axis translation

  """

  limit_lin_z_upper: float = ...

  """

  Upper limit of Z axis translation

  """

  motor_ang_max_impulse: float = ...

  """

  Maximum angular motor impulse

  """

  motor_ang_target_velocity: float = ...

  """

  Target angular motor velocity

  """

  motor_lin_max_impulse: float = ...

  """

  Maximum linear motor impulse

  """

  motor_lin_target_velocity: float = ...

  """

  Target linear motor velocity

  """

  object1: Object = ...

  """

  First Rigid Body Object to be constrained

  """

  object2: Object = ...

  """

  Second Rigid Body Object to be constrained

  """

  solver_iterations: int = ...

  """

  Number of constraint solver iterations made per simulation step (higher values are more accurate but slower)

  """

  spring_damping_ang_x: float = ...

  """

  Damping on the X rotational axis

  """

  spring_damping_ang_y: float = ...

  """

  Damping on the Y rotational axis

  """

  spring_damping_ang_z: float = ...

  """

  Damping on the Z rotational axis

  """

  spring_damping_x: float = ...

  """

  Damping on the X axis

  """

  spring_damping_y: float = ...

  """

  Damping on the Y axis

  """

  spring_damping_z: float = ...

  """

  Damping on the Z axis

  """

  spring_stiffness_ang_x: float = ...

  """

  Stiffness on the X rotational axis

  """

  spring_stiffness_ang_y: float = ...

  """

  Stiffness on the Y rotational axis

  """

  spring_stiffness_ang_z: float = ...

  """

  Stiffness on the Z rotational axis

  """

  spring_stiffness_x: float = ...

  """

  Stiffness on the X axis

  """

  spring_stiffness_y: float = ...

  """

  Stiffness on the Y axis

  """

  spring_stiffness_z: float = ...

  """

  Stiffness on the Z axis

  """

  spring_type: str = ...

  """

  Which implementation of spring to use

  * ``SPRING1``
Blender 2.7 -- Spring implementation used in blender 2.7. Damping is capped at 1.0.

  * ``SPRING2``
Blender 2.8 -- New implementation available since 2.8.

  """

  type: str = ...

  """

  Type of Rigid Body Constraint

  * ``FIXED``
Fixed -- Glue rigid bodies together.

  * ``POINT``
Point -- Constrain rigid bodies to move around common pivot point.

  * ``HINGE``
Hinge -- Restrict rigid body rotation to one axis.

  * ``SLIDER``
Slider -- Restrict rigid body translation to one axis.

  * ``PISTON``
Piston -- Restrict rigid body translation and rotation to one axis.

  * ``GENERIC``
Generic -- Restrict translation and rotation to specified axes.

  * ``GENERIC_SPRING``
Generic Spring -- Restrict translation and rotation to specified axes with springs.

  * ``MOTOR``
Motor -- Drive rigid body around or along an axis.

  """

  use_breaking: bool = ...

  """

  Constraint can be broken if it receives an impulse above the threshold

  """

  use_limit_ang_x: bool = ...

  """

  Limit rotation around X axis

  """

  use_limit_ang_y: bool = ...

  """

  Limit rotation around Y axis

  """

  use_limit_ang_z: bool = ...

  """

  Limit rotation around Z axis

  """

  use_limit_lin_x: bool = ...

  """

  Limit translation on X axis

  """

  use_limit_lin_y: bool = ...

  """

  Limit translation on Y axis

  """

  use_limit_lin_z: bool = ...

  """

  Limit translation on Z axis

  """

  use_motor_ang: bool = ...

  """

  Enable angular motor

  """

  use_motor_lin: bool = ...

  """

  Enable linear motor

  """

  use_override_solver_iterations: bool = ...

  """

  Override the number of solver iterations for this constraint

  """

  use_spring_ang_x: bool = ...

  """

  Enable spring on X rotational axis

  """

  use_spring_ang_y: bool = ...

  """

  Enable spring on Y rotational axis

  """

  use_spring_ang_z: bool = ...

  """

  Enable spring on Z rotational axis

  """

  use_spring_x: bool = ...

  """

  Enable spring on X axis

  """

  use_spring_y: bool = ...

  """

  Enable spring on Y axis

  """

  use_spring_z: bool = ...

  """

  Enable spring on Z axis

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class RigidBodyObject(bpy_struct):

  """

  Settings for object participating in Rigid Body Simulation

  """

  angular_damping: float = ...

  """

  Amount of angular velocity that is lost over time

  """

  collision_collections: typing.Tuple[bool, ...] = ...

  """

  Collision collections rigid body belongs to

  """

  collision_margin: float = ...

  """

  Threshold of distance near surface where collisions are still considered (best results when non-zero)

  """

  collision_shape: str = ...

  """

  Collision Shape of object in Rigid Body Simulations

  * ``BOX``
Box -- Box-like shapes (i.e. cubes), including planes (i.e. ground planes).

  * ``SPHERE``
Sphere.

  * ``CAPSULE``
Capsule.

  * ``CYLINDER``
Cylinder.

  * ``CONE``
Cone.

  * ``CONVEX_HULL``
Convex Hull -- A mesh-like surface encompassing (i.e. shrinkwrap over) all vertices (best results with fewer vertices).

  * ``MESH``
Mesh -- Mesh consisting of triangles only, allowing for more detailed interactions than convex hulls.

  * ``COMPOUND``
Compound Parent -- Combines all of its direct rigid body children into one rigid object.

  """

  deactivate_angular_velocity: float = ...

  """

  Angular Velocity below which simulation stops simulating object

  """

  deactivate_linear_velocity: float = ...

  """

  Linear Velocity below which simulation stops simulating object

  """

  enabled: bool = ...

  """

  Rigid Body actively participates to the simulation

  """

  friction: float = ...

  """

  Resistance of object to movement

  """

  kinematic: bool = ...

  """

  Allow rigid body to be controlled by the animation system

  """

  linear_damping: float = ...

  """

  Amount of linear velocity that is lost over time

  """

  mass: float = ...

  """

  How much the object 'weighs' irrespective of gravity

  """

  mesh_source: str = ...

  """

  Source of the mesh used to create collision shape

  * ``BASE``
Base -- Base mesh.

  * ``DEFORM``
Deform -- Deformations (shape keys, deform modifiers).

  * ``FINAL``
Final -- All modifiers.

  """

  restitution: float = ...

  """

  Tendency of object to bounce after colliding with another (0 = stays still, 1 = perfectly elastic)

  """

  type: str = ...

  """

  Role of object in Rigid Body Simulations

  * ``ACTIVE``
Active -- Object is directly controlled by simulation results.

  * ``PASSIVE``
Passive -- Object is directly controlled by animation system.

  """

  use_deactivation: bool = ...

  """

  Enable deactivation of resting rigid bodies (increases performance and stability but can cause glitches)

  """

  use_deform: bool = ...

  """

  Rigid body deforms during simulation

  """

  use_margin: bool = ...

  """

  Use custom collision margin (some shapes will have a visible gap around them)

  """

  use_start_deactivated: bool = ...

  """

  Deactivate rigid body at the start of the simulation

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class RigidBodyWorld(bpy_struct):

  """

  Self-contained rigid body simulation environment and settings

  """

  collection: Collection = ...

  """

  Collection containing objects participating in this simulation

  """

  constraints: Collection = ...

  """

  Collection containing rigid body constraint objects

  """

  effector_weights: EffectorWeights = ...

  enabled: bool = ...

  """

  Simulation will be evaluated

  """

  point_cache: PointCache = ...

  solver_iterations: int = ...

  """

  Number of constraint solver iterations made per simulation step (higher values are more accurate but slower)

  """

  substeps_per_frame: int = ...

  """

  Number of simulation steps taken per frame (higher values are more accurate but slower)

  """

  time_scale: float = ...

  """

  Change the speed of the simulation

  """

  use_split_impulse: bool = ...

  """

  Reduce extra velocity that can build up when objects collide (lowers simulation stability a little so use only when necessary)

  """

  def convex_sweep_test(self, object: Object, start: typing.Tuple[float, float, float], end: typing.Tuple[float, float, float]) -> None:

    """

    Sweep test convex rigidbody against the current rigidbody world

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SceneDisplay(bpy_struct):

  """

  Scene display settings for 3D viewport

  """

  light_direction: typing.Tuple[float, float, float] = ...

  """

  Direction of the light for shadows and highlights

  """

  matcap_ssao_attenuation: float = ...

  """

  Attenuation constant

  """

  matcap_ssao_distance: float = ...

  """

  Distance of object that contribute to the Cavity/Edge effect

  """

  matcap_ssao_samples: int = ...

  """

  Number of samples

  """

  render_aa: str = ...

  """

  Method of anti-aliasing when rendering final image

  * ``OFF``
No Anti-Aliasing -- Scene will be rendering without any anti-aliasing.

  * ``FXAA``
Single Pass Anti-Aliasing -- Scene will be rendered using a single pass anti-aliasing method (FXAA).

  * ``5``
5 Samples -- Scene will be rendered using 5 anti-aliasing samples.

  * ``8``
8 Samples -- Scene will be rendered using 8 anti-aliasing samples.

  * ``11``
11 Samples -- Scene will be rendered using 11 anti-aliasing samples.

  * ``16``
16 Samples -- Scene will be rendered using 16 anti-aliasing samples.

  * ``32``
32 Samples -- Scene will be rendered using 32 anti-aliasing samples.

  """

  shading: View3DShading = ...

  """

  Shading settings for OpenGL render engine

  """

  shadow_focus: float = ...

  """

  Shadow factor hardness

  """

  shadow_shift: float = ...

  """

  Shadow termination angle

  """

  viewport_aa: str = ...

  """

  Method of anti-aliasing when rendering 3d viewport

  * ``OFF``
No Anti-Aliasing -- Scene will be rendering without any anti-aliasing.

  * ``FXAA``
Single Pass Anti-Aliasing -- Scene will be rendered using a single pass anti-aliasing method (FXAA).

  * ``5``
5 Samples -- Scene will be rendered using 5 anti-aliasing samples.

  * ``8``
8 Samples -- Scene will be rendered using 8 anti-aliasing samples.

  * ``11``
11 Samples -- Scene will be rendered using 11 anti-aliasing samples.

  * ``16``
16 Samples -- Scene will be rendered using 16 anti-aliasing samples.

  * ``32``
32 Samples -- Scene will be rendered using 32 anti-aliasing samples.

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SceneEEVEE(bpy_struct):

  """

  Scene display settings for 3D viewport

  """

  bloom_clamp: float = ...

  """

  Maximum intensity a bloom pixel can have (0 to disabled)

  """

  bloom_color: typing.Tuple[float, float, float] = ...

  """

  Color applied to the bloom effect

  """

  bloom_intensity: float = ...

  """

  Blend factor

  """

  bloom_knee: float = ...

  """

  Makes transition between under/over-threshold gradual

  """

  bloom_radius: float = ...

  """

  Bloom spread distance

  """

  bloom_threshold: float = ...

  """

  Filters out pixels under this level of brightness

  """

  bokeh_denoise_fac: float = ...

  """

  Amount of flicker removal applied to bokeh highlights

  """

  bokeh_max_size: float = ...

  """

  Max size of the bokeh shape for the depth of field (lower is faster)

  """

  bokeh_neighbor_max: float = ...

  """

  Maximum brightness to consider when rejecting bokeh sprites based on neighborhood (lower is faster)

  """

  bokeh_overblur: float = ...

  """

  Apply blur to each jittered sample to reduce under-sampling artifacts

  """

  bokeh_threshold: float = ...

  """

  Brightness threshold for using sprite base depth of field

  """

  gi_auto_bake: bool = ...

  """

  Auto bake indirect lighting when editing probes

  """

  gi_cache_info: str = ...

  """

  Info on current cache status

  """

  gi_cubemap_display_size: float = ...

  """

  Size of the cubemap spheres to debug captured light

  """

  gi_cubemap_resolution: str = ...

  """

  Size of every cubemaps

  """

  gi_diffuse_bounces: int = ...

  """

  Number of time the light is reinjected inside light grids, 0 disable indirect diffuse light

  """

  gi_filter_quality: float = ...

  """

  Take more samples during cubemap filtering to remove artifacts

  """

  gi_glossy_clamp: float = ...

  """

  Clamp pixel intensity to reduce noise inside glossy reflections from reflection cubemaps (0 to disabled)

  """

  gi_irradiance_display_size: float = ...

  """

  Size of the irradiance sample spheres to debug captured light

  """

  gi_irradiance_smoothing: float = ...

  """

  Smoother irradiance interpolation but introduce light bleeding

  """

  gi_show_cubemaps: bool = ...

  """

  Display captured cubemaps in the viewport

  """

  gi_show_irradiance: bool = ...

  """

  Display irradiance samples in the viewport

  """

  gi_visibility_resolution: str = ...

  """

  Size of the shadow map applied to each irradiance sample

  """

  gtao_distance: float = ...

  """

  Distance of object that contribute to the ambient occlusion effect

  """

  gtao_factor: float = ...

  """

  Factor for ambient occlusion blending

  """

  gtao_quality: float = ...

  """

  Precision of the horizon search

  """

  light_threshold: float = ...

  """

  Minimum light intensity for a light to contribute to the lighting

  """

  motion_blur_depth_scale: float = ...

  """

  Lower values will reduce background bleeding onto foreground elements

  """

  motion_blur_max: int = ...

  """

  Maximum blur distance a pixel can spread over

  """

  motion_blur_position: str = ...

  """

  Offset for the shutter's time interval, allows to change the motion blur trails

  * ``START``
Start on Frame -- The shutter opens at the current frame.

  * ``CENTER``
Center on Frame -- The shutter is open during the current frame.

  * ``END``
End on Frame -- The shutter closes at the current frame.

  """

  motion_blur_shutter: float = ...

  """

  Time taken in frames between shutter open and close

  """

  motion_blur_steps: int = ...

  """

  Controls accuracy of motion blur, more steps means longer render time

  """

  overscan_size: float = ...

  """

  Percentage of render size to add as overscan to the internal render buffers

  """

  shadow_cascade_size: str = ...

  """

  Size of sun light shadow maps

  """

  shadow_cube_size: str = ...

  """

  Size of point and area light shadow maps

  """

  ssr_border_fade: float = ...

  """

  Screen percentage used to fade the SSR

  """

  ssr_firefly_fac: float = ...

  """

  Clamp pixel intensity to remove noise (0 to disabled)

  """

  ssr_max_roughness: float = ...

  """

  Do not raytrace reflections for roughness above this value

  """

  ssr_quality: float = ...

  """

  Precision of the screen space raytracing

  """

  ssr_thickness: float = ...

  """

  Pixel thickness used to detect intersection

  """

  sss_jitter_threshold: float = ...

  """

  Rotate samples that are below this threshold

  """

  sss_samples: int = ...

  """

  Number of samples to compute the scattering effect

  """

  taa_render_samples: int = ...

  """

  Number of samples per pixels for rendering

  """

  taa_samples: int = ...

  """

  Number of samples, unlimited if 0

  """

  use_bloom: bool = ...

  """

  High brightness pixels generate a glowing effect

  """

  use_bokeh_high_quality_slight_defocus: bool = ...

  """

  Sample all pixels in almost in-focus regions to eliminate noise

  """

  use_bokeh_jittered: bool = ...

  """

  Jitter camera position to create accurate blurring using render samples

  """

  use_gtao: bool = ...

  """

  Enable ambient occlusion to simulate medium scale indirect shadowing

  """

  use_gtao_bent_normals: bool = ...

  """

  Compute main non occluded direction to sample the environment

  """

  use_gtao_bounce: bool = ...

  """

  An approximation to simulate light bounces giving less occlusion on brighter objects

  """

  use_motion_blur: bool = ...

  """

  Enable motion blur effect (only in camera view)

  """

  use_overscan: bool = ...

  """

  Internally render past the image border to avoid screen-space effects disappearing

  """

  use_shadow_high_bitdepth: bool = ...

  """

  Use 32-bit shadows

  """

  use_soft_shadows: bool = ...

  """

  Randomize shadowmaps origin to create soft shadows

  """

  use_ssr: bool = ...

  """

  Enable screen space reflection

  """

  use_ssr_halfres: bool = ...

  """

  Raytrace at a lower resolution

  """

  use_ssr_refraction: bool = ...

  """

  Enable screen space Refractions

  """

  use_taa_reprojection: bool = ...

  """

  Denoise image using temporal reprojection (can leave some ghosting)

  """

  use_volumetric_lights: bool = ...

  """

  Enable scene light interactions with volumetrics

  """

  use_volumetric_shadows: bool = ...

  """

  Generate shadows from volumetric material (Very expensive)

  """

  volumetric_end: float = ...

  """

  End distance of the volumetric effect

  """

  volumetric_light_clamp: float = ...

  """

  Maximum light contribution, reducing noise

  """

  volumetric_sample_distribution: float = ...

  """

  Distribute more samples closer to the camera

  """

  volumetric_samples: int = ...

  """

  Number of samples to compute volumetric effects

  """

  volumetric_shadow_samples: int = ...

  """

  Number of samples to compute volumetric shadowing

  """

  volumetric_start: float = ...

  """

  Start distance of the volumetric effect

  """

  volumetric_tile_size: str = ...

  """

  Control the quality of the volumetric effects (lower size increase vram usage and quality)

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SceneGpencil(bpy_struct):

  """

  Render settings

  """

  antialias_threshold: float = ...

  """

  Threshold for edge detection algorithm (higher values might over-blur some part of the image)

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SceneObjects(bpy_struct):

  """

  All of the scene objects

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SceneRenderView(bpy_struct):

  """

  Render viewpoint for 3D stereo and multiview rendering

  """

  camera_suffix: str = ...

  """

  Suffix to identify the cameras to use, and added to the render images for this view

  """

  file_suffix: str = ...

  """

  Suffix added to the render images for this view

  """

  name: str = ...

  """

  Render view name

  """

  use: bool = ...

  """

  Disable or enable the render view

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Scopes(bpy_struct):

  """

  Scopes for statistical view of an image

  """

  accuracy: float = ...

  """

  Proportion of original image source pixel lines to sample

  """

  histogram: Histogram = ...

  """

  Histogram for viewing image statistics

  """

  use_full_resolution: bool = ...

  """

  Sample every pixel of the image

  """

  vectorscope_alpha: float = ...

  """

  Opacity of the points

  """

  waveform_alpha: float = ...

  """

  Opacity of the points

  """

  waveform_mode: str = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Sequence(bpy_struct):

  """

  Sequence strip in the sequence editor

  """

  blend_alpha: float = ...

  """

  Percentage of how much the strip's colors affect other strips

  """

  blend_type: str = ...

  """

  Method for controlling how the strip combines with other strips

  """

  channel: int = ...

  """

  Y position of the sequence strip

  """

  color_tag: str = ...

  """

  Color tag for a strip

  * ``NONE``
None -- Assign no color tag to the collection.

  * ``COLOR_01``
Color 01.

  * ``COLOR_02``
Color 02.

  * ``COLOR_03``
Color 03.

  * ``COLOR_04``
Color 04.

  * ``COLOR_05``
Color 05.

  * ``COLOR_06``
Color 06.

  * ``COLOR_07``
Color 07.

  * ``COLOR_08``
Color 08.

  * ``COLOR_09``
Color 09.

  """

  effect_fader: float = ...

  """

  Custom fade value

  """

  frame_duration: int = ...

  """

  The length of the contents of this strip before the handles are applied

  """

  frame_final_duration: int = ...

  """

  The length of the contents of this strip after the handles are applied

  """

  frame_final_end: int = ...

  """

  End frame displayed in the sequence editor after offsets are applied

  """

  frame_final_start: int = ...

  """

  Start frame displayed in the sequence editor after offsets are applied, setting this is equivalent to moving the handle, not the actual start frame

  """

  frame_offset_end: int = ...

  frame_offset_start: int = ...

  frame_start: int = ...

  """

  X position where the strip begins

  """

  frame_still_end: int = ...

  frame_still_start: int = ...

  lock: bool = ...

  """

  Lock strip so that it cannot be transformed

  """

  modifiers: typing.Union[SequenceModifiers, typing.Sequence[SequenceModifier], typing.Mapping[str, SequenceModifier], bpy_prop_collection] = ...

  """

  Modifiers affecting this strip

  """

  mute: bool = ...

  """

  Disable strip so that it cannot be viewed in the output

  """

  name: str = ...

  override_cache_settings: bool = ...

  """

  Override global cache settings

  """

  select: bool = ...

  select_left_handle: bool = ...

  select_right_handle: bool = ...

  type: str = ...

  use_cache_composite: bool = ...

  """

  Cache intermediate composited images, for faster tweaking of stacked strips at the cost of memory usage

  """

  use_cache_preprocessed: bool = ...

  """

  Cache preprocessed images, for faster tweaking of effects at the cost of memory usage

  """

  use_cache_raw: bool = ...

  """

  Cache raw images read from disk, for faster tweaking of strip parameters at the cost of memory usage

  """

  use_default_fade: bool = ...

  """

  Fade effect using the built-in default (usually make transition as long as effect strip)

  """

  use_linear_modifiers: bool = ...

  """

  Calculate modifiers in linear space instead of sequencer's space

  """

  def update(self, data: bool = False) -> None:

    """

    Update the strip dimensions

    """

    ...

  def strip_elem_from_frame(self, frame: int) -> SequenceElement:

    """

    Return the strip element from a given frame or None

    """

    ...

  def swap(self, other: Sequence) -> None:

    """

    swap

    """

    ...

  def move_to_meta(self, meta_sequence: Sequence) -> None:

    """

    move_to_meta

    """

    ...

  def parent_meta(self) -> Sequence:

    """

    Parent meta

    """

    ...

  def invalidate_cache(self, type: str) -> None:

    """

    Invalidate cached images for strip and all dependent strips

    """

    ...

  def split(self, frame: int, split_method: str) -> Sequence:

    """

    Split Sequence

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SequenceColorBalanceData(bpy_struct):

  """

  Color balance parameters for a sequence strip and its modifiers

  """

  correction_method: str = ...

  """

  * ``LIFT_GAMMA_GAIN``
Lift/Gamma/Gain.

  * ``OFFSET_POWER_SLOPE``
Offset/Power/Slope (ASC-CDL) -- ASC-CDL standard color correction.

  """

  gain: typing.Tuple[float, float, float] = ...

  """

  Color balance gain (highlights)

  """

  gamma: typing.Tuple[float, float, float] = ...

  """

  Color balance gamma (midtones)

  """

  invert_gain: bool = ...

  """

  Invert the gain color`

  """

  invert_gamma: bool = ...

  """

  Invert the gamma color

  """

  invert_lift: bool = ...

  """

  Invert the lift color

  """

  invert_offset: bool = ...

  """

  Invert the offset color

  """

  invert_power: bool = ...

  """

  Invert the power color

  """

  invert_slope: bool = ...

  """

  Invert the slope color`

  """

  lift: typing.Tuple[float, float, float] = ...

  """

  Color balance lift (shadows)

  """

  offset: typing.Tuple[float, float, float] = ...

  """

  Correction for entire tonal range

  """

  power: typing.Tuple[float, float, float] = ...

  """

  Correction for midtones

  """

  slope: typing.Tuple[float, float, float] = ...

  """

  Correction for highlights

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SequenceCrop(bpy_struct):

  """

  Cropping parameters for a sequence strip

  """

  max_x: int = ...

  """

  Number of pixels to crop from the right side

  """

  max_y: int = ...

  """

  Number of pixels to crop from the top

  """

  min_x: int = ...

  """

  Number of pixels to crop from the left side

  """

  min_y: int = ...

  """

  Number of pixels to crop from the bottom

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SequenceEditor(bpy_struct):

  """

  Sequence editing data for a Scene data-block

  """

  active_strip: Sequence = ...

  """

  Sequencer's active strip

  """

  meta_stack: typing.Union[typing.Sequence[Sequence], typing.Mapping[str, Sequence], bpy_prop_collection] = ...

  """

  Meta strip stack, last is currently edited meta strip

  """

  overlay_frame: int = ...

  """

  Number of frames to offset

  """

  proxy_dir: str = ...

  proxy_storage: str = ...

  """

  How to store proxies for this project

  * ``PER_STRIP``
Per Strip -- Store proxies using per strip settings.

  * ``PROJECT``
Project -- Store proxies using project directory.

  """

  sequences: typing.Union[SequencesTopLevel, typing.Sequence[Sequence], typing.Mapping[str, Sequence], bpy_prop_collection] = ...

  """

  Top-level strips only

  """

  sequences_all: typing.Union[typing.Sequence[Sequence], typing.Mapping[str, Sequence], bpy_prop_collection] = ...

  """

  All strips, recursively including those inside metastrips

  """

  show_cache: bool = ...

  """

  Visualize cached images on the timeline

  """

  show_cache_composite: bool = ...

  """

  Visualize cached composite images

  """

  show_cache_final_out: bool = ...

  """

  Visualize cached complete frames

  """

  show_cache_preprocessed: bool = ...

  """

  Visualize cached pre-processed images

  """

  show_cache_raw: bool = ...

  """

  Visualize cached raw images

  """

  show_overlay_frame: bool = ...

  """

  Partial overlay on top of the sequencer with a frame offset

  """

  use_cache_composite: bool = ...

  """

  Cache intermediate composited images, for faster tweaking of stacked strips at the cost of memory usage

  """

  use_cache_final: bool = ...

  """

  Cache final image for each frame

  """

  use_cache_preprocessed: bool = ...

  """

  Cache pre-processed images, for faster tweaking of effects at the cost of memory usage

  """

  use_cache_raw: bool = ...

  """

  Cache raw images read from disk, for faster tweaking of strip parameters at the cost of memory usage

  """

  use_overlay_frame_lock: bool = ...

  use_prefetch: bool = ...

  """

  Render frames ahead of current frame in the background for faster playback

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SequenceElement(bpy_struct):

  """

  Sequence strip data for a single frame

  """

  filename: str = ...

  """

  Name of the source file

  """

  orig_fps: float = ...

  """

  Original frames per second

  """

  orig_height: int = ...

  """

  Original image height

  """

  orig_width: int = ...

  """

  Original image width

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SequenceElements(bpy_struct):

  """

  Collection of SequenceElement

  """

  def append(self, filename: str) -> SequenceElement:

    """

    Push an image from ImageSequence.directory

    """

    ...

  def pop(self, index: int) -> None:

    """

    Pop an image off the collection

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SequenceModifier(bpy_struct):

  """

  Modifier for sequence strip

  """

  input_mask_id: Mask = ...

  """

  Mask ID used as mask input for the modifier

  """

  input_mask_strip: Sequence = ...

  """

  Strip used as mask input for the modifier

  """

  input_mask_type: str = ...

  """

  Type of input data used for mask

  * ``STRIP``
Strip -- Use sequencer strip as mask input.

  * ``ID``
Mask -- Use mask ID as mask input.

  """

  mask_time: str = ...

  """

  Time to use for the Mask animation

  * ``RELATIVE``
Relative -- Mask animation is offset to start of strip.

  * ``ABSOLUTE``
Absolute -- Mask animation is in sync with scene frame.

  """

  mute: bool = ...

  """

  Mute this modifier

  """

  name: str = ...

  show_expanded: bool = ...

  """

  Mute expanded settings for the modifier

  """

  type: str = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SequenceModifiers(bpy_struct):

  """

  Collection of strip modifiers

  """

  def new(self, name: str, type: str) -> SequenceModifier:

    """

    Add a new modifier

    """

    ...

  def remove(self, modifier: SequenceModifier) -> None:

    """

    Remove an existing modifier from the sequence

    """

    ...

  def clear(self) -> None:

    """

    Remove all modifiers from the sequence

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SequenceProxy(bpy_struct):

  """

  Proxy parameters for a sequence strip

  """

  build_100: bool = ...

  """

  Build 100% proxy resolution

  """

  build_25: bool = ...

  """

  Build 25% proxy resolution

  """

  build_50: bool = ...

  """

  Build 50% proxy resolution

  """

  build_75: bool = ...

  """

  Build 75% proxy resolution

  """

  build_free_run: bool = ...

  """

  Build free run time code index

  """

  build_free_run_rec_date: bool = ...

  """

  Build free run time code index using Record Date/Time

  """

  build_record_run: bool = ...

  """

  Build record run time code index

  """

  directory: str = ...

  """

  Location to store the proxy files

  """

  filepath: str = ...

  """

  Location of custom proxy file

  """

  quality: int = ...

  """

  Quality of proxies to build

  """

  timecode: str = ...

  """

  Method for reading the inputs timecode

  * ``NONE``
None.

  * ``RECORD_RUN``
Record Run -- Use images in the order as they are recorded.

  * ``FREE_RUN``
Free Run -- Use global timestamp written by recording device.

  * ``FREE_RUN_REC_DATE``
Free Run (rec date) -- Interpolate a global timestamp using the record date and time written by recording device.

  * ``RECORD_RUN_NO_GAPS``
Record Run No Gaps -- Like record run, but ignore timecode, changes in framerate or dropouts.

  """

  use_overwrite: bool = ...

  """

  Overwrite existing proxy files when building

  """

  use_proxy_custom_directory: bool = ...

  """

  Use a custom directory to store data

  """

  use_proxy_custom_file: bool = ...

  """

  Use a custom file to read proxy data from

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SequencerPreviewOverlay(bpy_struct):

  show_annotation: bool = ...

  """

  Show annotations for this view

  """

  show_cursor: bool = ...

  show_image_outline: bool = ...

  show_metadata: bool = ...

  """

  Show metadata of first visible strip

  """

  show_safe_areas: bool = ...

  """

  Show TV title safe and action safe areas in preview

  """

  show_safe_center: bool = ...

  """

  Show safe areas to fit content in a different aspect ratio

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SequencerTimelineOverlay(bpy_struct):

  show_fcurves: bool = ...

  """

  Display strip opacity/volume curve

  """

  show_grid: bool = ...

  """

  Show vertical grid lines

  """

  show_strip_duration: bool = ...

  show_strip_name: bool = ...

  show_strip_offset: bool = ...

  """

  Display strip in/out offsets

  """

  show_strip_source: bool = ...

  """

  Display path to source file, or name of source datablock

  """

  show_strip_tag_color: bool = ...

  """

  Display the strip color tags in the sequencer

  """

  show_thumbnails: bool = ...

  """

  Show strip thumbnails

  """

  waveform_display_type: str = ...

  """

  How Waveforms are displayed

  * ``NO_WAVEFORMS``
Waveforms Off -- Don't display waveforms for any sound strips.

  * ``ALL_WAVEFORMS``
Waveforms On -- Display waveforms for all sound strips.

  * ``DEFAULT_WAVEFORMS``
Use Strip Option -- Display waveforms depending on strip setting.

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SequencerToolSettings(bpy_struct):

  fit_method: str = ...

  """

  Scale fit method

  * ``FIT``
Scale to Fit -- Scale image to fit within the canvas.

  * ``FILL``
Scale to Fill -- Scale image to completely fill the canvas.

  * ``STRETCH``
Stretch to Fill -- Stretch image to fill the canvas.

  * ``ORIGINAL``
Use Original Size -- Keep image at its original size.

  """

  overlap_mode: str = ...

  """

  How to resolve overlap after transformation

  * ``EXPAND``
Expand -- Move strips so transformed strips fits.

  * ``OVERWRITE``
Overwrite -- Trim or split strips to resolve overlap.

  * ``SHUFFLE``
Shuffle -- Move transformed strips to nearest free space to resolve overlap.

  """

  pivot_point: str = ...

  """

  Rotation or scaling pivot point

  * ``CENTER``
Bounding Box Center.

  * ``MEDIAN``
Median Point.

  * ``CURSOR``
2D Cursor -- Pivot around the 2D cursor.

  * ``INDIVIDUAL_ORIGINS``
Individual Origins -- Pivot around each selected island's own median point.

  """

  snap_distance: int = ...

  """

  Maximum distance for snapping in pixels

  """

  snap_ignore_muted: bool = ...

  """

  Don't snap to hidden strips

  """

  snap_ignore_sound: bool = ...

  """

  Don't snap to sound strips

  """

  snap_to_current_frame: bool = ...

  """

  Snap to current frame

  """

  snap_to_hold_offset: bool = ...

  """

  Snap to strip hold offsets

  """

  use_snap_current_frame_to_strips: bool = ...

  """

  Snap current frame to strip start or end

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SequencesMeta(bpy_struct):

  """

  Collection of Sequences

  """

  def new_clip(self, name: str, clip: MovieClip, channel: int, frame_start: int) -> Sequence:

    """

    Add a new movie clip sequence

    """

    ...

  def new_mask(self, name: str, mask: Mask, channel: int, frame_start: int) -> Sequence:

    """

    Add a new mask sequence

    """

    ...

  def new_scene(self, name: str, scene: Scene, channel: int, frame_start: int) -> Sequence:

    """

    Add a new scene sequence

    """

    ...

  def new_image(self, name: str, filepath: str, channel: int, frame_start: int, fit_method: str = 'ORIGINAL') -> Sequence:

    """

    Add a new image sequence

    """

    ...

  def new_movie(self, name: str, filepath: str, channel: int, frame_start: int, fit_method: str = 'ORIGINAL') -> Sequence:

    """

    Add a new movie sequence

    """

    ...

  def new_sound(self, name: str, filepath: str, channel: int, frame_start: int) -> Sequence:

    """

    Add a new sound sequence

    """

    ...

  def new_meta(self, name: str, channel: int, frame_start: int) -> Sequence:

    """

    Add a new meta sequence

    """

    ...

  def new_effect(self, name: str, type: str, channel: int, frame_start: int, frame_end: int = 0, seq1: Sequence = None, seq2: Sequence = None, seq3: Sequence = None) -> Sequence:

    """

    Add a new effect sequence

    """

    ...

  def remove(self, sequence: Sequence) -> None:

    """

    Remove a Sequence

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SequencesTopLevel(bpy_struct):

  """

  Collection of Sequences

  """

  def new_clip(self, name: str, clip: MovieClip, channel: int, frame_start: int) -> Sequence:

    """

    Add a new movie clip sequence

    """

    ...

  def new_mask(self, name: str, mask: Mask, channel: int, frame_start: int) -> Sequence:

    """

    Add a new mask sequence

    """

    ...

  def new_scene(self, name: str, scene: Scene, channel: int, frame_start: int) -> Sequence:

    """

    Add a new scene sequence

    """

    ...

  def new_image(self, name: str, filepath: str, channel: int, frame_start: int, fit_method: str = 'ORIGINAL') -> Sequence:

    """

    Add a new image sequence

    """

    ...

  def new_movie(self, name: str, filepath: str, channel: int, frame_start: int, fit_method: str = 'ORIGINAL') -> Sequence:

    """

    Add a new movie sequence

    """

    ...

  def new_sound(self, name: str, filepath: str, channel: int, frame_start: int) -> Sequence:

    """

    Add a new sound sequence

    """

    ...

  def new_meta(self, name: str, channel: int, frame_start: int) -> Sequence:

    """

    Add a new meta sequence

    """

    ...

  def new_effect(self, name: str, type: str, channel: int, frame_start: int, frame_end: int = 0, seq1: Sequence = None, seq2: Sequence = None, seq3: Sequence = None) -> Sequence:

    """

    Add a new effect sequence

    """

    ...

  def remove(self, sequence: Sequence) -> None:

    """

    Remove a Sequence

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SequenceTransform(bpy_struct):

  """

  Transform parameters for a sequence strip

  """

  offset_x: int = ...

  """

  Move along X axis

  """

  offset_y: int = ...

  """

  Move along Y axis

  """

  origin: typing.Tuple[float, float] = ...

  """

  Origin of image for transformation

  """

  rotation: float = ...

  """

  Rotate around image center

  """

  scale_x: float = ...

  """

  Scale along X axis

  """

  scale_y: float = ...

  """

  Scale along Y axis

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ShaderFx(bpy_struct):

  """

  Effect affecting the grease pencil object

  """

  name: str = ...

  """

  Effect name

  """

  show_expanded: bool = ...

  """

  Set effect expansion in the user interface

  """

  show_in_editmode: bool = ...

  """

  Display effect in Edit mode

  """

  show_render: bool = ...

  """

  Use effect during render

  """

  show_viewport: bool = ...

  """

  Display effect in viewport

  """

  type: str = ...

  """

  * ``FX_BLUR``
Blur -- Apply Gaussian Blur to object.

  * ``FX_COLORIZE``
Colorize -- Apply different tint effects.

  * ``FX_FLIP``
Flip -- Flip image.

  * ``FX_GLOW``
Glow -- Create a glow effect.

  * ``FX_PIXEL``
Pixelate -- Pixelate image.

  * ``FX_RIM``
Rim -- Add a rim to the image.

  * ``FX_SHADOW``
Shadow -- Create a shadow effect.

  * ``FX_SWIRL``
Swirl -- Create a rotation distortion.

  * ``FX_WAVE``
Wave Distortion -- Apply sinusoidal deformation.

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ShapeKey(bpy_struct):

  """

  Shape key in a shape keys data-block

  """

  data: typing.Union[typing.Sequence[UnknownType], typing.Mapping[str, UnknownType], bpy_prop_collection] = ...

  frame: float = ...

  """

  Frame for absolute keys

  """

  interpolation: str = ...

  """

  Interpolation type for absolute shape keys

  """

  mute: bool = ...

  """

  Toggle this shape key

  """

  name: str = ...

  """

  Name of Shape Key

  """

  relative_key: ShapeKey = ...

  """

  Shape used as a relative key

  """

  slider_max: float = ...

  """

  Maximum for slider

  """

  slider_min: float = ...

  """

  Minimum for slider

  """

  value: float = ...

  """

  Value of shape key at the current frame

  """

  vertex_group: str = ...

  """

  Vertex weight group, to blend with basis shape

  """

  def normals_vertex_get(self) -> float:

    """

    Compute local space vertices' normals for this shape key

    """

    ...

  def normals_polygon_get(self) -> float:

    """

    Compute local space faces' normals for this shape key

    """

    ...

  def normals_split_get(self) -> float:

    """

    Compute local space face corners' normals for this shape key

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ShapeKeyBezierPoint(bpy_struct):

  """

  Point in a shape key for Bezier curves

  """

  co: typing.Tuple[float, float, float] = ...

  handle_left: typing.Tuple[float, float, float] = ...

  handle_right: typing.Tuple[float, float, float] = ...

  radius: float = ...

  """

  Radius for beveling

  """

  tilt: float = ...

  """

  Tilt in 3D View

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ShapeKeyCurvePoint(bpy_struct):

  """

  Point in a shape key for curves

  """

  co: typing.Tuple[float, float, float] = ...

  radius: float = ...

  """

  Radius for beveling

  """

  tilt: float = ...

  """

  Tilt in 3D View

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ShapeKeyPoint(bpy_struct):

  """

  Point in a shape key

  """

  co: typing.Tuple[float, float, float] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SoftBodySettings(bpy_struct):

  """

  Soft body simulation settings for an object

  """

  aero: int = ...

  """

  Make edges 'sail'

  """

  aerodynamics_type: str = ...

  """

  Method of calculating aerodynamic interaction

  * ``SIMPLE``
Simple -- Edges receive a drag force from surrounding media.

  * ``LIFT_FORCE``
Lift Force -- Edges receive a lift force when passing through surrounding media.

  """

  ball_damp: float = ...

  """

  Blending to inelastic collision

  """

  ball_size: float = ...

  """

  Absolute ball size or factor if not manually adjusted

  """

  ball_stiff: float = ...

  """

  Ball inflating pressure

  """

  bend: float = ...

  """

  Bending Stiffness

  """

  choke: int = ...

  """

  'Viscosity' inside collision target

  """

  collision_collection: Collection = ...

  """

  Limit colliders to this collection

  """

  collision_type: str = ...

  """

  Choose Collision Type

  * ``MANUAL``
Manual -- Manual adjust.

  * ``AVERAGE``
Average -- Average Spring length * Ball Size.

  * ``MINIMAL``
Minimal -- Minimal Spring length * Ball Size.

  * ``MAXIMAL``
Maximal -- Maximal Spring length * Ball Size.

  * ``MINMAX``
AvMinMax -- (Min+Max)/2 * Ball Size.

  """

  damping: float = ...

  """

  Edge spring friction

  """

  effector_weights: EffectorWeights = ...

  error_threshold: float = ...

  """

  The Runge-Kutta ODE solver error limit, low value gives more precision, high values speed

  """

  friction: float = ...

  """

  General media friction for point movements

  """

  fuzzy: int = ...

  """

  Fuzziness while on collision, high values make collision handling faster but less stable

  """

  goal_default: float = ...

  """

  Default Goal (vertex target position) value

  """

  goal_friction: float = ...

  """

  Goal (vertex target position) friction

  """

  goal_max: float = ...

  """

  Goal maximum, vertex weights are scaled to match this range

  """

  goal_min: float = ...

  """

  Goal minimum, vertex weights are scaled to match this range

  """

  goal_spring: float = ...

  """

  Goal (vertex target position) spring stiffness

  """

  gravity: float = ...

  """

  Apply gravitation to point movement

  """

  location_mass_center: typing.Tuple[float, float, float] = ...

  """

  Location of center of mass

  """

  mass: float = ...

  """

  General Mass value

  """

  plastic: int = ...

  """

  Permanent deform

  """

  pull: float = ...

  """

  Edge spring stiffness when longer than rest length

  """

  push: float = ...

  """

  Edge spring stiffness when shorter than rest length

  """

  rotation_estimate: typing.Tuple[typing.Tuple[float, float, float], typing.Tuple[float, float, float], typing.Tuple[float, float, float]] = ...

  """

  Estimated rotation matrix

  """

  scale_estimate: typing.Tuple[typing.Tuple[float, float, float], typing.Tuple[float, float, float], typing.Tuple[float, float, float]] = ...

  """

  Estimated scale matrix

  """

  shear: float = ...

  """

  Shear Stiffness

  """

  speed: float = ...

  """

  Tweak timing for physics to control frequency and speed

  """

  spring_length: int = ...

  """

  Alter spring length to shrink/blow up (unit %) 0 to disable

  """

  step_max: int = ...

  """

  Maximal # solver steps/frame

  """

  step_min: int = ...

  """

  Minimal # solver steps/frame

  """

  use_auto_step: bool = ...

  """

  Use velocities for automagic step sizes

  """

  use_diagnose: bool = ...

  """

  Turn on SB diagnose console prints

  """

  use_edge_collision: bool = ...

  """

  Edges collide too

  """

  use_edges: bool = ...

  """

  Use Edges as springs

  """

  use_estimate_matrix: bool = ...

  """

  Store the estimated transforms in the soft body settings

  """

  use_face_collision: bool = ...

  """

  Faces collide too, can be very slow

  """

  use_goal: bool = ...

  """

  Define forces for vertices to stick to animated position

  """

  use_self_collision: bool = ...

  """

  Enable naive vertex ball self collision

  """

  use_stiff_quads: bool = ...

  """

  Add diagonal springs on 4-gons

  """

  vertex_group_goal: str = ...

  """

  Control point weight values

  """

  vertex_group_mass: str = ...

  """

  Control point mass values

  """

  vertex_group_spring: str = ...

  """

  Control point spring strength values

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Space(bpy_struct):

  """

  Space data for a screen area

  """

  show_locked_time: bool = ...

  """

  Synchronize the visible timeline range with other time-based editors

  """

  show_region_header: bool = ...

  type: str = ...

  """

  Space data type

  * ``EMPTY``
Empty.

  * ``VIEW_3D``
3D Viewport -- Manipulate objects in a 3D environment.

  * ``IMAGE_EDITOR``
UV/Image Editor -- View and edit images and UV Maps.

  * ``NODE_EDITOR``
Node Editor -- Editor for node-based shading and compositing tools.

  * ``SEQUENCE_EDITOR``
Video Sequencer -- Video editing tools.

  * ``CLIP_EDITOR``
Movie Clip Editor -- Motion tracking tools.

  * ``DOPESHEET_EDITOR``
Dope Sheet -- Adjust timing of keyframes.

  * ``GRAPH_EDITOR``
Graph Editor -- Edit drivers and keyframe interpolation.

  * ``NLA_EDITOR``
Nonlinear Animation -- Combine and layer Actions.

  * ``TEXT_EDITOR``
Text Editor -- Edit scripts and in-file documentation.

  * ``CONSOLE``
Python Console -- Interactive programmatic console for advanced editing and script development.

  * ``INFO``
Info -- Log of operations, warnings and error messages.

  * ``TOPBAR``
Top Bar -- Global bar at the top of the screen for global per-window settings.

  * ``STATUSBAR``
Status Bar -- Global bar at the bottom of the screen for general status information.

  * ``OUTLINER``
Outliner -- Overview of scene graph and all available data-blocks.

  * ``PROPERTIES``
Properties -- Edit properties of active object and related data-blocks.

  * ``FILE_BROWSER``
File Browser -- Browse for files and assets.

  * ``SPREADSHEET``
Spreadsheet -- Explore geometry data in a table.

  * ``PREFERENCES``
Preferences -- Edit persistent configuration settings.

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

  def draw_handler_add(self, callback: typing.Callable, args: typing.Tuple[typing.Any, ...], region_type: str, draw_type: str) -> Object:

    """

    Add a new draw handler to this space type.
It will be called every time the specified region in the space type will be drawn.
Note: All arguments are positional only for now.

    """

    ...

  def draw_handler_remove(self, handler: Object, region_type: str) -> None:

    """

    Remove a draw handler that was added previously.

    """

    ...

class SpaceImageOverlay(bpy_struct):

  """

  Settings for display of overlays in the UV/Image editor

  """

  show_overlays: bool = ...

  """

  Display overlays like UV Maps and Metadata

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SpaceNodeEditorPath(bpy_struct):

  """

  Get the node tree path as a string

  """

  to_string: str = ...

  def clear(self) -> None:

    """

    Reset the node tree path

    """

    ...

  def start(self, node_tree: NodeTree) -> None:

    """

    Set the root node tree

    """

    ...

  def append(self, node_tree: NodeTree, node: Node = None) -> None:

    """

    Append a node group tree to the path

    """

    ...

  def pop(self) -> None:

    """

    Remove the last node tree from the path

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SpaceNodeOverlay(bpy_struct):

  """

  Settings for display of overlays in the Node Editor

  """

  show_overlays: bool = ...

  """

  Display overlays like colored or dashed wires

  """

  show_wire_color: bool = ...

  """

  Color node links based on their connected sockets

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SpaceUVEditor(bpy_struct):

  """

  UV editor data for the image editor space

  """

  custom_grid_subdivisions: int = ...

  """

  Number of grid units in UV space that make one UV Unit

  """

  display_stretch_type: str = ...

  """

  Type of stretch to display

  * ``ANGLE``
Angle -- Angular distortion between UV and 3D angles.

  * ``AREA``
Area -- Area distortion between UV and 3D faces.

  """

  edge_display_type: str = ...

  """

  Display style for UV edges

  * ``OUTLINE``
Outline -- Display white edges with black outline.

  * ``DASH``
Dash -- Display dashed black-white edges.

  * ``BLACK``
Black -- Display black edges.

  * ``WHITE``
White -- Display white edges.

  """

  lock_bounds: bool = ...

  """

  Constraint to stay within the image bounds while editing

  """

  pixel_snap_mode: str = ...

  """

  Snap UVs to pixels while editing

  * ``DISABLED``
Disabled -- Don't snap to pixels.

  * ``CORNER``
Corner -- Snap to pixel corners.

  * ``CENTER``
Center -- Snap to pixel centers.

  """

  show_faces: bool = ...

  """

  Display faces over the image

  """

  show_metadata: bool = ...

  """

  Display metadata properties of the image

  """

  show_modified_edges: bool = ...

  """

  Display edges after modifiers are applied

  """

  show_pixel_coords: bool = ...

  """

  Display UV coordinates in pixels rather than from 0.0 to 1.0

  """

  show_stretch: bool = ...

  """

  Display faces colored according to the difference in shape between UVs and their 3D coordinates (blue for low distortion, red for high distortion)

  """

  show_texpaint: bool = ...

  """

  Display overlay of texture paint uv layer

  """

  sticky_select_mode: str = ...

  """

  Method for extending UV vertex selection

  * ``DISABLED``
Disabled -- Sticky vertex selection disabled.

  * ``SHARED_LOCATION``
Shared Location -- Select UVs that are at the same location and share a mesh vertex.

  * ``SHARED_VERTEX``
Shared Vertex -- Select UVs that share a mesh vertex, whether or not they are at the same location.

  """

  tile_grid_shape: typing.Tuple[int, int] = ...

  """

  How many tiles will be shown in the background

  """

  use_custom_grid: bool = ...

  """

  Use a grid with a user-defined number of steps

  """

  use_live_unwrap: bool = ...

  """

  Continuously unwrap the selected UV island while transforming pinned vertices

  """

  uv_opacity: float = ...

  """

  Opacity of UV overlays

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SPHFluidSettings(bpy_struct):

  """

  Settings for particle fluids physics

  """

  buoyancy: float = ...

  """

  Artificial buoyancy force in negative gravity direction based on pressure differences inside the fluid

  """

  fluid_radius: float = ...

  """

  Fluid interaction radius

  """

  linear_viscosity: float = ...

  """

  Linear viscosity

  """

  plasticity: float = ...

  """

  How much the spring rest length can change after the elastic limit is crossed

  """

  repulsion: float = ...

  """

  How strongly the fluid tries to keep from clustering (factor of stiffness)

  """

  rest_density: float = ...

  """

  Fluid rest density

  """

  rest_length: float = ...

  """

  Spring rest length (factor of particle radius)

  """

  solver: str = ...

  """

  The code used to calculate internal forces on particles

  * ``DDR``
Double-Density -- An artistic solver with strong surface tension effects (original).

  * ``CLASSICAL``
Classical -- A more physically-accurate solver.

  """

  spring_force: float = ...

  """

  Spring force

  """

  spring_frames: int = ...

  """

  Create springs for this number of frames since particles birth (0 is always)

  """

  stiff_viscosity: float = ...

  """

  Creates viscosity for expanding fluid

  """

  stiffness: float = ...

  """

  How incompressible the fluid is (speed of sound)

  """

  use_factor_density: bool = ...

  """

  Density is calculated as a factor of default density (depends on particle size)

  """

  use_factor_radius: bool = ...

  """

  Interaction radius is a factor of 4 * particle size

  """

  use_factor_repulsion: bool = ...

  """

  Repulsion is a factor of stiffness

  """

  use_factor_rest_length: bool = ...

  """

  Spring rest length is a factor of 2 * particle size

  """

  use_factor_stiff_viscosity: bool = ...

  """

  Stiff viscosity is a factor of normal viscosity

  """

  use_initial_rest_length: bool = ...

  """

  Use the initial length as spring rest length instead of 2 * particle size

  """

  use_viscoelastic_springs: bool = ...

  """

  Use viscoelastic springs instead of Hooke's springs

  """

  yield_ratio: float = ...

  """

  How much the spring has to be stretched/compressed in order to change its rest length

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Spline(bpy_struct):

  """

  Element of a curve, either NURBS, Bezier or Polyline or a character with text objects

  """

  bezier_points: typing.Union[SplineBezierPoints, typing.Sequence[BezierSplinePoint], typing.Mapping[str, BezierSplinePoint], bpy_prop_collection] = ...

  """

  Collection of points for Bezier curves only

  """

  character_index: int = ...

  """

  Location of this character in the text data (only for text curves)

  """

  hide: bool = ...

  """

  Hide this curve in Edit mode

  """

  material_index: int = ...

  """

  Material slot index of this curve

  """

  order_u: int = ...

  """

  NURBS order in the U direction (for splines and surfaces, higher values let points influence a greater area)

  """

  order_v: int = ...

  """

  NURBS order in the V direction (for surfaces only, higher values let points influence a greater area)

  """

  point_count_u: int = ...

  """

  Total number points for the curve or surface in the U direction

  """

  point_count_v: int = ...

  """

  Total number points for the surface on the V direction

  """

  points: typing.Union[SplinePoints, typing.Sequence[SplinePoint], typing.Mapping[str, SplinePoint], bpy_prop_collection] = ...

  """

  Collection of points that make up this poly or nurbs spline

  """

  radius_interpolation: str = ...

  """

  The type of radius interpolation for Bezier curves

  """

  resolution_u: int = ...

  """

  Curve or Surface subdivisions per segment

  """

  resolution_v: int = ...

  """

  Surface subdivisions per segment

  """

  tilt_interpolation: str = ...

  """

  The type of tilt interpolation for 3D, Bezier curves

  """

  type: str = ...

  """

  The interpolation type for this curve element

  """

  use_bezier_u: bool = ...

  """

  Make this nurbs curve or surface act like a Bezier spline in the U direction (Order U must be 3 or 4, Cyclic U must be disabled)

  """

  use_bezier_v: bool = ...

  """

  Make this nurbs surface act like a Bezier spline in the V direction (Order V must be 3 or 4, Cyclic V must be disabled)

  """

  use_cyclic_u: bool = ...

  """

  Make this curve or surface a closed loop in the U direction

  """

  use_cyclic_v: bool = ...

  """

  Make this surface a closed loop in the V direction

  """

  use_endpoint_u: bool = ...

  """

  Make this nurbs curve or surface meet the endpoints in the U direction (Cyclic U must be disabled)

  """

  use_endpoint_v: bool = ...

  """

  Make this nurbs surface meet the endpoints in the V direction (Cyclic V must be disabled)

  """

  use_smooth: bool = ...

  """

  Smooth the normals of the surface or beveled curve

  """

  def calc_length(self, resolution: int = 0) -> float:

    """

    Calculate spline length

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SplineBezierPoints(bpy_struct):

  """

  Collection of spline Bezier points

  """

  def add(self, count: int) -> None:

    """

    Add a number of points to this spline

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SplinePoint(bpy_struct):

  """

  Spline point without handles

  """

  co: typing.Tuple[float, float, float, float] = ...

  """

  Point coordinates

  """

  hide: bool = ...

  """

  Visibility status

  """

  radius: float = ...

  """

  Radius for beveling

  """

  select: bool = ...

  """

  Selection status

  """

  tilt: float = ...

  """

  Tilt in 3D View

  """

  weight: float = ...

  """

  NURBS weight

  """

  weight_softbody: float = ...

  """

  Softbody goal weight

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SplinePoints(bpy_struct):

  """

  Collection of spline points

  """

  def add(self, count: int) -> None:

    """

    Add a number of points to this spline

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SpreadsheetColumn(bpy_struct):

  """

  Persistent data associated with a spreadsheet column

  """

  data_type: str = ...

  """

  The data type of the corresponding column visible in the spreadsheet

  """

  id: SpreadsheetColumnID = ...

  """

  Data used to identify the corresponding data from the data source

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SpreadsheetColumnID(bpy_struct):

  """

  Data used to identify a spreadsheet column

  """

  name: str = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SpreadsheetContext(bpy_struct):

  """

  Element of spreadsheet context path

  """

  show_region_channels: bool = ...

  show_region_footer: bool = ...

  type: str = ...

  """

  Type of the context

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SpreadsheetContextPath(bpy_struct):

  def append(self, type: str) -> SpreadsheetContext:

    """

    Append a context path element

    """

    ...

  def clear(self) -> None:

    """

    Clear entire context path

    """

    ...

  def guess(self) -> None:

    """

    Guess the context path from the current context

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SpreadsheetRowFilter(bpy_struct):

  column_name: str = ...

  enabled: bool = ...

  operation: str = ...

  show_expanded: bool = ...

  threshold: float = ...

  """

  How close float values need to be to be equal

  """

  value_boolean: bool = ...

  value_color: typing.Tuple[float, float, float, float] = ...

  value_float: float = ...

  value_float2: typing.Tuple[float, float] = ...

  value_float3: typing.Tuple[float, float, float] = ...

  value_int: int = ...

  value_string: str = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Stereo3dDisplay(bpy_struct):

  """

  Settings for stereo 3D display

  """

  anaglyph_type: str = ...

  display_mode: str = ...

  """

  * ``ANAGLYPH``
Anaglyph -- Render views for left and right eyes as two differently filtered colors in a single image (anaglyph glasses are required).

  * ``INTERLACE``
Interlace -- Render views for left and right eyes interlaced in a single image (3D-ready monitor is required).

  * ``TIMESEQUENTIAL``
Time Sequential -- Render alternate eyes (also known as page flip, quad buffer support in the graphic card is required).

  * ``SIDEBYSIDE``
Side-by-Side -- Render views for left and right eyes side-by-side.

  * ``TOPBOTTOM``
Top-Bottom -- Render views for left and right eyes one above another.

  """

  interlace_type: str = ...

  use_interlace_swap: bool = ...

  """

  Swap left and right stereo channels

  """

  use_sidebyside_crosseyed: bool = ...

  """

  Right eye should see left image and vice versa

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Stereo3dFormat(bpy_struct):

  """

  Settings for stereo output

  """

  anaglyph_type: str = ...

  display_mode: str = ...

  """

  * ``ANAGLYPH``
Anaglyph -- Render views for left and right eyes as two differently filtered colors in a single image (anaglyph glasses are required).

  * ``INTERLACE``
Interlace -- Render views for left and right eyes interlaced in a single image (3D-ready monitor is required).

  * ``SIDEBYSIDE``
Side-by-Side -- Render views for left and right eyes side-by-side.

  * ``TOPBOTTOM``
Top-Bottom -- Render views for left and right eyes one above another.

  """

  interlace_type: str = ...

  use_interlace_swap: bool = ...

  """

  Swap left and right stereo channels

  """

  use_sidebyside_crosseyed: bool = ...

  """

  Right eye should see left image and vice versa

  """

  use_squeezed_frame: bool = ...

  """

  Combine both views in a squeezed image

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class StringAttributeValue(bpy_struct):

  """

  String value in geometry attribute

  """

  value: str = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Struct(bpy_struct):

  """

  RNA structure definition

  """

  base: Struct = ...

  """

  Struct definition this is derived from

  """

  description: str = ...

  """

  Description of the Struct's purpose

  """

  functions: typing.Union[typing.Sequence[Function], typing.Mapping[str, Function], bpy_prop_collection] = ...

  identifier: str = ...

  """

  Unique name used in the code and scripting

  """

  name: str = ...

  """

  Human readable name

  """

  name_property: StringProperty = ...

  """

  Property that gives the name of the struct

  """

  nested: Struct = ...

  """

  Struct in which this struct is always nested, and to which it logically belongs

  """

  properties: typing.Union[typing.Sequence[Property], typing.Mapping[str, Property], bpy_prop_collection] = ...

  """

  Properties in the struct

  """

  property_tags: typing.Union[typing.Sequence[EnumPropertyItem], typing.Mapping[str, EnumPropertyItem], bpy_prop_collection] = ...

  """

  Tags that properties can use to influence behavior

  """

  translation_context: str = ...

  """

  Translation context of the struct's name

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class StudioLight(bpy_struct):

  """

  Studio light

  """

  has_specular_highlight_pass: bool = ...

  """

  Studio light image file has separate "diffuse" and "specular" passes

  """

  index: int = ...

  is_user_defined: bool = ...

  light_ambient: typing.Tuple[float, float, float] = ...

  """

  Color of the ambient light that uniformly lit the scene

  """

  name: str = ...

  path: str = ...

  path_irr_cache: str = ...

  """

  Path where the irradiance cache is stored

  """

  path_sh_cache: str = ...

  """

  Path where the spherical harmonics cache is stored

  """

  solid_lights: typing.Union[typing.Sequence[UserSolidLight], typing.Mapping[str, UserSolidLight], bpy_prop_collection] = ...

  """

  Lights user to display objects in solid draw mode

  """

  spherical_harmonics_coefficients: typing.Tuple[typing.Tuple[float, float, float], typing.Tuple[float, float, float], typing.Tuple[float, float, float], typing.Tuple[float, float, float]] = ...

  type: str = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class StudioLights(bpy_struct):

  """

  Collection of studio lights

  """

  def load(self, path: str, type: str) -> StudioLight:

    """

    Load studiolight from file

    """

    ...

  def new(self, path: str) -> StudioLight:

    """

    Create studiolight from default lighting

    """

    ...

  def remove(self, studio_light: StudioLight) -> None:

    """

    Remove a studio light

    """

    ...

  def refresh(self) -> None:

    """

    Refresh Studio Lights from disk

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class TexMapping(bpy_struct):

  """

  Texture coordinate mapping settings

  """

  mapping: str = ...

  """

  * ``FLAT``
Flat -- Map X and Y coordinates directly.

  * ``CUBE``
Cube -- Map using the normal vector.

  * ``TUBE``
Tube -- Map with Z as central axis.

  * ``SPHERE``
Sphere -- Map with Z as central axis.

  """

  mapping_x: str = ...

  mapping_y: str = ...

  mapping_z: str = ...

  max: typing.Tuple[float, float, float] = ...

  """

  Maximum value for clipping

  """

  min: typing.Tuple[float, float, float] = ...

  """

  Minimum value for clipping

  """

  rotation: typing.Tuple[float, float, float] = ...

  scale: typing.Tuple[float, float, float] = ...

  translation: typing.Tuple[float, float, float] = ...

  use_max: bool = ...

  """

  Whether to use maximum clipping value

  """

  use_min: bool = ...

  """

  Whether to use minimum clipping value

  """

  vector_type: str = ...

  """

  Type of vector that the mapping transforms

  * ``POINT``
Point -- Transform a point.

  * ``TEXTURE``
Texture -- Transform a texture by inverse mapping the texture coordinate.

  * ``VECTOR``
Vector -- Transform a direction vector. Location is ignored.

  * ``NORMAL``
Normal -- Transform a unit normal vector. Location is ignored.

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class TexPaintSlot(bpy_struct):

  """

  Slot that contains information about texture painting

  """

  is_valid: bool = ...

  """

  Slot has a valid image and UV map

  """

  uv_layer: str = ...

  """

  Name of UV map

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class TextBox(bpy_struct):

  """

  Text bounding box for layout

  """

  height: float = ...

  width: float = ...

  x: float = ...

  y: float = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class TextCharacterFormat(bpy_struct):

  """

  Text character formatting settings

  """

  kerning: int = ...

  """

  Spacing between characters

  """

  material_index: int = ...

  """

  Material slot index of this character

  """

  use_bold: bool = ...

  use_italic: bool = ...

  use_small_caps: bool = ...

  use_underline: bool = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class TextLine(bpy_struct):

  """

  Line of text in a Text data-block

  """

  body: str = ...

  """

  Text in the line

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class TextureSlot(bpy_struct):

  """

  Texture slot defining the mapping and influence of a texture

  """

  blend_type: str = ...

  """

  Mode used to apply the texture

  """

  color: typing.Tuple[float, float, float] = ...

  """

  Default color for textures that don't return RGB or when RGB to intensity is enabled

  """

  default_value: float = ...

  """

  Value to use for Ref, Spec, Amb, Emit, Alpha, RayMir, TransLu and Hard

  """

  name: str = ...

  """

  Texture slot name

  """

  offset: typing.Tuple[float, float, float] = ...

  """

  Fine tune of the texture mapping X, Y and Z locations

  """

  output_node: str = ...

  """

  Which output node to use, for node-based textures

  """

  scale: typing.Tuple[float, float, float] = ...

  """

  Set scaling for the texture's X, Y and Z sizes

  """

  texture: Texture = ...

  """

  Texture data-block used by this texture slot

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Theme(bpy_struct):

  """

  User interface styling and color settings

  """

  bone_color_sets: typing.Union[typing.Sequence[ThemeBoneColorSet], typing.Mapping[str, ThemeBoneColorSet], bpy_prop_collection] = ...

  clip_editor: ThemeClipEditor = ...

  collection_color: typing.Union[typing.Sequence[ThemeCollectionColor], typing.Mapping[str, ThemeCollectionColor], bpy_prop_collection] = ...

  console: ThemeConsole = ...

  dopesheet_editor: ThemeDopeSheet = ...

  file_browser: ThemeFileBrowser = ...

  graph_editor: ThemeGraphEditor = ...

  image_editor: ThemeImageEditor = ...

  info: ThemeInfo = ...

  name: str = ...

  """

  Name of the theme

  """

  nla_editor: ThemeNLAEditor = ...

  node_editor: ThemeNodeEditor = ...

  outliner: ThemeOutliner = ...

  preferences: ThemePreferences = ...

  properties: ThemeProperties = ...

  sequence_editor: ThemeSequenceEditor = ...

  spreadsheet: ThemeSpreadsheet = ...

  statusbar: ThemeStatusBar = ...

  strip_color: typing.Union[typing.Sequence[ThemeStripColor], typing.Mapping[str, ThemeStripColor], bpy_prop_collection] = ...

  text_editor: ThemeTextEditor = ...

  theme_area: str = ...

  topbar: ThemeTopBar = ...

  user_interface: ThemeUserInterface = ...

  view_3d: ThemeView3D = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThemeBoneColorSet(bpy_struct):

  """

  Theme settings for bone color sets

  """

  active: typing.Tuple[float, float, float] = ...

  """

  Color used for active bones

  """

  normal: typing.Tuple[float, float, float] = ...

  """

  Color used for the surface of bones

  """

  select: typing.Tuple[float, float, float] = ...

  """

  Color used for selected bones

  """

  show_colored_constraints: bool = ...

  """

  Allow the use of colors indicating constraints/keyed status

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThemeClipEditor(bpy_struct):

  """

  Theme settings for the Movie Clip Editor

  """

  active_marker: typing.Tuple[float, float, float] = ...

  """

  Color of active marker

  """

  disabled_marker: typing.Tuple[float, float, float] = ...

  """

  Color of disabled marker

  """

  frame_current: typing.Tuple[float, float, float] = ...

  grid: typing.Tuple[float, float, float, float] = ...

  handle_align: typing.Tuple[float, float, float] = ...

  handle_auto: typing.Tuple[float, float, float] = ...

  handle_auto_clamped: typing.Tuple[float, float, float] = ...

  handle_free: typing.Tuple[float, float, float] = ...

  handle_sel_align: typing.Tuple[float, float, float] = ...

  handle_sel_auto: typing.Tuple[float, float, float] = ...

  handle_sel_auto_clamped: typing.Tuple[float, float, float] = ...

  handle_sel_free: typing.Tuple[float, float, float] = ...

  handle_vertex: typing.Tuple[float, float, float] = ...

  handle_vertex_select: typing.Tuple[float, float, float] = ...

  handle_vertex_size: int = ...

  locked_marker: typing.Tuple[float, float, float] = ...

  """

  Color of locked marker

  """

  marker: typing.Tuple[float, float, float] = ...

  """

  Color of marker

  """

  marker_outline: typing.Tuple[float, float, float] = ...

  """

  Color of marker's outline

  """

  metadatabg: typing.Tuple[float, float, float] = ...

  metadatatext: typing.Tuple[float, float, float] = ...

  path_after: typing.Tuple[float, float, float] = ...

  """

  Color of path after current frame

  """

  path_before: typing.Tuple[float, float, float] = ...

  """

  Color of path before current frame

  """

  path_keyframe_after: typing.Tuple[float, float, float] = ...

  """

  Color of path after current frame

  """

  path_keyframe_before: typing.Tuple[float, float, float] = ...

  """

  Color of path before current frame

  """

  selected_marker: typing.Tuple[float, float, float] = ...

  """

  Color of selected marker

  """

  space: ThemeSpaceGeneric = ...

  """

  Settings for space

  """

  space_list: ThemeSpaceListGeneric = ...

  """

  Settings for space list

  """

  strips: typing.Tuple[float, float, float] = ...

  strips_selected: typing.Tuple[float, float, float] = ...

  time_marker_line: typing.Tuple[float, float, float, float] = ...

  time_marker_line_selected: typing.Tuple[float, float, float, float] = ...

  time_scrub_background: typing.Tuple[float, float, float, float] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThemeCollectionColor(bpy_struct):

  """

  Theme settings for collection colors

  """

  color: typing.Tuple[float, float, float] = ...

  """

  Collection Color Tag

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThemeConsole(bpy_struct):

  """

  Theme settings for the Console

  """

  cursor: typing.Tuple[float, float, float] = ...

  line_error: typing.Tuple[float, float, float] = ...

  line_info: typing.Tuple[float, float, float] = ...

  line_input: typing.Tuple[float, float, float] = ...

  line_output: typing.Tuple[float, float, float] = ...

  select: typing.Tuple[float, float, float, float] = ...

  space: ThemeSpaceGeneric = ...

  """

  Settings for space

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThemeDopeSheet(bpy_struct):

  """

  Theme settings for the Dope Sheet

  """

  active_channels_group: typing.Tuple[float, float, float, float] = ...

  channel_group: typing.Tuple[float, float, float, float] = ...

  channels: typing.Tuple[float, float, float, float] = ...

  channels_selected: typing.Tuple[float, float, float, float] = ...

  dopesheet_channel: typing.Tuple[float, float, float, float] = ...

  dopesheet_subchannel: typing.Tuple[float, float, float, float] = ...

  frame_current: typing.Tuple[float, float, float] = ...

  grid: typing.Tuple[float, float, float] = ...

  interpolation_line: typing.Tuple[float, float, float, float] = ...

  """

  Color of lines showing non-bezier interpolation modes

  """

  keyframe: typing.Tuple[float, float, float] = ...

  """

  Color of Keyframe

  """

  keyframe_border: typing.Tuple[float, float, float, float] = ...

  """

  Color of keyframe border

  """

  keyframe_border_selected: typing.Tuple[float, float, float, float] = ...

  """

  Color of selected keyframe border

  """

  keyframe_breakdown: typing.Tuple[float, float, float] = ...

  """

  Color of breakdown keyframe

  """

  keyframe_breakdown_selected: typing.Tuple[float, float, float] = ...

  """

  Color of selected breakdown keyframe

  """

  keyframe_extreme: typing.Tuple[float, float, float] = ...

  """

  Color of extreme keyframe

  """

  keyframe_extreme_selected: typing.Tuple[float, float, float] = ...

  """

  Color of selected extreme keyframe

  """

  keyframe_jitter: typing.Tuple[float, float, float] = ...

  """

  Color of jitter keyframe

  """

  keyframe_jitter_selected: typing.Tuple[float, float, float] = ...

  """

  Color of selected jitter keyframe

  """

  keyframe_movehold: typing.Tuple[float, float, float] = ...

  """

  Color of moving hold keyframe

  """

  keyframe_movehold_selected: typing.Tuple[float, float, float] = ...

  """

  Color of selected moving hold keyframe

  """

  keyframe_scale_factor: float = ...

  """

  Scale factor for adjusting the height of keyframes

  """

  keyframe_selected: typing.Tuple[float, float, float] = ...

  """

  Color of selected keyframe

  """

  long_key: typing.Tuple[float, float, float, float] = ...

  long_key_selected: typing.Tuple[float, float, float, float] = ...

  preview_range: typing.Tuple[float, float, float, float] = ...

  """

  Color of preview range overlay

  """

  space: ThemeSpaceGeneric = ...

  """

  Settings for space

  """

  space_list: ThemeSpaceListGeneric = ...

  """

  Settings for space list

  """

  summary: typing.Tuple[float, float, float, float] = ...

  """

  Color of summary channel

  """

  time_marker_line: typing.Tuple[float, float, float, float] = ...

  time_marker_line_selected: typing.Tuple[float, float, float, float] = ...

  time_scrub_background: typing.Tuple[float, float, float, float] = ...

  value_sliders: typing.Tuple[float, float, float] = ...

  view_sliders: typing.Tuple[float, float, float] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThemeFileBrowser(bpy_struct):

  """

  Theme settings for the File Browser

  """

  row_alternate: typing.Tuple[float, float, float, float] = ...

  """

  Overlay color on every other row

  """

  selected_file: typing.Tuple[float, float, float] = ...

  space: ThemeSpaceGeneric = ...

  """

  Settings for space

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThemeFontStyle(bpy_struct):

  """

  Theme settings for Font

  """

  points: int = ...

  """

  Font size in points

  """

  shadow: int = ...

  """

  Shadow size (0, 3 and 5 supported)

  """

  shadow_alpha: float = ...

  shadow_offset_x: int = ...

  """

  Shadow offset in pixels

  """

  shadow_offset_y: int = ...

  """

  Shadow offset in pixels

  """

  shadow_value: float = ...

  """

  Shadow color in gray value

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThemeGradientColors(bpy_struct):

  """

  Theme settings for background colors and gradient

  """

  background_type: str = ...

  """

  Type of background in the 3D viewport

  * ``SINGLE_COLOR``
Single Color -- Use a solid color as viewport background.

  * ``LINEAR``
Linear Gradient -- Use a screen space vertical linear gradient as viewport background.

  * ``RADIAL``
Vignette -- Use a radial gradient as viewport background.

  """

  gradient: typing.Tuple[float, float, float] = ...

  high_gradient: typing.Tuple[float, float, float] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThemeGraphEditor(bpy_struct):

  """

  Theme settings for the graph editor

  """

  active_channels_group: typing.Tuple[float, float, float] = ...

  channel_group: typing.Tuple[float, float, float] = ...

  channels_region: typing.Tuple[float, float, float] = ...

  dopesheet_channel: typing.Tuple[float, float, float] = ...

  dopesheet_subchannel: typing.Tuple[float, float, float] = ...

  frame_current: typing.Tuple[float, float, float] = ...

  grid: typing.Tuple[float, float, float] = ...

  handle_align: typing.Tuple[float, float, float] = ...

  handle_auto: typing.Tuple[float, float, float] = ...

  handle_auto_clamped: typing.Tuple[float, float, float] = ...

  handle_free: typing.Tuple[float, float, float] = ...

  handle_sel_align: typing.Tuple[float, float, float] = ...

  handle_sel_auto: typing.Tuple[float, float, float] = ...

  handle_sel_auto_clamped: typing.Tuple[float, float, float] = ...

  handle_sel_free: typing.Tuple[float, float, float] = ...

  handle_sel_vect: typing.Tuple[float, float, float] = ...

  handle_vect: typing.Tuple[float, float, float] = ...

  handle_vertex: typing.Tuple[float, float, float] = ...

  handle_vertex_select: typing.Tuple[float, float, float] = ...

  handle_vertex_size: int = ...

  lastsel_point: typing.Tuple[float, float, float] = ...

  preview_range: typing.Tuple[float, float, float, float] = ...

  """

  Color of preview range overlay

  """

  space: ThemeSpaceGeneric = ...

  """

  Settings for space

  """

  space_list: ThemeSpaceListGeneric = ...

  """

  Settings for space list

  """

  time_marker_line: typing.Tuple[float, float, float, float] = ...

  time_marker_line_selected: typing.Tuple[float, float, float, float] = ...

  time_scrub_background: typing.Tuple[float, float, float, float] = ...

  vertex: typing.Tuple[float, float, float] = ...

  vertex_active: typing.Tuple[float, float, float] = ...

  vertex_bevel: typing.Tuple[float, float, float] = ...

  vertex_select: typing.Tuple[float, float, float] = ...

  vertex_size: int = ...

  vertex_unreferenced: typing.Tuple[float, float, float] = ...

  window_sliders: typing.Tuple[float, float, float] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThemeImageEditor(bpy_struct):

  """

  Theme settings for the Image Editor

  """

  edge_select: typing.Tuple[float, float, float] = ...

  editmesh_active: typing.Tuple[float, float, float, float] = ...

  face: typing.Tuple[float, float, float, float] = ...

  face_back: typing.Tuple[float, float, float, float] = ...

  face_dot: typing.Tuple[float, float, float] = ...

  face_front: typing.Tuple[float, float, float, float] = ...

  face_select: typing.Tuple[float, float, float, float] = ...

  facedot_size: int = ...

  frame_current: typing.Tuple[float, float, float] = ...

  freestyle_face_mark: typing.Tuple[float, float, float, float] = ...

  grid: typing.Tuple[float, float, float, float] = ...

  handle_align: typing.Tuple[float, float, float] = ...

  handle_auto: typing.Tuple[float, float, float] = ...

  handle_auto_clamped: typing.Tuple[float, float, float] = ...

  handle_free: typing.Tuple[float, float, float] = ...

  handle_sel_align: typing.Tuple[float, float, float] = ...

  handle_sel_auto: typing.Tuple[float, float, float] = ...

  handle_sel_auto_clamped: typing.Tuple[float, float, float] = ...

  handle_sel_free: typing.Tuple[float, float, float] = ...

  handle_vertex: typing.Tuple[float, float, float] = ...

  handle_vertex_select: typing.Tuple[float, float, float] = ...

  handle_vertex_size: int = ...

  metadatabg: typing.Tuple[float, float, float] = ...

  metadatatext: typing.Tuple[float, float, float] = ...

  paint_curve_handle: typing.Tuple[float, float, float, float] = ...

  paint_curve_pivot: typing.Tuple[float, float, float, float] = ...

  preview_stitch_active: typing.Tuple[float, float, float, float] = ...

  preview_stitch_edge: typing.Tuple[float, float, float, float] = ...

  preview_stitch_face: typing.Tuple[float, float, float, float] = ...

  preview_stitch_stitchable: typing.Tuple[float, float, float, float] = ...

  preview_stitch_unstitchable: typing.Tuple[float, float, float, float] = ...

  preview_stitch_vert: typing.Tuple[float, float, float, float] = ...

  scope_back: typing.Tuple[float, float, float, float] = ...

  space: ThemeSpaceGeneric = ...

  """

  Settings for space

  """

  uv_shadow: typing.Tuple[float, float, float, float] = ...

  vertex: typing.Tuple[float, float, float] = ...

  vertex_active: typing.Tuple[float, float, float] = ...

  vertex_bevel: typing.Tuple[float, float, float] = ...

  vertex_select: typing.Tuple[float, float, float] = ...

  vertex_size: int = ...

  vertex_unreferenced: typing.Tuple[float, float, float] = ...

  wire_edit: typing.Tuple[float, float, float] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThemeInfo(bpy_struct):

  """

  Theme settings for Info

  """

  info_debug: typing.Tuple[float, float, float, float] = ...

  """

  Background color of Debug icon

  """

  info_debug_text: typing.Tuple[float, float, float] = ...

  """

  Foreground color of Debug icon

  """

  info_error: typing.Tuple[float, float, float, float] = ...

  """

  Background color of Error icon

  """

  info_error_text: typing.Tuple[float, float, float] = ...

  """

  Foreground color of Error icon

  """

  info_info: typing.Tuple[float, float, float, float] = ...

  """

  Background color of Info icon

  """

  info_info_text: typing.Tuple[float, float, float] = ...

  """

  Foreground color of Info icon

  """

  info_operator: typing.Tuple[float, float, float, float] = ...

  """

  Background color of Operator icon

  """

  info_operator_text: typing.Tuple[float, float, float] = ...

  """

  Foreground color of Operator icon

  """

  info_property: typing.Tuple[float, float, float, float] = ...

  """

  Background color of Property icon

  """

  info_property_text: typing.Tuple[float, float, float] = ...

  """

  Foreground color of Property icon

  """

  info_selected: typing.Tuple[float, float, float] = ...

  """

  Background color of selected line

  """

  info_selected_text: typing.Tuple[float, float, float] = ...

  """

  Text color of selected line

  """

  info_warning: typing.Tuple[float, float, float, float] = ...

  """

  Background color of Warning icon

  """

  info_warning_text: typing.Tuple[float, float, float] = ...

  """

  Foreground color of Warning icon

  """

  space: ThemeSpaceGeneric = ...

  """

  Settings for space

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThemeNLAEditor(bpy_struct):

  """

  Theme settings for the NLA Editor

  """

  active_action: typing.Tuple[float, float, float, float] = ...

  """

  Animation data-block has active action

  """

  active_action_unset: typing.Tuple[float, float, float, float] = ...

  """

  Animation data-block doesn't have active action

  """

  dopesheet_channel: typing.Tuple[float, float, float] = ...

  """

  Nonlinear Animation Channel

  """

  frame_current: typing.Tuple[float, float, float] = ...

  grid: typing.Tuple[float, float, float] = ...

  keyframe_border: typing.Tuple[float, float, float, float] = ...

  """

  Color of keyframe border

  """

  keyframe_border_selected: typing.Tuple[float, float, float, float] = ...

  """

  Color of selected keyframe border

  """

  meta_strips: typing.Tuple[float, float, float] = ...

  """

  Unselected Meta Strip (for grouping related strips)

  """

  meta_strips_selected: typing.Tuple[float, float, float] = ...

  """

  Selected Meta Strip (for grouping related strips)

  """

  nla_track: typing.Tuple[float, float, float] = ...

  """

  Nonlinear Animation Track

  """

  preview_range: typing.Tuple[float, float, float, float] = ...

  """

  Color of preview range overlay

  """

  sound_strips: typing.Tuple[float, float, float] = ...

  """

  Unselected Sound Strip (for timing speaker sounds)

  """

  sound_strips_selected: typing.Tuple[float, float, float] = ...

  """

  Selected Sound Strip (for timing speaker sounds)

  """

  space: ThemeSpaceGeneric = ...

  """

  Settings for space

  """

  space_list: ThemeSpaceListGeneric = ...

  """

  Settings for space list

  """

  strips: typing.Tuple[float, float, float] = ...

  """

  Unselected Action-Clip Strip

  """

  strips_selected: typing.Tuple[float, float, float] = ...

  """

  Selected Action-Clip Strip

  """

  time_marker_line: typing.Tuple[float, float, float, float] = ...

  time_marker_line_selected: typing.Tuple[float, float, float, float] = ...

  time_scrub_background: typing.Tuple[float, float, float, float] = ...

  transition_strips: typing.Tuple[float, float, float] = ...

  """

  Unselected Transition Strip

  """

  transition_strips_selected: typing.Tuple[float, float, float] = ...

  """

  Selected Transition Strip

  """

  tweak: typing.Tuple[float, float, float] = ...

  """

  Color for strip/action being "tweaked" or edited

  """

  tweak_duplicate: typing.Tuple[float, float, float] = ...

  """

  Warning/error indicator color for strips referencing the strip being tweaked

  """

  view_sliders: typing.Tuple[float, float, float] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThemeNodeEditor(bpy_struct):

  """

  Theme settings for the Node Editor

  """

  attribute_node: typing.Tuple[float, float, float] = ...

  color_node: typing.Tuple[float, float, float] = ...

  converter_node: typing.Tuple[float, float, float] = ...

  dash_alpha: float = ...

  """

  Opacity for the dashed lines in wires

  """

  distor_node: typing.Tuple[float, float, float] = ...

  filter_node: typing.Tuple[float, float, float] = ...

  frame_node: typing.Tuple[float, float, float, float] = ...

  geometry_node: typing.Tuple[float, float, float] = ...

  grid: typing.Tuple[float, float, float] = ...

  grid_levels: int = ...

  """

  Number of subdivisions for the dot grid displayed in the background

  """

  group_node: typing.Tuple[float, float, float, float] = ...

  group_socket_node: typing.Tuple[float, float, float] = ...

  input_node: typing.Tuple[float, float, float] = ...

  layout_node: typing.Tuple[float, float, float] = ...

  matte_node: typing.Tuple[float, float, float] = ...

  node_active: typing.Tuple[float, float, float] = ...

  node_backdrop: typing.Tuple[float, float, float, float] = ...

  node_selected: typing.Tuple[float, float, float] = ...

  noodle_curving: int = ...

  """

  Curving of the noodle

  """

  output_node: typing.Tuple[float, float, float] = ...

  pattern_node: typing.Tuple[float, float, float] = ...

  script_node: typing.Tuple[float, float, float] = ...

  selected_text: typing.Tuple[float, float, float] = ...

  shader_node: typing.Tuple[float, float, float] = ...

  space: ThemeSpaceGeneric = ...

  """

  Settings for space

  """

  space_list: ThemeSpaceListGeneric = ...

  """

  Settings for space list

  """

  texture_node: typing.Tuple[float, float, float] = ...

  vector_node: typing.Tuple[float, float, float] = ...

  wire: typing.Tuple[float, float, float] = ...

  wire_inner: typing.Tuple[float, float, float] = ...

  wire_select: typing.Tuple[float, float, float, float] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThemeOutliner(bpy_struct):

  """

  Theme settings for the Outliner

  """

  active: typing.Tuple[float, float, float] = ...

  active_object: typing.Tuple[float, float, float] = ...

  edited_object: typing.Tuple[float, float, float, float] = ...

  match: typing.Tuple[float, float, float] = ...

  row_alternate: typing.Tuple[float, float, float, float] = ...

  """

  Overlay color on every other row

  """

  selected_highlight: typing.Tuple[float, float, float] = ...

  selected_object: typing.Tuple[float, float, float] = ...

  space: ThemeSpaceGeneric = ...

  """

  Settings for space

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThemePanelColors(bpy_struct):

  """

  Theme settings for panel colors

  """

  back: typing.Tuple[float, float, float, float] = ...

  header: typing.Tuple[float, float, float, float] = ...

  sub_back: typing.Tuple[float, float, float, float] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThemePreferences(bpy_struct):

  """

  Theme settings for the Blender Preferences

  """

  space: ThemeSpaceGeneric = ...

  """

  Settings for space

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThemeProperties(bpy_struct):

  """

  Theme settings for the Properties

  """

  active_modifier: typing.Tuple[float, float, float, float] = ...

  match: typing.Tuple[float, float, float] = ...

  space: ThemeSpaceGeneric = ...

  """

  Settings for space

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThemeSequenceEditor(bpy_struct):

  """

  Theme settings for the Sequence Editor

  """

  active_strip: typing.Tuple[float, float, float] = ...

  audio_strip: typing.Tuple[float, float, float] = ...

  color_strip: typing.Tuple[float, float, float] = ...

  draw_action: typing.Tuple[float, float, float] = ...

  effect_strip: typing.Tuple[float, float, float] = ...

  frame_current: typing.Tuple[float, float, float] = ...

  grid: typing.Tuple[float, float, float] = ...

  image_strip: typing.Tuple[float, float, float] = ...

  keyframe: typing.Tuple[float, float, float] = ...

  mask_strip: typing.Tuple[float, float, float] = ...

  meta_strip: typing.Tuple[float, float, float] = ...

  metadatabg: typing.Tuple[float, float, float] = ...

  metadatatext: typing.Tuple[float, float, float] = ...

  movie_strip: typing.Tuple[float, float, float] = ...

  movieclip_strip: typing.Tuple[float, float, float] = ...

  preview_back: typing.Tuple[float, float, float] = ...

  preview_range: typing.Tuple[float, float, float, float] = ...

  """

  Color of preview range overlay

  """

  row_alternate: typing.Tuple[float, float, float, float] = ...

  """

  Overlay color on every other row

  """

  scene_strip: typing.Tuple[float, float, float] = ...

  selected_strip: typing.Tuple[float, float, float] = ...

  space: ThemeSpaceGeneric = ...

  """

  Settings for space

  """

  text_strip: typing.Tuple[float, float, float] = ...

  time_marker_line: typing.Tuple[float, float, float, float] = ...

  time_marker_line_selected: typing.Tuple[float, float, float, float] = ...

  time_scrub_background: typing.Tuple[float, float, float, float] = ...

  window_sliders: typing.Tuple[float, float, float] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThemeSpaceGeneric(bpy_struct):

  back: typing.Tuple[float, float, float] = ...

  button: typing.Tuple[float, float, float, float] = ...

  button_text: typing.Tuple[float, float, float] = ...

  button_text_hi: typing.Tuple[float, float, float] = ...

  button_title: typing.Tuple[float, float, float] = ...

  execution_buts: typing.Tuple[float, float, float, float] = ...

  header: typing.Tuple[float, float, float, float] = ...

  header_text: typing.Tuple[float, float, float] = ...

  header_text_hi: typing.Tuple[float, float, float] = ...

  navigation_bar: typing.Tuple[float, float, float, float] = ...

  panelcolors: ThemePanelColors = ...

  tab_active: typing.Tuple[float, float, float] = ...

  tab_back: typing.Tuple[float, float, float, float] = ...

  tab_inactive: typing.Tuple[float, float, float] = ...

  tab_outline: typing.Tuple[float, float, float] = ...

  text: typing.Tuple[float, float, float] = ...

  text_hi: typing.Tuple[float, float, float] = ...

  title: typing.Tuple[float, float, float] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThemeSpaceGradient(bpy_struct):

  button: typing.Tuple[float, float, float, float] = ...

  button_text: typing.Tuple[float, float, float] = ...

  button_text_hi: typing.Tuple[float, float, float] = ...

  button_title: typing.Tuple[float, float, float] = ...

  execution_buts: typing.Tuple[float, float, float, float] = ...

  gradients: ThemeGradientColors = ...

  header: typing.Tuple[float, float, float, float] = ...

  header_text: typing.Tuple[float, float, float] = ...

  header_text_hi: typing.Tuple[float, float, float] = ...

  navigation_bar: typing.Tuple[float, float, float, float] = ...

  panelcolors: ThemePanelColors = ...

  tab_active: typing.Tuple[float, float, float] = ...

  tab_back: typing.Tuple[float, float, float, float] = ...

  tab_inactive: typing.Tuple[float, float, float] = ...

  tab_outline: typing.Tuple[float, float, float] = ...

  text: typing.Tuple[float, float, float] = ...

  text_hi: typing.Tuple[float, float, float] = ...

  title: typing.Tuple[float, float, float] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThemeSpaceListGeneric(bpy_struct):

  list: typing.Tuple[float, float, float] = ...

  list_text: typing.Tuple[float, float, float] = ...

  list_text_hi: typing.Tuple[float, float, float] = ...

  list_title: typing.Tuple[float, float, float] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThemeSpreadsheet(bpy_struct):

  """

  Theme settings for the Spreadsheet

  """

  row_alternate: typing.Tuple[float, float, float, float] = ...

  """

  Overlay color on every other row

  """

  space: ThemeSpaceGeneric = ...

  """

  Settings for space

  """

  space_list: ThemeSpaceListGeneric = ...

  """

  Settings for space list

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThemeStatusBar(bpy_struct):

  """

  Theme settings for the Status Bar

  """

  space: ThemeSpaceGeneric = ...

  """

  Settings for space

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThemeStripColor(bpy_struct):

  """

  Theme settings for strip colors

  """

  color: typing.Tuple[float, float, float] = ...

  """

  Strip Color

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThemeStyle(bpy_struct):

  """

  Theme settings for style sets

  """

  panel_title: ThemeFontStyle = ...

  widget: ThemeFontStyle = ...

  widget_label: ThemeFontStyle = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThemeTextEditor(bpy_struct):

  """

  Theme settings for the Text Editor

  """

  cursor: typing.Tuple[float, float, float] = ...

  line_numbers: typing.Tuple[float, float, float] = ...

  line_numbers_background: typing.Tuple[float, float, float] = ...

  selected_text: typing.Tuple[float, float, float] = ...

  space: ThemeSpaceGeneric = ...

  """

  Settings for space

  """

  syntax_builtin: typing.Tuple[float, float, float] = ...

  syntax_comment: typing.Tuple[float, float, float] = ...

  syntax_numbers: typing.Tuple[float, float, float] = ...

  syntax_preprocessor: typing.Tuple[float, float, float] = ...

  syntax_reserved: typing.Tuple[float, float, float] = ...

  syntax_special: typing.Tuple[float, float, float] = ...

  syntax_string: typing.Tuple[float, float, float] = ...

  syntax_symbols: typing.Tuple[float, float, float] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThemeTopBar(bpy_struct):

  """

  Theme settings for the Top Bar

  """

  space: ThemeSpaceGeneric = ...

  """

  Settings for space

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThemeUserInterface(bpy_struct):

  """

  Theme settings for user interface elements

  """

  axis_x: typing.Tuple[float, float, float] = ...

  axis_y: typing.Tuple[float, float, float] = ...

  axis_z: typing.Tuple[float, float, float] = ...

  editor_outline: typing.Tuple[float, float, float] = ...

  """

  Color of the outline of the editors and their round corners

  """

  gizmo_a: typing.Tuple[float, float, float] = ...

  gizmo_b: typing.Tuple[float, float, float] = ...

  gizmo_hi: typing.Tuple[float, float, float] = ...

  gizmo_primary: typing.Tuple[float, float, float] = ...

  gizmo_secondary: typing.Tuple[float, float, float] = ...

  gizmo_view_align: typing.Tuple[float, float, float] = ...

  icon_alpha: float = ...

  """

  Transparency of icons in the interface, to reduce contrast

  """

  icon_border_intensity: float = ...

  """

  Control the intensity of the border around themes icons

  """

  icon_collection: typing.Tuple[float, float, float, float] = ...

  icon_folder: typing.Tuple[float, float, float, float] = ...

  """

  Color of folders in the file browser

  """

  icon_modifier: typing.Tuple[float, float, float, float] = ...

  icon_object: typing.Tuple[float, float, float, float] = ...

  icon_object_data: typing.Tuple[float, float, float, float] = ...

  icon_saturation: float = ...

  """

  Saturation of icons in the interface

  """

  icon_scene: typing.Tuple[float, float, float, float] = ...

  icon_shading: typing.Tuple[float, float, float, float] = ...

  menu_shadow_fac: float = ...

  """

  Blending factor for menu shadows

  """

  menu_shadow_width: int = ...

  """

  Width of menu shadows, set to zero to disable

  """

  panel_roundness: float = ...

  """

  Roundness of the corners of panels and sub-panels

  """

  transparent_checker_primary: typing.Tuple[float, float, float] = ...

  """

  Primary color of checkerboard pattern indicating transparent areas

  """

  transparent_checker_secondary: typing.Tuple[float, float, float] = ...

  """

  Secondary color of checkerboard pattern indicating transparent areas

  """

  transparent_checker_size: int = ...

  """

  Size of checkerboard pattern indicating transparent areas

  """

  wcol_box: ThemeWidgetColors = ...

  wcol_list_item: ThemeWidgetColors = ...

  wcol_menu: ThemeWidgetColors = ...

  wcol_menu_back: ThemeWidgetColors = ...

  wcol_menu_item: ThemeWidgetColors = ...

  wcol_num: ThemeWidgetColors = ...

  wcol_numslider: ThemeWidgetColors = ...

  wcol_option: ThemeWidgetColors = ...

  wcol_pie_menu: ThemeWidgetColors = ...

  wcol_progress: ThemeWidgetColors = ...

  wcol_pulldown: ThemeWidgetColors = ...

  wcol_radio: ThemeWidgetColors = ...

  wcol_regular: ThemeWidgetColors = ...

  wcol_scroll: ThemeWidgetColors = ...

  wcol_state: ThemeWidgetStateColors = ...

  wcol_tab: ThemeWidgetColors = ...

  wcol_text: ThemeWidgetColors = ...

  wcol_toggle: ThemeWidgetColors = ...

  wcol_tool: ThemeWidgetColors = ...

  wcol_toolbar_item: ThemeWidgetColors = ...

  wcol_tooltip: ThemeWidgetColors = ...

  widget_emboss: typing.Tuple[float, float, float, float] = ...

  """

  Color of the 1px shadow line underlying widgets

  """

  widget_text_cursor: typing.Tuple[float, float, float] = ...

  """

  Color of the interface widgets text insertion cursor (caret)

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThemeView3D(bpy_struct):

  """

  Theme settings for the 3D View

  """

  act_spline: typing.Tuple[float, float, float] = ...

  bone_locked_weight: typing.Tuple[float, float, float, float] = ...

  """

  Shade for bones corresponding to a locked weight group during painting

  """

  bone_pose: typing.Tuple[float, float, float] = ...

  bone_pose_active: typing.Tuple[float, float, float] = ...

  bone_solid: typing.Tuple[float, float, float] = ...

  bundle_solid: typing.Tuple[float, float, float] = ...

  camera: typing.Tuple[float, float, float] = ...

  camera_path: typing.Tuple[float, float, float] = ...

  clipping_border_3d: typing.Tuple[float, float, float, float] = ...

  edge_bevel: typing.Tuple[float, float, float] = ...

  edge_crease: typing.Tuple[float, float, float] = ...

  edge_facesel: typing.Tuple[float, float, float] = ...

  edge_seam: typing.Tuple[float, float, float] = ...

  edge_select: typing.Tuple[float, float, float] = ...

  edge_sharp: typing.Tuple[float, float, float] = ...

  editmesh_active: typing.Tuple[float, float, float, float] = ...

  empty: typing.Tuple[float, float, float] = ...

  extra_edge_angle: typing.Tuple[float, float, float] = ...

  extra_edge_len: typing.Tuple[float, float, float] = ...

  extra_face_angle: typing.Tuple[float, float, float] = ...

  extra_face_area: typing.Tuple[float, float, float] = ...

  face: typing.Tuple[float, float, float, float] = ...

  face_back: typing.Tuple[float, float, float, float] = ...

  face_dot: typing.Tuple[float, float, float] = ...

  face_front: typing.Tuple[float, float, float, float] = ...

  face_select: typing.Tuple[float, float, float, float] = ...

  facedot_size: int = ...

  frame_current: typing.Tuple[float, float, float] = ...

  freestyle_edge_mark: typing.Tuple[float, float, float] = ...

  freestyle_face_mark: typing.Tuple[float, float, float, float] = ...

  gp_vertex: typing.Tuple[float, float, float] = ...

  gp_vertex_select: typing.Tuple[float, float, float] = ...

  gp_vertex_size: int = ...

  grid: typing.Tuple[float, float, float, float] = ...

  handle_align: typing.Tuple[float, float, float] = ...

  handle_auto: typing.Tuple[float, float, float] = ...

  handle_free: typing.Tuple[float, float, float] = ...

  handle_sel_align: typing.Tuple[float, float, float] = ...

  handle_sel_auto: typing.Tuple[float, float, float] = ...

  handle_sel_free: typing.Tuple[float, float, float] = ...

  handle_sel_vect: typing.Tuple[float, float, float] = ...

  handle_vect: typing.Tuple[float, float, float] = ...

  lastsel_point: typing.Tuple[float, float, float] = ...

  light: typing.Tuple[float, float, float, float] = ...

  normal: typing.Tuple[float, float, float] = ...

  nurb_sel_uline: typing.Tuple[float, float, float] = ...

  nurb_sel_vline: typing.Tuple[float, float, float] = ...

  nurb_uline: typing.Tuple[float, float, float] = ...

  nurb_vline: typing.Tuple[float, float, float] = ...

  object_active: typing.Tuple[float, float, float] = ...

  object_origin_size: int = ...

  """

  Diameter in pixels for object/light origin display

  """

  object_selected: typing.Tuple[float, float, float] = ...

  outline_width: int = ...

  paint_curve_handle: typing.Tuple[float, float, float, float] = ...

  paint_curve_pivot: typing.Tuple[float, float, float, float] = ...

  skin_root: typing.Tuple[float, float, float] = ...

  space: ThemeSpaceGradient = ...

  """

  Settings for space

  """

  speaker: typing.Tuple[float, float, float] = ...

  split_normal: typing.Tuple[float, float, float] = ...

  text_grease_pencil: typing.Tuple[float, float, float] = ...

  """

  Color for indicating Grease Pencil keyframes

  """

  text_keyframe: typing.Tuple[float, float, float] = ...

  """

  Color for indicating object keyframes

  """

  transform: typing.Tuple[float, float, float] = ...

  vertex: typing.Tuple[float, float, float] = ...

  vertex_active: typing.Tuple[float, float, float] = ...

  vertex_bevel: typing.Tuple[float, float, float] = ...

  vertex_normal: typing.Tuple[float, float, float] = ...

  vertex_select: typing.Tuple[float, float, float] = ...

  vertex_size: int = ...

  vertex_unreferenced: typing.Tuple[float, float, float] = ...

  view_overlay: typing.Tuple[float, float, float] = ...

  wire: typing.Tuple[float, float, float] = ...

  wire_edit: typing.Tuple[float, float, float] = ...

  """

  Color for wireframe when in edit mode, but edge selection is active

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThemeWidgetColors(bpy_struct):

  """

  Theme settings for widget color sets

  """

  inner: typing.Tuple[float, float, float, float] = ...

  inner_sel: typing.Tuple[float, float, float, float] = ...

  item: typing.Tuple[float, float, float, float] = ...

  outline: typing.Tuple[float, float, float] = ...

  roundness: float = ...

  """

  Amount of edge rounding

  """

  shadedown: int = ...

  shadetop: int = ...

  show_shaded: bool = ...

  text: typing.Tuple[float, float, float] = ...

  text_sel: typing.Tuple[float, float, float] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThemeWidgetStateColors(bpy_struct):

  """

  Theme settings for widget state colors

  """

  blend: float = ...

  inner_anim: typing.Tuple[float, float, float] = ...

  inner_anim_sel: typing.Tuple[float, float, float] = ...

  inner_changed: typing.Tuple[float, float, float] = ...

  inner_changed_sel: typing.Tuple[float, float, float] = ...

  inner_driven: typing.Tuple[float, float, float] = ...

  inner_driven_sel: typing.Tuple[float, float, float] = ...

  inner_key: typing.Tuple[float, float, float] = ...

  inner_key_sel: typing.Tuple[float, float, float] = ...

  inner_overridden: typing.Tuple[float, float, float] = ...

  inner_overridden_sel: typing.Tuple[float, float, float] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class TimelineMarker(bpy_struct):

  """

  Marker for noting points in the timeline

  """

  camera: Object = ...

  """

  Camera that becomes active on this frame

  """

  frame: int = ...

  """

  The frame on which the timeline marker appears

  """

  name: str = ...

  select: bool = ...

  """

  Marker selection state

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class TimelineMarkers(bpy_struct):

  """

  Collection of timeline markers

  """

  def new(self, name: str, frame: int = 1) -> TimelineMarker:

    """

    Add a keyframe to the curve

    """

    ...

  def remove(self, marker: TimelineMarker) -> None:

    """

    Remove a timeline marker

    """

    ...

  def clear(self) -> None:

    """

    Remove all timeline markers

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Timer(bpy_struct):

  """

  Window event timer

  """

  time_delta: float = ...

  """

  Time since last step in seconds

  """

  time_duration: float = ...

  """

  Time since last step in seconds

  """

  time_step: float = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ToolSettings(bpy_struct):

  annotation_stroke_placement_view2d: str = ...

  """

  * ``IMAGE``
Image -- Stick stroke to the image.

  * ``VIEW``
View -- Stick stroke to the view.

  """

  annotation_stroke_placement_view3d: str = ...

  """

  How annotation strokes are orientated in 3D space

  * ``CURSOR``
3D Cursor -- Draw stroke at 3D cursor location.

  * ``VIEW``
View -- Stick stroke to the view.

  * ``SURFACE``
Surface -- Stick stroke to surfaces.

  """

  annotation_thickness: int = ...

  """

  Thickness of annotation strokes

  """

  auto_keying_mode: str = ...

  """

  Mode of automatic keyframe insertion for Objects, Bones and Masks

  """

  curve_paint_settings: CurvePaintSettings = ...

  custom_bevel_profile_preset: CurveProfile = ...

  """

  Used for defining a profile's path

  """

  double_threshold: float = ...

  """

  Threshold distance for Auto Merge

  """

  gpencil_interpolate: GPencilInterpolateSettings = ...

  """

  Settings for Grease Pencil Interpolation tools

  """

  gpencil_paint: GpPaint = ...

  gpencil_sculpt: GPencilSculptSettings = ...

  """

  Settings for stroke sculpting tools and brushes

  """

  gpencil_sculpt_paint: GpSculptPaint = ...

  gpencil_selectmode_edit: str = ...

  """

  * ``POINT``
Point -- Select only points.

  * ``STROKE``
Stroke -- Select all stroke points.

  * ``SEGMENT``
Segment -- Select all stroke points between other strokes.

  """

  gpencil_stroke_placement_view3d: str = ...

  """

  * ``ORIGIN``
Origin -- Draw stroke at Object origin.

  * ``CURSOR``
3D Cursor -- Draw stroke at 3D cursor location.

  * ``SURFACE``
Surface -- Stick stroke to surfaces.

  * ``STROKE``
Stroke -- Stick stroke to other strokes.

  """

  gpencil_stroke_snap_mode: str = ...

  """

  * ``NONE``
All Points -- Snap to all points.

  * ``ENDS``
End Points -- Snap to first and last points and interpolate.

  * ``FIRST``
First Point -- Snap to first point.

  """

  gpencil_vertex_paint: GpVertexPaint = ...

  gpencil_weight_paint: GpWeightPaint = ...

  image_paint: ImagePaint = ...

  keyframe_type: str = ...

  """

  Type of keyframes to create when inserting keyframes

  * ``KEYFRAME``
Keyframe -- Normal keyframe, e.g. for key poses.

  * ``BREAKDOWN``
Breakdown -- A breakdown pose, e.g. for transitions between key poses.

  * ``MOVING_HOLD``
Moving Hold -- A keyframe that is part of a moving hold.

  * ``EXTREME``
Extreme -- An "extreme" pose, or some other purpose as needed.

  * ``JITTER``
Jitter -- A filler or baked keyframe for keying on ones, or some other purpose as needed.

  """

  lock_markers: bool = ...

  """

  Prevent marker editing

  """

  lock_object_mode: bool = ...

  """

  Restrict select to the current mode

  """

  mesh_select_mode: typing.Tuple[bool, bool, bool] = ...

  """

  Which mesh elements selection works on

  """

  normal_vector: typing.Tuple[float, float, float] = ...

  """

  Normal Vector used to copy, add or multiply

  """

  particle_edit: ParticleEdit = ...

  proportional_edit_falloff: str = ...

  """

  Falloff type for proportional editing mode

  * ``SMOOTH``
Smooth -- Smooth falloff.

  * ``SPHERE``
Sphere -- Spherical falloff.

  * ``ROOT``
Root -- Root falloff.

  * ``INVERSE_SQUARE``
Inverse Square -- Inverse Square falloff.

  * ``SHARP``
Sharp -- Sharp falloff.

  * ``LINEAR``
Linear -- Linear falloff.

  * ``CONSTANT``
Constant -- Constant falloff.

  * ``RANDOM``
Random -- Random falloff.

  """

  proportional_size: float = ...

  """

  Display size for proportional editing circle

  """

  sculpt: Sculpt = ...

  sequencer_tool_settings: SequencerToolSettings = ...

  show_uv_local_view: bool = ...

  """

  Display only faces with the currently displayed image assigned

  """

  snap_elements: typing.Set[str] = ...

  """

  Type of element to snap to

  * ``INCREMENT``
Increment -- Snap to increments of grid.

  * ``VERTEX``
Vertex -- Snap to vertices.

  * ``EDGE``
Edge -- Snap to edges.

  * ``FACE``
Face -- Snap to faces.

  * ``VOLUME``
Volume -- Snap to volume.

  * ``EDGE_MIDPOINT``
Edge Center -- Snap to the middle of edges.

  * ``EDGE_PERPENDICULAR``
Edge Perpendicular -- Snap to the nearest point on an edge.

  """

  snap_node_element: str = ...

  """

  Type of element to snap to

  * ``GRID``
Grid -- Snap to grid.

  * ``NODE_X``
Node X -- Snap to left/right node border.

  * ``NODE_Y``
Node Y -- Snap to top/bottom node border.

  * ``NODE_XY``
Node X / Y -- Snap to any node border.

  """

  snap_target: str = ...

  """

  Which part to snap onto the target

  * ``CLOSEST``
Closest -- Snap closest point onto target.

  * ``CENTER``
Center -- Snap transformation center onto target.

  * ``MEDIAN``
Median -- Snap median onto target.

  * ``ACTIVE``
Active -- Snap active onto target.

  """

  snap_uv_element: str = ...

  """

  Type of element to snap to

  * ``INCREMENT``
Increment -- Snap to increments of grid.

  * ``VERTEX``
Vertex -- Snap to vertices.

  """

  statvis: MeshStatVis = ...

  transform_pivot_point: str = ...

  """

  Pivot center for rotation/scaling

  * ``BOUNDING_BOX_CENTER``
Bounding Box Center -- Pivot around bounding box center of selected object(s).

  * ``CURSOR``
3D Cursor -- Pivot around the 3D cursor.

  * ``INDIVIDUAL_ORIGINS``
Individual Origins -- Pivot around each object's own origin.

  * ``MEDIAN_POINT``
Median Point -- Pivot around the median point of selected objects.

  * ``ACTIVE_ELEMENT``
Active Element -- Pivot around active object.

  """

  unified_paint_settings: UnifiedPaintSettings = ...

  use_auto_normalize: bool = ...

  """

  Ensure all bone-deforming vertex groups add up to 1.0 while weight painting

  """

  use_edge_path_live_unwrap: bool = ...

  """

  Changing edge seams recalculates UV unwrap

  """

  use_gpencil_automerge_strokes: bool = ...

  """

  Join by distance last drawn stroke with previous strokes in the active layer

  """

  use_gpencil_draw_additive: bool = ...

  """

  When creating new frames, the strokes from the previous/active frame are included as the basis for the new one

  """

  use_gpencil_draw_onback: bool = ...

  """

  When draw new strokes, the new stroke is drawn below of all strokes in the layer

  """

  use_gpencil_select_mask_point: bool = ...

  """

  Only sculpt selected stroke points

  """

  use_gpencil_select_mask_segment: bool = ...

  """

  Only sculpt selected stroke points between other strokes

  """

  use_gpencil_select_mask_stroke: bool = ...

  """

  Only sculpt selected stroke

  """

  use_gpencil_stroke_endpoints: bool = ...

  """

  Only use the first and last parts of the stroke for snapping

  """

  use_gpencil_thumbnail_list: bool = ...

  """

  Show compact list of color instead of thumbnails

  """

  use_gpencil_vertex_select_mask_point: bool = ...

  """

  Only paint selected stroke points

  """

  use_gpencil_vertex_select_mask_segment: bool = ...

  """

  Only paint selected stroke points between other strokes

  """

  use_gpencil_vertex_select_mask_stroke: bool = ...

  """

  Only paint selected stroke

  """

  use_gpencil_weight_data_add: bool = ...

  """

  When creating new strokes, the weight data is added according to the current vertex group and weight, if no vertex group selected, weight is not added

  """

  use_keyframe_cycle_aware: bool = ...

  """

  For channels with cyclic extrapolation, keyframe insertion is automatically remapped inside the cycle time range, and keeps ends in sync

  """

  use_keyframe_insert_auto: bool = ...

  """

  Automatic keyframe insertion for Objects, Bones and Masks

  """

  use_keyframe_insert_keyingset: bool = ...

  """

  Automatic keyframe insertion using active Keying Set only

  """

  use_lock_relative: bool = ...

  """

  Display bone-deforming groups as if all locked deform groups were deleted, and the remaining ones were re-normalized

  """

  use_mesh_automerge: bool = ...

  """

  Automatically merge vertices moved to the same location

  """

  use_mesh_automerge_and_split: bool = ...

  """

  Automatically split edges and faces

  """

  use_multipaint: bool = ...

  """

  Paint across the weights of all selected bones, maintaining their relative influence

  """

  use_proportional_action: bool = ...

  """

  Proportional editing in action editor

  """

  use_proportional_connected: bool = ...

  """

  Proportional Editing using connected geometry only

  """

  use_proportional_edit: bool = ...

  """

  Proportional edit mode

  """

  use_proportional_edit_mask: bool = ...

  """

  Proportional editing mask mode

  """

  use_proportional_edit_objects: bool = ...

  """

  Proportional editing object mode

  """

  use_proportional_fcurve: bool = ...

  """

  Proportional editing in FCurve editor

  """

  use_proportional_projected: bool = ...

  """

  Proportional Editing using screen space locations

  """

  use_record_with_nla: bool = ...

  """

  Add a new NLA Track + Strip for every loop/pass made over the animation to allow non-destructive tweaking

  """

  use_snap: bool = ...

  """

  Snap during transform

  """

  use_snap_align_rotation: bool = ...

  """

  Align rotation with the snapping target

  """

  use_snap_backface_culling: bool = ...

  """

  Exclude back facing geometry from snapping

  """

  use_snap_grid_absolute: bool = ...

  """

  Absolute grid alignment while translating (based on the pivot center)

  """

  use_snap_peel_object: bool = ...

  """

  Consider objects as whole when finding volume center

  """

  use_snap_project: bool = ...

  """

  Project individual elements on the surface of other objects

  """

  use_snap_rotate: bool = ...

  """

  Rotate is affected by the snapping settings

  """

  use_snap_scale: bool = ...

  """

  Scale is affected by snapping settings

  """

  use_snap_self: bool = ...

  """

  Snap onto itself (Edit Mode Only)

  """

  use_snap_sequencer: bool = ...

  """

  Snap to strip edges or current frame

  """

  use_snap_translate: bool = ...

  """

  Move is affected by snapping settings

  """

  use_snap_uv_grid_absolute: bool = ...

  """

  Absolute grid alignment while translating (based on the pivot center)

  """

  use_transform_correct_face_attributes: bool = ...

  """

  Correct data such as UV's and vertex colors when transforming

  """

  use_transform_correct_keep_connected: bool = ...

  """

  During the Face Attributes correction, merge attributes connected to the same vertex

  """

  use_transform_data_origin: bool = ...

  """

  Transform object origins, while leaving the shape in place

  """

  use_transform_pivot_point_align: bool = ...

  """

  Only transform object locations, without affecting rotation or scaling

  """

  use_transform_skip_children: bool = ...

  """

  Transform the parents, leaving the children in place

  """

  use_uv_select_sync: bool = ...

  """

  Keep UV and edit mode mesh selection in sync

  """

  uv_relax_method: str = ...

  """

  Algorithm used for UV relaxation

  * ``LAPLACIAN``
Laplacian -- Use Laplacian method for relaxation.

  * ``HC``
HC -- Use HC method for relaxation.

  """

  uv_sculpt: UvSculpt = ...

  uv_sculpt_all_islands: bool = ...

  """

  Brush operates on all islands

  """

  uv_sculpt_lock_borders: bool = ...

  """

  Disable editing of boundary edges

  """

  uv_select_mode: str = ...

  """

  UV selection and display mode

  * ``VERTEX``
Vertex -- Vertex selection mode.

  * ``EDGE``
Edge -- Edge selection mode.

  * ``FACE``
Face -- Face selection mode.

  * ``ISLAND``
Island -- Island selection mode.

  """

  vertex_group_subset: str = ...

  """

  Filter Vertex groups for Display

  * ``ALL``
All -- All Vertex Groups.

  * ``BONE_DEFORM``
Deform -- Vertex Groups assigned to Deform Bones.

  * ``OTHER_DEFORM``
Other -- Vertex Groups assigned to non Deform Bones.

  """

  vertex_group_user: str = ...

  """

  Display unweighted vertices

  * ``NONE``
None.

  * ``ACTIVE``
Active -- Show vertices with no weights in the active group.

  * ``ALL``
All -- Show vertices with no weights in any group.

  """

  vertex_group_weight: float = ...

  """

  Weight to assign in vertex groups

  """

  vertex_paint: VertexPaint = ...

  weight_paint: VertexPaint = ...

  workspace_tool_type: str = ...

  """

  Action when dragging in the viewport

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class TransformOrientation(bpy_struct):

  matrix: typing.Tuple[typing.Tuple[float, float, float], typing.Tuple[float, float, float], typing.Tuple[float, float, float]] = ...

  name: str = ...

  """

  Name of the custom transform orientation

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class TransformOrientationSlot(bpy_struct):

  custom_orientation: TransformOrientation = ...

  type: str = ...

  """

  Transformation orientation

  * ``GLOBAL``
Global -- Align the transformation axes to world space.

  * ``LOCAL``
Local -- Align the transformation axes to the selected objects' local space.

  * ``NORMAL``
Normal -- Align the transformation axes to average normal of selected elements (bone Y axis for pose mode).

  * ``GIMBAL``
Gimbal -- Align each axis to the Euler rotation axis as used for input.

  * ``VIEW``
View -- Align the transformation axes to the window.

  * ``CURSOR``
Cursor -- Align the transformation axes to the 3D cursor.

  """

  use: bool = ...

  """

  Use scene orientation instead of a custom setting

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class UDIMTile(bpy_struct):

  """

  Properties of the UDIM tile

  """

  label: str = ...

  """

  Tile label

  """

  number: int = ...

  """

  Number of the position that this tile covers

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class UDIMTiles(bpy_struct):

  """

  Collection of UDIM tiles

  """

  active: UDIMTile = ...

  """

  Active Image Tile

  """

  active_index: int = ...

  """

  Active index in tiles array

  """

  def new(self, tile_number: int, label: str = '') -> UDIMTile:

    """

    Add a tile to the image

    """

    ...

  def get(self, tile_number: int) -> UDIMTile:

    """

    Get a tile based on its tile number

    """

    ...

  def remove(self, tile: UDIMTile) -> None:

    """

    Remove an image tile

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class UILayout(bpy_struct):

  """

  User interface layout in a panel or header

  """

  activate_init: bool = ...

  """

  When true, buttons defined in popups will be activated on first display (use so you can type into a field without having to click on it first)

  """

  active: bool = ...

  active_default: bool = ...

  """

  When true, an operator button defined after this will be activated when pressing return(use with popup dialogs)

  """

  alert: bool = ...

  alignment: str = ...

  direction: str = ...

  emboss: str = ...

  """

  * ``NORMAL``
Regular -- Draw standard button emboss style.

  * ``NONE``
None -- Draw only text and icons.

  * ``PULLDOWN_MENU``
Pulldown Menu -- Draw pulldown menu style.

  * ``RADIAL_MENU``
Radial Menu -- Draw radial menu style.

  * ``NONE_OR_STATUS``
None or Status -- Draw with no emboss unless the button has a coloring status like an animation state.

  """

  enabled: bool = ...

  """

  When false, this (sub)layout is grayed out

  """

  operator_context: str = ...

  scale_x: float = ...

  """

  Scale factor along the X for items in this (sub)layout

  """

  scale_y: float = ...

  """

  Scale factor along the Y for items in this (sub)layout

  """

  ui_units_x: float = ...

  """

  Fixed size along the X for items in this (sub)layout

  """

  ui_units_y: float = ...

  """

  Fixed size along the Y for items in this (sub)layout

  """

  use_property_decorate: bool = ...

  use_property_split: bool = ...

  def row(self, align: bool = False, heading: str = '', heading_ctxt: str = '', translate: bool = True) -> UILayout:

    """

    Sub-layout. Items placed in this sublayout are placed next to each other in a row

    """

    ...

  def column(self, align: bool = False, heading: str = '', heading_ctxt: str = '', translate: bool = True) -> UILayout:

    """

    Sub-layout. Items placed in this sublayout are placed under each other in a column

    """

    ...

  def column_flow(self, columns: int = 0, align: bool = False) -> UILayout:

    """

    column_flow

    """

    ...

  def grid_flow(self, row_major: bool = False, columns: int = 0, even_columns: bool = False, even_rows: bool = False, align: bool = False) -> UILayout:

    """

    grid_flow

    """

    ...

  def box(self) -> UILayout:

    """

    Sublayout (items placed in this sublayout are placed under each other in a column and are surrounded by a box)

    """

    ...

  def split(self, factor: float = 0.0, align: bool = False) -> UILayout:

    """

    split

    """

    ...

  def menu_pie(self) -> UILayout:

    """

    Sublayout. Items placed in this sublayout are placed in a radial fashion around the menu center)

    """

    ...

  @classmethod

  def icon(cls, data: typing.Any) -> int:

    """

    Return the custom icon for this data, use it e.g. to get materials or texture icons

    """

    ...

  @classmethod

  def enum_item_name(cls, data: typing.Any, property: str, identifier: str) -> str:

    """

    Return the UI name for this enum item

    """

    ...

  @classmethod

  def enum_item_description(cls, data: typing.Any, property: str, identifier: str) -> str:

    """

    Return the UI description for this enum item

    """

    ...

  @classmethod

  def enum_item_icon(cls, data: typing.Any, property: str, identifier: str) -> int:

    """

    Return the icon for this enum item

    """

    ...

  def prop(self, data: typing.Any, property: str, text: str = '', text_ctxt: str = '', translate: bool = True, icon: str = 'NONE', expand: bool = False, slider: bool = False, toggle: int = -1, icon_only: bool = False, event: bool = False, full_event: bool = False, emboss: bool = True, index: int = -1, icon_value: int = 0, invert_checkbox: bool = False) -> None:

    """

    Item. Exposes an RNA item and places it into the layout

    """

    ...

  def props_enum(self, data: typing.Any, property: str) -> None:

    """

    props_enum

    """

    ...

  def prop_menu_enum(self, data: typing.Any, property: str, text: str = '', text_ctxt: str = '', translate: bool = True, icon: str = 'NONE') -> None:

    """

    prop_menu_enum

    """

    ...

  def prop_tabs_enum(self, data: typing.Any, property: str, data_highlight: typing.Any = None, property_highlight: str = '', icon_only: bool = False) -> None:

    """

    prop_tabs_enum

    """

    ...

  def prop_enum(self, data: typing.Any, property: str, value: str, text: str = '', text_ctxt: str = '', translate: bool = True, icon: str = 'NONE') -> None:

    """

    prop_enum

    """

    ...

  def prop_search(self, data: typing.Any, property: str, search_data: typing.Any, search_property: str, text: str = '', text_ctxt: str = '', translate: bool = True, icon: str = 'NONE') -> None:

    """

    prop_search

    """

    ...

  def prop_decorator(self, data: typing.Any, property: str, index: int = -1) -> None:

    """

    prop_decorator

    """

    ...

  def operator(self, operator: str, text: str = '', text_ctxt: str = '', translate: bool = True, icon: str = 'NONE', emboss: bool = True, depress: bool = False, icon_value: int = 0) -> OperatorProperties:

    """

    Item. Places a button into the layout to call an Operator

    """

    ...

  def operator_enum(self, operator: str, property: str, icon_only: bool = False) -> None:

    """

    operator_enum

    """

    ...

  def operator_menu_enum(self, operator: str, property: str, text: str = '', text_ctxt: str = '', translate: bool = True, icon: str = 'NONE') -> OperatorProperties:

    """

    operator_menu_enum

    """

    ...

  def label(self, text: str = '', text_ctxt: str = '', translate: bool = True, icon: str = 'NONE', icon_value: int = 0) -> None:

    """

    Item. Displays text and/or icon in the layout

    """

    ...

  def menu(self, menu: str, text: str = '', text_ctxt: str = '', translate: bool = True, icon: str = 'NONE', icon_value: int = 0) -> None:

    """

    menu

    """

    ...

  def menu_contents(self, menu: str) -> None:

    """

    menu_contents

    """

    ...

  def popover(self, panel: str, text: str = '', text_ctxt: str = '', translate: bool = True, icon: str = 'NONE', icon_value: int = 0) -> None:

    """

    popover

    """

    ...

  def popover_group(self, space_type: str, region_type: str, context: str, category: str) -> None:

    """

    popover_group

    """

    ...

  def separator(self, factor: float = 1.0) -> None:

    """

    Item. Inserts empty space into the layout between items

    """

    ...

  def separator_spacer(self) -> None:

    """

    Item. Inserts horizontal spacing empty space into the layout between items

    """

    ...

  def context_pointer_set(self, name: str, data: typing.Any) -> None:

    """

    context_pointer_set

    """

    ...

  def template_header(self) -> None:

    """

    Inserts common Space header UI (editor type selector)

    """

    ...

  def template_ID(self, data: typing.Any, property: str, new: str = '', open: str = '', unlink: str = '', filter: str = 'ALL', live_icon: bool = False, text: str = '', text_ctxt: str = '', translate: bool = True) -> None:

    """

    template_ID

    """

    ...

  def template_ID_preview(self, data: typing.Any, property: str, new: str = '', open: str = '', unlink: str = '', rows: int = 0, cols: int = 0, filter: str = 'ALL', hide_buttons: bool = False) -> None:

    """

    template_ID_preview

    """

    ...

  def template_any_ID(self, data: typing.Any, property: str, type_property: str, text: str = '', text_ctxt: str = '', translate: bool = True) -> None:

    """

    template_any_ID

    """

    ...

  def template_ID_tabs(self, data: typing.Any, property: str, new: str = '', menu: str = '', filter: str = 'ALL') -> None:

    """

    template_ID_tabs

    """

    ...

  def template_search(self, data: typing.Any, property: str, search_data: typing.Any, search_property: str, new: str = '', unlink: str = '') -> None:

    """

    template_search

    """

    ...

  def template_search_preview(self, data: typing.Any, property: str, search_data: typing.Any, search_property: str, new: str = '', unlink: str = '', rows: int = 0, cols: int = 0) -> None:

    """

    template_search_preview

    """

    ...

  def template_path_builder(self, data: typing.Any, property: str, root: ID, text: str = '', text_ctxt: str = '', translate: bool = True) -> None:

    """

    template_path_builder

    """

    ...

  def template_modifiers(self) -> None:

    """

    Generates the UI layout for the modifier stack

    """

    ...

  def template_constraints(self, use_bone_constraints: bool = True) -> None:

    """

    Generates the panels for the constraint stack

    """

    ...

  def template_grease_pencil_modifiers(self) -> None:

    """

    Generates the panels for the grease pencil modifier stack

    """

    ...

  def template_shaderfx(self) -> None:

    """

    Generates the panels for the shader effect stack

    """

    ...

  def template_greasepencil_color(self, data: typing.Any, property: str, rows: int = 0, cols: int = 0, scale: float = 1.0, filter: str = 'ALL') -> None:

    """

    template_greasepencil_color

    """

    ...

  def template_constraint_header(self, data: Constraint) -> None:

    """

    Generates the header for constraint panels

    """

    ...

  def template_preview(self, id: ID, show_buttons: bool = True, parent: ID = None, slot: TextureSlot = None, preview_id: str = '') -> None:

    """

    Item. A preview window for materials, textures, lights or worlds

    """

    ...

  def template_curve_mapping(self, data: typing.Any, property: str, type: str = 'NONE', levels: bool = False, brush: bool = False, use_negative_slope: bool = False, show_tone: bool = False) -> None:

    """

    Item. A curve mapping widget used for e.g falloff curves for lights

    """

    ...

  def template_curveprofile(self, data: typing.Any, property: str) -> None:

    """

    A profile path editor used for custom profiles

    """

    ...

  def template_color_ramp(self, data: typing.Any, property: str, expand: bool = False) -> None:

    """

    Item. A color ramp widget

    """

    ...

  def template_icon(self, icon_value: int, scale: float = 1.0) -> None:

    """

    Display a large icon

    """

    ...

  def template_icon_view(self, data: typing.Any, property: str, show_labels: bool = False, scale: float = 6.0, scale_popup: float = 5.0) -> None:

    """

    Enum. Large widget showing Icon previews

    """

    ...

  def template_histogram(self, data: typing.Any, property: str) -> None:

    """

    Item. A histogramm widget to analyze imaga data

    """

    ...

  def template_waveform(self, data: typing.Any, property: str) -> None:

    """

    Item. A waveform widget to analyze imaga data

    """

    ...

  def template_vectorscope(self, data: typing.Any, property: str) -> None:

    """

    Item. A vectorscope widget to analyze imaga data

    """

    ...

  def template_layers(self, data: typing.Any, property: str, used_layers_data: typing.Any, used_layers_property: str, active_layer: int) -> None:

    """

    template_layers

    """

    ...

  def template_color_picker(self, data: typing.Any, property: str, value_slider: bool = False, lock: bool = False, lock_luminosity: bool = False, cubic: bool = False) -> None:

    """

    Item. A color wheel widget to pick colors

    """

    ...

  def template_palette(self, data: typing.Any, property: str, color: bool = False) -> None:

    """

    Item. A palette used to pick colors

    """

    ...

  def template_image_layers(self, image: Image, image_user: ImageUser) -> None:

    """

    template_image_layers

    """

    ...

  def template_image(self, data: typing.Any, property: str, image_user: ImageUser, compact: bool = False, multiview: bool = False) -> None:

    """

    Item(s). User interface for selecting images and their source paths

    """

    ...

  def template_image_settings(self, image_settings: ImageFormatSettings, color_management: bool = False) -> None:

    """

    User interface for setting image format options

    """

    ...

  def template_image_stereo_3d(self, stereo_3d_format: Stereo3dFormat) -> None:

    """

    User interface for setting image stereo 3d options

    """

    ...

  def template_image_views(self, image_settings: ImageFormatSettings) -> None:

    """

    User interface for setting image views output options

    """

    ...

  def template_movieclip(self, data: typing.Any, property: str, compact: bool = False) -> None:

    """

    Item(s). User interface for selecting movie clips and their source paths

    """

    ...

  def template_track(self, data: typing.Any, property: str) -> None:

    """

    Item. A movie-track widget to preview tracking image.

    """

    ...

  def template_marker(self, data: typing.Any, property: str, clip_user: MovieClipUser, track: MovieTrackingTrack, compact: bool = False) -> None:

    """

    Item. A widget to control single marker settings.

    """

    ...

  def template_movieclip_information(self, data: typing.Any, property: str, clip_user: MovieClipUser) -> None:

    """

    Item. Movie clip information data.

    """

    ...

  def template_list(self, listtype_name: str, list_id: str, dataptr: typing.Any, propname: str, active_dataptr: typing.Any, active_propname: str, item_dyntip_propname: str = '', rows: int = 5, maxrows: int = 5, type: str = 'DEFAULT', columns: int = 9, sort_reverse: bool = False, sort_lock: bool = False) -> None:

    """

    Item. A list widget to display data, e.g. vertexgroups.

    """

    ...

  def template_running_jobs(self) -> None:

    """

    template_running_jobs

    """

    ...

  def template_operator_search(self) -> None:

    """

    template_operator_search

    """

    ...

  def template_menu_search(self) -> None:

    """

    template_menu_search

    """

    ...

  def template_header_3D_mode(self) -> None:

    ...

  def template_edit_mode_selection(self) -> None:

    """

    Inserts common 3DView Edit modes header UI (selector for selection mode)

    """

    ...

  def template_reports_banner(self) -> None:

    """

    template_reports_banner

    """

    ...

  def template_input_status(self) -> None:

    """

    template_input_status

    """

    ...

  def template_node_link(self, ntree: NodeTree, node: Node, socket: NodeSocket) -> None:

    """

    template_node_link

    """

    ...

  def template_node_view(self, ntree: NodeTree, node: Node, socket: NodeSocket) -> None:

    """

    template_node_view

    """

    ...

  def template_texture_user(self) -> None:

    """

    template_texture_user

    """

    ...

  def template_keymap_item_properties(self, item: KeyMapItem) -> None:

    """

    template_keymap_item_properties

    """

    ...

  def template_component_menu(self, data: typing.Any, property: str, name: str = '') -> None:

    """

    Item. Display expanded property in a popup menu

    """

    ...

  def template_colorspace_settings(self, data: typing.Any, property: str) -> None:

    """

    Item. A widget to control input color space settings.

    """

    ...

  def template_colormanaged_view_settings(self, data: typing.Any, property: str) -> None:

    """

    Item. A widget to control color managed view settings settings.

    """

    ...

  def template_node_socket(self, color: typing.Tuple[float, float, float, float] = (0.0, 0.0, 0.0, 1.0)) -> None:

    """

    Node Socket Icon

    """

    ...

  def template_cache_file(self, data: typing.Any, property: str) -> None:

    """

    Item(s). User interface for selecting cache files and their source paths

    """

    ...

  def template_recent_files(self, rows: int = 5) -> int:

    """

    Show list of recently saved .blend files

    """

    ...

  def template_file_select_path(self, params: FileSelectParams) -> None:

    """

    Item. A text button to set the active file browser path.

    """

    ...

  def template_event_from_keymap_item(self, item: KeyMapItem, text: str = '', text_ctxt: str = '', translate: bool = True) -> None:

    """

    Display keymap item as icons/text

    """

    ...

  def template_asset_view(self, list_id: str, asset_library_dataptr: typing.Any, asset_library_propname: str, assets_dataptr: typing.Any, assets_propname: str, active_dataptr: typing.Any, active_propname: str, filter_id_types: typing.Set[str] = {}, display_options: typing.Set[str] = {}, activate_operator: str = '', drag_operator: str = '') -> None:

    """

    Item. A scrollable list of assets in a grid view

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class UIList(bpy_struct):

  """

  UI list containing the elements of a collection

  """

  bitflag_filter_item: int = ...

  """

  The value of the reserved bitflag 'FILTER_ITEM' (in filter_flags values)

  """

  bl_idname: str = ...

  """

  If this is set, the uilist gets a custom ID, otherwise it takes the name of the class used to define the uilist (for example, if the class name is "OBJECT_UL_vgroups", and bl_idname is not set by the script, then bl_idname = "OBJECT_UL_vgroups")

  """

  filter_name: str = ...

  """

  Only show items matching this name (use '*' as wildcard)

  """

  layout_type: str = ...

  """

  * ``DEFAULT``
Default Layout -- Use the default, multi-rows layout.

  * ``COMPACT``
Compact Layout -- Use the compact, single-row layout.

  * ``GRID``
Grid Layout -- Use the grid-based layout.

  """

  list_id: str = ...

  """

  Identifier of the list, if any was passed to the "list_id" parameter of "template_list()"

  """

  use_filter_invert: bool = ...

  """

  Invert filtering (show hidden items, and vice versa)

  """

  use_filter_show: bool = ...

  """

  Show filtering options

  """

  use_filter_sort_alpha: bool = ...

  """

  Sort items by their name

  """

  use_filter_sort_lock: bool = ...

  """

  Lock the order of shown items (user cannot change it)

  """

  use_filter_sort_reverse: bool = ...

  """

  Reverse the order of shown items

  """

  def draw_item(self, context: Context, layout: UILayout, data: typing.Any, item: typing.Any, icon: int, active_data: typing.Any, active_property: str, index: int = 0, flt_flag: int = 0) -> None:

    """

    Draw an item in the list (NOTE: when you define your own draw_item function, you may want to check given 'item' is of the right type...)

    """

    ...

  def draw_filter(self, context: Context, layout: UILayout) -> None:

    """

    Draw filtering options

    """

    ...

  def filter_items(self, context: Context, data: typing.Any, property: str) -> None:

    """

    Filter and/or re-order items of the collection (output filter results in filter_flags, and reorder results in filter_neworder arrays)

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class UIPieMenu(bpy_struct):

  layout: UILayout = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class UIPopover(bpy_struct):

  layout: UILayout = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class UIPopupMenu(bpy_struct):

  layout: UILayout = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class UnifiedPaintSettings(bpy_struct):

  """

  Overrides for some of the active brush's settings

  """

  color: typing.Tuple[float, float, float] = ...

  secondary_color: typing.Tuple[float, float, float] = ...

  size: int = ...

  """

  Radius of the brush

  """

  strength: float = ...

  """

  How powerful the effect of the brush is when applied

  """

  unprojected_radius: float = ...

  """

  Radius of brush in Blender units

  """

  use_locked_size: str = ...

  """

  Measure brush size relative to the view or the scene

  * ``VIEW``
View -- Measure brush size relative to the view.

  * ``SCENE``
Scene -- Measure brush size relative to the scene.

  """

  use_unified_color: bool = ...

  """

  Instead of per-brush color, the color is shared across brushes

  """

  use_unified_size: bool = ...

  """

  Instead of per-brush radius, the radius is shared across brushes

  """

  use_unified_strength: bool = ...

  """

  Instead of per-brush strength, the strength is shared across brushes

  """

  use_unified_weight: bool = ...

  """

  Instead of per-brush weight, the weight is shared across brushes

  """

  weight: float = ...

  """

  Weight to assign in vertex groups

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class UnitSettings(bpy_struct):

  length_unit: str = ...

  """

  Unit that will be used to display length values

  """

  mass_unit: str = ...

  """

  Unit that will be used to display mass values

  """

  scale_length: float = ...

  """

  Scale to use when converting between blender units and dimensions. When working at microscopic or astronomical scale, a small or large unit scale respectively can be used to avoid numerical precision problems

  """

  system: str = ...

  """

  The unit system to use for user interface controls

  """

  system_rotation: str = ...

  """

  Unit to use for displaying/editing rotation values

  * ``DEGREES``
Degrees -- Use degrees for measuring angles and rotations.

  * ``RADIANS``
Radians.

  """

  temperature_unit: str = ...

  """

  Unit that will be used to display temperature values

  """

  time_unit: str = ...

  """

  Unit that will be used to display time values

  """

  use_separate: bool = ...

  """

  Display units in pairs (e.g. 1m 0cm)

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class UnknownType(bpy_struct):

  """

  Stub RNA type used for pointers to unknown or internal data

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class UserAssetLibrary(bpy_struct):

  """

  Settings to define a reusable library for Asset Browsers to use

  """

  name: str = ...

  """

  Identifier (not necessarily unique) for the asset library

  """

  path: str = ...

  """

  Path to a directory with .blend files to use as an asset library

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class UserSolidLight(bpy_struct):

  """

  Light used for Studio lighting in solid shading mode

  """

  diffuse_color: typing.Tuple[float, float, float] = ...

  """

  Color of the light's diffuse highlight

  """

  direction: typing.Tuple[float, float, float] = ...

  """

  Direction that the light is shining

  """

  smooth: float = ...

  """

  Smooth the lighting from this light

  """

  specular_color: typing.Tuple[float, float, float] = ...

  """

  Color of the light's specular highlight

  """

  use: bool = ...

  """

  Enable this light in solid shading mode

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class UVLoopLayers(bpy_struct):

  """

  Collection of uv loop layers

  """

  active: MeshUVLoopLayer = ...

  """

  Active UV loop layer

  """

  active_index: int = ...

  """

  Active UV loop layer index

  """

  def new(self, name: str = 'UVMap', do_init: bool = True) -> MeshUVLoopLayer:

    """

    Add a UV map layer to Mesh

    """

    ...

  def remove(self, layer: MeshUVLoopLayer) -> None:

    """

    Remove a vertex color layer

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class UVProjector(bpy_struct):

  """

  UV projector used by the UV project modifier

  """

  object: Object = ...

  """

  Object to use as projector transform

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class VertColors(bpy_struct):

  """

  Collection of sculpt vertex colors

  """

  active: MeshVertColorLayer = ...

  """

  Active sculpt vertex color layer

  """

  active_index: int = ...

  """

  Active sculpt vertex color index

  """

  def new(self, name: str = 'Col', do_init: bool = True) -> MeshVertColorLayer:

    """

    Add a sculpt vertex color layer to Mesh

    """

    ...

  def remove(self, layer: MeshVertColorLayer) -> None:

    """

    Remove a vertex color layer

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class VertexFloatProperties(bpy_struct):

  """

  Collection of float properties

  """

  def new(self, name: str = 'Float Prop') -> MeshVertexFloatPropertyLayer:

    """

    Add a float property layer to Mesh

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class VertexGroup(bpy_struct):

  """

  Group of vertices, used for armature deform and other purposes

  """

  index: int = ...

  """

  Index number of the vertex group

  """

  lock_weight: bool = ...

  """

  Maintain the relative weights for the group

  """

  name: str = ...

  """

  Vertex group name

  """

  def add(self, index: typing.Tuple[int], weight: float, type: str) -> None:

    """

    Add vertices to the group

    """

    ...

  def remove(self, index: typing.Tuple[int]) -> None:

    """

    Remove vertices from the group

    """

    ...

  def weight(self, index: int) -> float:

    """

    Get a vertex weight from the group

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class VertexGroupElement(bpy_struct):

  """

  Weight value of a vertex in a vertex group

  """

  group: int = ...

  weight: float = ...

  """

  Vertex Weight

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class VertexGroups(bpy_struct):

  """

  Collection of vertex groups

  """

  active: VertexGroup = ...

  """

  Vertex groups of the object

  """

  active_index: int = ...

  """

  Active index in vertex group array

  """

  def new(self, name: str = 'Group') -> VertexGroup:

    """

    Add vertex group to object

    """

    ...

  def remove(self, group: VertexGroup) -> None:

    """

    Delete vertex group from object

    """

    ...

  def clear(self) -> None:

    """

    Delete all vertex groups from object

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class VertexIntProperties(bpy_struct):

  """

  Collection of int properties

  """

  def new(self, name: str = 'Int Prop') -> MeshVertexIntPropertyLayer:

    """

    Add a integer property layer to Mesh

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class VertexStringProperties(bpy_struct):

  """

  Collection of string properties

  """

  def new(self, name: str = 'String Prop') -> MeshVertexStringPropertyLayer:

    """

    Add a string property layer to Mesh

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class View2D(bpy_struct):

  """

  Scroll and zoom for a 2D region

  """

  def region_to_view(self, x: float, y: float) -> typing.Tuple[float, float]:

    """

    Transform region coordinates to 2D view

    """

    ...

  def view_to_region(self, x: float, y: float, clip: bool = True) -> typing.Tuple[int, int]:

    """

    Transform 2D view coordinates to region

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class View3DCursor(bpy_struct):

  location: typing.Tuple[float, float, float] = ...

  matrix: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]] = ...

  """

  Matrix combining location and rotation of the cursor

  """

  rotation_axis_angle: typing.Tuple[float, float, float, float] = ...

  """

  Angle of Rotation for Axis-Angle rotation representation

  """

  rotation_euler: typing.Tuple[float, float, float] = ...

  """

  3D rotation

  """

  rotation_mode: str = ...

  """

  * ``QUATERNION``
Quaternion (WXYZ) -- No Gimbal Lock.

  * ``XYZ``
XYZ Euler -- XYZ Rotation Order - prone to Gimbal Lock (default).

  * ``XZY``
XZY Euler -- XZY Rotation Order - prone to Gimbal Lock.

  * ``YXZ``
YXZ Euler -- YXZ Rotation Order - prone to Gimbal Lock.

  * ``YZX``
YZX Euler -- YZX Rotation Order - prone to Gimbal Lock.

  * ``ZXY``
ZXY Euler -- ZXY Rotation Order - prone to Gimbal Lock.

  * ``ZYX``
ZYX Euler -- ZYX Rotation Order - prone to Gimbal Lock.

  * ``AXIS_ANGLE``
Axis Angle -- Axis Angle (W+XYZ), defines a rotation around some axis defined by 3D-Vector.

  """

  rotation_quaternion: typing.Tuple[float, float, float, float] = ...

  """

  Rotation in quaternions (keep normalized)

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class View3DOverlay(bpy_struct):

  """

  Settings for display of overlays in the 3D viewport

  """

  backwire_opacity: float = ...

  """

  Opacity when rendering transparent wires

  """

  display_handle: str = ...

  """

  Limit the display of curve handles in edit mode

  """

  fade_inactive_alpha: float = ...

  """

  Strength of the fade effect

  """

  gpencil_fade_layer: float = ...

  """

  Fade layer opacity for Grease Pencil layers except the active one

  """

  gpencil_fade_objects: float = ...

  """

  Fade factor

  """

  gpencil_grid_opacity: float = ...

  """

  Canvas grid opacity

  """

  gpencil_vertex_paint_opacity: float = ...

  """

  Vertex Paint mix factor

  """

  grid_lines: int = ...

  """

  Number of grid lines to display in perspective view

  """

  grid_scale: float = ...

  """

  Multiplier for the distance between 3D View grid lines

  """

  grid_scale_unit: float = ...

  """

  Grid cell size scaled by scene unit system settings

  """

  grid_subdivisions: int = ...

  """

  Number of subdivisions between grid lines

  """

  normals_constant_screen_size: float = ...

  """

  Screen size for normals in the 3D view

  """

  normals_length: float = ...

  """

  Display size for normals in the 3D view

  """

  sculpt_mode_face_sets_opacity: float = ...

  sculpt_mode_mask_opacity: float = ...

  show_annotation: bool = ...

  """

  Show annotations for this view

  """

  show_axis_x: bool = ...

  """

  Show the X axis line

  """

  show_axis_y: bool = ...

  """

  Show the Y axis line

  """

  show_axis_z: bool = ...

  """

  Show the Z axis line

  """

  show_bones: bool = ...

  """

  Display bones (disable to show motion paths only)

  """

  show_cursor: bool = ...

  """

  Display 3D Cursor Overlay

  """

  show_curve_normals: bool = ...

  """

  Display 3D curve normals in editmode

  """

  show_edge_bevel_weight: bool = ...

  """

  Display weights created for the Bevel modifier

  """

  show_edge_crease: bool = ...

  """

  Display creases created for Subdivision Surface modifier

  """

  show_edge_seams: bool = ...

  """

  Display UV unwrapping seams

  """

  show_edge_sharp: bool = ...

  """

  Display sharp edges, used with the Edge Split modifier

  """

  show_edges: bool = ...

  """

  Highlight selected edges

  """

  show_extra_edge_angle: bool = ...

  """

  Display selected edge angle, using global values when set in the transform panel

  """

  show_extra_edge_length: bool = ...

  """

  Display selected edge lengths, using global values when set in the transform panel

  """

  show_extra_face_angle: bool = ...

  """

  Display the angles in the selected edges, using global values when set in the transform panel

  """

  show_extra_face_area: bool = ...

  """

  Display the area of selected faces, using global values when set in the transform panel

  """

  show_extra_indices: bool = ...

  """

  Display the index numbers of selected vertices, edges, and faces

  """

  show_extras: bool = ...

  """

  Object details, including empty wire, cameras and other visual guides

  """

  show_face_center: bool = ...

  """

  Display face center when face selection is enabled in solid shading modes

  """

  show_face_normals: bool = ...

  """

  Display face normals as lines

  """

  show_face_orientation: bool = ...

  """

  Show the Face Orientation Overlay

  """

  show_faces: bool = ...

  """

  Highlight selected faces

  """

  show_fade_inactive: bool = ...

  """

  Fade inactive geometry using the viewport background color

  """

  show_floor: bool = ...

  """

  Show the ground plane grid

  """

  show_freestyle_edge_marks: bool = ...

  """

  Display Freestyle edge marks, used with the Freestyle renderer

  """

  show_freestyle_face_marks: bool = ...

  """

  Display Freestyle face marks, used with the Freestyle renderer

  """

  show_look_dev: bool = ...

  """

  Show HDRI preview spheres

  """

  show_motion_paths: bool = ...

  """

  Show the Motion Paths Overlay

  """

  show_object_origins: bool = ...

  """

  Show object center dots

  """

  show_object_origins_all: bool = ...

  """

  Show the object origin center dot for all (selected and unselected) objects

  """

  show_occlude_wire: bool = ...

  """

  Use hidden wireframe display

  """

  show_onion_skins: bool = ...

  """

  Show the Onion Skinning Overlay

  """

  show_ortho_grid: bool = ...

  """

  Show grid in orthographic side view

  """

  show_outline_selected: bool = ...

  """

  Show an outline highlight around selected objects

  """

  show_overlays: bool = ...

  """

  Display overlays like gizmos and outlines

  """

  show_paint_wire: bool = ...

  """

  Use wireframe display in painting modes

  """

  show_relationship_lines: bool = ...

  """

  Show dashed lines indicating parent or constraint relationships

  """

  show_split_normals: bool = ...

  """

  Display vertex-per-face normals as lines

  """

  show_stats: bool = ...

  """

  Display scene statistics overlay text

  """

  show_statvis: bool = ...

  """

  Display statistical information about the mesh

  """

  show_text: bool = ...

  """

  Display overlay text

  """

  show_vertex_normals: bool = ...

  """

  Display vertex normals as lines

  """

  show_weight: bool = ...

  """

  Display weights in editmode

  """

  show_wireframes: bool = ...

  """

  Show face edges wires

  """

  show_wpaint_contours: bool = ...

  """

  Show contour lines formed by points with the same interpolated weight

  """

  show_xray_bone: bool = ...

  """

  Show the bone selection overlay

  """

  texture_paint_mode_opacity: float = ...

  """

  Opacity of the texture paint mode stencil mask overlay

  """

  use_gpencil_canvas_xray: bool = ...

  """

  Show Canvas grid in front

  """

  use_gpencil_edit_lines: bool = ...

  """

  Show Edit Lines when editing strokes

  """

  use_gpencil_fade_gp_objects: bool = ...

  """

  Fade Grease Pencil Objects, except the active one

  """

  use_gpencil_fade_layers: bool = ...

  """

  Toggle fading of Grease Pencil layers except the active one

  """

  use_gpencil_fade_objects: bool = ...

  """

  Fade all viewport objects with a full color layer to improve visibility

  """

  use_gpencil_grid: bool = ...

  """

  Display a grid over grease pencil paper

  """

  use_gpencil_multiedit_line_only: bool = ...

  """

  Show Edit Lines only in multiframe

  """

  use_gpencil_onion_skin: bool = ...

  """

  Show ghosts of the keyframes before and after the current frame

  """

  use_gpencil_show_directions: bool = ...

  """

  Show stroke drawing direction with a bigger green dot (start) and smaller red dot (end) points

  """

  use_gpencil_show_material_name: bool = ...

  """

  Show material name assigned to each stroke

  """

  use_normals_constant_screen_size: bool = ...

  """

  Keep size of normals constant in relation to 3D view

  """

  vertex_opacity: float = ...

  """

  Opacity for edit vertices

  """

  vertex_paint_mode_opacity: float = ...

  """

  Opacity of the texture paint mode stencil mask overlay

  """

  weight_paint_mode_opacity: float = ...

  """

  Opacity of the weight paint mode overlay

  """

  wireframe_opacity: float = ...

  """

  Opacity of the displayed edges (1.0 for opaque)

  """

  wireframe_threshold: float = ...

  """

  Adjust the angle threshold for displaying edges (1.0 for all)

  """

  xray_alpha_bone: float = ...

  """

  Opacity to use for bone selection

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class View3DShading(bpy_struct):

  """

  Settings for shading in the 3D viewport

  """

  aov_name: str = ...

  """

  Name of the active Shader AOV

  """

  background_color: typing.Tuple[float, float, float] = ...

  """

  Color for custom background color

  """

  background_type: str = ...

  """

  Way to display the background

  * ``THEME``
Theme -- Use the theme for background color.

  * ``WORLD``
World -- Use the world for background color.

  * ``VIEWPORT``
Viewport -- Use a custom color limited to this viewport only.

  """

  cavity_ridge_factor: float = ...

  """

  Factor for the cavity ridges

  """

  cavity_type: str = ...

  """

  Way to display the cavity shading

  * ``WORLD``
World -- Cavity shading computed in world space, useful for larger-scale occlusion.

  * ``SCREEN``
Screen -- Curvature-based shading, useful for making fine details more visible.

  * ``BOTH``
Both -- Use both effects simultaneously.

  """

  cavity_valley_factor: float = ...

  """

  Factor for the cavity valleys

  """

  color_type: str = ...

  """

  Color Type

  * ``MATERIAL``
Material -- Show material color.

  * ``SINGLE``
Single -- Show scene in a single color.

  * ``OBJECT``
Object -- Show object color.

  * ``RANDOM``
Random -- Show random object color.

  * ``VERTEX``
Vertex -- Show active vertex color.

  * ``TEXTURE``
Texture -- Show texture.

  """

  curvature_ridge_factor: float = ...

  """

  Factor for the curvature ridges

  """

  curvature_valley_factor: float = ...

  """

  Factor for the curvature valleys

  """

  cycles: CyclesView3DShadingSettings = ...

  light: str = ...

  """

  Lighting Method for Solid/Texture Viewport Shading

  * ``STUDIO``
Studio -- Display using studio lighting.

  * ``MATCAP``
MatCap -- Display using matcap material and lighting.

  * ``FLAT``
Flat -- Display using flat lighting.

  """

  object_outline_color: typing.Tuple[float, float, float] = ...

  """

  Color for object outline

  """

  render_pass: str = ...

  """

  Render Pass to show in the viewport

  """

  selected_studio_light: StudioLight = ...

  """

  Selected StudioLight

  """

  shadow_intensity: float = ...

  """

  Darkness of shadows

  """

  show_backface_culling: bool = ...

  """

  Use back face culling to hide the back side of faces

  """

  show_cavity: bool = ...

  """

  Show Cavity

  """

  show_object_outline: bool = ...

  """

  Show Object Outline

  """

  show_shadows: bool = ...

  """

  Show Shadow

  """

  show_specular_highlight: bool = ...

  """

  Render specular highlights

  """

  show_xray: bool = ...

  """

  Show whole scene transparent

  """

  show_xray_wireframe: bool = ...

  """

  Show whole scene transparent

  """

  single_color: typing.Tuple[float, float, float] = ...

  """

  Color for single color mode

  """

  studio_light: str = ...

  """

  Studio lighting setup

  """

  studiolight_background_alpha: float = ...

  """

  Show the studiolight in the background

  """

  studiolight_background_blur: float = ...

  """

  Blur the studiolight in the background

  """

  studiolight_intensity: float = ...

  """

  Strength of the studiolight

  """

  studiolight_rotate_z: float = ...

  """

  Rotation of the studiolight around the Z-Axis

  """

  type: str = ...

  """

  Method to display/shade objects in the 3D View

  * ``WIREFRAME``
Wireframe -- Display the object as wire edges.

  * ``SOLID``
Solid -- Display in solid mode.

  * ``MATERIAL``
Material Preview -- Display in Material Preview mode.

  * ``RENDERED``
Rendered -- Display render preview.

  """

  use_dof: bool = ...

  """

  Use depth of field on viewport using the values from the active camera

  """

  use_scene_lights: bool = ...

  """

  Render lights and light probes of the scene

  """

  use_scene_lights_render: bool = ...

  """

  Render lights and light probes of the scene

  """

  use_scene_world: bool = ...

  """

  Use scene world for lighting

  """

  use_scene_world_render: bool = ...

  """

  Use scene world for lighting

  """

  use_studiolight_view_rotation: bool = ...

  """

  Make the HDR rotation fixed and not follow the camera

  """

  use_world_space_lighting: bool = ...

  """

  Make the lighting fixed and not follow the camera

  """

  wireframe_color_type: str = ...

  """

  Color Type

  * ``MATERIAL``
Material -- Show material color.

  * ``SINGLE``
Single -- Show scene in a single color.

  * ``OBJECT``
Object -- Show object color.

  * ``RANDOM``
Random -- Show random object color.

  * ``VERTEX``
Vertex -- Show active vertex color.

  * ``TEXTURE``
Texture -- Show texture.

  """

  xray_alpha: float = ...

  """

  Amount of alpha to use

  """

  xray_alpha_wireframe: float = ...

  """

  Amount of alpha to use

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ViewLayer(bpy_struct):

  """

  View layer

  """

  active_aov: AOV = ...

  """

  Active AOV

  """

  active_aov_index: int = ...

  """

  Index of active aov

  """

  active_layer_collection: LayerCollection = ...

  """

  Active layer collection in this view layer's hierarchy

  """

  aovs: typing.Union[AOVs, typing.Sequence[AOV], typing.Mapping[str, AOV], bpy_prop_collection] = ...

  cycles: CyclesRenderLayerSettings = ...

  """

  Cycles ViewLayer Settings

  """

  depsgraph: Depsgraph = ...

  """

  Dependencies in the scene data

  """

  eevee: ViewLayerEEVEE = ...

  """

  View layer settings for Eevee

  """

  freestyle_settings: FreestyleSettings = ...

  layer_collection: LayerCollection = ...

  """

  Root of collections hierarchy of this view layer,its 'collection' pointer property is the same as the scene's master collection

  """

  material_override: Material = ...

  """

  Material to override all other materials in this view layer

  """

  name: str = ...

  """

  View layer name

  """

  objects: typing.Union[LayerObjects, typing.Sequence[Object], typing.Mapping[str, Object], bpy_prop_collection] = ...

  """

  All the objects in this layer

  """

  pass_alpha_threshold: float = ...

  """

  Z, Index, normal, UV and vector passes are only affected by surfaces with alpha transparency equal to or higher than this threshold

  """

  pass_cryptomatte_depth: int = ...

  """

  Sets how many unique objects can be distinguished per pixel

  """

  samples: int = ...

  """

  Override number of render samples for this view layer, 0 will use the scene setting

  """

  use: bool = ...

  """

  Enable or disable rendering of this View Layer

  """

  use_ao: bool = ...

  """

  Render Ambient Occlusion in this Layer

  """

  use_freestyle: bool = ...

  """

  Render stylized strokes in this Layer

  """

  use_motion_blur: bool = ...

  """

  Render motion blur in this Layer, if enabled in the scene

  """

  use_pass_ambient_occlusion: bool = ...

  """

  Deliver Ambient Occlusion pass

  """

  use_pass_combined: bool = ...

  """

  Deliver full combined RGBA buffer

  """

  use_pass_cryptomatte_accurate: bool = ...

  """

  Generate a more accurate cryptomatte pass

  """

  use_pass_cryptomatte_asset: bool = ...

  """

  Render cryptomatte asset pass, for isolating groups of objects with the same parent

  """

  use_pass_cryptomatte_material: bool = ...

  """

  Render cryptomatte material pass, for isolating materials in compositing

  """

  use_pass_cryptomatte_object: bool = ...

  """

  Render cryptomatte object pass, for isolating objects in compositing

  """

  use_pass_diffuse_color: bool = ...

  """

  Deliver diffuse color pass

  """

  use_pass_diffuse_direct: bool = ...

  """

  Deliver diffuse direct pass

  """

  use_pass_diffuse_indirect: bool = ...

  """

  Deliver diffuse indirect pass

  """

  use_pass_emit: bool = ...

  """

  Deliver emission pass

  """

  use_pass_environment: bool = ...

  """

  Deliver environment lighting pass

  """

  use_pass_glossy_color: bool = ...

  """

  Deliver glossy color pass

  """

  use_pass_glossy_direct: bool = ...

  """

  Deliver glossy direct pass

  """

  use_pass_glossy_indirect: bool = ...

  """

  Deliver glossy indirect pass

  """

  use_pass_material_index: bool = ...

  """

  Deliver material index pass

  """

  use_pass_mist: bool = ...

  """

  Deliver mist factor pass (0.0 to 1.0)

  """

  use_pass_normal: bool = ...

  """

  Deliver normal pass

  """

  use_pass_object_index: bool = ...

  """

  Deliver object index pass

  """

  use_pass_position: bool = ...

  """

  Deliver position pass

  """

  use_pass_shadow: bool = ...

  """

  Deliver shadow pass

  """

  use_pass_subsurface_color: bool = ...

  """

  Deliver subsurface color pass

  """

  use_pass_subsurface_direct: bool = ...

  """

  Deliver subsurface direct pass

  """

  use_pass_subsurface_indirect: bool = ...

  """

  Deliver subsurface indirect pass

  """

  use_pass_transmission_color: bool = ...

  """

  Deliver transmission color pass

  """

  use_pass_transmission_direct: bool = ...

  """

  Deliver transmission direct pass

  """

  use_pass_transmission_indirect: bool = ...

  """

  Deliver transmission indirect pass

  """

  use_pass_uv: bool = ...

  """

  Deliver texture UV pass

  """

  use_pass_vector: bool = ...

  """

  Deliver speed vector pass

  """

  use_pass_z: bool = ...

  """

  Deliver Z values pass

  """

  use_sky: bool = ...

  """

  Render Sky in this Layer

  """

  use_solid: bool = ...

  """

  Render Solid faces in this Layer

  """

  use_strand: bool = ...

  """

  Render Strands in this Layer

  """

  use_volumes: bool = ...

  """

  Render volumes in this Layer

  """

  @classmethod

  def update_render_passes(cls) -> None:

    """

    Requery the enabled render passes from the render engine

    """

    ...

  def update(self) -> None:

    """

    Update data tagged to be updated from previous access to data or operators

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ViewLayerEEVEE(bpy_struct):

  """

  View layer settings for Eevee

  """

  use_pass_bloom: bool = ...

  """

  Deliver bloom pass

  """

  use_pass_volume_direct: bool = ...

  """

  Deliver volume direct light pass

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ViewLayers(bpy_struct):

  """

  Collection of render layers

  """

  def new(self, name: str) -> ViewLayer:

    """

    Add a view layer to scene

    """

    ...

  def remove(self, layer: ViewLayer) -> None:

    """

    Remove a view layer

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class VolumeDisplay(bpy_struct):

  """

  Volume object display settings for 3D viewport

  """

  density: float = ...

  """

  Thickness of volume display in the viewport

  """

  interpolation_method: str = ...

  """

  Interpolation method to use for volumes in solid mode

  * ``LINEAR``
Linear -- Good smoothness and speed.

  * ``CUBIC``
Cubic -- Smoothed high quality interpolation, but slower.

  * ``CLOSEST``
Closest -- No interpolation.

  """

  slice_axis: str = ...

  """

  * ``AUTO``
Auto -- Adjust slice direction according to the view direction.

  * ``X``
X -- Slice along the X axis.

  * ``Y``
Y -- Slice along the Y axis.

  * ``Z``
Z -- Slice along the Z axis.

  """

  slice_depth: float = ...

  """

  Position of the slice

  """

  use_slice: bool = ...

  """

  Perform a single slice of the domain object

  """

  wireframe_detail: str = ...

  """

  Amount of detail for wireframe display

  * ``COARSE``
Coarse -- Display one box or point for each intermediate tree node.

  * ``FINE``
Fine -- Display box for each leaf node containing 8x8 voxels.

  """

  wireframe_type: str = ...

  """

  Type of wireframe display

  * ``NONE``
None -- Don't display volume in wireframe mode.

  * ``BOUNDS``
Bounds -- Display single bounding box for the entire grid.

  * ``BOXES``
Boxes -- Display bounding boxes for nodes in the volume tree.

  * ``POINTS``
Points -- Display points for nodes in the volume tree.

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class VolumeGrid(bpy_struct):

  """

  3D volume grid

  """

  channels: int = ...

  """

  Number of dimensions of the grid data type

  """

  data_type: str = ...

  """

  Data type of voxel values

  * ``BOOLEAN``
Boolean -- Boolean.

  * ``FLOAT``
Float -- Single precision float.

  * ``DOUBLE``
Double -- Double precision.

  * ``INT``
Integer -- 32-bit integer.

  * ``INT64``
Integer 64-bit -- 64-bit integer.

  * ``MASK``
Mask -- No data, boolean mask of active voxels.

  * ``STRING``
String -- Text string.

  * ``VECTOR_FLOAT``
Float Vector -- 3D float vector.

  * ``VECTOR_DOUBLE``
Double Vector -- 3D double vector.

  * ``VECTOR_INT``
Integer Vector -- 3D integer vector.

  * ``POINTS``
Points (Unsupported) -- Points grid, currently unsupported by volume objects.

  * ``UNKNOWN``
Unknown -- Unsupported data type.

  """

  is_loaded: bool = ...

  """

  Grid tree is loaded in memory

  """

  matrix_object: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]] = ...

  """

  Transformation matrix from voxel index to object space

  """

  name: str = ...

  """

  Volume grid name

  """

  def load(self) -> bool:

    """

    Load grid tree from file

    """

    ...

  def unload(self) -> None:

    """

    Unload grid tree and voxel data from memory, leaving only metadata

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class VolumeGrids(bpy_struct):

  """

  3D volume grids

  """

  active_index: int = ...

  """

  Index of active volume grid

  """

  error_message: str = ...

  """

  If loading grids failed, error message with details

  """

  frame: int = ...

  """

  Frame number that volume grids will be loaded at, based on scene time and volume parameters

  """

  frame_filepath: str = ...

  """

  Volume file used for loading the volume at the current frame. Empty if the volume has not be loaded or the frame only exists in memory

  """

  is_loaded: bool = ...

  """

  List of grids and metadata are loaded in memory

  """

  def load(self) -> bool:

    """

    Load list of grids and metadata from file

    """

    ...

  def unload(self) -> None:

    """

    Unload all grid and voxel data from memory

    """

    ...

  def save(self, filepath: str) -> bool:

    """

    Save grids and metadata to file

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class VolumeRender(bpy_struct):

  """

  Volume object render settings

  """

  clipping: float = ...

  """

  Value under which voxels are considered empty space to optimize rendering

  """

  space: str = ...

  """

  Specify volume density and step size in object or world space

  * ``OBJECT``
Object -- Keep volume opacity and detail the same regardless of object scale.

  * ``WORLD``
World -- Specify volume step size and density in world space.

  """

  step_size: float = ...

  """

  Distance between volume samples. Lower values render more detail at the cost of performance. If set to zero, the step size is automatically determined based on voxel size

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class WalkNavigation(bpy_struct):

  """

  Walk navigation settings

  """

  jump_height: float = ...

  """

  Maximum height of a jump

  """

  mouse_speed: float = ...

  """

  Speed factor for when looking around, high values mean faster mouse movement

  """

  teleport_time: float = ...

  """

  Interval of time warp when teleporting in navigation mode

  """

  use_gravity: bool = ...

  """

  Walk with gravity, or free navigate

  """

  use_mouse_reverse: bool = ...

  """

  Reverse the vertical movement of the mouse

  """

  view_height: float = ...

  """

  View distance from the floor when walking

  """

  walk_speed: float = ...

  """

  Base speed for walking and flying

  """

  walk_speed_factor: float = ...

  """

  Multiplication factor when using the fast or slow modifiers

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Window(bpy_struct):

  """

  Open window

  """

  height: int = ...

  """

  Window height

  """

  parent: Window = ...

  """

  Active workspace and scene follow this window

  """

  scene: Scene = ...

  """

  Active scene to be edited in the window

  """

  screen: Screen = ...

  """

  Active workspace screen showing in the window

  """

  stereo_3d_display: Stereo3dDisplay = ...

  """

  Settings for stereo 3D display

  """

  view_layer: ViewLayer = ...

  """

  The active workspace view layer showing in the window

  """

  width: int = ...

  """

  Window width

  """

  workspace: WorkSpace = ...

  """

  Active workspace showing in the window

  """

  x: int = ...

  """

  Horizontal location of the window

  """

  y: int = ...

  """

  Vertical location of the window

  """

  def cursor_warp(self, x: int, y: int) -> None:

    """

    Set the cursor position

    """

    ...

  def cursor_set(self, cursor: str) -> None:

    """

    Set the cursor

    """

    ...

  def cursor_modal_set(self, cursor: str) -> None:

    """

    Restore the previous cursor after calling ``cursor_modal_set``

    """

    ...

  def cursor_modal_restore(self) -> None:

    """

    cursor_modal_restore

    """

    ...

  def event_simulate(self, type: str, value: str, unicode: str = '', x: int = 0, y: int = 0, shift: bool = False, ctrl: bool = False, alt: bool = False, oskey: bool = False) -> Event:

    """

    event_simulate

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class wmOwnerID(bpy_struct):

  name: str = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class wmOwnerIDs(bpy_struct):

  def new(self, name: str) -> wmOwnerID:

    """

    Add ui tag

    """

    ...

  def remove(self, owner_id: wmOwnerID) -> None:

    """

    Remove ui tag

    """

    ...

  def clear(self) -> None:

    """

    Remove all tags

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class wmTools(bpy_struct):

  def from_space_view3d_mode(self, mode: str, create: bool = False) -> WorkSpaceTool:

    ...

  def from_space_image_mode(self, mode: str, create: bool = False) -> WorkSpaceTool:

    ...

  def from_space_node(self, create: bool = False) -> WorkSpaceTool:

    ...

  def from_space_sequencer(self, mode: str, create: bool = False) -> WorkSpaceTool:

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class WorkSpaceTool(bpy_struct):

  has_datablock: bool = ...

  idname: str = ...

  idname_fallback: str = ...

  index: int = ...

  mode: str = ...

  space_type: str = ...

  """

  * ``EMPTY``
Empty.

  * ``VIEW_3D``
3D Viewport -- Manipulate objects in a 3D environment.

  * ``IMAGE_EDITOR``
UV/Image Editor -- View and edit images and UV Maps.

  * ``NODE_EDITOR``
Node Editor -- Editor for node-based shading and compositing tools.

  * ``SEQUENCE_EDITOR``
Video Sequencer -- Video editing tools.

  * ``CLIP_EDITOR``
Movie Clip Editor -- Motion tracking tools.

  * ``DOPESHEET_EDITOR``
Dope Sheet -- Adjust timing of keyframes.

  * ``GRAPH_EDITOR``
Graph Editor -- Edit drivers and keyframe interpolation.

  * ``NLA_EDITOR``
Nonlinear Animation -- Combine and layer Actions.

  * ``TEXT_EDITOR``
Text Editor -- Edit scripts and in-file documentation.

  * ``CONSOLE``
Python Console -- Interactive programmatic console for advanced editing and script development.

  * ``INFO``
Info -- Log of operations, warnings and error messages.

  * ``TOPBAR``
Top Bar -- Global bar at the top of the screen for global per-window settings.

  * ``STATUSBAR``
Status Bar -- Global bar at the bottom of the screen for general status information.

  * ``OUTLINER``
Outliner -- Overview of scene graph and all available data-blocks.

  * ``PROPERTIES``
Properties -- Edit properties of active object and related data-blocks.

  * ``FILE_BROWSER``
File Browser -- Browse for files and assets.

  * ``SPREADSHEET``
Spreadsheet -- Explore geometry data in a table.

  * ``PREFERENCES``
Preferences -- Edit persistent configuration settings.

  """

  widget: str = ...

  def setup(self, idname: str, cursor: str = 'DEFAULT', keymap: str = '', gizmo_group: str = '', data_block: str = '', operator: str = '', index: int = 0, options: typing.Set[str] = {}, idname_fallback: str = '', keymap_fallback: str = '') -> None:

    """

    Set the tool settings

    """

    ...

  def operator_properties(self, operator: str) -> OperatorProperties:

    """

    operator_properties

    """

    ...

  def gizmo_group_properties(self, group: str) -> GizmoGroupProperties:

    """

    gizmo_group_properties

    """

    ...

  def refresh_from_context(self) -> None:

    """

    refresh_from_context

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class WorldLighting(bpy_struct):

  """

  Lighting for a World data-block

  """

  ao_factor: float = ...

  """

  Factor for ambient occlusion blending

  """

  distance: float = ...

  """

  Length of rays, defines how far away other faces give occlusion effect

  """

  use_ambient_occlusion: bool = ...

  """

  Use Ambient Occlusion to add shadowing based on distance between objects

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class WorldMistSettings(bpy_struct):

  """

  Mist settings for a World data-block

  """

  depth: float = ...

  """

  Distance over which the mist effect fades in

  """

  falloff: str = ...

  """

  Type of transition used to fade mist

  * ``QUADRATIC``
Quadratic -- Use quadratic progression.

  * ``LINEAR``
Linear -- Use linear progression.

  * ``INVERSE_QUADRATIC``
Inverse Quadratic -- Use inverse quadratic progression.

  """

  height: float = ...

  """

  Control how much mist density decreases with height

  """

  intensity: float = ...

  """

  Overall minimum intensity of the mist effect

  """

  start: float = ...

  """

  Starting distance of the mist, measured from the camera

  """

  use_mist: bool = ...

  """

  Occlude objects with the environment color as they are further away

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class XrActionMap(bpy_struct):

  actionmap_items: typing.Union[XrActionMapItems, typing.Sequence[XrActionMapItem], typing.Mapping[str, XrActionMapItem], bpy_prop_collection] = ...

  """

  Items in the action map, mapping an XR event to an operator, pose, or haptic output

  """

  name: str = ...

  """

  Name of the action map

  """

  selected_item: int = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class XrActionMapBinding(bpy_struct):

  """

  Binding in an XR action map item

  """

  axis0_region: str = ...

  """

  Action execution region for the first input axis

  * ``ANY``
Any -- Use any axis region for operator execution.

  * ``POSITIVE``
Positive -- Use positive axis region only for operator execution.

  * ``NEGATIVE``
Negative -- Use negative axis region only for operator execution.

  """

  axis1_region: str = ...

  """

  Action execution region for the second input axis

  * ``ANY``
Any -- Use any axis region for operator execution.

  * ``POSITIVE``
Positive -- Use positive axis region only for operator execution.

  * ``NEGATIVE``
Negative -- Use negative axis region only for operator execution.

  """

  component_path0: str = ...

  """

  OpenXR component path

  """

  component_path1: str = ...

  """

  OpenXR component path

  """

  name: str = ...

  """

  Name of the action map binding

  """

  pose_location: typing.Tuple[float, float, float] = ...

  pose_rotation: typing.Tuple[float, float, float] = ...

  profile: str = ...

  """

  OpenXR interaction profile path

  """

  threshold: float = ...

  """

  Input threshold for button/axis actions

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class XrActionMapBindings(bpy_struct):

  """

  Collection of XR action map bindings

  """

  def new(self, name: str, replace_existing: bool) -> XrActionMapBinding:

    """

    new

    """

    ...

  def new_from_binding(self, binding: XrActionMapBinding) -> XrActionMapBinding:

    """

    new_from_binding

    """

    ...

  def remove(self, binding: XrActionMapBinding) -> None:

    """

    remove

    """

    ...

  def find(self, name: str) -> XrActionMapBinding:

    """

    find

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class XrActionMapItem(bpy_struct):

  bimanual: bool = ...

  """

  The action depends on the states/poses of both user paths

  """

  bindings: typing.Union[XrActionMapBindings, typing.Sequence[XrActionMapBinding], typing.Mapping[str, XrActionMapBinding], bpy_prop_collection] = ...

  """

  Bindings for the action map item, mapping the action to an XR input

  """

  haptic_amplitude: float = ...

  """

  Intensity of the haptic vibration, ranging from 0.0 to 1.0

  """

  haptic_duration: float = ...

  """

  Haptic duration in seconds. 0.0 is the minimum supported duration

  """

  haptic_frequency: float = ...

  """

  Frequency of the haptic vibration in hertz. 0.0 specifies the OpenXR runtime's default frequency

  """

  haptic_match_user_paths: bool = ...

  """

  Apply haptics to the same user paths for the haptic action and this action

  """

  haptic_mode: str = ...

  """

  Haptic application mode

  * ``PRESS``
Press -- Apply haptics on button press.

  * ``RELEASE``
Release -- Apply haptics on button release.

  * ``PRESS_RELEASE``
Press Release -- Apply haptics on button press and release.

  * ``REPEAT``
Repeat -- Apply haptics repeatedly for the duration of the button press.

  """

  haptic_name: str = ...

  """

  Name of the haptic action to apply when executing this action

  """

  name: str = ...

  """

  Name of the action map item

  """

  op: str = ...

  """

  Identifier of operator to call on action event

  """

  op_mode: str = ...

  """

  Operator execution mode

  * ``PRESS``
Press -- Execute operator on button press (non-modal operators only).

  * ``RELEASE``
Release -- Execute operator on button release (non-modal operators only).

  * ``MODAL``
Modal -- Use modal execution (modal operators only).

  """

  op_name: str = ...

  """

  Name of operator (translated) to call on action event

  """

  op_properties: OperatorProperties = ...

  """

  Properties to set when the operator is called

  """

  pose_is_controller_aim: bool = ...

  """

  The action poses will be used for the VR controller aims

  """

  pose_is_controller_grip: bool = ...

  """

  The action poses will be used for the VR controller grips

  """

  selected_binding: int = ...

  """

  Currently selected binding

  """

  type: str = ...

  """

  Action type

  * ``FLOAT``
Float -- Float action, representing either a digital or analog button.

  * ``VECTOR2D``
Vector2D -- 2D float vector action, representing a thumbstick or trackpad.

  * ``POSE``
Pose -- 3D pose action, representing a controller's location and rotation.

  * ``VIBRATION``
Vibration -- Haptic vibration output action, to be applied with a duration, frequency, and amplitude.

  """

  user_path0: str = ...

  """

  OpenXR user path

  """

  user_path1: str = ...

  """

  OpenXR user path

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class XrActionMapItems(bpy_struct):

  """

  Collection of XR action map items

  """

  def new(self, name: str, replace_existing: bool) -> XrActionMapItem:

    """

    new

    """

    ...

  def new_from_item(self, item: XrActionMapItem) -> XrActionMapItem:

    """

    new_from_item

    """

    ...

  def remove(self, item: XrActionMapItem) -> None:

    """

    remove

    """

    ...

  def find(self, name: str) -> XrActionMapItem:

    """

    find

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class XrActionMaps(bpy_struct):

  """

  Collection of XR action maps

  """

  @classmethod

  def new(cls, xr_session_state: XrSessionState, name: str, replace_existing: bool) -> XrActionMap:

    """

    new

    """

    ...

  @classmethod

  def new_from_actionmap(cls, xr_session_state: XrSessionState, actionmap: XrActionMap) -> XrActionMap:

    """

    new_from_actionmap

    """

    ...

  @classmethod

  def remove(cls, xr_session_state: XrSessionState, actionmap: XrActionMap) -> None:

    """

    remove

    """

    ...

  @classmethod

  def find(cls, xr_session_state: XrSessionState, name: str) -> XrActionMap:

    """

    find

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class XrEventData(bpy_struct):

  """

  XR Data for Window Manager Event

  """

  action: str = ...

  """

  XR action name

  """

  action_set: str = ...

  """

  XR action set name

  """

  bimanual: bool = ...

  """

  Whether bimanual interaction is occurring

  """

  controller_location: typing.Tuple[float, float, float] = ...

  """

  Location of the action's corresponding controller aim in world space

  """

  controller_location_other: typing.Tuple[float, float, float] = ...

  """

  Controller aim location of the other user path for bimanual actions

  """

  controller_rotation: typing.Tuple[float, float, float, float] = ...

  """

  Rotation of the action's corresponding controller aim in world space

  """

  controller_rotation_other: typing.Tuple[float, float, float, float] = ...

  """

  Controller aim rotation of the other user path for bimanual actions

  """

  float_threshold: float = ...

  """

  Input threshold for float/2D vector actions

  """

  state: typing.Tuple[float, float] = ...

  """

  XR action values corresponding to type

  """

  state_other: typing.Tuple[float, float] = ...

  """

  State of the other user path for bimanual actions

  """

  type: str = ...

  """

  XR action type

  * ``FLOAT``
Float -- Float action, representing either a digital or analog button.

  * ``VECTOR2D``
Vector2D -- 2D float vector action, representing a thumbstick or trackpad.

  * ``POSE``
Pose -- 3D pose action, representing a controller's location and rotation.

  * ``VIBRATION``
Vibration -- Haptic vibration output action, to be applied with a duration, frequency, and amplitude.

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class XrSessionSettings(bpy_struct):

  base_pose_angle: float = ...

  """

  Rotation angle around the Z-Axis to apply the rotation deltas from the VR headset to

  """

  base_pose_location: typing.Tuple[float, float, float] = ...

  """

  Coordinates to apply translation deltas from the VR headset to

  """

  base_pose_object: Object = ...

  """

  Object to take the location and rotation to which translation and rotation deltas from the VR headset will be applied to

  """

  base_pose_type: str = ...

  """

  Define where the location and rotation for the VR view come from, to which translation and rotation deltas from the VR headset will be applied to

  * ``SCENE_CAMERA``
Scene Camera -- Follow the active scene camera to define the VR view's base pose.

  * ``OBJECT``
Object -- Follow the transformation of an object to define the VR view's base pose.

  * ``CUSTOM``
Custom -- Follow a custom transformation to define the VR view's base pose.

  """

  base_scale: float = ...

  """

  Uniform scale to apply to VR view

  """

  clip_end: float = ...

  """

  VR viewport far clipping distance

  """

  clip_start: float = ...

  """

  VR viewport near clipping distance

  """

  controller_draw_style: str = ...

  """

  Style to use when drawing VR controllers

  * ``DARK``
Dark -- Draw dark controller.

  * ``LIGHT``
Light -- Draw light controller.

  * ``DARK_RAY``
Dark + Ray -- Draw dark controller with aiming axis ray.

  * ``LIGHT_RAY``
Light + Ray -- Draw light controller with aiming axis ray.

  """

  shading: View3DShading = ...

  show_annotation: bool = ...

  """

  Show annotations for this view

  """

  show_controllers: bool = ...

  """

  Show VR controllers (requires VR actions for controller poses)

  """

  show_custom_overlays: bool = ...

  """

  Show custom VR overlays

  """

  show_floor: bool = ...

  """

  Show the ground plane grid

  """

  show_selection: bool = ...

  """

  Show selection outlines

  """

  use_absolute_tracking: bool = ...

  """

  Allow the VR tracking origin to be defined independently of the headset location

  """

  use_positional_tracking: bool = ...

  """

  Allow VR headsets to affect the location in virtual space, in addition to the rotation

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class XrSessionState(bpy_struct):

  """

  Runtime state information about the VR session

  """

  actionmaps: typing.Union[XrActionMaps, typing.Sequence[XrActionMap], typing.Mapping[str, XrActionMap], bpy_prop_collection] = ...

  active_actionmap: int = ...

  navigation_location: typing.Tuple[float, float, float] = ...

  """

  Location offset to apply to base pose when determining viewer location

  """

  navigation_rotation: typing.Tuple[float, float, float, float] = ...

  """

  Rotation offset to apply to base pose when determining viewer rotation

  """

  navigation_scale: float = ...

  """

  Additional scale multiplier to apply to base scale when determining viewer scale

  """

  selected_actionmap: int = ...

  viewer_pose_location: typing.Tuple[float, float, float] = ...

  """

  Last known location of the viewer pose (center between the eyes) in world space

  """

  viewer_pose_rotation: typing.Tuple[float, float, float, float] = ...

  """

  Last known rotation of the viewer pose (center between the eyes) in world space

  """

  @classmethod

  def is_running(cls, context: Context) -> bool:

    """

    Query if the VR session is currently running

    """

    ...

  @classmethod

  def reset_to_base_pose(cls, context: Context) -> None:

    """

    Force resetting of position and rotation deltas

    """

    ...

  @classmethod

  def action_set_create(cls, context: Context, actionmap: XrActionMap) -> bool:

    """

    Create a VR action set

    """

    ...

  @classmethod

  def action_create(cls, context: Context, actionmap: XrActionMap, actionmap_item: XrActionMapItem) -> bool:

    """

    Create a VR action

    """

    ...

  @classmethod

  def action_binding_create(cls, context: Context, actionmap: XrActionMap, actionmap_item: XrActionMapItem, actionmap_binding: XrActionMapBinding) -> bool:

    """

    Create a VR action binding

    """

    ...

  @classmethod

  def active_action_set_set(cls, context: Context, action_set: str) -> bool:

    """

    Set the active VR action set

    """

    ...

  @classmethod

  def controller_pose_actions_set(cls, context: Context, action_set: str, grip_action: str, aim_action: str) -> bool:

    """

    Set the actions that determine the VR controller poses

    """

    ...

  @classmethod

  def action_state_get(cls, context: Context, action_set_name: str, action_name: str, user_path: str) -> typing.Tuple[float, float]:

    """

    Get the current state of a VR action

    """

    ...

  @classmethod

  def haptic_action_apply(cls, context: Context, action_set_name: str, action_name: str, user_path: str, duration: float, frequency: float, amplitude: float) -> bool:

    """

    Apply a VR haptic action

    """

    ...

  @classmethod

  def haptic_action_stop(cls, context: Context, action_set_name: str, action_name: str, user_path: str) -> None:

    """

    Stop a VR haptic action

    """

    ...

  @classmethod

  def controller_grip_location_get(cls, context: Context, index: int) -> typing.Tuple[float, float, float]:

    """

    Get the last known controller grip location in world space

    """

    ...

  @classmethod

  def controller_grip_rotation_get(cls, context: Context, index: int) -> typing.Tuple[float, float, float, float]:

    """

    Get the last known controller grip rotation (quaternion) in world space

    """

    ...

  @classmethod

  def controller_aim_location_get(cls, context: Context, index: int) -> typing.Tuple[float, float, float]:

    """

    Get the last known controller aim location in world space

    """

    ...

  @classmethod

  def controller_aim_rotation_get(cls, context: Context, index: int) -> typing.Tuple[float, float, float, float]:

    """

    Get the last known controller aim rotation (quaternion) in world space

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BoolAttribute(Attribute, bpy_struct):

  """

  Bool geometry attribute

  """

  data: typing.Union[typing.Sequence[BoolAttributeValue], typing.Mapping[str, BoolAttributeValue], bpy_prop_collection] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ByteColorAttribute(Attribute, bpy_struct):

  """

  Color geometry attribute, with 8-bit values

  """

  data: typing.Union[typing.Sequence[ByteColorAttributeValue], typing.Mapping[str, ByteColorAttributeValue], bpy_prop_collection] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Float2Attribute(Attribute, bpy_struct):

  """

  2D vector geometry attribute, with floating-point values

  """

  data: typing.Union[typing.Sequence[Float2AttributeValue], typing.Mapping[str, Float2AttributeValue], bpy_prop_collection] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FloatAttribute(Attribute, bpy_struct):

  """

  Geometry attribute with floating-point values

  """

  data: typing.Union[typing.Sequence[FloatAttributeValue], typing.Mapping[str, FloatAttributeValue], bpy_prop_collection] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FloatColorAttribute(Attribute, bpy_struct):

  """

  Color geometry attribute, with floating-point values

  """

  data: typing.Union[typing.Sequence[FloatColorAttributeValue], typing.Mapping[str, FloatColorAttributeValue], bpy_prop_collection] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FloatVectorAttribute(Attribute, bpy_struct):

  """

  Vector geometry attribute, with floating-point values

  """

  data: typing.Union[typing.Sequence[FloatVectorAttributeValue], typing.Mapping[str, FloatVectorAttributeValue], bpy_prop_collection] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class IntAttribute(Attribute, bpy_struct):

  """

  Integer geometry attribute

  """

  data: typing.Union[typing.Sequence[IntAttributeValue], typing.Mapping[str, IntAttributeValue], bpy_prop_collection] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class StringAttribute(Attribute, bpy_struct):

  """

  String geometry attribute

  """

  data: typing.Union[typing.Sequence[StringAttributeValue], typing.Mapping[str, StringAttributeValue], bpy_prop_collection] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BoidRuleAverageSpeed(BoidRule, bpy_struct):

  level: float = ...

  """

  How much velocity's z-component is kept constant

  """

  speed: float = ...

  """

  Percentage of maximum speed

  """

  wander: float = ...

  """

  How fast velocity's direction is randomized

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BoidRuleAvoid(BoidRule, bpy_struct):

  fear_factor: float = ...

  """

  Avoid object if danger from it is above this threshold

  """

  object: Object = ...

  """

  Object to avoid

  """

  use_predict: bool = ...

  """

  Predict target movement

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BoidRuleAvoidCollision(BoidRule, bpy_struct):

  look_ahead: float = ...

  """

  Time to look ahead in seconds

  """

  use_avoid: bool = ...

  """

  Avoid collision with other boids

  """

  use_avoid_collision: bool = ...

  """

  Avoid collision with deflector objects

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BoidRuleFight(BoidRule, bpy_struct):

  distance: float = ...

  """

  Attack boids at max this distance

  """

  flee_distance: float = ...

  """

  Flee to this distance

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BoidRuleFollowLeader(BoidRule, bpy_struct):

  distance: float = ...

  """

  Distance behind leader to follow

  """

  object: Object = ...

  """

  Follow this object instead of a boid

  """

  queue_count: int = ...

  """

  How many boids in a line

  """

  use_line: bool = ...

  """

  Follow leader in a line

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BoidRuleGoal(BoidRule, bpy_struct):

  object: Object = ...

  """

  Goal object

  """

  use_predict: bool = ...

  """

  Predict target movement

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ActionConstraint(Constraint, bpy_struct):

  """

  Map an action to the transform axes of a bone

  """

  action: Action = ...

  """

  The constraining action

  """

  eval_time: float = ...

  """

  Interpolates between Action Start and End frames

  """

  frame_end: int = ...

  """

  Last frame of the Action to use

  """

  frame_start: int = ...

  """

  First frame of the Action to use

  """

  max: float = ...

  """

  Maximum value for target channel range

  """

  min: float = ...

  """

  Minimum value for target channel range

  """

  mix_mode: str = ...

  """

  Specify how existing transformations and the action channels are combined

  * ``BEFORE_FULL``
Before Original (Full) -- Apply the action channels before the original transformation, as if applied to an imaginary parent in Full Inherit Scale mode. Will create shear when combining rotation and non-uniform scale.

  * ``BEFORE``
Before Original (Aligned) -- Apply the action channels before the original transformation, as if applied to an imaginary parent in Aligned Inherit Scale mode. This effectively uses Full for location and Split Channels for rotation and scale.

  * ``BEFORE_SPLIT``
Before Original (Split Channels) -- Apply the action channels before the original transformation, handling location, rotation and scale separately.

  * ``AFTER_FULL``
After Original (Full) -- Apply the action channels after the original transformation, as if applied to an imaginary child in Full Inherit Scale mode. Will create shear when combining rotation and non-uniform scale.

  * ``AFTER``
After Original (Aligned) -- Apply the action channels after the original transformation, as if applied to an imaginary child in Aligned Inherit Scale mode. This effectively uses Full for location and Split Channels for rotation and scale.

  * ``AFTER_SPLIT``
After Original (Split Channels) -- Apply the action channels after the original transformation, handling location, rotation and scale separately.

  """

  subtarget: str = ...

  """

  Armature bone, mesh or lattice vertex group, ...

  """

  target: Object = ...

  """

  Target object

  """

  transform_channel: str = ...

  """

  Transformation channel from the target that is used to key the Action

  """

  use_bone_object_action: bool = ...

  """

  Bones only: apply the object's transformation channels of the action to the constrained bone, instead of bone's channels

  """

  use_eval_time: bool = ...

  """

  Interpolate between Action Start and End frames, with the Evaluation Time slider instead of the Target object/bone

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ArmatureConstraint(Constraint, bpy_struct):

  """

  Applies transformations done by the Armature modifier

  """

  targets: typing.Union[ArmatureConstraintTargets, typing.Sequence[ConstraintTargetBone], typing.Mapping[str, ConstraintTargetBone], bpy_prop_collection] = ...

  """

  Target Bones

  """

  use_bone_envelopes: bool = ...

  """

  Multiply weights by envelope for all bones, instead of acting like Vertex Group based blending. The specified weights are still used, and only the listed bones are considered

  """

  use_current_location: bool = ...

  """

  Use the current bone location for envelopes and choosing B-Bone segments instead of rest position

  """

  use_deform_preserve_volume: bool = ...

  """

  Deform rotation interpolation with quaternions

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class CameraSolverConstraint(Constraint, bpy_struct):

  """

  Lock motion to the reconstructed camera movement

  """

  clip: MovieClip = ...

  """

  Movie Clip to get tracking data from

  """

  use_active_clip: bool = ...

  """

  Use active clip defined in scene

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ChildOfConstraint(Constraint, bpy_struct):

  """

  Create constraint-based parent-child relationship

  """

  inverse_matrix: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]] = ...

  """

  Transformation matrix to apply before

  """

  set_inverse_pending: bool = ...

  """

  Set to true to request recalculation of the inverse matrix

  """

  subtarget: str = ...

  """

  Armature bone, mesh or lattice vertex group, ...

  """

  target: Object = ...

  """

  Target object

  """

  use_location_x: bool = ...

  """

  Use X Location of Parent

  """

  use_location_y: bool = ...

  """

  Use Y Location of Parent

  """

  use_location_z: bool = ...

  """

  Use Z Location of Parent

  """

  use_rotation_x: bool = ...

  """

  Use X Rotation of Parent

  """

  use_rotation_y: bool = ...

  """

  Use Y Rotation of Parent

  """

  use_rotation_z: bool = ...

  """

  Use Z Rotation of Parent

  """

  use_scale_x: bool = ...

  """

  Use X Scale of Parent

  """

  use_scale_y: bool = ...

  """

  Use Y Scale of Parent

  """

  use_scale_z: bool = ...

  """

  Use Z Scale of Parent

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ClampToConstraint(Constraint, bpy_struct):

  """

  Constrain an object's location to the nearest point along the target path

  """

  main_axis: str = ...

  """

  Main axis of movement

  """

  target: Object = ...

  """

  Target Object (Curves only)

  """

  use_cyclic: bool = ...

  """

  Treat curve as cyclic curve (no clamping to curve bounding box)

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class CopyLocationConstraint(Constraint, bpy_struct):

  """

  Copy the location of the target

  """

  head_tail: float = ...

  """

  Target along length of bone: Head is 0, Tail is 1

  """

  invert_x: bool = ...

  """

  Invert the X location

  """

  invert_y: bool = ...

  """

  Invert the Y location

  """

  invert_z: bool = ...

  """

  Invert the Z location

  """

  subtarget: str = ...

  """

  Armature bone, mesh or lattice vertex group, ...

  """

  target: Object = ...

  """

  Target object

  """

  use_bbone_shape: bool = ...

  """

  Follow shape of B-Bone segments when calculating Head/Tail position

  """

  use_offset: bool = ...

  """

  Add original location into copied location

  """

  use_x: bool = ...

  """

  Copy the target's X location

  """

  use_y: bool = ...

  """

  Copy the target's Y location

  """

  use_z: bool = ...

  """

  Copy the target's Z location

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class CopyRotationConstraint(Constraint, bpy_struct):

  """

  Copy the rotation of the target

  """

  euler_order: str = ...

  """

  Explicitly specify the euler rotation order

  * ``AUTO``
Default -- Euler using the default rotation order.

  * ``XYZ``
XYZ Euler -- Euler using the XYZ rotation order.

  * ``XZY``
XZY Euler -- Euler using the XZY rotation order.

  * ``YXZ``
YXZ Euler -- Euler using the YXZ rotation order.

  * ``YZX``
YZX Euler -- Euler using the YZX rotation order.

  * ``ZXY``
ZXY Euler -- Euler using the ZXY rotation order.

  * ``ZYX``
ZYX Euler -- Euler using the ZYX rotation order.

  """

  invert_x: bool = ...

  """

  Invert the X rotation

  """

  invert_y: bool = ...

  """

  Invert the Y rotation

  """

  invert_z: bool = ...

  """

  Invert the Z rotation

  """

  mix_mode: str = ...

  """

  Specify how the copied and existing rotations are combined

  * ``REPLACE``
Replace -- Replace the original rotation with copied.

  * ``ADD``
Add -- Add euler component values together.

  * ``BEFORE``
Before Original -- Apply copied rotation before original, as if the constraint target is a parent.

  * ``AFTER``
After Original -- Apply copied rotation after original, as if the constraint target is a child.

  * ``OFFSET``
Offset (Legacy) -- Combine rotations like the original Offset checkbox. Does not work well for multiple axis rotations.

  """

  subtarget: str = ...

  """

  Armature bone, mesh or lattice vertex group, ...

  """

  target: Object = ...

  """

  Target object

  """

  use_offset: bool = ...

  """

  DEPRECATED: Add original rotation into copied rotation

  """

  use_x: bool = ...

  """

  Copy the target's X rotation

  """

  use_y: bool = ...

  """

  Copy the target's Y rotation

  """

  use_z: bool = ...

  """

  Copy the target's Z rotation

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class CopyScaleConstraint(Constraint, bpy_struct):

  """

  Copy the scale of the target

  """

  power: float = ...

  """

  Raise the target's scale to the specified power

  """

  subtarget: str = ...

  """

  Armature bone, mesh or lattice vertex group, ...

  """

  target: Object = ...

  """

  Target object

  """

  use_add: bool = ...

  """

  Use addition instead of multiplication to combine scale (2.7 compatibility)

  """

  use_make_uniform: bool = ...

  """

  Redistribute the copied change in volume equally between the three axes of the owner

  """

  use_offset: bool = ...

  """

  Combine original scale with copied scale

  """

  use_x: bool = ...

  """

  Copy the target's X scale

  """

  use_y: bool = ...

  """

  Copy the target's Y scale

  """

  use_z: bool = ...

  """

  Copy the target's Z scale

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class CopyTransformsConstraint(Constraint, bpy_struct):

  """

  Copy all the transforms of the target

  """

  head_tail: float = ...

  """

  Target along length of bone: Head is 0, Tail is 1

  """

  mix_mode: str = ...

  """

  Specify how the copied and existing transformations are combined

  * ``REPLACE``
Replace -- Replace the original transformation with copied.

  * ``BEFORE_FULL``
Before Original (Full) -- Apply copied transformation before original, using simple matrix multiplication as if the constraint target is a parent in Full Inherit Scale mode. Will create shear when combining rotation and non-uniform scale.

  * ``BEFORE``
Before Original (Aligned) -- Apply copied transformation before original, as if the constraint target is a parent in Aligned Inherit Scale mode. This effectively uses Full for location and Split Channels for rotation and scale.

  * ``BEFORE_SPLIT``
Before Original (Split Channels) -- Apply copied transformation before original, handling location, rotation and scale separately, similar to a sequence of three Copy constraints.

  * ``AFTER_FULL``
After Original (Full) -- Apply copied transformation after original, using simple matrix multiplication as if the constraint target is a child in Full Inherit Scale mode. Will create shear when combining rotation and non-uniform scale.

  * ``AFTER``
After Original (Aligned) -- Apply copied transformation after original, as if the constraint target is a child in Aligned Inherit Scale mode. This effectively uses Full for location and Split Channels for rotation and scale.

  * ``AFTER_SPLIT``
After Original (Split Channels) -- Apply copied transformation after original, handling location, rotation and scale separately, similar to a sequence of three Copy constraints.

  """

  remove_target_shear: bool = ...

  """

  Remove shear from the target transformation before combining

  """

  subtarget: str = ...

  """

  Armature bone, mesh or lattice vertex group, ...

  """

  target: Object = ...

  """

  Target object

  """

  use_bbone_shape: bool = ...

  """

  Follow shape of B-Bone segments when calculating Head/Tail position

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class DampedTrackConstraint(Constraint, bpy_struct):

  """

  Point toward target by taking the shortest rotation path

  """

  head_tail: float = ...

  """

  Target along length of bone: Head is 0, Tail is 1

  """

  subtarget: str = ...

  """

  Armature bone, mesh or lattice vertex group, ...

  """

  target: Object = ...

  """

  Target object

  """

  track_axis: str = ...

  """

  Axis that points to the target object

  """

  use_bbone_shape: bool = ...

  """

  Follow shape of B-Bone segments when calculating Head/Tail position

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FloorConstraint(Constraint, bpy_struct):

  """

  Use the target object for location limitation

  """

  floor_location: str = ...

  """

  Location of target that object will not pass through

  """

  offset: float = ...

  """

  Offset of floor from object origin

  """

  subtarget: str = ...

  """

  Armature bone, mesh or lattice vertex group, ...

  """

  target: Object = ...

  """

  Target object

  """

  use_rotation: bool = ...

  """

  Use the target's rotation to determine floor

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FollowPathConstraint(Constraint, bpy_struct):

  """

  Lock motion to the target path

  """

  forward_axis: str = ...

  """

  Axis that points forward along the path

  """

  offset: float = ...

  """

  Offset from the position corresponding to the time frame

  """

  offset_factor: float = ...

  """

  Percentage value defining target position along length of curve

  """

  target: Object = ...

  """

  Target Curve object

  """

  up_axis: str = ...

  """

  Axis that points upward

  """

  use_curve_follow: bool = ...

  """

  Object will follow the heading and banking of the curve

  """

  use_curve_radius: bool = ...

  """

  Object is scaled by the curve radius

  """

  use_fixed_location: bool = ...

  """

  Object will stay locked to a single point somewhere along the length of the curve regardless of time

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FollowTrackConstraint(Constraint, bpy_struct):

  """

  Lock motion to the target motion track

  """

  camera: Object = ...

  """

  Camera to which motion is parented (if empty active scene camera is used)

  """

  clip: MovieClip = ...

  """

  Movie Clip to get tracking data from

  """

  depth_object: Object = ...

  """

  Object used to define depth in camera space by projecting onto surface of this object

  """

  frame_method: str = ...

  """

  How the footage fits in the camera frame

  """

  object: str = ...

  """

  Movie tracking object to follow (if empty, camera object is used)

  """

  track: str = ...

  """

  Movie tracking track to follow

  """

  use_3d_position: bool = ...

  """

  Use 3D position of track to parent to

  """

  use_active_clip: bool = ...

  """

  Use active clip defined in scene

  """

  use_undistorted_position: bool = ...

  """

  Parent to undistorted position of 2D track

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class KinematicConstraint(Constraint, bpy_struct):

  """

  Inverse Kinematics

  """

  chain_count: int = ...

  """

  How many bones are included in the IK effect - 0 uses all bones

  """

  distance: float = ...

  """

  Radius of limiting sphere

  """

  ik_type: str = ...

  iterations: int = ...

  """

  Maximum number of solving iterations

  """

  limit_mode: str = ...

  """

  Distances in relation to sphere of influence to allow

  * ``LIMITDIST_INSIDE``
Inside -- The object is constrained inside a virtual sphere around the target object, with a radius defined by the limit distance.

  * ``LIMITDIST_OUTSIDE``
Outside -- The object is constrained outside a virtual sphere around the target object, with a radius defined by the limit distance.

  * ``LIMITDIST_ONSURFACE``
On Surface -- The object is constrained on the surface of a virtual sphere around the target object, with a radius defined by the limit distance.

  """

  lock_location_x: bool = ...

  """

  Constraint position along X axis

  """

  lock_location_y: bool = ...

  """

  Constraint position along Y axis

  """

  lock_location_z: bool = ...

  """

  Constraint position along Z axis

  """

  lock_rotation_x: bool = ...

  """

  Constraint rotation along X axis

  """

  lock_rotation_y: bool = ...

  """

  Constraint rotation along Y axis

  """

  lock_rotation_z: bool = ...

  """

  Constraint rotation along Z axis

  """

  orient_weight: float = ...

  """

  For Tree-IK: Weight of orientation control for this target

  """

  pole_angle: float = ...

  """

  Pole rotation offset

  """

  pole_subtarget: str = ...

  pole_target: Object = ...

  """

  Object for pole rotation

  """

  reference_axis: str = ...

  """

  Constraint axis Lock options relative to Bone or Target reference

  """

  subtarget: str = ...

  """

  Armature bone, mesh or lattice vertex group, ...

  """

  target: Object = ...

  """

  Target object

  """

  use_location: bool = ...

  """

  Chain follows position of target

  """

  use_rotation: bool = ...

  """

  Chain follows rotation of target

  """

  use_stretch: bool = ...

  """

  Enable IK Stretching

  """

  use_tail: bool = ...

  """

  Include bone's tail as last element in chain

  """

  weight: float = ...

  """

  For Tree-IK: Weight of position control for this target

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class LimitDistanceConstraint(Constraint, bpy_struct):

  """

  Limit the distance from target object

  """

  distance: float = ...

  """

  Radius of limiting sphere

  """

  head_tail: float = ...

  """

  Target along length of bone: Head is 0, Tail is 1

  """

  limit_mode: str = ...

  """

  Distances in relation to sphere of influence to allow

  * ``LIMITDIST_INSIDE``
Inside -- The object is constrained inside a virtual sphere around the target object, with a radius defined by the limit distance.

  * ``LIMITDIST_OUTSIDE``
Outside -- The object is constrained outside a virtual sphere around the target object, with a radius defined by the limit distance.

  * ``LIMITDIST_ONSURFACE``
On Surface -- The object is constrained on the surface of a virtual sphere around the target object, with a radius defined by the limit distance.

  """

  subtarget: str = ...

  """

  Armature bone, mesh or lattice vertex group, ...

  """

  target: Object = ...

  """

  Target object

  """

  use_bbone_shape: bool = ...

  """

  Follow shape of B-Bone segments when calculating Head/Tail position

  """

  use_transform_limit: bool = ...

  """

  Transforms are affected by this constraint as well

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class LimitLocationConstraint(Constraint, bpy_struct):

  """

  Limit the location of the constrained object

  """

  max_x: float = ...

  """

  Highest X value to allow

  """

  max_y: float = ...

  """

  Highest Y value to allow

  """

  max_z: float = ...

  """

  Highest Z value to allow

  """

  min_x: float = ...

  """

  Lowest X value to allow

  """

  min_y: float = ...

  """

  Lowest Y value to allow

  """

  min_z: float = ...

  """

  Lowest Z value to allow

  """

  use_max_x: bool = ...

  """

  Use the maximum X value

  """

  use_max_y: bool = ...

  """

  Use the maximum Y value

  """

  use_max_z: bool = ...

  """

  Use the maximum Z value

  """

  use_min_x: bool = ...

  """

  Use the minimum X value

  """

  use_min_y: bool = ...

  """

  Use the minimum Y value

  """

  use_min_z: bool = ...

  """

  Use the minimum Z value

  """

  use_transform_limit: bool = ...

  """

  Transform tools are affected by this constraint as well

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class LimitRotationConstraint(Constraint, bpy_struct):

  """

  Limit the rotation of the constrained object

  """

  euler_order: str = ...

  """

  Explicitly specify the euler rotation order

  * ``AUTO``
Default -- Euler using the default rotation order.

  * ``XYZ``
XYZ Euler -- Euler using the XYZ rotation order.

  * ``XZY``
XZY Euler -- Euler using the XZY rotation order.

  * ``YXZ``
YXZ Euler -- Euler using the YXZ rotation order.

  * ``YZX``
YZX Euler -- Euler using the YZX rotation order.

  * ``ZXY``
ZXY Euler -- Euler using the ZXY rotation order.

  * ``ZYX``
ZYX Euler -- Euler using the ZYX rotation order.

  """

  max_x: float = ...

  """

  Highest X value to allow

  """

  max_y: float = ...

  """

  Highest Y value to allow

  """

  max_z: float = ...

  """

  Highest Z value to allow

  """

  min_x: float = ...

  """

  Lowest X value to allow

  """

  min_y: float = ...

  """

  Lowest Y value to allow

  """

  min_z: float = ...

  """

  Lowest Z value to allow

  """

  use_limit_x: bool = ...

  """

  Use the minimum X value

  """

  use_limit_y: bool = ...

  """

  Use the minimum Y value

  """

  use_limit_z: bool = ...

  """

  Use the minimum Z value

  """

  use_transform_limit: bool = ...

  """

  Transform tools are affected by this constraint as well

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class LimitScaleConstraint(Constraint, bpy_struct):

  """

  Limit the scaling of the constrained object

  """

  max_x: float = ...

  """

  Highest X value to allow

  """

  max_y: float = ...

  """

  Highest Y value to allow

  """

  max_z: float = ...

  """

  Highest Z value to allow

  """

  min_x: float = ...

  """

  Lowest X value to allow

  """

  min_y: float = ...

  """

  Lowest Y value to allow

  """

  min_z: float = ...

  """

  Lowest Z value to allow

  """

  use_max_x: bool = ...

  """

  Use the maximum X value

  """

  use_max_y: bool = ...

  """

  Use the maximum Y value

  """

  use_max_z: bool = ...

  """

  Use the maximum Z value

  """

  use_min_x: bool = ...

  """

  Use the minimum X value

  """

  use_min_y: bool = ...

  """

  Use the minimum Y value

  """

  use_min_z: bool = ...

  """

  Use the minimum Z value

  """

  use_transform_limit: bool = ...

  """

  Transform tools are affected by this constraint as well

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class LockedTrackConstraint(Constraint, bpy_struct):

  """

  Point toward the target along the track axis, while locking the other axis

  """

  head_tail: float = ...

  """

  Target along length of bone: Head is 0, Tail is 1

  """

  lock_axis: str = ...

  """

  Axis that points upward

  """

  subtarget: str = ...

  """

  Armature bone, mesh or lattice vertex group, ...

  """

  target: Object = ...

  """

  Target object

  """

  track_axis: str = ...

  """

  Axis that points to the target object

  """

  use_bbone_shape: bool = ...

  """

  Follow shape of B-Bone segments when calculating Head/Tail position

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MaintainVolumeConstraint(Constraint, bpy_struct):

  """

  Maintain a constant volume along a single scaling axis

  """

  free_axis: str = ...

  """

  The free scaling axis of the object

  """

  mode: str = ...

  """

  The way the constraint treats original non-free axis scaling

  * ``STRICT``
Strict -- Volume is strictly preserved, overriding the scaling of non-free axes.

  * ``UNIFORM``
Uniform -- Volume is preserved when the object is scaled uniformly. Deviations from uniform scale on non-free axes are passed through.

  * ``SINGLE_AXIS``
Single Axis -- Volume is preserved when the object is scaled only on the free axis. Non-free axis scaling is passed through.

  """

  volume: float = ...

  """

  Volume of the bone at rest

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ObjectSolverConstraint(Constraint, bpy_struct):

  """

  Lock motion to the reconstructed object movement

  """

  camera: Object = ...

  """

  Camera to which motion is parented (if empty active scene camera is used)

  """

  clip: MovieClip = ...

  """

  Movie Clip to get tracking data from

  """

  object: str = ...

  """

  Movie tracking object to follow

  """

  set_inverse_pending: bool = ...

  """

  Set to true to request recalculation of the inverse matrix

  """

  use_active_clip: bool = ...

  """

  Use active clip defined in scene

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class PivotConstraint(Constraint, bpy_struct):

  """

  Rotate around a different point

  """

  head_tail: float = ...

  """

  Target along length of bone: Head is 0, Tail is 1

  """

  offset: typing.Tuple[float, float, float] = ...

  """

  Offset of pivot from target (when set), or from owner's location (when Fixed Position is off), or the absolute pivot point

  """

  rotation_range: str = ...

  """

  Rotation range on which pivoting should occur

  * ``ALWAYS_ACTIVE``
Always -- Use the pivot point in every rotation.

  * ``NX``
-X Rotation -- Use the pivot point in the negative rotation range around the X-axis.

  * ``NY``
-Y Rotation -- Use the pivot point in the negative rotation range around the Y-axis.

  * ``NZ``
-Z Rotation -- Use the pivot point in the negative rotation range around the Z-axis.

  * ``X``
X Rotation -- Use the pivot point in the positive rotation range around the X-axis.

  * ``Y``
Y Rotation -- Use the pivot point in the positive rotation range around the Y-axis.

  * ``Z``
Z Rotation -- Use the pivot point in the positive rotation range around the Z-axis.

  """

  subtarget: str = ...

  target: Object = ...

  """

  Target Object, defining the position of the pivot when defined

  """

  use_bbone_shape: bool = ...

  """

  Follow shape of B-Bone segments when calculating Head/Tail position

  """

  use_relative_location: bool = ...

  """

  Offset will be an absolute point in space instead of relative to the target

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class PythonConstraint(Constraint, bpy_struct):

  """

  Use Python script for constraint evaluation

  """

  has_script_error: bool = ...

  """

  The linked Python script has thrown an error

  """

  target_count: int = ...

  """

  Usually only 1 to 3 are needed

  """

  targets: typing.Union[typing.Sequence[ConstraintTarget], typing.Mapping[str, ConstraintTarget], bpy_prop_collection] = ...

  """

  Target Objects

  """

  text: Text = ...

  """

  The text object that contains the Python script

  """

  use_targets: bool = ...

  """

  Use the targets indicated in the constraint panel

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ShrinkwrapConstraint(Constraint, bpy_struct):

  """

  Create constraint-based shrinkwrap relationship

  """

  cull_face: str = ...

  """

  Stop vertices from projecting to a face on the target when facing towards/away

  * ``OFF``
Off -- No culling.

  * ``FRONT``
Front -- No projection when in front of the face.

  * ``BACK``
Back -- No projection when behind the face.

  """

  distance: float = ...

  """

  Distance to Target

  """

  project_axis: str = ...

  """

  Axis constrain to

  """

  project_axis_space: str = ...

  """

  Space for the projection axis

  * ``WORLD``
World Space -- The constraint is applied relative to the world coordinate system.

  * ``CUSTOM``
Custom Space -- The constraint is applied in local space of a custom object/bone/vertex group.

  * ``POSE``
Pose Space -- The constraint is applied in Pose Space, the object transformation is ignored.

  * ``LOCAL_WITH_PARENT``
Local With Parent -- The constraint is applied relative to the rest pose local coordinate system of the bone, thus including the parent-induced transformation.

  * ``LOCAL``
Local Space -- The constraint is applied relative to the local coordinate system of the object.

  """

  project_limit: float = ...

  """

  Limit the distance used for projection (zero disables)

  """

  shrinkwrap_type: str = ...

  """

  Select type of shrinkwrap algorithm for target position

  * ``NEAREST_SURFACE``
Nearest Surface Point -- Shrink the location to the nearest target surface.

  * ``PROJECT``
Project -- Shrink the location to the nearest target surface along a given axis.

  * ``NEAREST_VERTEX``
Nearest Vertex -- Shrink the location to the nearest target vertex.

  * ``TARGET_PROJECT``
Target Normal Project -- Shrink the location to the nearest target surface along the interpolated vertex normals of the target.

  """

  target: Object = ...

  """

  Target Mesh object

  """

  track_axis: str = ...

  """

  Axis that is aligned to the normal

  """

  use_invert_cull: bool = ...

  """

  When projecting in the opposite direction invert the face cull mode

  """

  use_project_opposite: bool = ...

  """

  Project in both specified and opposite directions

  """

  use_track_normal: bool = ...

  """

  Align the specified axis to the surface normal

  """

  wrap_mode: str = ...

  """

  Select how to constrain the object to the target surface

  * ``ON_SURFACE``
On Surface -- The point is constrained to the surface of the target object, with distance offset towards the original point location.

  * ``INSIDE``
Inside -- The point is constrained to be inside the target object.

  * ``OUTSIDE``
Outside -- The point is constrained to be outside the target object.

  * ``OUTSIDE_SURFACE``
Outside Surface -- The point is constrained to the surface of the target object, with distance offset always to the outside, towards or away from the original location.

  * ``ABOVE_SURFACE``
Above Surface -- The point is constrained to the surface of the target object, with distance offset applied exactly along the target normal.

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SplineIKConstraint(Constraint, bpy_struct):

  """

  Align 'n' bones along a curve

  """

  bulge: float = ...

  """

  Factor between volume variation and stretching

  """

  bulge_max: float = ...

  """

  Maximum volume stretching factor

  """

  bulge_min: float = ...

  """

  Minimum volume stretching factor

  """

  bulge_smooth: float = ...

  """

  Strength of volume stretching clamping

  """

  chain_count: int = ...

  """

  How many bones are included in the chain

  """

  joint_bindings: typing.Tuple[float, ...] = ...

  """

  (EXPERIENCED USERS ONLY) The relative positions of the joints along the chain, as percentages

  """

  target: Object = ...

  """

  Curve that controls this relationship

  """

  use_bulge_max: bool = ...

  """

  Use upper limit for volume variation

  """

  use_bulge_min: bool = ...

  """

  Use lower limit for volume variation

  """

  use_chain_offset: bool = ...

  """

  Offset the entire chain relative to the root joint

  """

  use_curve_radius: bool = ...

  """

  Average radius of the endpoints is used to tweak the X and Z Scaling of the bones, on top of XZ Scale mode

  """

  use_even_divisions: bool = ...

  """

  Ignore the relative lengths of the bones when fitting to the curve

  """

  use_original_scale: bool = ...

  """

  Apply volume preservation over the original scaling

  """

  xz_scale_mode: str = ...

  """

  Method used for determining the scaling of the X and Z axes of the bones

  * ``NONE``
None -- Don't scale the X and Z axes (Default).

  * ``BONE_ORIGINAL``
Bone Original -- Use the original scaling of the bones.

  * ``INVERSE_PRESERVE``
Inverse Scale -- Scale of the X and Z axes is the inverse of the Y-Scale.

  * ``VOLUME_PRESERVE``
Volume Preservation -- Scale of the X and Z axes are adjusted to preserve the volume of the bones.

  """

  y_scale_mode: str = ...

  """

  Method used for determining the scaling of the Y axis of the bones, on top of the shape and scaling of the curve itself

  * ``NONE``
None -- Don't scale in the Y axis.

  * ``FIT_CURVE``
Fit Curve -- Scale the bones to fit the entire length of the curve.

  * ``BONE_ORIGINAL``
Bone Original -- Use the original Y scale of the bone.

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class StretchToConstraint(Constraint, bpy_struct):

  """

  Stretch to meet the target object

  """

  bulge: float = ...

  """

  Factor between volume variation and stretching

  """

  bulge_max: float = ...

  """

  Maximum volume stretching factor

  """

  bulge_min: float = ...

  """

  Minimum volume stretching factor

  """

  bulge_smooth: float = ...

  """

  Strength of volume stretching clamping

  """

  head_tail: float = ...

  """

  Target along length of bone: Head is 0, Tail is 1

  """

  keep_axis: str = ...

  """

  The rotation type and axis order to use

  * ``PLANE_X``
XZ -- Rotate around local X, then Z.

  * ``PLANE_Z``
ZX -- Rotate around local Z, then X.

  * ``SWING_Y``
Swing -- Use the smallest single axis rotation, similar to Damped Track.

  """

  rest_length: float = ...

  """

  Length at rest position

  """

  subtarget: str = ...

  """

  Armature bone, mesh or lattice vertex group, ...

  """

  target: Object = ...

  """

  Target object

  """

  use_bbone_shape: bool = ...

  """

  Follow shape of B-Bone segments when calculating Head/Tail position

  """

  use_bulge_max: bool = ...

  """

  Use upper limit for volume variation

  """

  use_bulge_min: bool = ...

  """

  Use lower limit for volume variation

  """

  volume: str = ...

  """

  Maintain the object's volume as it stretches

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class TrackToConstraint(Constraint, bpy_struct):

  """

  Aim the constrained object toward the target

  """

  head_tail: float = ...

  """

  Target along length of bone: Head is 0, Tail is 1

  """

  subtarget: str = ...

  """

  Armature bone, mesh or lattice vertex group, ...

  """

  target: Object = ...

  """

  Target object

  """

  track_axis: str = ...

  """

  Axis that points to the target object

  """

  up_axis: str = ...

  """

  Axis that points upward

  """

  use_bbone_shape: bool = ...

  """

  Follow shape of B-Bone segments when calculating Head/Tail position

  """

  use_target_z: bool = ...

  """

  Target's Z axis, not World Z axis, will constraint the Up direction

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class TransformCacheConstraint(Constraint, bpy_struct):

  """

  Look up transformation from an external file

  """

  cache_file: CacheFile = ...

  object_path: str = ...

  """

  Path to the object in the Alembic archive used to lookup the transform matrix

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class TransformConstraint(Constraint, bpy_struct):

  """

  Map transformations of the target to the object

  """

  from_max_x: float = ...

  """

  Top range of X axis source motion

  """

  from_max_x_rot: float = ...

  """

  Top range of X axis source motion

  """

  from_max_x_scale: float = ...

  """

  Top range of X axis source motion

  """

  from_max_y: float = ...

  """

  Top range of Y axis source motion

  """

  from_max_y_rot: float = ...

  """

  Top range of Y axis source motion

  """

  from_max_y_scale: float = ...

  """

  Top range of Y axis source motion

  """

  from_max_z: float = ...

  """

  Top range of Z axis source motion

  """

  from_max_z_rot: float = ...

  """

  Top range of Z axis source motion

  """

  from_max_z_scale: float = ...

  """

  Top range of Z axis source motion

  """

  from_min_x: float = ...

  """

  Bottom range of X axis source motion

  """

  from_min_x_rot: float = ...

  """

  Bottom range of X axis source motion

  """

  from_min_x_scale: float = ...

  """

  Bottom range of X axis source motion

  """

  from_min_y: float = ...

  """

  Bottom range of Y axis source motion

  """

  from_min_y_rot: float = ...

  """

  Bottom range of Y axis source motion

  """

  from_min_y_scale: float = ...

  """

  Bottom range of Y axis source motion

  """

  from_min_z: float = ...

  """

  Bottom range of Z axis source motion

  """

  from_min_z_rot: float = ...

  """

  Bottom range of Z axis source motion

  """

  from_min_z_scale: float = ...

  """

  Bottom range of Z axis source motion

  """

  from_rotation_mode: str = ...

  """

  Specify the type of rotation channels to use

  * ``AUTO``
Auto Euler -- Euler using the rotation order of the target.

  * ``XYZ``
XYZ Euler -- Euler using the XYZ rotation order.

  * ``XZY``
XZY Euler -- Euler using the XZY rotation order.

  * ``YXZ``
YXZ Euler -- Euler using the YXZ rotation order.

  * ``YZX``
YZX Euler -- Euler using the YZX rotation order.

  * ``ZXY``
ZXY Euler -- Euler using the ZXY rotation order.

  * ``ZYX``
ZYX Euler -- Euler using the ZYX rotation order.

  * ``QUATERNION``
Quaternion -- Quaternion rotation.

  * ``SWING_TWIST_X``
Swing and X Twist -- Decompose into a swing rotation to aim the X axis, followed by twist around it.

  * ``SWING_TWIST_Y``
Swing and Y Twist -- Decompose into a swing rotation to aim the Y axis, followed by twist around it.

  * ``SWING_TWIST_Z``
Swing and Z Twist -- Decompose into a swing rotation to aim the Z axis, followed by twist around it.

  """

  map_from: str = ...

  """

  The transformation type to use from the target

  """

  map_to: str = ...

  """

  The transformation type to affect of the constrained object

  """

  map_to_x_from: str = ...

  """

  The source axis constrained object's X axis uses

  """

  map_to_y_from: str = ...

  """

  The source axis constrained object's Y axis uses

  """

  map_to_z_from: str = ...

  """

  The source axis constrained object's Z axis uses

  """

  mix_mode: str = ...

  """

  Specify how to combine the new location with original

  * ``REPLACE``
Replace -- Replace component values.

  * ``ADD``
Add -- Add component values together.

  """

  mix_mode_rot: str = ...

  """

  Specify how to combine the new rotation with original

  * ``REPLACE``
Replace -- Replace component values.

  * ``ADD``
Add -- Add component values together.

  * ``BEFORE``
Before Original -- Apply new rotation before original, as if it was on a parent.

  * ``AFTER``
After Original -- Apply new rotation after original, as if it was on a child.

  """

  mix_mode_scale: str = ...

  """

  Specify how to combine the new scale with original

  * ``REPLACE``
Replace -- Replace component values.

  * ``MULTIPLY``
Multiply -- Multiply component values together.

  """

  subtarget: str = ...

  """

  Armature bone, mesh or lattice vertex group, ...

  """

  target: Object = ...

  """

  Target object

  """

  to_euler_order: str = ...

  """

  Explicitly specify the output euler rotation order

  * ``AUTO``
Default -- Euler using the default rotation order.

  * ``XYZ``
XYZ Euler -- Euler using the XYZ rotation order.

  * ``XZY``
XZY Euler -- Euler using the XZY rotation order.

  * ``YXZ``
YXZ Euler -- Euler using the YXZ rotation order.

  * ``YZX``
YZX Euler -- Euler using the YZX rotation order.

  * ``ZXY``
ZXY Euler -- Euler using the ZXY rotation order.

  * ``ZYX``
ZYX Euler -- Euler using the ZYX rotation order.

  """

  to_max_x: float = ...

  """

  Top range of X axis destination motion

  """

  to_max_x_rot: float = ...

  """

  Top range of X axis destination motion

  """

  to_max_x_scale: float = ...

  """

  Top range of X axis destination motion

  """

  to_max_y: float = ...

  """

  Top range of Y axis destination motion

  """

  to_max_y_rot: float = ...

  """

  Top range of Y axis destination motion

  """

  to_max_y_scale: float = ...

  """

  Top range of Y axis destination motion

  """

  to_max_z: float = ...

  """

  Top range of Z axis destination motion

  """

  to_max_z_rot: float = ...

  """

  Top range of Z axis destination motion

  """

  to_max_z_scale: float = ...

  """

  Top range of Z axis destination motion

  """

  to_min_x: float = ...

  """

  Bottom range of X axis destination motion

  """

  to_min_x_rot: float = ...

  """

  Bottom range of X axis destination motion

  """

  to_min_x_scale: float = ...

  """

  Bottom range of X axis destination motion

  """

  to_min_y: float = ...

  """

  Bottom range of Y axis destination motion

  """

  to_min_y_rot: float = ...

  """

  Bottom range of Y axis destination motion

  """

  to_min_y_scale: float = ...

  """

  Bottom range of Y axis destination motion

  """

  to_min_z: float = ...

  """

  Bottom range of Z axis destination motion

  """

  to_min_z_rot: float = ...

  """

  Bottom range of Z axis destination motion

  """

  to_min_z_scale: float = ...

  """

  Bottom range of Z axis destination motion

  """

  use_motion_extrapolate: bool = ...

  """

  Extrapolate ranges

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FileAssetSelectParams(bpy_struct, FileSelectParams):

  """

  Settings for the file selection in Asset Browser mode

  """

  asset_library_ref: str = ...

  catalog_id: str = ...

  """

  The UUID of the catalog shown in the browser

  """

  filter_asset_id: FileAssetSelectIDFilter = ...

  """

  Which asset types to show/hide, when browsing an asset library

  """

  import_type: str = ...

  """

  Determine how the asset will be imported

  * ``LINK``
Link -- Import the assets as linked data-block.

  * ``APPEND``
Append -- Import the assets as copied data-block, with no link to the original asset data-block.

  * ``APPEND_REUSE``
Append (Reuse Data) -- Import the assets as copied data-block while avoiding multiple copies of nested, typically heavy data. For example the textures of a material asset, or the mesh of an object asset, don't have to be copied every time this asset is imported. The instances of the asset share the data instead.

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FModifierCycles(bpy_struct, FModifier):

  """

  Repeat the values of the modified F-Curve

  """

  cycles_after: int = ...

  """

  Maximum number of cycles to allow after last keyframe (0 = infinite)

  """

  cycles_before: int = ...

  """

  Maximum number of cycles to allow before first keyframe (0 = infinite)

  """

  mode_after: str = ...

  """

  Cycling mode to use after last keyframe

  * ``NONE``
No Cycles -- Don't do anything.

  * ``REPEAT``
Repeat Motion -- Repeat keyframe range as-is.

  * ``REPEAT_OFFSET``
Repeat with Offset -- Repeat keyframe range, but with offset based on gradient between start and end values.

  * ``MIRROR``
Repeat Mirrored -- Alternate between forward and reverse playback of keyframe range.

  """

  mode_before: str = ...

  """

  Cycling mode to use before first keyframe

  * ``NONE``
No Cycles -- Don't do anything.

  * ``REPEAT``
Repeat Motion -- Repeat keyframe range as-is.

  * ``REPEAT_OFFSET``
Repeat with Offset -- Repeat keyframe range, but with offset based on gradient between start and end values.

  * ``MIRROR``
Repeat Mirrored -- Alternate between forward and reverse playback of keyframe range.

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FModifierEnvelope(bpy_struct, FModifier):

  """

  Scale the values of the modified F-Curve

  """

  control_points: typing.Union[FModifierEnvelopeControlPoints, typing.Sequence[FModifierEnvelopeControlPoint], typing.Mapping[str, FModifierEnvelopeControlPoint], bpy_prop_collection] = ...

  """

  Control points defining the shape of the envelope

  """

  default_max: float = ...

  """

  Upper distance from Reference Value for 1:1 default influence

  """

  default_min: float = ...

  """

  Lower distance from Reference Value for 1:1 default influence

  """

  reference_value: float = ...

  """

  Value that envelope's influence is centered around / based on

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FModifierFunctionGenerator(bpy_struct, FModifier):

  """

  Generate values using a built-in function

  """

  amplitude: float = ...

  """

  Scale factor determining the maximum/minimum values

  """

  function_type: str = ...

  """

  Type of built-in function to use

  * ``SIN``
Sine.

  * ``COS``
Cosine.

  * ``TAN``
Tangent.

  * ``SQRT``
Square Root.

  * ``LN``
Natural Logarithm.

  * ``SINC``
Normalized Sine -- sin(x) / x.

  """

  phase_multiplier: float = ...

  """

  Scale factor determining the 'speed' of the function

  """

  phase_offset: float = ...

  """

  Constant factor to offset time by for function

  """

  use_additive: bool = ...

  """

  Values generated by this modifier are applied on top of the existing values instead of overwriting them

  """

  value_offset: float = ...

  """

  Constant factor to offset values by

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FModifierGenerator(bpy_struct, FModifier):

  """

  Deterministically generate values for the modified F-Curve

  """

  coefficients: typing.Tuple[float, ...] = ...

  """

  Coefficients for 'x' (starting from lowest power of x^0)

  """

  mode: str = ...

  """

  Type of generator to use

  """

  poly_order: int = ...

  """

  The highest power of 'x' for this polynomial (number of coefficients - 1)

  """

  use_additive: bool = ...

  """

  Values generated by this modifier are applied on top of the existing values instead of overwriting them

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FModifierLimits(bpy_struct, FModifier):

  """

  Limit the time/value ranges of the modified F-Curve

  """

  max_x: float = ...

  """

  Highest X value to allow

  """

  max_y: float = ...

  """

  Highest Y value to allow

  """

  min_x: float = ...

  """

  Lowest X value to allow

  """

  min_y: float = ...

  """

  Lowest Y value to allow

  """

  use_max_x: bool = ...

  """

  Use the maximum X value

  """

  use_max_y: bool = ...

  """

  Use the maximum Y value

  """

  use_min_x: bool = ...

  """

  Use the minimum X value

  """

  use_min_y: bool = ...

  """

  Use the minimum Y value

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FModifierNoise(bpy_struct, FModifier):

  """

  Give randomness to the modified F-Curve

  """

  blend_type: str = ...

  """

  Method of modifying the existing F-Curve

  """

  depth: int = ...

  """

  Amount of fine level detail present in the noise

  """

  offset: float = ...

  """

  Time offset for the noise effect

  """

  phase: float = ...

  """

  A random seed for the noise effect

  """

  scale: float = ...

  """

  Scaling (in time) of the noise

  """

  strength: float = ...

  """

  Amplitude of the noise - the amount that it modifies the underlying curve

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FModifierPython(bpy_struct, FModifier):

  """

  Perform user-defined operation on the modified F-Curve

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FModifierStepped(bpy_struct, FModifier):

  """

  Hold each interpolated value from the F-Curve for several frames without changing the timing

  """

  frame_end: float = ...

  """

  Frame that modifier's influence ends (if applicable)

  """

  frame_offset: float = ...

  """

  Reference number of frames before frames get held (use to get hold for '1-3' vs '5-7' holding patterns)

  """

  frame_start: float = ...

  """

  Frame that modifier's influence starts (if applicable)

  """

  frame_step: float = ...

  """

  Number of frames to hold each value

  """

  use_frame_end: bool = ...

  """

  Restrict modifier to only act before its 'end' frame

  """

  use_frame_start: bool = ...

  """

  Restrict modifier to only act after its 'start' frame

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ArmatureGpencilModifier(bpy_struct, GpencilModifier):

  """

  Change stroke using armature to deform modifier

  """

  invert_vertex_group: bool = ...

  """

  Invert vertex group influence

  """

  object: Object = ...

  """

  Armature object to deform with

  """

  use_bone_envelopes: bool = ...

  """

  Bind Bone envelopes to armature modifier

  """

  use_deform_preserve_volume: bool = ...

  """

  Deform rotation interpolation with quaternions

  """

  use_vertex_groups: bool = ...

  """

  Bind vertex groups to armature modifier

  """

  vertex_group: str = ...

  """

  Name of Vertex Group which determines influence of modifier per point

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ArrayGpencilModifier(bpy_struct, GpencilModifier):

  """

  Create grid of duplicate instances

  """

  constant_offset: typing.Tuple[float, float, float] = ...

  """

  Value for the distance between items

  """

  count: int = ...

  """

  Number of items

  """

  invert_layer_pass: bool = ...

  """

  Inverse filter

  """

  invert_layers: bool = ...

  """

  Inverse filter

  """

  invert_material_pass: bool = ...

  """

  Inverse filter

  """

  invert_materials: bool = ...

  """

  Inverse filter

  """

  layer: str = ...

  """

  Layer name

  """

  layer_pass: int = ...

  """

  Layer pass index

  """

  material: Material = ...

  """

  Material used for filtering effect

  """

  offset_object: Object = ...

  """

  Use the location and rotation of another object to determine the distance and rotational change between arrayed items

  """

  pass_index: int = ...

  """

  Pass index

  """

  random_offset: typing.Tuple[float, float, float] = ...

  """

  Value for changes in location

  """

  random_rotation: typing.Tuple[float, float, float] = ...

  """

  Value for changes in rotation

  """

  random_scale: typing.Tuple[float, float, float] = ...

  """

  Value for changes in scale

  """

  relative_offset: typing.Tuple[float, float, float] = ...

  """

  The size of the geometry will determine the distance between arrayed items

  """

  replace_material: int = ...

  """

  Index of the material used for generated strokes (0 keep original material)

  """

  seed: int = ...

  """

  Random seed

  """

  use_constant_offset: bool = ...

  """

  Enable offset

  """

  use_object_offset: bool = ...

  """

  Enable object offset

  """

  use_relative_offset: bool = ...

  """

  Enable shift

  """

  use_uniform_random_scale: bool = ...

  """

  Use the same random seed for each scale axis for a uniform scale

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class BuildGpencilModifier(bpy_struct, GpencilModifier):

  """

  Animate strokes appearing and disappearing

  """

  concurrent_time_alignment: str = ...

  """

  When should strokes start to appear/disappear

  * ``START``
Align Start -- All strokes start at same time (i.e. short strokes finish earlier).

  * ``END``
Align End -- All strokes end at same time (i.e. short strokes start later).

  """

  frame_end: float = ...

  """

  End Frame (when Restrict Frame Range is enabled)

  """

  frame_start: float = ...

  """

  Start Frame (when Restrict Frame Range is enabled)

  """

  invert_layer_pass: bool = ...

  """

  Inverse filter

  """

  invert_layers: bool = ...

  """

  Inverse filter

  """

  layer: str = ...

  """

  Layer name

  """

  layer_pass: int = ...

  """

  Layer pass index

  """

  length: float = ...

  """

  Maximum number of frames that the build effect can run for (unless another GP keyframe occurs before this time has elapsed)

  """

  mode: str = ...

  """

  How many strokes are being animated at a time

  * ``SEQUENTIAL``
Sequential -- Strokes appear/disappear one after the other, but only a single one changes at a time.

  * ``CONCURRENT``
Concurrent -- Multiple strokes appear/disappear at once.

  """

  percentage_factor: float = ...

  """

  Defines how much of the stroke is visible

  """

  start_delay: float = ...

  """

  Number of frames after each GP keyframe before the modifier has any effect

  """

  transition: str = ...

  """

  How are strokes animated (i.e. are they appearing or disappearing)

  * ``GROW``
Grow -- Show points in the order they occur in each stroke (e.g. for animating lines being drawn).

  * ``SHRINK``
Shrink -- Hide points from the end of each stroke to the start (e.g. for animating lines being erased).

  * ``FADE``
Fade -- Hide points in the order they occur in each stroke (e.g. for animating ink fading or vanishing after getting drawn).

  """

  use_percentage: bool = ...

  """

  Use a percentage factor to determine the visible points

  """

  use_restrict_frame_range: bool = ...

  """

  Only modify strokes during the specified frame range

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ColorGpencilModifier(bpy_struct, GpencilModifier):

  """

  Change Hue/Saturation modifier

  """

  curve: CurveMapping = ...

  """

  Custom curve to apply effect

  """

  hue: float = ...

  """

  Color Hue

  """

  invert_layer_pass: bool = ...

  """

  Inverse filter

  """

  invert_layers: bool = ...

  """

  Inverse filter

  """

  invert_material_pass: bool = ...

  """

  Inverse filter

  """

  invert_materials: bool = ...

  """

  Inverse filter

  """

  layer: str = ...

  """

  Layer name

  """

  layer_pass: int = ...

  """

  Layer pass index

  """

  material: Material = ...

  """

  Material used for filtering effect

  """

  modify_color: str = ...

  """

  Set what colors of the stroke are affected

  * ``BOTH``
Stroke and Fill -- Modify fill and stroke colors.

  * ``STROKE``
Stroke -- Modify stroke color only.

  * ``FILL``
Fill -- Modify fill color only.

  """

  pass_index: int = ...

  """

  Pass index

  """

  saturation: float = ...

  """

  Color Saturation

  """

  use_custom_curve: bool = ...

  """

  Use a custom curve to define color effect along the strokes

  """

  value: float = ...

  """

  Color Value

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class DashGpencilModifierData(bpy_struct, GpencilModifier):

  """

  Create dot-dash effect for strokes

  """

  dash_offset: int = ...

  """

  Offset into each stroke before the beginning of  the dashed segment generation

  """

  invert_layer_pass: bool = ...

  """

  Inverse filter

  """

  invert_layers: bool = ...

  """

  Inverse filter

  """

  invert_material_pass: bool = ...

  """

  Inverse filter

  """

  invert_materials: bool = ...

  """

  Inverse filter

  """

  layer: str = ...

  """

  Layer name

  """

  layer_pass: int = ...

  """

  Layer pass index

  """

  material: Material = ...

  """

  Material used for filtering effect

  """

  pass_index: int = ...

  """

  Pass index

  """

  segment_active_index: int = ...

  """

  Active index in the segment list

  """

  segments: typing.Union[typing.Sequence[DashGpencilModifierSegment], typing.Mapping[str, DashGpencilModifierSegment], bpy_prop_collection] = ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class HookGpencilModifier(bpy_struct, GpencilModifier):

  """

  Hook modifier to modify the location of stroke points

  """

  center: typing.Tuple[float, float, float] = ...

  falloff_curve: CurveMapping = ...

  """

  Custom light falloff curve

  """

  falloff_radius: float = ...

  """

  If not zero, the distance from the hook where influence ends

  """

  falloff_type: str = ...

  invert_layer_pass: bool = ...

  """

  Inverse filter

  """

  invert_layers: bool = ...

  """

  Inverse filter

  """

  invert_material_pass: bool = ...

  """

  Inverse filter

  """

  invert_materials: bool = ...

  """

  Inverse filter

  """

  invert_vertex: bool = ...

  """

  Inverse filter

  """

  layer: str = ...

  """

  Layer name

  """

  layer_pass: int = ...

  """

  Layer pass index

  """

  material: Material = ...

  """

  Material used for filtering effect

  """

  matrix_inverse: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]] = ...

  """

  Reverse the transformation between this object and its target

  """

  object: Object = ...

  """

  Parent Object for hook, also recalculates and clears offset

  """

  pass_index: int = ...

  """

  Pass index

  """

  strength: float = ...

  """

  Relative force of the hook

  """

  subtarget: str = ...

  """

  Name of Parent Bone for hook (if applicable), also recalculates and clears offset

  """

  use_falloff_uniform: bool = ...

  """

  Compensate for non-uniform object scale

  """

  vertex_group: str = ...

  """

  Vertex group name for modulating the deform

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class LatticeGpencilModifier(bpy_struct, GpencilModifier):

  """

  Change stroke using lattice to deform modifier

  """

  invert_layer_pass: bool = ...

  """

  Inverse filter

  """

  invert_layers: bool = ...

  """

  Inverse filter

  """

  invert_material_pass: bool = ...

  """

  Inverse filter

  """

  invert_materials: bool = ...

  """

  Inverse filter

  """

  invert_vertex: bool = ...

  """

  Inverse filter

  """

  layer: str = ...

  """

  Layer name

  """

  layer_pass: int = ...

  """

  Layer pass index

  """

  material: Material = ...

  """

  Material used for filtering effect

  """

  object: Object = ...

  """

  Lattice object to deform with

  """

  pass_index: int = ...

  """

  Pass index

  """

  strength: float = ...

  """

  Strength of modifier effect

  """

  vertex_group: str = ...

  """

  Vertex group name for modulating the deform

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class LengthGpencilModifier(bpy_struct, GpencilModifier):

  """

  Stretch or shrink strokes

  """

  end_factor: float = ...

  """

  Added length to the end of each stroke relative to its length

  """

  end_length: float = ...

  """

  Absolute added length to the end of each stroke

  """

  invert_curvature: bool = ...

  """

  Invert the curvature of the stroke's extension

  """

  invert_layer_pass: bool = ...

  """

  Inverse filter

  """

  invert_layers: bool = ...

  """

  Inverse filter

  """

  invert_material_pass: bool = ...

  """

  Inverse filter

  """

  invert_materials: bool = ...

  """

  Inverse filter

  """

  layer: str = ...

  """

  Layer name

  """

  layer_pass: int = ...

  """

  Layer pass index

  """

  material: Material = ...

  """

  Material used for filtering effect

  """

  max_angle: float = ...

  """

  Ignore points on the stroke that deviate from their neighbors by more than this angle when determining the extrapolation shape

  """

  mode: str = ...

  """

  Mode to define length

  * ``RELATIVE``
Relative -- Length in ratio to the stroke's length.

  * ``ABSOLUTE``
Absolute -- Length in geometry space.

  """

  overshoot_factor: float = ...

  """

  Defines what portion of the stroke is used for the calculation of the extension

  """

  pass_index: int = ...

  """

  Pass index

  """

  point_density: float = ...

  """

  Multiplied by Start/End for the total added point count

  """

  segment_influence: float = ...

  """

  Factor to determine how much the length of the individual segments should influence the final computed curvature. Higher factors makes small segments influence the overall curvature less

  """

  start_factor: float = ...

  """

  Added length to the start of each stroke relative to its length

  """

  start_length: float = ...

  """

  Absolute added length to the start of each stroke

  """

  use_curvature: bool = ...

  """

  Follow the curvature of the stroke

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class LineartGpencilModifier(bpy_struct, GpencilModifier):

  """

  Generate line art strokes from selected source

  """

  chaining_image_threshold: float = ...

  """

  Segments with an image distance smaller than this will be chained together

  """

  crease_threshold: float = ...

  """

  Angles smaller than this will be treated as creases

  """

  invert_source_vertex_group: bool = ...

  """

  Invert source vertex group values

  """

  is_baked: bool = ...

  """

  This modifier has baked data

  """

  level_end: int = ...

  """

  Maximum number of occlusions for the generated strokes

  """

  level_start: int = ...

  """

  Minimum number of occlusions for the generated strokes

  """

  opacity: float = ...

  """

  The strength value for the generate strokes

  """

  overscan: float = ...

  """

  A margin to prevent strokes from ending abruptly at the edge of the image

  """

  smooth_tolerance: float = ...

  """

  Strength of smoothing applied on jagged chains

  """

  source_camera: Object = ...

  """

  Use specified camera object for generating line art

  """

  source_collection: Collection = ...

  """

  Generate strokes from the objects in this collection

  """

  source_object: Object = ...

  """

  Generate strokes from this object

  """

  source_type: str = ...

  """

  Line art stroke source type

  """

  source_vertex_group: str = ...

  """

  Match the beginning of vertex group names from mesh objects, match all when left empty

  """

  split_angle: float = ...

  """

  Angle in screen space below which a stroke is split in two

  """

  stroke_depth_offset: float = ...

  """

  Move strokes slightly towards the camera to avoid clipping while preserve depth for the viewport

  """

  target_layer: str = ...

  """

  Grease Pencil layer assigned to the generated strokes

  """

  target_material: Material = ...

  """

  Grease Pencil material assigned to the generated strokes

  """

  thickness: int = ...

  """

  The thickness for the generated strokes

  """

  use_cache: bool = ...

  """

  Use cached scene data from the first line art modifier in the stack. Certain settings will be unavailable

  """

  use_clip_plane_boundaries: bool = ...

  """

  Allow lines generated by the near/far clipping plane to be shown

  """

  use_contour: bool = ...

  """

  Generate strokes from contours lines

  """

  use_crease: bool = ...

  """

  Generate strokes from creased edges

  """

  use_crease_on_sharp: bool = ...

  """

  Allow crease to show on sharp edges

  """

  use_crease_on_smooth: bool = ...

  """

  Allow crease edges to show inside smooth surfaces

  """

  use_custom_camera: bool = ...

  """

  Use custom camera instead of the active camera

  """

  use_edge_mark: bool = ...

  """

  Generate strokes from freestyle marked edges

  """

  use_edge_overlap: bool = ...

  """

  Allow edges in the same location (i.e. from edge split) to show properly. May run slower

  """

  use_face_mark: bool = ...

  """

  Filter feature lines using freestyle face marks

  """

  use_face_mark_boundaries: bool = ...

  """

  Filter feature lines based on face mark boundaries

  """

  use_face_mark_invert: bool = ...

  """

  Invert face mark filtering

  """

  use_fuzzy_all: bool = ...

  """

  Treat all lines as the same line type so they can be chained together

  """

  use_fuzzy_intersections: bool = ...

  """

  Treat intersection and contour lines as if they were the same type so they can be chained together

  """

  use_geometry_space_chain: bool = ...

  """

  Use geometry distance for chaining instead of image space

  """

  use_image_boundary_trimming: bool = ...

  """

  Trim all edges right at the boundary of image(including overscan region)

  """

  use_intersection: bool = ...

  """

  Generate strokes from intersections

  """

  use_intersection_mask: typing.Tuple[bool, ...] = ...

  """

  Mask bits to match from Collection Line Art settings

  """

  use_intersection_match: bool = ...

  """

  Require matching all intersection masks instead of just one

  """

  use_loose: bool = ...

  """

  Generate strokes from loose edges

  """

  use_loose_as_contour: bool = ...

  """

  Loose edges will have contour type

  """

  use_loose_edge_chain: bool = ...

  """

  Allow loose edges to be chained together

  """

  use_material: bool = ...

  """

  Generate strokes from borders between materials

  """

  use_material_mask: bool = ...

  """

  Use material masks to filter out occluded strokes

  """

  use_material_mask_bits: typing.Tuple[bool, ...] = ...

  """

  Mask bits to match from Material Line Art settings

  """

  use_material_mask_match: bool = ...

  """

  Require matching all material masks instead of just one

  """

  use_multiple_levels: bool = ...

  """

  Generate strokes from a range of occlusion levels

  """

  use_object_instances: bool = ...

  """

  Support particle objects and face/vertex instances to show in line art

  """

  use_offset_towards_custom_camera: bool = ...

  """

  Offset strokes towards selected camera instead of the active camera

  """

  use_output_vertex_group_match_by_name: bool = ...

  """

  Match output vertex group based on name

  """

  use_overlap_edge_type_support: bool = ...

  """

  Allow an edge to have multiple overlapping types. This will create a separate stroke for each overlapping type

  """

  use_remove_doubles: bool = ...

  """

  Remove doubles from the source geometry before generating stokes

  """

  vertex_group: str = ...

  """

  Vertex group name for selected strokes

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MirrorGpencilModifier(bpy_struct, GpencilModifier):

  """

  Create mirroring strokes

  """

  invert_layer_pass: bool = ...

  """

  Inverse filter

  """

  invert_layers: bool = ...

  """

  Inverse filter

  """

  invert_material_pass: bool = ...

  """

  Inverse filter

  """

  invert_materials: bool = ...

  """

  Inverse filter

  """

  layer: str = ...

  """

  Layer name

  """

  layer_pass: int = ...

  """

  Layer pass index

  """

  material: Material = ...

  """

  Material used for filtering effect

  """

  object: Object = ...

  """

  Object used as center

  """

  pass_index: int = ...

  """

  Pass index

  """

  use_axis_x: bool = ...

  """

  Mirror the X axis

  """

  use_axis_y: bool = ...

  """

  Mirror the Y axis

  """

  use_axis_z: bool = ...

  """

  Mirror the Z axis

  """

  use_clip: bool = ...

  """

  Clip points

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class MultiplyGpencilModifier(bpy_struct, GpencilModifier):

  """

  Generate multiple strokes from one stroke

  """

  distance: float = ...

  """

  Distance of duplications

  """

  duplicates: int = ...

  """

  How many copies of strokes be displayed

  """

  fading_center: float = ...

  """

  Fade center

  """

  fading_opacity: float = ...

  """

  Fade influence of stroke's opacity

  """

  fading_thickness: float = ...

  """

  Fade influence of stroke's thickness

  """

  invert_layer_pass: bool = ...

  """

  Inverse filter

  """

  invert_layers: bool = ...

  """

  Inverse filter

  """

  invert_material_pass: bool = ...

  """

  Inverse filter

  """

  invert_materials: bool = ...

  """

  Inverse filter

  """

  layer: str = ...

  """

  Layer name

  """

  layer_pass: int = ...

  """

  Layer pass index

  """

  material: Material = ...

  """

  Material used for filtering effect

  """

  offset: float = ...

  """

  Offset of duplicates. -1 to 1: inner to outer

  """

  pass_index: int = ...

  """

  Pass index

  """

  use_fade: bool = ...

  """

  Fade the stroke thickness for each generated stroke

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class NoiseGpencilModifier(bpy_struct, GpencilModifier):

  """

  Noise effect modifier

  """

  curve: CurveMapping = ...

  """

  Custom curve to apply effect

  """

  factor: float = ...

  """

  Amount of noise to apply

  """

  factor_strength: float = ...

  """

  Amount of noise to apply to opacity

  """

  factor_thickness: float = ...

  """

  Amount of noise to apply to thickness

  """

  factor_uvs: float = ...

  """

  Amount of noise to apply uv rotation

  """

  invert_layer_pass: bool = ...

  """

  Inverse filter

  """

  invert_layers: bool = ...

  """

  Inverse filter

  """

  invert_material_pass: bool = ...

  """

  Inverse filter

  """

  invert_materials: bool = ...

  """

  Inverse filter

  """

  invert_vertex: bool = ...

  """

  Inverse filter

  """

  layer: str = ...

  """

  Layer name

  """

  layer_pass: int = ...

  """

  Layer pass index

  """

  material: Material = ...

  """

  Material used for filtering effect

  """

  noise_offset: float = ...

  """

  Offset the noise along the strokes

  """

  noise_scale: float = ...

  """

  Scale the noise frequency

  """

  pass_index: int = ...

  """

  Pass index

  """

  seed: int = ...

  """

  Random seed

  """

  step: int = ...

  """

  Number of frames before recalculate random values again

  """

  use_custom_curve: bool = ...

  """

  Use a custom curve to define noise effect along the strokes

  """

  use_random: bool = ...

  """

  Use random values over time

  """

  vertex_group: str = ...

  """

  Vertex group name for modulating the deform

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class OffsetGpencilModifier(bpy_struct, GpencilModifier):

  """

  Offset Stroke modifier

  """

  invert_layer_pass: bool = ...

  """

  Inverse filter

  """

  invert_layers: bool = ...

  """

  Inverse filter

  """

  invert_material_pass: bool = ...

  """

  Inverse filter

  """

  invert_materials: bool = ...

  """

  Inverse filter

  """

  invert_vertex: bool = ...

  """

  Inverse filter

  """

  layer: str = ...

  """

  Layer name

  """

  layer_pass: int = ...

  """

  Layer pass index

  """

  location: typing.Tuple[float, float, float] = ...

  """

  Values for change location

  """

  material: Material = ...

  """

  Material used for filtering effect

  """

  pass_index: int = ...

  """

  Pass index

  """

  random_offset: typing.Tuple[float, float, float] = ...

  """

  Value for changes in location

  """

  random_rotation: typing.Tuple[float, float, float] = ...

  """

  Value for changes in rotation

  """

  random_scale: typing.Tuple[float, float, float] = ...

  """

  Value for changes in scale

  """

  rotation: typing.Tuple[float, float, float] = ...

  """

  Values for changes in rotation

  """

  scale: typing.Tuple[float, float, float] = ...

  """

  Values for changes in scale

  """

  seed: int = ...

  """

  Random seed

  """

  use_uniform_random_scale: bool = ...

  """

  Use the same random seed for each scale axis for a uniform scale

  """

  vertex_group: str = ...

  """

  Vertex group name for modulating the deform

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class OpacityGpencilModifier(bpy_struct, GpencilModifier):

  """

  Opacity of Strokes modifier

  """

  curve: CurveMapping = ...

  """

  Custom curve to apply effect

  """

  factor: float = ...

  """

  Factor of Opacity

  """

  hardness: float = ...

  """

  Factor of stroke hardness

  """

  invert_layer_pass: bool = ...

  """

  Inverse filter

  """

  invert_layers: bool = ...

  """

  Inverse filter

  """

  invert_material_pass: bool = ...

  """

  Inverse filter

  """

  invert_materials: bool = ...

  """

  Inverse filter

  """

  invert_vertex: bool = ...

  """

  Inverse filter

  """

  layer: str = ...

  """

  Layer name

  """

  layer_pass: int = ...

  """

  Layer pass index

  """

  material: Material = ...

  """

  Material used for filtering effect

  """

  modify_color: str = ...

  """

  Set what colors of the stroke are affected

  * ``BOTH``
Stroke and Fill -- Modify fill and stroke colors.

  * ``STROKE``
Stroke -- Modify stroke color only.

  * ``FILL``
Fill -- Modify fill color only.

  * ``HARDNESS``
Hardness -- Modify stroke hardness.

  """

  pass_index: int = ...

  """

  Pass index

  """

  use_custom_curve: bool = ...

  """

  Use a custom curve to define opacity effect along the strokes

  """

  use_normalized_opacity: bool = ...

  """

  Replace the stroke opacity

  """

  use_weight_factor: bool = ...

  """

  Use weight to modulate effect

  """

  vertex_group: str = ...

  """

  Vertex group name for modulating the deform

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SimplifyGpencilModifier(bpy_struct, GpencilModifier):

  """

  Simplify Stroke modifier

  """

  distance: float = ...

  """

  Distance between points

  """

  factor: float = ...

  """

  Factor of Simplify

  """

  invert_layer_pass: bool = ...

  """

  Inverse filter

  """

  invert_layers: bool = ...

  """

  Inverse filter

  """

  invert_material_pass: bool = ...

  """

  Inverse filter

  """

  invert_materials: bool = ...

  """

  Inverse filter

  """

  layer: str = ...

  """

  Layer name

  """

  layer_pass: int = ...

  """

  Layer pass index

  """

  length: float = ...

  """

  Length of each segment

  """

  material: Material = ...

  """

  Material used for filtering effect

  """

  mode: str = ...

  """

  How to simplify the stroke

  * ``FIXED``
Fixed -- Delete alternating vertices in the stroke, except extremes.

  * ``ADAPTIVE``
Adaptive -- Use a Ramer-Douglas-Peucker algorithm to simplify the stroke preserving main shape.

  * ``SAMPLE``
Sample -- Re-sample the stroke with segments of the specified length.

  * ``MERGE``
Merge -- Simplify the stroke by merging vertices closer than a given distance.

  """

  pass_index: int = ...

  """

  Pass index

  """

  step: int = ...

  """

  Number of times to apply simplify

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SmoothGpencilModifier(bpy_struct, GpencilModifier):

  """

  Smooth effect modifier

  """

  curve: CurveMapping = ...

  """

  Custom curve to apply effect

  """

  factor: float = ...

  """

  Amount of smooth to apply

  """

  invert_layer_pass: bool = ...

  """

  Inverse filter

  """

  invert_layers: bool = ...

  """

  Inverse filter

  """

  invert_material_pass: bool = ...

  """

  Inverse filter

  """

  invert_materials: bool = ...

  """

  Inverse filter

  """

  invert_vertex: bool = ...

  """

  Inverse filter

  """

  layer: str = ...

  """

  Layer name

  """

  layer_pass: int = ...

  """

  Layer pass index

  """

  material: Material = ...

  """

  Material used for filtering effect

  """

  pass_index: int = ...

  """

  Pass index

  """

  step: int = ...

  """

  Number of times to apply smooth (high numbers can reduce fps)

  """

  use_custom_curve: bool = ...

  """

  Use a custom curve to define smooth effect along the strokes

  """

  use_edit_position: bool = ...

  """

  The modifier affects the position of the point

  """

  use_edit_strength: bool = ...

  """

  The modifier affects the color strength of the point

  """

  use_edit_thickness: bool = ...

  """

  The modifier affects the thickness of the point

  """

  use_edit_uv: bool = ...

  """

  The modifier affects the UV rotation factor of the point

  """

  vertex_group: str = ...

  """

  Vertex group name for modulating the deform

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class SubdivGpencilModifier(bpy_struct, GpencilModifier):

  """

  Subdivide Stroke modifier

  """

  invert_layer_pass: bool = ...

  """

  Inverse filter

  """

  invert_layers: bool = ...

  """

  Inverse filter

  """

  invert_material_pass: bool = ...

  """

  Inverse filter

  """

  invert_materials: bool = ...

  """

  Inverse filter

  """

  layer: str = ...

  """

  Layer name

  """

  layer_pass: int = ...

  """

  Layer pass index

  """

  level: int = ...

  """

  Number of subdivisions

  """

  material: Material = ...

  """

  Material used for filtering effect

  """

  pass_index: int = ...

  """

  Pass index

  """

  subdivision_type: str = ...

  """

  Select type of subdivision algorithm

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class TextureGpencilModifier(bpy_struct, GpencilModifier):

  """

  Transform stroke texture coordinates Modifier

  """

  alignment_rotation: float = ...

  """

  Additional rotation applied to dots and square strokes

  """

  fill_offset: typing.Tuple[float, float] = ...

  """

  Additional offset of the fill UV

  """

  fill_rotation: float = ...

  """

  Additional rotation of the fill UV

  """

  fill_scale: float = ...

  """

  Additional scale of the fill UV

  """

  fit_method: str = ...

  """

  * ``CONSTANT_LENGTH``
Constant Length -- Keep the texture at a constant length regardless of the length of each stroke.

  * ``FIT_STROKE``
Stroke Length -- Scale the texture to fit the length of each stroke.

  """

  invert_layer_pass: bool = ...

  """

  Inverse filter

  """

  invert_layers: bool = ...

  """

  Inverse filter

  """

  invert_material_pass: bool = ...

  """

  Inverse filter

  """

  invert_materials: bool = ...

  """

  Inverse filter

  """

  invert_vertex: bool = ...

  """

  Inverse filter

  """

  layer: str = ...

  """

  Layer name

  """

  layer_pass: int = ...

  """

  Layer pass index

  """

  material: Material = ...

  """

  Material used for filtering effect

  """

  mode: str = ...

  """

  * ``STROKE``
Stroke -- Manipulate only stroke texture coordinates.

  * ``FILL``
Fill -- Manipulate only fill texture coordinates.

  * ``STROKE_AND_FILL``
Stroke and Fill -- Manipulate both stroke and fill texture coordinates.

  """

  pass_index: int = ...

  """

  Pass index

  """

  uv_offset: float = ...

  """

  Offset value to add to stroke UVs

  """

  uv_scale: float = ...

  """

  Factor to scale the UVs

  """

  vertex_group: str = ...

  """

  Vertex group name for modulating the deform

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class ThickGpencilModifier(bpy_struct, GpencilModifier):

  """

  Subdivide and Smooth Stroke modifier

  """

  curve: CurveMapping = ...

  """

  Custom curve to apply effect

  """

  invert_layer_pass: bool = ...

  """

  Inverse filter

  """

  invert_layers: bool = ...

  """

  Inverse filter

  """

  invert_material_pass: bool = ...

  """

  Inverse filter

  """

  invert_materials: bool = ...

  """

  Inverse filter

  """

  invert_vertex: bool = ...

  """

  Inverse filter

  """

  layer: str = ...

  """

  Layer name

  """

  layer_pass: int = ...

  """

  Layer pass index

  """

  material: Material = ...

  """

  Material used for filtering effect

  """

  pass_index: int = ...

  """

  Pass index

  """

  thickness: int = ...

  """

  Absolute thickness to apply everywhere

  """

  thickness_factor: float = ...

  """

  Factor to multiply the thickness with

  """

  use_custom_curve: bool = ...

  """

  Use a custom curve to define thickness change along the strokes

  """

  use_normalized_thickness: bool = ...

  """

  Replace the stroke thickness

  """

  use_weight_factor: bool = ...

  """

  Use weight to modulate effect

  """

  vertex_group: str = ...

  """

  Vertex group name for modulating the deform

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class TimeGpencilModifier(bpy_struct, GpencilModifier):

  """

  Time offset modifier

  """

  frame_end: int = ...

  """

  Final frame of the range

  """

  frame_scale: float = ...

  """

  Evaluation time in seconds

  """

  frame_start: int = ...

  """

  First frame of the range

  """

  invert_layer_pass: bool = ...

  """

  Inverse filter

  """

  invert_layers: bool = ...

  """

  Inverse filter

  """

  layer: str = ...

  """

  Layer name

  """

  layer_pass: int = ...

  """

  Layer pass index

  """

  mode: str = ...

  """

  * ``NORMAL``
Regular -- Apply offset in usual animation direction.

  * ``REVERSE``
Reverse -- Apply offset in reverse animation direction.

  * ``FIX``
Fixed Frame -- Keep frame and do not change with time.

  """

  offset: int = ...

  """

  Number of frames to offset original keyframe number or frame to fix

  """

  use_custom_frame_range: bool = ...

  """

  Define a custom range of frames to use in modifier

  """

  use_keep_loop: bool = ...

  """

  Retiming end frames and move to start of animation to keep loop

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class TintGpencilModifier(bpy_struct, GpencilModifier):

  """

  Tint modifier

  """

  color: typing.Tuple[float, float, float] = ...

  """

  Color used for tinting

  """

  colors: ColorRamp = ...

  """

  Color ramp used to define tinting colors

  """

  curve: CurveMapping = ...

  """

  Custom curve to apply effect

  """

  factor: float = ...

  """

  Factor for tinting

  """

  invert_layer_pass: bool = ...

  """

  Inverse filter

  """

  invert_layers: bool = ...

  """

  Inverse filter

  """

  invert_material_pass: bool = ...

  """

  Inverse filter

  """

  invert_materials: bool = ...

  """

  Inverse filter

  """

  invert_vertex: bool = ...

  """

  Inverse filter

  """

  layer: str = ...

  """

  Layer name

  """

  layer_pass: int = ...

  """

  Layer pass index

  """

  material: Material = ...

  """

  Material used for filtering effect

  """

  object: Object = ...

  """

  Parent object to define the center of the effect

  """

  pass_index: int = ...

  """

  Pass index

  """

  radius: float = ...

  """

  Defines the maximum distance of the effect

  """

  tint_type: str = ...

  """

  Select type of tinting algorithm

  """

  use_custom_curve: bool = ...

  """

  Use a custom curve to define vertex color effect along the strokes

  """

  use_weight_factor: bool = ...

  """

  Use weight to modulate effect

  """

  vertex_group: str = ...

  """

  Vertex group name for modulating the deform

  """

  vertex_mode: str = ...

  """

  Defines how vertex color affect to the strokes

  * ``STROKE``
Stroke -- Vertex Color affects to Stroke only.

  * ``FILL``
Fill -- Vertex Color affects to Fill only.

  * ``BOTH``
Stroke and Fill -- Vertex Color affects to Stroke and Fill.

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class WeightAngleGpencilModifier(bpy_struct, GpencilModifier):

  """

  Calculate Vertex Weight dynamically

  """

  angle: float = ...

  """

  Angle

  """

  axis: str = ...

  invert_layer_pass: bool = ...

  """

  Inverse filter

  """

  invert_layers: bool = ...

  """

  Inverse filter

  """

  invert_material_pass: bool = ...

  """

  Inverse filter

  """

  invert_materials: bool = ...

  """

  Inverse filter

  """

  invert_vertex: bool = ...

  """

  Inverse filter

  """

  layer: str = ...

  """

  Layer name

  """

  layer_pass: int = ...

  """

  Layer pass index

  """

  material: Material = ...

  """

  Material used for filtering effect

  """

  minimum_weight: float = ...

  """

  Minimum value for vertex weight

  """

  pass_index: int = ...

  """

  Pass index

  """

  space: str = ...

  """

  Coordinates space

  """

  target_vertex_group: str = ...

  """

  Output Vertex group

  """

  use_invert_output: bool = ...

  """

  Invert output weight values

  """

  use_multiply: bool = ...

  """

  Multiply the calculated weights with the existing values in the vertex group

  """

  vertex_group: str = ...

  """

  Vertex group name for modulating the deform

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class WeightProxGpencilModifier(bpy_struct, GpencilModifier):

  """

  Calculate Vertex Weight dynamically

  """

  distance_end: float = ...

  """

  Distance mapping to 1.0 weight

  """

  distance_start: float = ...

  """

  Distance mapping to 0.0 weight

  """

  invert_layer_pass: bool = ...

  """

  Inverse filter

  """

  invert_layers: bool = ...

  """

  Inverse filter

  """

  invert_material_pass: bool = ...

  """

  Inverse filter

  """

  invert_materials: bool = ...

  """

  Inverse filter

  """

  invert_vertex: bool = ...

  """

  Inverse filter

  """

  layer: str = ...

  """

  Layer name

  """

  layer_pass: int = ...

  """

  Layer pass index

  """

  material: Material = ...

  """

  Material used for filtering effect

  """

  minimum_weight: float = ...

  """

  Minimum value for vertex weight

  """

  object: Object = ...

  """

  Object used as distance reference

  """

  pass_index: int = ...

  """

  Pass index

  """

  target_vertex_group: str = ...

  """

  Output Vertex group

  """

  use_invert_output: bool = ...

  """

  Invert output weight values

  """

  use_multiply: bool = ...

  """

  Multiply the calculated weights with the existing values in the vertex group

  """

  vertex_group: str = ...

  """

  Vertex group name for modulating the deform

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Action(ID, bpy_struct):

  """

  A collection of F-Curves for animation

  """

  fcurves: typing.Union[ActionFCurves, typing.Sequence[FCurve], typing.Mapping[str, FCurve], bpy_prop_collection] = ...

  """

  The individual F-Curves that make up the action

  """

  frame_range: typing.Tuple[float, float] = ...

  """

  The final frame range of all F-Curves within this action

  """

  groups: typing.Union[ActionGroups, typing.Sequence[ActionGroup], typing.Mapping[str, ActionGroup], bpy_prop_collection] = ...

  """

  Convenient groupings of F-Curves

  """

  id_root: str = ...

  """

  Type of ID block that action can be used on - DO NOT CHANGE UNLESS YOU KNOW WHAT YOU ARE DOING

  """

  pose_markers: typing.Union[ActionPoseMarkers, typing.Sequence[TimelineMarker], typing.Mapping[str, TimelineMarker], bpy_prop_collection] = ...

  """

  Markers specific to this action, for labeling poses

  """

  def flip_with_pose(self, object: Object) -> None:

    """

    Flip the action around the X axis using a pose

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Armature(ID, bpy_struct):

  """

  Armature data-block containing a hierarchy of bones, usually used for rigging characters

  """

  animation_data: AnimData = ...

  """

  Animation data for this data-block

  """

  axes_position: float = ...

  """

  The position for the axes on the bone. Increasing the value moves it closer to the tip; decreasing moves it closer to the root

  """

  bones: typing.Union[ArmatureBones, typing.Sequence[Bone], typing.Mapping[str, Bone], bpy_prop_collection] = ...

  display_type: str = ...

  """

  * ``OCTAHEDRAL``
Octahedral -- Display bones as octahedral shape (default).

  * ``STICK``
Stick -- Display bones as simple 2D lines with dots.

  * ``BBONE``
B-Bone -- Display bones as boxes, showing subdivision and B-Splines.

  * ``ENVELOPE``
Envelope -- Display bones as extruded spheres, showing deformation influence volume.

  * ``WIRE``
Wire -- Display bones as thin wires, showing subdivision and B-Splines.

  """

  edit_bones: typing.Union[ArmatureEditBones, typing.Sequence[EditBone], typing.Mapping[str, EditBone], bpy_prop_collection] = ...

  is_editmode: bool = ...

  """

  True when used in editmode

  """

  layers: typing.Tuple[bool, ...] = ...

  """

  Armature layer visibility

  """

  layers_protected: typing.Tuple[bool, ...] = ...

  """

  Protected layers in Proxy Instances are restored to Proxy settings on file reload and undo

  """

  pose_position: str = ...

  """

  Show armature in binding pose or final posed state

  * ``POSE``
Pose Position -- Show armature in posed state.

  * ``REST``
Rest Position -- Show Armature in binding pose state (no posing possible).

  """

  show_axes: bool = ...

  """

  Display bone axes

  """

  show_bone_custom_shapes: bool = ...

  """

  Display bones with their custom shapes

  """

  show_group_colors: bool = ...

  """

  Display bone group colors

  """

  show_names: bool = ...

  """

  Display bone names

  """

  use_mirror_x: bool = ...

  """

  Apply changes to matching bone on opposite side of X-Axis

  """

  def transform(self, matrix: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]]) -> None:

    """

    Transform armature bones by a matrix

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Brush(ID, bpy_struct):

  """

  Brush data-block for storing brush settings for painting and sculpting

  """

  area_radius_factor: float = ...

  """

  Ratio between the brush radius and the radius that is going to be used to sample the area center

  """

  auto_smooth_factor: float = ...

  """

  Amount of smoothing to automatically apply to each stroke

  """

  automasking_boundary_edges_propagation_steps: int = ...

  """

  Distance where boundary edge automasking is going to protect vertices from the fully masked edge

  """

  blend: str = ...

  """

  Brush blending mode

  * ``MIX``
Mix -- Use Mix blending mode while painting.

  * ``DARKEN``
Darken -- Use Darken blending mode while painting.

  * ``MUL``
Multiply -- Use Multiply blending mode while painting.

  * ``COLORBURN``
Color Burn -- Use Color Burn blending mode while painting.

  * ``LINEARBURN``
Linear Burn -- Use Linear Burn blending mode while painting.

  * ``LIGHTEN``
Lighten -- Use Lighten blending mode while painting.

  * ``SCREEN``
Screen -- Use Screen blending mode while painting.

  * ``COLORDODGE``
Color Dodge -- Use Color Dodge blending mode while painting.

  * ``ADD``
Add -- Use Add blending mode while painting.

  * ``OVERLAY``
Overlay -- Use Overlay blending mode while painting.

  * ``SOFTLIGHT``
Soft Light -- Use Soft Light blending mode while painting.

  * ``HARDLIGHT``
Hard Light -- Use Hard Light blending mode while painting.

  * ``VIVIDLIGHT``
Vivid Light -- Use Vivid Light blending mode while painting.

  * ``LINEARLIGHT``
Linear Light -- Use Linear Light blending mode while painting.

  * ``PINLIGHT``
Pin Light -- Use Pin Light blending mode while painting.

  * ``DIFFERENCE``
Difference -- Use Difference blending mode while painting.

  * ``EXCLUSION``
Exclusion -- Use Exclusion blending mode while painting.

  * ``SUB``
Subtract -- Use Subtract blending mode while painting.

  * ``HUE``
Hue -- Use Hue blending mode while painting.

  * ``SATURATION``
Saturation -- Use Saturation blending mode while painting.

  * ``COLOR``
Color -- Use Color blending mode while painting.

  * ``LUMINOSITY``
Value -- Use Value blending mode while painting.

  * ``ERASE_ALPHA``
Erase Alpha -- Erase alpha while painting.

  * ``ADD_ALPHA``
Add Alpha -- Add alpha while painting.

  """

  blur_kernel_radius: int = ...

  """

  Radius of kernel used for soften and sharpen in pixels

  """

  blur_mode: str = ...

  boundary_deform_type: str = ...

  """

  Deformation type that is used in the brush

  """

  boundary_falloff_type: str = ...

  """

  How the brush falloff is applied across the boundary

  * ``CONSTANT``
Constant -- Applies the same deformation in the entire boundary.

  * ``RADIUS``
Brush Radius -- Applies the deformation in a localized area limited by the brush radius.

  * ``LOOP``
Loop -- Applies the brush falloff in a loop pattern.

  * ``LOOP_INVERT``
Loop and Invert -- Applies the falloff radius in a loop pattern, inverting the displacement direction in each pattern repetition.

  """

  boundary_offset: float = ...

  """

  Offset of the boundary origin in relation to the brush radius

  """

  brush_capabilities: BrushCapabilities = ...

  """

  Brush's capabilities

  """

  clone_alpha: float = ...

  """

  Opacity of clone image display

  """

  clone_image: Image = ...

  """

  Image for clone tool

  """

  clone_offset: typing.Tuple[float, float] = ...

  cloth_constraint_softbody_strength: float = ...

  """

  How much the cloth preserves the original shape, acting as a soft body

  """

  cloth_damping: float = ...

  """

  How much the applied forces are propagated through the cloth

  """

  cloth_deform_type: str = ...

  """

  Deformation type that is used in the brush

  """

  cloth_force_falloff_type: str = ...

  """

  Shape used in the brush to apply force to the cloth

  """

  cloth_mass: float = ...

  """

  Mass of each simulation particle

  """

  cloth_sim_falloff: float = ...

  """

  Area to apply deformation falloff to the effects of the simulation

  """

  cloth_sim_limit: float = ...

  """

  Factor added relative to the size of the radius to limit the cloth simulation effects

  """

  cloth_simulation_area_type: str = ...

  """

  Part of the mesh that is going to be simulated when the stroke is active

  * ``LOCAL``
Local -- Simulates only a specific area around the brush limited by a fixed radius.

  * ``GLOBAL``
Global -- Simulates the entire mesh.

  * ``DYNAMIC``
Dynamic -- The active simulation area moves with the brush.

  """

  color: typing.Tuple[float, float, float] = ...

  color_type: str = ...

  """

  Use single color or gradient when painting

  * ``COLOR``
Color -- Paint with a single color.

  * ``GRADIENT``
Gradient -- Paint with a gradient.

  """

  crease_pinch_factor: float = ...

  """

  How much the crease brush pinches

  """

  cursor_color_add: typing.Tuple[float, float, float, float] = ...

  """

  Color of cursor when adding

  """

  cursor_color_subtract: typing.Tuple[float, float, float, float] = ...

  """

  Color of cursor when subtracting

  """

  cursor_overlay_alpha: int = ...

  curve: CurveMapping = ...

  """

  Editable falloff curve

  """

  curve_preset: str = ...

  dash_ratio: float = ...

  """

  Ratio of samples in a cycle that the brush is enabled

  """

  dash_samples: int = ...

  """

  Length of a dash cycle measured in stroke samples

  """

  deform_target: str = ...

  """

  How the deformation of the brush will affect the object

  * ``GEOMETRY``
Geometry -- Brush deformation displaces the vertices of the mesh.

  * ``CLOTH_SIM``
Cloth Simulation -- Brush deforms the mesh by deforming the constraints of a cloth simulation.

  """

  density: float = ...

  """

  Amount of random elements that are going to be affected by the brush

  """

  direction: str = ...

  """

  * ``ADD``
Add -- Add effect of brush.

  * ``SUBTRACT``
Subtract -- Subtract effect of brush.

  """

  disconnected_distance_max: float = ...

  """

  Maximum distance to search for disconnected loose parts in the mesh

  """

  elastic_deform_type: str = ...

  """

  Deformation type that is used in the brush

  """

  elastic_deform_volume_preservation: float = ...

  """

  Poisson ratio for elastic deformation. Higher values preserve volume more, but also lead to more bulging

  """

  falloff_angle: float = ...

  """

  Paint most on faces pointing towards the view according to this angle

  """

  falloff_shape: str = ...

  """

  Use projected or spherical falloff

  * ``SPHERE``
Sphere -- Apply brush influence in a Sphere, outwards from the center.

  * ``PROJECTED``
Projected -- Apply brush influence in a 2D circle, projected from the view.

  """

  fill_threshold: float = ...

  """

  Threshold above which filling is not propagated

  """

  flow: float = ...

  """

  Amount of paint that is applied per stroke sample

  """

  gpencil_sculpt_tool: str = ...

  """

  * ``SMOOTH``
Smooth -- Smooth stroke points.

  * ``THICKNESS``
Thickness -- Adjust thickness of strokes.

  * ``STRENGTH``
Strength -- Adjust color strength of strokes.

  * ``RANDOMIZE``
Randomize -- Introduce jitter/randomness into strokes.

  * ``GRAB``
Grab -- Translate the set of points initially within the brush circle.

  * ``PUSH``
Push -- Move points out of the way, as if combing them.

  * ``TWIST``
Twist -- Rotate points around the midpoint of the brush.

  * ``PINCH``
Pinch -- Pull points towards the midpoint of the brush.

  * ``CLONE``
Clone -- Paste copies of the strokes stored on the clipboard.

  """

  gpencil_settings: BrushGpencilSettings = ...

  gpencil_tool: str = ...

  """

  * ``DRAW``
Draw -- The brush is of type used for drawing strokes.

  * ``FILL``
Fill -- The brush is of type used for filling areas.

  * ``ERASE``
Erase -- The brush is used for erasing strokes.

  * ``TINT``
Tint -- The brush is of type used for tinting strokes.

  """

  gpencil_vertex_tool: str = ...

  gpencil_weight_tool: str = ...

  """

  * ``WEIGHT``
Weight -- Weight Paint for Vertex Groups.

  """

  grad_spacing: int = ...

  """

  Spacing before brush gradient goes full circle

  """

  gradient: ColorRamp = ...

  gradient_fill_mode: str = ...

  gradient_stroke_mode: str = ...

  hardness: float = ...

  """

  How close the brush falloff starts from the edge of the brush

  """

  height: float = ...

  """

  Affectable height of brush (layer height for layer tool, i.e.)

  """

  icon_filepath: str = ...

  """

  File path to brush icon

  """

  image_paint_capabilities: BrushCapabilitiesImagePaint = ...

  image_tool: str = ...

  invert_density_pressure: bool = ...

  """

  Invert the modulation of pressure in density

  """

  invert_flow_pressure: bool = ...

  """

  Invert the modulation of pressure in flow

  """

  invert_hardness_pressure: bool = ...

  """

  Invert the modulation of pressure in hardness

  """

  invert_to_scrape_fill: bool = ...

  """

  Use Scrape or Fill tool when inverting this brush instead of inverting its displacement direction

  """

  invert_wet_mix_pressure: bool = ...

  """

  Invert the modulation of pressure in wet mix

  """

  invert_wet_persistence_pressure: bool = ...

  """

  Invert the modulation of pressure in wet persistence

  """

  jitter: float = ...

  """

  Jitter the position of the brush while painting

  """

  jitter_absolute: int = ...

  """

  Jitter the position of the brush in pixels while painting

  """

  jitter_unit: str = ...

  """

  Jitter in screen space or relative to brush size

  * ``VIEW``
View -- Jittering happens in screen space, in pixels.

  * ``BRUSH``
Brush -- Jittering happens relative to the brush size.

  """

  mask_overlay_alpha: int = ...

  mask_stencil_dimension: typing.Tuple[float, float] = ...

  """

  Dimensions of mask stencil in viewport

  """

  mask_stencil_pos: typing.Tuple[float, float] = ...

  """

  Position of mask stencil in viewport

  """

  mask_texture: Texture = ...

  mask_texture_slot: BrushTextureSlot = ...

  mask_tool: str = ...

  multiplane_scrape_angle: float = ...

  """

  Angle between the planes of the crease

  """

  normal_radius_factor: float = ...

  """

  Ratio between the brush radius and the radius that is going to be used to sample the normal

  """

  normal_weight: float = ...

  """

  How much grab will pull vertexes out of surface during a grab

  """

  paint_curve: PaintCurve = ...

  """

  Active paint curve

  """

  plane_offset: float = ...

  """

  Adjust plane on which the brush acts towards or away from the object surface

  """

  plane_trim: float = ...

  """

  If a vertex is further away from offset plane than this, then it is not affected

  """

  pose_deform_type: str = ...

  """

  Deformation type that is used in the brush

  """

  pose_ik_segments: int = ...

  """

  Number of segments of the inverse kinematics chain that will deform the mesh

  """

  pose_offset: float = ...

  """

  Offset of the pose origin in relation to the brush radius

  """

  pose_origin_type: str = ...

  """

  Method to set the rotation origins for the segments of the brush

  * ``TOPOLOGY``
Topology -- Sets the rotation origin automatically using the topology and shape of the mesh as a guide.

  * ``FACE_SETS``
Face Sets -- Creates a pose segment per face sets, starting from the active face set.

  * ``FACE_SETS_FK``
Face Sets FK -- Simulates an FK deformation using the Face Set under the cursor as control.

  """

  pose_smooth_iterations: int = ...

  """

  Smooth iterations applied after calculating the pose factor of each vertex

  """

  rake_factor: float = ...

  """

  How much grab will follow cursor rotation

  """

  rate: float = ...

  """

  Interval between paints for Airbrush

  """

  sculpt_capabilities: BrushCapabilitiesSculpt = ...

  sculpt_plane: str = ...

  sculpt_tool: str = ...

  secondary_color: typing.Tuple[float, float, float] = ...

  sharp_threshold: float = ...

  """

  Threshold below which, no sharpening is done

  """

  show_multiplane_scrape_planes_preview: bool = ...

  """

  Preview the scrape planes in the cursor during the stroke

  """

  size: int = ...

  """

  Radius of the brush in pixels

  """

  slide_deform_type: str = ...

  """

  Deformation type that is used in the brush

  """

  smear_deform_type: str = ...

  """

  Deformation type that is used in the brush

  """

  smooth_deform_type: str = ...

  """

  Deformation type that is used in the brush

  * ``LAPLACIAN``
Laplacian -- Smooths the surface and the volume.

  * ``SURFACE``
Surface -- Smooths the surface of the mesh, preserving the volume.

  """

  smooth_stroke_factor: float = ...

  """

  Higher values give a smoother stroke

  """

  smooth_stroke_radius: int = ...

  """

  Minimum distance from last point before stroke continues

  """

  snake_hook_deform_type: str = ...

  """

  Deformation type that is used in the brush

  * ``FALLOFF``
Radius Falloff -- Applies the brush falloff in the tip of the brush.

  * ``ELASTIC``
Elastic -- Modifies the entire mesh using elastic deform.

  """

  spacing: int = ...

  """

  Spacing between brush daubs as a percentage of brush diameter

  """

  stencil_dimension: typing.Tuple[float, float] = ...

  """

  Dimensions of stencil in viewport

  """

  stencil_pos: typing.Tuple[float, float] = ...

  """

  Position of stencil in viewport

  """

  strength: float = ...

  """

  How powerful the effect of the brush is when applied

  """

  stroke_method: str = ...

  """

  * ``DOTS``
Dots -- Apply paint on each mouse move step.

  * ``DRAG_DOT``
Drag Dot -- Allows a single dot to be carefully positioned.

  * ``SPACE``
Space -- Limit brush application to the distance specified by spacing.

  * ``AIRBRUSH``
Airbrush -- Keep applying paint effect while holding mouse (spray).

  * ``ANCHORED``
Anchored -- Keep the brush anchored to the initial location.

  * ``LINE``
Line -- Draw a line with dabs separated according to spacing.

  * ``CURVE``
Curve -- Define the stroke curve with a bezier curve (dabs are separated according to spacing).

  """

  surface_smooth_current_vertex: float = ...

  """

  How much the position of each individual vertex influences the final result

  """

  surface_smooth_iterations: int = ...

  """

  Number of smoothing iterations per brush step

  """

  surface_smooth_shape_preservation: float = ...

  """

  How much of the original shape is preserved when smoothing

  """

  texture: Texture = ...

  texture_overlay_alpha: int = ...

  texture_sample_bias: float = ...

  """

  Value added to texture samples

  """

  texture_slot: BrushTextureSlot = ...

  tilt_strength_factor: float = ...

  """

  How much the tilt of the pen will affect the brush

  """

  tip_roundness: float = ...

  """

  Roundness of the brush tip

  """

  tip_scale_x: float = ...

  """

  Scale of the brush tip in the X axis

  """

  topology_rake_factor: float = ...

  """

  Automatically align edges to the brush direction to generate cleaner topology and define sharp features. Best used on low-poly meshes as it has a performance impact

  """

  unprojected_radius: float = ...

  """

  Radius of brush in Blender units

  """

  use_accumulate: bool = ...

  """

  Accumulate stroke daubs on top of each other

  """

  use_adaptive_space: bool = ...

  """

  Space daubs according to surface orientation instead of screen space

  """

  use_airbrush: bool = ...

  """

  Keep applying paint effect while holding mouse (spray)

  """

  use_alpha: bool = ...

  """

  When this is disabled, lock alpha while painting

  """

  use_anchor: bool = ...

  """

  Keep the brush anchored to the initial location

  """

  use_automasking_boundary_edges: bool = ...

  """

  Do not affect non manifold boundary edges

  """

  use_automasking_boundary_face_sets: bool = ...

  """

  Do not affect vertices that belong to a Face Set boundary

  """

  use_automasking_face_sets: bool = ...

  """

  Affect only vertices that share Face Sets with the active vertex

  """

  use_automasking_topology: bool = ...

  """

  Affect only vertices connected to the active vertex under the brush

  """

  use_cloth_collision: bool = ...

  """

  Collide with objects during the simulation

  """

  use_cloth_pin_simulation_boundary: bool = ...

  """

  Lock the position of the vertices in the simulation falloff area to avoid artifacts and create a softer transition with unaffected areas

  """

  use_connected_only: bool = ...

  """

  Affect only topologically connected elements

  """

  use_cursor_overlay: bool = ...

  """

  Show cursor in viewport

  """

  use_cursor_overlay_override: bool = ...

  """

  Don't show overlay during a stroke

  """

  use_curve: bool = ...

  """

  Define the stroke curve with a bezier curve. Dabs are separated according to spacing

  """

  use_custom_icon: bool = ...

  """

  Set the brush icon from an image file

  """

  use_density_pressure: bool = ...

  """

  Use pressure to modulate density

  """

  use_edge_to_edge: bool = ...

  """

  Drag anchor brush from edge-to-edge

  """

  use_flow_pressure: bool = ...

  """

  Use pressure to modulate flow

  """

  use_frontface: bool = ...

  """

  Brush only affects vertexes that face the viewer

  """

  use_frontface_falloff: bool = ...

  """

  Blend brush influence by how much they face the front

  """

  use_grab_active_vertex: bool = ...

  """

  Apply the maximum grab strength to the active vertex instead of the cursor location

  """

  use_grab_silhouette: bool = ...

  """

  Grabs trying to automask the silhouette of the object

  """

  use_hardness_pressure: bool = ...

  """

  Use pressure to modulate hardness

  """

  use_inverse_smooth_pressure: bool = ...

  """

  Lighter pressure causes more smoothing to be applied

  """

  use_line: bool = ...

  """

  Draw a line with dabs separated according to spacing

  """

  use_locked_size: str = ...

  """

  Measure brush size relative to the view or the scene

  * ``VIEW``
View -- Measure brush size relative to the view.

  * ``SCENE``
Scene -- Measure brush size relative to the scene.

  """

  use_multiplane_scrape_dynamic: bool = ...

  """

  The angle between the planes changes during the stroke to fit the surface under the cursor

  """

  use_offset_pressure: bool = ...

  """

  Enable tablet pressure sensitivity for offset

  """

  use_original_normal: bool = ...

  """

  When locked keep using normal of surface where stroke was initiated

  """

  use_original_plane: bool = ...

  """

  When locked keep using the plane origin of surface where stroke was initiated

  """

  use_paint_antialiasing: bool = ...

  """

  Smooths the edges of the strokes

  """

  use_paint_grease_pencil: bool = ...

  """

  Use this brush in grease pencil drawing mode

  """

  use_paint_image: bool = ...

  """

  Use this brush in texture paint mode

  """

  use_paint_sculpt: bool = ...

  """

  Use this brush in sculpt mode

  """

  use_paint_uv_sculpt: bool = ...

  """

  Use this brush in UV sculpt mode

  """

  use_paint_vertex: bool = ...

  """

  Use this brush in vertex paint mode

  """

  use_paint_weight: bool = ...

  """

  Use this brush in weight paint mode

  """

  use_persistent: bool = ...

  """

  Sculpt on a persistent layer of the mesh

  """

  use_plane_trim: bool = ...

  """

  Enable Plane Trim

  """

  use_pose_ik_anchored: bool = ...

  """

  Keep the position of the last segment in the IK chain fixed

  """

  use_pose_lock_rotation: bool = ...

  """

  Do not rotate the segment when using the scale deform mode

  """

  use_pressure_area_radius: bool = ...

  """

  Enable tablet pressure sensitivity for area radius

  """

  use_pressure_jitter: bool = ...

  """

  Enable tablet pressure sensitivity for jitter

  """

  use_pressure_masking: str = ...

  """

  Pen pressure makes texture influence smaller

  """

  use_pressure_size: bool = ...

  """

  Enable tablet pressure sensitivity for size

  """

  use_pressure_spacing: bool = ...

  """

  Enable tablet pressure sensitivity for spacing

  """

  use_pressure_strength: bool = ...

  """

  Enable tablet pressure sensitivity for strength

  """

  use_primary_overlay: bool = ...

  """

  Show texture in viewport

  """

  use_primary_overlay_override: bool = ...

  """

  Don't show overlay during a stroke

  """

  use_restore_mesh: bool = ...

  """

  Allow a single dot to be carefully positioned

  """

  use_scene_spacing: str = ...

  """

  Calculate the brush spacing using view or scene distance

  * ``VIEW``
View -- Calculate brush spacing relative to the view.

  * ``SCENE``
Scene -- Calculate brush spacing relative to the scene using the stroke location.

  """

  use_secondary_overlay: bool = ...

  """

  Show texture in viewport

  """

  use_secondary_overlay_override: bool = ...

  """

  Don't show overlay during a stroke

  """

  use_smooth_stroke: bool = ...

  """

  Brush lags behind mouse and follows a smoother path

  """

  use_space: bool = ...

  """

  Limit brush application to the distance specified by spacing

  """

  use_space_attenuation: bool = ...

  """

  Automatically adjust strength to give consistent results for different spacings

  """

  use_vertex_grease_pencil: bool = ...

  """

  Use this brush in grease pencil vertex color mode

  """

  use_wet_mix_pressure: bool = ...

  """

  Use pressure to modulate wet mix

  """

  use_wet_persistence_pressure: bool = ...

  """

  Use pressure to modulate wet persistence

  """

  uv_sculpt_tool: str = ...

  """

  * ``GRAB``
Grab -- Grab UVs.

  * ``RELAX``
Relax -- Relax UVs.

  * ``PINCH``
Pinch -- Pinch UVs.

  """

  vertex_paint_capabilities: BrushCapabilitiesVertexPaint = ...

  vertex_tool: str = ...

  weight: float = ...

  """

  Vertex weight when brush is applied

  """

  weight_paint_capabilities: BrushCapabilitiesWeightPaint = ...

  weight_tool: str = ...

  wet_mix: float = ...

  """

  Amount of paint that is picked from the surface into the brush color

  """

  wet_paint_radius_factor: float = ...

  """

  Ratio between the brush radius and the radius that is going to be used to sample the color to blend in wet paint

  """

  wet_persistence: float = ...

  """

  Amount of wet paint that stays in the brush after applying paint to the surface

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class CacheFile(ID, bpy_struct):

  animation_data: AnimData = ...

  """

  Animation data for this data-block

  """

  filepath: str = ...

  """

  Path to external displacements file

  """

  forward_axis: str = ...

  frame: float = ...

  """

  The time to use for looking up the data in the cache file, or to determine which file to use in a file sequence

  """

  frame_offset: float = ...

  """

  Subtracted from the current frame to use for looking up the data in the cache file, or to determine which file to use in a file sequence

  """

  is_sequence: bool = ...

  """

  Whether the cache is separated in a series of files

  """

  object_paths: typing.Union[CacheObjectPaths, typing.Sequence[CacheObjectPath], typing.Mapping[str, CacheObjectPath], bpy_prop_collection] = ...

  """

  Paths of the objects inside the Alembic archive

  """

  override_frame: bool = ...

  """

  Whether to use a custom frame for looking up data in the cache file, instead of using the current scene frame

  """

  prefetch_cache_size: int = ...

  """

  Memory usage limit in megabytes for the Cycles Procedural cache, if the data does not fit within the limit, rendering is aborted

  """

  scale: float = ...

  """

  Value by which to enlarge or shrink the object with respect to the world's origin (only applicable through a Transform Cache constraint)

  """

  up_axis: str = ...

  use_prefetch: bool = ...

  """

  When enabled, the Cycles Procedural will preload animation data for faster updates

  """

  use_render_procedural: bool = ...

  """

  Display boxes in the viewport as placeholders for the objects, Cycles will use a procedural to load the objects during viewport rendering in experimental mode, other render engines will also receive a placeholder and should take care of loading the Alembic data themselves if possible

  """

  velocity_name: str = ...

  """

  Name of the Alembic attribute used for generating motion blur data

  """

  velocity_unit: str = ...

  """

  Define how the velocity vectors are interpreted with regard to time, 'frame' means the delta time is 1 frame, 'second' means the delta time is 1 / FPS

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Camera(ID, bpy_struct):

  """

  Camera data-block for storing camera settings

  """

  angle: float = ...

  """

  Camera lens field of view

  """

  angle_x: float = ...

  """

  Camera lens horizontal field of view

  """

  angle_y: float = ...

  """

  Camera lens vertical field of view

  """

  animation_data: AnimData = ...

  """

  Animation data for this data-block

  """

  background_images: typing.Union[CameraBackgroundImages, typing.Sequence[CameraBackgroundImage], typing.Mapping[str, CameraBackgroundImage], bpy_prop_collection] = ...

  """

  List of background images

  """

  clip_end: float = ...

  """

  Camera far clipping distance

  """

  clip_start: float = ...

  """

  Camera near clipping distance

  """

  cycles: CyclesCameraSettings = ...

  """

  Cycles camera settings

  """

  display_size: float = ...

  """

  Apparent size of the Camera object in the 3D View

  """

  dof: CameraDOFSettings = ...

  lens: float = ...

  """

  Perspective Camera lens value in millimeters

  """

  lens_unit: str = ...

  """

  Unit to edit lens in for the user interface

  * ``MILLIMETERS``
Millimeters -- Specify the lens in millimeters.

  * ``FOV``
Field of View -- Specify the lens as the field of view's angle.

  """

  ortho_scale: float = ...

  """

  Orthographic Camera scale (similar to zoom)

  """

  passepartout_alpha: float = ...

  """

  Opacity (alpha) of the darkened overlay in Camera view

  """

  sensor_fit: str = ...

  """

  Method to fit image and field of view angle inside the sensor

  * ``AUTO``
Auto -- Fit to the sensor width or height depending on image resolution.

  * ``HORIZONTAL``
Horizontal -- Fit to the sensor width.

  * ``VERTICAL``
Vertical -- Fit to the sensor height.

  """

  sensor_height: float = ...

  """

  Vertical size of the image sensor area in millimeters

  """

  sensor_width: float = ...

  """

  Horizontal size of the image sensor area in millimeters

  """

  shift_x: float = ...

  """

  Camera horizontal shift

  """

  shift_y: float = ...

  """

  Camera vertical shift

  """

  show_background_images: bool = ...

  """

  Display reference images behind objects in the 3D View

  """

  show_composition_center: bool = ...

  """

  Display center composition guide inside the camera view

  """

  show_composition_center_diagonal: bool = ...

  """

  Display diagonal center composition guide inside the camera view

  """

  show_composition_golden: bool = ...

  """

  Display golden ratio composition guide inside the camera view

  """

  show_composition_golden_tria_a: bool = ...

  """

  Display golden triangle A composition guide inside the camera view

  """

  show_composition_golden_tria_b: bool = ...

  """

  Display golden triangle B composition guide inside the camera view

  """

  show_composition_harmony_tri_a: bool = ...

  """

  Display harmony A composition guide inside the camera view

  """

  show_composition_harmony_tri_b: bool = ...

  """

  Display harmony B composition guide inside the camera view

  """

  show_composition_thirds: bool = ...

  """

  Display rule of thirds composition guide inside the camera view

  """

  show_limits: bool = ...

  """

  Display the clipping range and focus point on the camera

  """

  show_mist: bool = ...

  """

  Display a line from the Camera to indicate the mist area

  """

  show_name: bool = ...

  """

  Show the active Camera's name in Camera view

  """

  show_passepartout: bool = ...

  """

  Show a darkened overlay outside the image area in Camera view

  """

  show_safe_areas: bool = ...

  """

  Show TV title safe and action safe areas in Camera view

  """

  show_safe_center: bool = ...

  """

  Show safe areas to fit content in a different aspect ratio

  """

  show_sensor: bool = ...

  """

  Show sensor size (film gate) in Camera view

  """

  stereo: CameraStereoData = ...

  type: str = ...

  """

  Camera types

  """

  def view_frame(self, scene: Scene = None) -> None:

    """

    Return 4 points for the cameras frame (before object transformation)

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Collection(ID, bpy_struct):

  """

  Collection of Object data-blocks

  """

  all_objects: typing.Union[typing.Sequence[Object], typing.Mapping[str, Object], bpy_prop_collection] = ...

  """

  Objects that are in this collection and its child collections

  """

  children: typing.Union[CollectionChildren, typing.Sequence[Collection], typing.Mapping[str, Collection], bpy_prop_collection] = ...

  """

  Collections that are immediate children of this collection

  """

  color_tag: str = ...

  """

  Color tag for a collection

  * ``NONE``
None -- Assign no color tag to the collection.

  * ``COLOR_01``
Color 01.

  * ``COLOR_02``
Color 02.

  * ``COLOR_03``
Color 03.

  * ``COLOR_04``
Color 04.

  * ``COLOR_05``
Color 05.

  * ``COLOR_06``
Color 06.

  * ``COLOR_07``
Color 07.

  * ``COLOR_08``
Color 08.

  """

  hide_render: bool = ...

  """

  Globally disable in renders

  """

  hide_select: bool = ...

  """

  Disable selection in viewport

  """

  hide_viewport: bool = ...

  """

  Globally disable in viewports

  """

  instance_offset: typing.Tuple[float, float, float] = ...

  """

  Offset from the origin to use when instancing

  """

  lineart_intersection_mask: typing.Tuple[bool, ...] = ...

  """

  Intersection generated by this collection will have this mask value

  """

  lineart_usage: str = ...

  """

  How to use this collection in line art

  * ``INCLUDE``
Include -- Generate feature lines for this collection.

  * ``OCCLUSION_ONLY``
Occlusion Only -- Only use the collection to produce occlusion.

  * ``EXCLUDE``
Exclude -- Don't use this collection in line art.

  * ``INTERSECTION_ONLY``
Intersection Only -- Only generate intersection lines for this collection.

  * ``NO_INTERSECTION``
No Intersection -- Include this collection but do not generate intersection lines.

  """

  lineart_use_intersection_mask: bool = ...

  """

  Use custom intersection mask for faces in this collection

  """

  objects: typing.Union[CollectionObjects, typing.Sequence[Object], typing.Mapping[str, Object], bpy_prop_collection] = ...

  """

  Objects that are directly in this collection

  """

  users_dupli_group: typing.Any = ...

  """

  The collection instance objects this collection is used in

  (readonly)

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Curve(ID):

  """

  Curve data-block storing curves, splines and NURBS

  """

  animation_data: AnimData = ...

  """

  Animation data for this data-block

  """

  bevel_depth: float = ...

  """

  Radius of the bevel geometry, not including extrusion

  """

  bevel_factor_end: float = ...

  """

  Define where along the spline the curve geometry ends (0 for the beginning, 1 for the end)

  """

  bevel_factor_mapping_end: str = ...

  """

  Determine how the geometry end factor is mapped to a spline

  * ``RESOLUTION``
Resolution -- Map the geometry factor to the number of subdivisions of a spline (U resolution).

  * ``SEGMENTS``
Segments -- Map the geometry factor to the length of a segment and to the number of subdivisions of a segment.

  * ``SPLINE``
Spline -- Map the geometry factor to the length of a spline.

  """

  bevel_factor_mapping_start: str = ...

  """

  Determine how the geometry start factor is mapped to a spline

  * ``RESOLUTION``
Resolution -- Map the geometry factor to the number of subdivisions of a spline (U resolution).

  * ``SEGMENTS``
Segments -- Map the geometry factor to the length of a segment and to the number of subdivisions of a segment.

  * ``SPLINE``
Spline -- Map the geometry factor to the length of a spline.

  """

  bevel_factor_start: float = ...

  """

  Define where along the spline the curve geometry starts (0 for the beginning, 1 for the end)

  """

  bevel_mode: str = ...

  """

  Determine how to build the curve's bevel geometry

  * ``ROUND``
Round -- Use circle for the section of the curve's bevel geometry.

  * ``OBJECT``
Object -- Use an object for the section of the curve's bevel geometry segment.

  * ``PROFILE``
Profile -- Use a custom profile for each quarter of curve's bevel geometry.

  """

  bevel_object: Object = ...

  """

  The name of the Curve object that defines the bevel shape

  """

  bevel_profile: CurveProfile = ...

  """

  The path for the curve's custom profile

  """

  bevel_resolution: int = ...

  """

  The number of segments in each quarter-circle of the bevel

  """

  cycles: CyclesMeshSettings = ...

  """

  Cycles mesh settings

  """

  dimensions: str = ...

  """

  Select 2D or 3D curve type

  * ``2D``
2D -- Clamp the Z axis of the curve.

  * ``3D``
3D -- Allow editing on the Z axis of this curve, also allows tilt and curve radius to be used.

  """

  eval_time: float = ...

  """

  Parametric position along the length of the curve that Objects 'following' it should be at (position is evaluated by dividing by the 'Path Length' value)

  """

  extrude: float = ...

  """

  Length of the depth added in the local Z direction along the curve, perpendicular to its normals

  """

  fill_mode: str = ...

  """

  Mode of filling curve

  """

  is_editmode: bool = ...

  """

  True when used in editmode

  """

  materials: typing.Union[IDMaterials, typing.Sequence[Material], typing.Mapping[str, Material], bpy_prop_collection] = ...

  offset: float = ...

  """

  Distance to move the curve parallel to its normals

  """

  path_duration: int = ...

  """

  The number of frames that are needed to traverse the path, defining the maximum value for the 'Evaluation Time' setting

  """

  render_resolution_u: int = ...

  """

  Surface resolution in U direction used while rendering (zero uses preview resolution)

  """

  render_resolution_v: int = ...

  """

  Surface resolution in V direction used while rendering (zero uses preview resolution)

  """

  resolution_u: int = ...

  """

  Number of computed points in the U direction between every pair of control points

  """

  resolution_v: int = ...

  """

  The number of computed points in the V direction between every pair of control points

  """

  shape_keys: Key = ...

  splines: typing.Union[CurveSplines, typing.Sequence[Spline], typing.Mapping[str, Spline], bpy_prop_collection] = ...

  """

  Collection of splines in this curve data object

  """

  taper_object: Object = ...

  """

  Curve object name that defines the taper (width)

  """

  taper_radius_mode: str = ...

  """

  Determine how the effective radius of the spline point is computed when a taper object is specified

  * ``OVERRIDE``
Override -- Override the radius of the spline point with the taper radius.

  * ``MULTIPLY``
Multiply -- Multiply the radius of the spline point by the taper radius.

  * ``ADD``
Add -- Add the radius of the bevel point to the taper radius.

  """

  texspace_location: typing.Tuple[float, float, float] = ...

  texspace_size: typing.Tuple[float, float, float] = ...

  twist_mode: str = ...

  """

  The type of tilt calculation for 3D Curves

  * ``Z_UP``
Z-Up -- Use Z-Up axis to calculate the curve twist at each point.

  * ``MINIMUM``
Minimum -- Use the least twist over the entire curve.

  * ``TANGENT``
Tangent -- Use the tangent to calculate twist.

  """

  twist_smooth: float = ...

  """

  Smoothing iteration for tangents

  """

  use_auto_texspace: bool = ...

  """

  Adjust active object's texture space automatically when transforming object

  """

  use_deform_bounds: bool = ...

  """

  Option for curve-deform: Use the mesh bounds to clamp the deformation

  """

  use_fill_caps: bool = ...

  """

  Fill caps for beveled curves

  """

  use_map_taper: bool = ...

  """

  Map effect of the taper object to the beveled part of the curve

  """

  use_path: bool = ...

  """

  Enable the curve to become a translation path

  """

  use_path_clamp: bool = ...

  """

  Clamp the curve path children so they can't travel past the start/end point of the curve

  """

  use_path_follow: bool = ...

  """

  Make curve path children to rotate along the path

  """

  use_radius: bool = ...

  """

  Option for paths and curve-deform: apply the curve radius with path following it and deforming

  """

  use_stretch: bool = ...

  """

  Option for curve-deform: make deformed child to stretch along entire path

  """

  def transform(self, matrix: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]], shape_keys: bool = False) -> None:

    """

    Transform curve by a matrix

    """

    ...

  def validate_material_indices(self) -> bool:

    """

    Validate material indices of splines or letters, return True when the curve has had invalid indices corrected (to default 0)

    """

    ...

  def update_gpu_tag(self) -> None:

    """

    update_gpu_tag

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class FreestyleLineStyle(ID, bpy_struct):

  """

  Freestyle line style, reusable by multiple line sets

  """

  active_texture: Texture = ...

  """

  Active texture slot being displayed

  """

  active_texture_index: int = ...

  """

  Index of active texture slot

  """

  alpha: float = ...

  """

  Base alpha transparency, possibly modified by alpha transparency modifiers

  """

  alpha_modifiers: typing.Union[LineStyleAlphaModifiers, typing.Sequence[LineStyleAlphaModifier], typing.Mapping[str, LineStyleAlphaModifier], bpy_prop_collection] = ...

  """

  List of alpha transparency modifiers

  """

  angle_max: float = ...

  """

  Maximum 2D angle for splitting chains

  """

  angle_min: float = ...

  """

  Minimum 2D angle for splitting chains

  """

  animation_data: AnimData = ...

  """

  Animation data for this data-block

  """

  caps: str = ...

  """

  Select the shape of both ends of strokes

  * ``BUTT``
Butt -- Butt cap (flat).

  * ``ROUND``
Round -- Round cap (half-circle).

  * ``SQUARE``
Square -- Square cap (flat and extended).

  """

  chain_count: int = ...

  """

  Chain count for the selection of first N chains

  """

  chaining: str = ...

  """

  Select the way how feature edges are jointed to form chains

  * ``PLAIN``
Plain -- Plain chaining.

  * ``SKETCHY``
Sketchy -- Sketchy chaining with a multiple touch.

  """

  color: typing.Tuple[float, float, float] = ...

  """

  Base line color, possibly modified by line color modifiers

  """

  color_modifiers: typing.Union[LineStyleColorModifiers, typing.Sequence[LineStyleColorModifier], typing.Mapping[str, LineStyleColorModifier], bpy_prop_collection] = ...

  """

  List of line color modifiers

  """

  dash1: int = ...

  """

  Length of the 1st dash for dashed lines

  """

  dash2: int = ...

  """

  Length of the 2nd dash for dashed lines

  """

  dash3: int = ...

  """

  Length of the 3rd dash for dashed lines

  """

  gap1: int = ...

  """

  Length of the 1st gap for dashed lines

  """

  gap2: int = ...

  """

  Length of the 2nd gap for dashed lines

  """

  gap3: int = ...

  """

  Length of the 3rd gap for dashed lines

  """

  geometry_modifiers: typing.Union[LineStyleGeometryModifiers, typing.Sequence[LineStyleGeometryModifier], typing.Mapping[str, LineStyleGeometryModifier], bpy_prop_collection] = ...

  """

  List of stroke geometry modifiers

  """

  integration_type: str = ...

  """

  Select the way how the sort key is computed for each chain

  * ``MEAN``
Mean -- The value computed for the chain is the mean of the values obtained for chain vertices.

  * ``MIN``
Min -- The value computed for the chain is the minimum of the values obtained for chain vertices.

  * ``MAX``
Max -- The value computed for the chain is the maximum of the values obtained for chain vertices.

  * ``FIRST``
First -- The value computed for the chain is the value obtained for the first chain vertex.

  * ``LAST``
Last -- The value computed for the chain is the value obtained for the last chain vertex.

  """

  length_max: float = ...

  """

  Maximum curvilinear 2D length for the selection of chains

  """

  length_min: float = ...

  """

  Minimum curvilinear 2D length for the selection of chains

  """

  material_boundary: bool = ...

  """

  If true, chains of feature edges are split at material boundaries

  """

  node_tree: NodeTree = ...

  """

  Node tree for node-based shaders

  """

  panel: str = ...

  """

  Select the property panel to be shown

  * ``STROKES``
Strokes -- Show the panel for stroke construction.

  * ``COLOR``
Color -- Show the panel for line color options.

  * ``ALPHA``
Alpha -- Show the panel for alpha transparency options.

  * ``THICKNESS``
Thickness -- Show the panel for line thickness options.

  * ``GEOMETRY``
Geometry -- Show the panel for stroke geometry options.

  * ``TEXTURE``
Texture -- Show the panel for stroke texture options.

  """

  rounds: int = ...

  """

  Number of rounds in a sketchy multiple touch

  """

  sort_key: str = ...

  """

  Select the sort key to determine the stacking order of chains

  * ``DISTANCE_FROM_CAMERA``
Distance from Camera -- Sort by distance from camera (closer lines lie on top of further lines).

  * ``2D_LENGTH``
2D Length -- Sort by curvilinear 2D length (longer lines lie on top of shorter lines).

  * ``PROJECTED_X``
Projected X -- Sort by the projected X value in the image coordinate system.

  * ``PROJECTED_Y``
Projected Y -- Sort by the projected Y value in the image coordinate system.

  """

  sort_order: str = ...

  """

  Select the sort order

  * ``DEFAULT``
Default -- Default order of the sort key.

  * ``REVERSE``
Reverse -- Reverse order.

  """

  split_dash1: int = ...

  """

  Length of the 1st dash for splitting

  """

  split_dash2: int = ...

  """

  Length of the 2nd dash for splitting

  """

  split_dash3: int = ...

  """

  Length of the 3rd dash for splitting

  """

  split_gap1: int = ...

  """

  Length of the 1st gap for splitting

  """

  split_gap2: int = ...

  """

  Length of the 2nd gap for splitting

  """

  split_gap3: int = ...

  """

  Length of the 3rd gap for splitting

  """

  split_length: float = ...

  """

  Curvilinear 2D length for chain splitting

  """

  texture_slots: typing.Union[LineStyleTextureSlots, typing.Sequence[LineStyleTextureSlot], typing.Mapping[str, LineStyleTextureSlot], bpy_prop_collection] = ...

  """

  Texture slots defining the mapping and influence of textures

  """

  texture_spacing: float = ...

  """

  Spacing for textures along stroke length

  """

  thickness: float = ...

  """

  Base line thickness, possibly modified by line thickness modifiers

  """

  thickness_modifiers: typing.Union[LineStyleThicknessModifiers, typing.Sequence[LineStyleThicknessModifier], typing.Mapping[str, LineStyleThicknessModifier], bpy_prop_collection] = ...

  """

  List of line thickness modifiers

  """

  thickness_position: str = ...

  """

  Thickness position of silhouettes and border edges (applicable when plain chaining is used with the Same Object option)

  * ``CENTER``
Center -- Silhouettes and border edges are centered along stroke geometry.

  * ``INSIDE``
Inside -- Silhouettes and border edges are drawn inside of stroke geometry.

  * ``OUTSIDE``
Outside -- Silhouettes and border edges are drawn outside of stroke geometry.

  * ``RELATIVE``
Relative -- Silhouettes and border edges are shifted by a user-defined ratio.

  """

  thickness_ratio: float = ...

  """

  A number between 0 (inside) and 1 (outside) specifying the relative position of stroke thickness

  """

  use_angle_max: bool = ...

  """

  Split chains at points with angles larger than the maximum 2D angle

  """

  use_angle_min: bool = ...

  """

  Split chains at points with angles smaller than the minimum 2D angle

  """

  use_chain_count: bool = ...

  """

  Enable the selection of first N chains

  """

  use_chaining: bool = ...

  """

  Enable chaining of feature edges

  """

  use_dashed_line: bool = ...

  """

  Enable or disable dashed line

  """

  use_length_max: bool = ...

  """

  Enable the selection of chains by a maximum 2D length

  """

  use_length_min: bool = ...

  """

  Enable the selection of chains by a minimum 2D length

  """

  use_nodes: bool = ...

  """

  Use shader nodes for the line style

  """

  use_same_object: bool = ...

  """

  If true, only feature edges of the same object are joined

  """

  use_sorting: bool = ...

  """

  Arrange the stacking order of strokes

  """

  use_split_length: bool = ...

  """

  Enable chain splitting by curvilinear 2D length

  """

  use_split_pattern: bool = ...

  """

  Enable chain splitting by dashed line patterns

  """

  use_texture: bool = ...

  """

  Enable or disable textured strokes

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class GreasePencil(ID, bpy_struct):

  """

  Freehand annotation sketchbook

  """

  after_color: typing.Tuple[float, float, float] = ...

  """

  Base color for ghosts after the active frame

  """

  animation_data: AnimData = ...

  """

  Animation data for this data-block

  """

  before_color: typing.Tuple[float, float, float] = ...

  """

  Base color for ghosts before the active frame

  """

  curve_edit_corner_angle: float = ...

  """

  Angle threshold to be treated as corners

  """

  curve_edit_threshold: float = ...

  """

  Curve conversion error threshold

  """

  edit_curve_resolution: int = ...

  """

  Number of segments generated between control points when editing strokes in curve mode

  """

  edit_line_color: typing.Tuple[float, float, float, float] = ...

  """

  Color for editing line

  """

  ghost_after_range: int = ...

  """

  Maximum number of frames to show after current frame (0 = don't show any frames after current)

  """

  ghost_before_range: int = ...

  """

  Maximum number of frames to show before current frame (0 = don't show any frames before current)

  """

  grid: GreasePencilGrid = ...

  """

  Settings for grid and canvas in the 3D viewport

  """

  is_annotation: bool = ...

  """

  Current data-block is an annotation

  """

  is_stroke_paint_mode: bool = ...

  """

  Draw Grease Pencil strokes on click/drag

  """

  is_stroke_sculpt_mode: bool = ...

  """

  Sculpt Grease Pencil strokes instead of viewport data

  """

  is_stroke_vertex_mode: bool = ...

  """

  Grease Pencil vertex paint

  """

  is_stroke_weight_mode: bool = ...

  """

  Grease Pencil weight paint

  """

  layers: typing.Union[GreasePencilLayers, typing.Sequence[GPencilLayer], typing.Mapping[str, GPencilLayer], bpy_prop_collection] = ...

  materials: typing.Union[IDMaterials, typing.Sequence[Material], typing.Mapping[str, Material], bpy_prop_collection] = ...

  onion_factor: float = ...

  """

  Change fade opacity of displayed onion frames

  """

  onion_keyframe_type: str = ...

  """

  Type of keyframe (for filtering)

  * ``ALL``
All -- Include all Keyframe types.

  * ``KEYFRAME``
Keyframe -- Normal keyframe - e.g. for key poses.

  * ``BREAKDOWN``
Breakdown -- A breakdown pose - e.g. for transitions between key poses.

  * ``MOVING_HOLD``
Moving Hold -- A keyframe that is part of a moving hold.

  * ``EXTREME``
Extreme -- An 'extreme' pose, or some other purpose as needed.

  * ``JITTER``
Jitter -- A filler or baked keyframe for keying on ones, or some other purpose as needed.

  """

  onion_mode: str = ...

  """

  Mode to display frames

  * ``ABSOLUTE``
Frames -- Frames in absolute range of the scene frame.

  * ``RELATIVE``
Keyframes -- Frames in relative range of the Grease Pencil keyframes.

  * ``SELECTED``
Selected -- Only selected keyframes.

  """

  pixel_factor: float = ...

  """

  Scale conversion factor for pixel size (use larger values for thicker lines)

  """

  stroke_depth_order: str = ...

  """

  Defines how the strokes are ordered in 3D space (for objects not displayed 'In Front')

  * ``2D``
2D Layers -- Display strokes using grease pencil layers to define order.

  * ``3D``
3D Location -- Display strokes using real 3D position in 3D space.

  """

  stroke_thickness_space: str = ...

  """

  Set stroke thickness in screen space or world space

  * ``WORLDSPACE``
World Space -- Set stroke thickness relative to the world space.

  * ``SCREENSPACE``
Screen Space -- Set stroke thickness relative to the screen space.

  """

  use_adaptive_curve_resolution: bool = ...

  """

  Set the resolution of each editcurve segment dynamically depending on the length of the segment. The resolution is the number of points generated per unit distance

  """

  use_autolock_layers: bool = ...

  """

  Automatically lock all layers except the active one to avoid accidental changes

  """

  use_curve_edit: bool = ...

  """

  Edit strokes using curve handles

  """

  use_ghost_custom_colors: bool = ...

  """

  Use custom colors for ghost frames

  """

  use_ghosts_always: bool = ...

  """

  Ghosts are shown in renders and animation playback. Useful for special effects (e.g. motion blur)

  """

  use_multiedit: bool = ...

  """

  Edit strokes from multiple grease pencil keyframes at the same time (keyframes must be selected to be included)

  """

  use_onion_fade: bool = ...

  """

  Display onion keyframes with a fade in color transparency

  """

  use_onion_loop: bool = ...

  """

  Display onion keyframes for looping animations

  """

  use_onion_skinning: bool = ...

  """

  Show ghosts of the keyframes before and after the current frame

  """

  use_stroke_edit_mode: bool = ...

  """

  Edit Grease Pencil strokes instead of viewport data

  """

  zdepth_offset: float = ...

  """

  Offset amount when drawing in surface mode

  """

  def clear(self) -> None:

    """

    Remove all the Grease Pencil data

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Image(ID, bpy_struct):

  """

  Image data-block referencing an external or packed image

  """

  alpha_mode: str = ...

  """

  Representation of alpha in the image file, to convert to and from when saving and loading the image

  * ``STRAIGHT``
Straight -- Store RGB and alpha channels separately with alpha acting as a mask, also known as unassociated alpha. Commonly used by image editing applications and file formats like PNG.

  * ``PREMUL``
Premultiplied -- Store RGB channels with alpha multiplied in, also known as associated alpha. The natural format for renders and used by file formats like OpenEXR.

  * ``CHANNEL_PACKED``
Channel Packed -- Different images are packed in the RGB and alpha channels, and they should not affect each other. Channel packing is commonly used by game engines to save memory.

  * ``NONE``
None -- Ignore alpha channel from the file and make image fully opaque.

  """

  bindcode: int = ...

  """

  OpenGL bindcode

  """

  channels: int = ...

  """

  Number of channels in pixels buffer

  """

  colorspace_settings: ColorManagedInputColorspaceSettings = ...

  """

  Input color space settings

  """

  depth: int = ...

  """

  Image bit depth

  """

  display_aspect: typing.Tuple[float, float] = ...

  """

  Display Aspect for this image, does not affect rendering

  """

  file_format: str = ...

  """

  Format used for re-saving this file

  * ``BMP``
BMP -- Output image in bitmap format.

  * ``IRIS``
Iris -- Output image in SGI IRIS format.

  * ``PNG``
PNG -- Output image in PNG format.

  * ``JPEG``
JPEG -- Output image in JPEG format.

  * ``JPEG2000``
JPEG 2000 -- Output image in JPEG 2000 format.

  * ``TARGA``
Targa -- Output image in Targa format.

  * ``TARGA_RAW``
Targa Raw -- Output image in uncompressed Targa format.

  * ``CINEON``
Cineon -- Output image in Cineon format.

  * ``DPX``
DPX -- Output image in DPX format.

  * ``OPEN_EXR_MULTILAYER``
OpenEXR MultiLayer -- Output image in multilayer OpenEXR format.

  * ``OPEN_EXR``
OpenEXR -- Output image in OpenEXR format.

  * ``HDR``
Radiance HDR -- Output image in Radiance HDR format.

  * ``TIFF``
TIFF -- Output image in TIFF format.

  * ``AVI_JPEG``
AVI JPEG -- Output video in AVI JPEG format.

  * ``AVI_RAW``
AVI Raw -- Output video in AVI Raw format.

  * ``FFMPEG``
FFmpeg Video -- The most versatile way to output video files.

  """

  filepath: str = ...

  """

  Image/Movie file name

  """

  filepath_raw: str = ...

  """

  Image/Movie file name (without data refreshing)

  """

  frame_duration: int = ...

  """

  Duration (in frames) of the image (1 when not a video/sequence)

  """

  generated_color: typing.Tuple[float, float, float, float] = ...

  """

  Fill color for the generated image

  """

  generated_height: int = ...

  """

  Generated image height

  """

  generated_type: str = ...

  """

  Generated image type

  * ``BLANK``
Blank -- Generate a blank image.

  * ``UV_GRID``
UV Grid -- Generated grid to test UV mappings.

  * ``COLOR_GRID``
Color Grid -- Generated improved UV grid to test UV mappings.

  """

  generated_width: int = ...

  """

  Generated image width

  """

  has_data: bool = ...

  """

  True if the image data is loaded into memory

  """

  is_dirty: bool = ...

  """

  Image has changed and is not saved

  """

  is_float: bool = ...

  """

  True if this image is stored in floating-point buffer

  """

  is_multiview: bool = ...

  """

  Image has more than one view

  """

  is_stereo_3d: bool = ...

  """

  Image has left and right views

  """

  packed_file: PackedFile = ...

  """

  First packed file of the image

  """

  packed_files: typing.Union[typing.Sequence[ImagePackedFile], typing.Mapping[str, ImagePackedFile], bpy_prop_collection] = ...

  """

  Collection of packed images

  """

  pixels: float = ...

  """

  Image pixels in floating-point values

  """

  render_slots: typing.Union[RenderSlots, typing.Sequence[RenderSlot], typing.Mapping[str, RenderSlot], bpy_prop_collection] = ...

  """

  Render slots of the image

  """

  resolution: typing.Tuple[float, float] = ...

  """

  X/Y pixels per meter

  """

  size: typing.Tuple[int, int] = ...

  """

  Width and height in pixels, zero when image data can't be loaded

  """

  source: str = ...

  """

  Where the image comes from

  * ``FILE``
Single Image -- Single image file.

  * ``SEQUENCE``
Image Sequence -- Multiple image files, as a sequence.

  * ``MOVIE``
Movie -- Movie file.

  * ``GENERATED``
Generated -- Generated image.

  * ``VIEWER``
Viewer -- Compositing node viewer.

  * ``TILED``
UDIM Tiles -- Tiled UDIM image texture.

  """

  stereo_3d_format: Stereo3dFormat = ...

  """

  Settings for stereo 3d

  """

  tiles: typing.Union[UDIMTiles, typing.Sequence[UDIMTile], typing.Mapping[str, UDIMTile], bpy_prop_collection] = ...

  """

  Tiles of the image

  """

  type: str = ...

  """

  How to generate the image

  """

  use_deinterlace: bool = ...

  """

  Deinterlace movie file on load

  """

  use_generated_float: bool = ...

  """

  Generate floating-point buffer

  """

  use_half_precision: bool = ...

  """

  Use 16 bits per channel to lower the memory usage during rendering

  """

  use_multiview: bool = ...

  """

  Use Multiple Views (when available)

  """

  use_view_as_render: bool = ...

  """

  Apply render part of display transformation when displaying this image on the screen

  """

  views_format: str = ...

  """

  Mode to load image views

  * ``INDIVIDUAL``
Individual -- Individual files for each view with the prefix as defined by the scene views.

  * ``STEREO_3D``
Stereo 3D -- Single file with an encoded stereo pair.

  """

  def save_render(self, filepath: str, scene: Scene = None) -> None:

    """

    Save image to a specific path using a scenes render settings

    """

    ...

  def save(self) -> None:

    """

    Save image to its source path

    """

    ...

  def pack(self, data: str = '', data_len: int = 0) -> None:

    """

    Pack an image as embedded data into the .blend file

    """

    ...

  def unpack(self, method: str = 'USE_LOCAL') -> None:

    """

    Save an image packed in the .blend file to disk

    """

    ...

  def reload(self) -> None:

    """

    Reload the image from its source path

    """

    ...

  def update(self) -> None:

    """

    Update the display image from the floating-point buffer

    """

    ...

  def scale(self, width: int, height: int) -> None:

    """

    Scale the image in pixels

    """

    ...

  def gl_touch(self, frame: int = 0) -> int:

    """

    Delay the image from being cleaned from the cache due inactivity

    """

    ...

  def gl_load(self, frame: int = 0) -> int:

    """

    Load the image into an OpenGL texture. On success, image.bindcode will contain the OpenGL texture bindcode. Colors read from the texture will be in scene linear color space and have premultiplied or straight alpha matching the image alpha mode

    """

    ...

  def gl_free(self) -> None:

    """

    Free the image from OpenGL graphics memory

    """

    ...

  def filepath_from_user(self, image_user: ImageUser = None) -> str:

    """

    Return the absolute path to the filepath of an image frame specified by the image user

    """

    ...

  def buffers_free(self) -> None:

    """

    Free the image buffers from memory

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Key(ID, bpy_struct):

  """

  Shape keys data-block containing different shapes of geometric data-blocks

  """

  animation_data: AnimData = ...

  """

  Animation data for this data-block

  """

  eval_time: float = ...

  """

  Evaluation time for absolute shape keys

  """

  key_blocks: typing.Union[typing.Sequence[ShapeKey], typing.Mapping[str, ShapeKey], bpy_prop_collection] = ...

  """

  Shape keys

  """

  reference_key: ShapeKey = ...

  use_relative: bool = ...

  """

  Make shape keys relative, otherwise play through shapes as a sequence using the evaluation time

  """

  user: ID = ...

  """

  Data-block using these shape keys

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Lattice(ID, bpy_struct):

  """

  Lattice data-block defining a grid for deforming other objects

  """

  animation_data: AnimData = ...

  """

  Animation data for this data-block

  """

  interpolation_type_u: str = ...

  interpolation_type_v: str = ...

  interpolation_type_w: str = ...

  is_editmode: bool = ...

  """

  True when used in editmode

  """

  points: typing.Union[typing.Sequence[LatticePoint], typing.Mapping[str, LatticePoint], bpy_prop_collection] = ...

  """

  Points of the lattice

  """

  points_u: int = ...

  """

  Point in U direction (can't be changed when there are shape keys)

  """

  points_v: int = ...

  """

  Point in V direction (can't be changed when there are shape keys)

  """

  points_w: int = ...

  """

  Point in W direction (can't be changed when there are shape keys)

  """

  shape_keys: Key = ...

  use_outside: bool = ...

  """

  Only display and take into account the outer vertices

  """

  vertex_group: str = ...

  """

  Vertex group to apply the influence of the lattice

  """

  def transform(self, matrix: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]], shape_keys: bool = False) -> None:

    """

    Transform lattice by a matrix

    """

    ...

  def update_gpu_tag(self) -> None:

    """

    update_gpu_tag

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Library(ID, bpy_struct):

  """

  External .blend file from which data is linked

  """

  filepath: str = ...

  """

  Path to the library .blend file

  """

  packed_file: PackedFile = ...

  parent: Library = ...

  version: typing.Tuple[int, int, int] = ...

  """

  Version of Blender the library .blend was saved with

  """

  users_id: typing.Any = ...

  """

  ID data blocks which use this library

  (readonly)

  """

  def reload(self) -> None:

    """

    Reload this library and all its linked data-blocks

    """

    ...

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Light(ID):

  """

  Light data-block for lighting a scene

  """

  animation_data: AnimData = ...

  """

  Animation data for this data-block

  """

  color: typing.Tuple[float, float, float] = ...

  """

  Light color

  """

  cutoff_distance: float = ...

  """

  Distance at which the light influence will be set to 0

  """

  cycles: CyclesLightSettings = ...

  """

  Cycles light settings

  """

  diffuse_factor: float = ...

  """

  Diffuse reflection multiplier

  """

  distance: float = ...

  """

  Falloff distance - the light is at half the original intensity at this point

  """

  node_tree: NodeTree = ...

  """

  Node tree for node based lights

  """

  specular_factor: float = ...

  """

  Specular reflection multiplier

  """

  type: str = ...

  """

  Type of light

  * ``POINT``
Point -- Omnidirectional point light source.

  * ``SUN``
Sun -- Constant direction parallel ray light source.

  * ``SPOT``
Spot -- Directional cone light source.

  * ``AREA``
Area -- Directional area light source.

  """

  use_custom_distance: bool = ...

  """

  Use custom attenuation distance instead of global light threshold

  """

  use_nodes: bool = ...

  """

  Use shader nodes to render the light

  """

  volume_factor: float = ...

  """

  Volume light multiplier

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class LightProbe(ID, bpy_struct):

  """

  Light Probe data-block for lighting capture objects

  """

  animation_data: AnimData = ...

  """

  Animation data for this data-block

  """

  clip_end: float = ...

  """

  Probe clip end, beyond which objects will not appear in reflections

  """

  clip_start: float = ...

  """

  Probe clip start, below which objects will not appear in reflections

  """

  falloff: float = ...

  """

  Control how fast the probe influence decreases

  """

  grid_resolution_x: int = ...

  """

  Number of sample along the x axis of the volume

  """

  grid_resolution_y: int = ...

  """

  Number of sample along the y axis of the volume

  """

  grid_resolution_z: int = ...

  """

  Number of sample along the z axis of the volume

  """

  influence_distance: float = ...

  """

  Influence distance of the probe

  """

  influence_type: str = ...

  """

  Type of influence volume

  """

  intensity: float = ...

  """

  Modify the intensity of the lighting captured by this probe

  """

  invert_visibility_collection: bool = ...

  """

  Invert visibility collection

  """

  parallax_distance: float = ...

  """

  Lowest corner of the parallax bounding box

  """

  parallax_type: str = ...

  """

  Type of parallax volume

  """

  show_clip: bool = ...

  """

  Show the clipping distances in the 3D view

  """

  show_data: bool = ...

  """

  Show captured lighting data into the 3D view for debugging purpose

  """

  show_influence: bool = ...

  """

  Show the influence volume in the 3D view

  """

  show_parallax: bool = ...

  """

  Show the parallax correction volume in the 3D view

  """

  type: str = ...

  """

  Type of light probe

  * ``CUBEMAP``
Reflection Cubemap -- Capture reflections.

  * ``PLANAR``
Reflection Plane.

  * ``GRID``
Irradiance Volume -- Volume used for precomputing indirect lighting.

  """

  use_custom_parallax: bool = ...

  """

  Enable custom settings for the parallax correction volume

  """

  visibility_bleed_bias: float = ...

  """

  Bias for reducing light-bleed on variance shadow maps

  """

  visibility_blur: float = ...

  """

  Filter size of the visibility blur

  """

  visibility_buffer_bias: float = ...

  """

  Bias for reducing self shadowing

  """

  visibility_collection: Collection = ...

  """

  Restrict objects visible for this probe

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Mask(ID, bpy_struct):

  """

  Mask data-block defining mask for compositing

  """

  active_layer_index: int = ...

  """

  Index of active layer in list of all mask's layers

  """

  animation_data: AnimData = ...

  """

  Animation data for this data-block

  """

  frame_end: int = ...

  """

  Final frame of the mask (used for sequencer)

  """

  frame_start: int = ...

  """

  First frame of the mask (used for sequencer)

  """

  layers: typing.Union[MaskLayers, typing.Sequence[MaskLayer], typing.Mapping[str, MaskLayer], bpy_prop_collection] = ...

  """

  Collection of layers which defines this mask

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Material(ID, bpy_struct):

  """

  Material data-block to define the appearance of geometric objects for rendering

  """

  alpha_threshold: float = ...

  """

  A pixel is rendered only if its alpha value is above this threshold

  """

  animation_data: AnimData = ...

  """

  Animation data for this data-block

  """

  blend_method: str = ...

  """

  Blend Mode for Transparent Faces

  * ``OPAQUE``
Opaque -- Render surface without transparency.

  * ``CLIP``
Alpha Clip -- Use the alpha threshold to clip the visibility (binary visibility).

  * ``HASHED``
Alpha Hashed -- Use noise to dither the binary visibility (works well with multi-samples).

  * ``BLEND``
Alpha Blend -- Render polygon transparent, depending on alpha channel of the texture.

  """

  cycles: CyclesMaterialSettings = ...

  """

  Cycles material settings

  """

  diffuse_color: typing.Tuple[float, float, float, float] = ...

  """

  Diffuse color of the material

  """

  grease_pencil: MaterialGPencilStyle = ...

  """

  Grease pencil color settings for material

  """

  is_grease_pencil: bool = ...

  """

  True if this material has grease pencil data

  """

  line_color: typing.Tuple[float, float, float, float] = ...

  """

  Line color used for Freestyle line rendering

  """

  line_priority: int = ...

  """

  The line color of a higher priority is used at material boundaries

  """

  lineart: MaterialLineArt = ...

  """

  Line art settings for material

  """

  metallic: float = ...

  """

  Amount of mirror reflection for raytrace

  """

  node_tree: NodeTree = ...

  """

  Node tree for node based materials

  """

  paint_active_slot: int = ...

  """

  Index of active texture paint slot

  """

  paint_clone_slot: int = ...

  """

  Index of clone texture paint slot

  """

  pass_index: int = ...

  """

  Index number for the "Material Index" render pass

  """

  preview_render_type: str = ...

  """

  Type of preview render

  * ``FLAT``
Flat -- Flat XY plane.

  * ``SPHERE``
Sphere -- Sphere.

  * ``CUBE``
Cube -- Cube.

  * ``HAIR``
Hair -- Hair strands.

  * ``SHADERBALL``
Shader Ball -- Shader ball.

  * ``CLOTH``
Cloth -- Cloth.

  * ``FLUID``
Fluid -- Fluid.

  """

  refraction_depth: float = ...

  """

  Approximate the thickness of the object to compute two refraction event (0 is disabled)

  """

  roughness: float = ...

  """

  Roughness of the material

  """

  shadow_method: str = ...

  """

  Shadow mapping method

  * ``NONE``
None -- Material will cast no shadow.

  * ``OPAQUE``
Opaque -- Material will cast shadows without transparency.

  * ``CLIP``
Alpha Clip -- Use the alpha threshold to clip the visibility (binary visibility).

  * ``HASHED``
Alpha Hashed -- Use noise to dither the binary visibility and use filtering to reduce the noise.

  """

  show_transparent_back: bool = ...

  """

  Limit transparency to a single layer (avoids transparency sorting problems)

  """

  specular_color: typing.Tuple[float, float, float] = ...

  """

  Specular color of the material

  """

  specular_intensity: float = ...

  """

  How intense (bright) the specular reflection is

  """

  texture_paint_images: typing.Union[typing.Sequence[Image], typing.Mapping[str, Image], bpy_prop_collection] = ...

  """

  Texture images used for texture painting

  """

  texture_paint_slots: typing.Union[typing.Sequence[TexPaintSlot], typing.Mapping[str, TexPaintSlot], bpy_prop_collection] = ...

  """

  Texture slots defining the mapping and influence of textures

  """

  use_backface_culling: bool = ...

  """

  Use back face culling to hide the back side of faces

  """

  use_nodes: bool = ...

  """

  Use shader nodes to render the material

  """

  use_preview_world: bool = ...

  """

  Use the current world background to light the preview render

  """

  use_screen_refraction: bool = ...

  """

  Use raytraced screen space refractions

  """

  use_sss_translucency: bool = ...

  """

  Add translucency effect to subsurface

  """

  @classmethod

  def bl_rna_get_subclass(cls, id: str, default: typing.Any = None) -> Struct:

    ...

  @classmethod

  def bl_rna_get_subclass_py(cls, id: str, default: typing.Any = None) -> typing.Type:

    ...

class Mesh(ID, bpy_struct):

  """

  Mesh data-block defining geometric surfaces

  """

  animation_data: AnimData = ...

  """

  Animation data for this data-block

  """

  attributes: typing.Union[AttributeGroup, typing.Sequence[Attribute], typing.Mapping[str, Attribute], bpy_prop_collection] = ...

  """

  Geometry attributes

  """

  auto_smooth_angle: float = ...

  """

  Maximum angle between face normals that will be considered as smooth (unused if custom split normals data are available)

  """

  auto_texspace: bool = ...

  """

  Adjust active object's texture space automatically when transforming object

  """

  cycles: CyclesMeshSettings = ...

  """

  Cycles mesh settings

  """

  edges: typing.Union[MeshEdges, typing.Sequence[MeshEdge], typing.Mapping[str, MeshEdge], bpy_prop_collection] = ...

  """

  Edges of the mesh

  """

  face_maps: typing.Union[MeshFaceMapLayers, typing.Sequence[MeshFaceMapLayer], typing.Mapping[str, MeshFaceMapLayer], bpy_prop_collection] = ...

  has_custom_normals: bool = ...

  """

  True if there are custom split normals data in this mesh

  """

  is_editmode: bool = ...

  """

  True when used in editmode

  """

  loop_triangles: typing.Union[MeshLoopTriangles, typing.Sequence[MeshLoopTriangle], typing.Mapping[str, MeshLoopTriangle], bpy_prop_collection] = ...

  """

  Tessellation of mesh polygons into triangles

  """

  loops: typing.Union[MeshLoops, typing.Sequence[MeshLoop], typing.Mapping[str, MeshLoop], bpy_prop_collection] = ...

  """

  Loops of the mesh (polygon corners)

  """

  materials: typing.Union[IDMaterials, typing.Sequence[Material], typing.Mapping[str, Material], bpy_prop_collection] = ...

  polygon_layers_float: typing.Union[PolygonFloatProperties, typing.Sequence[MeshPolygonFloatPropertyLayer], typing.Mapping[str, MeshPolygonFloatPropertyLayer], bpy_prop_collection] = ...

  polygon_layers_int: typing.Union[PolygonIntProperties, typing.Sequence[MeshPolygonIntPropertyLayer], typing.Mapping[str, MeshPolygonIntPropertyLayer], bpy_prop_collection] = ...

  polygon_layers_string: typing.Union[PolygonStringProperties, typing.Sequence[MeshPolygonStringPropertyLayer], typing.Mapping[str, MeshPolygonStringPropertyLayer], bpy_prop_collection] = ...

  polygons: typing.Union[MeshPolygons, typing.Sequence[MeshPolygon], typing.Mapping[str, MeshPolygon], bpy_prop_collection] = ...

  """

  Polygons of the mesh

  """

  remesh_mode: str = ...

  """

  * ``VOXEL``
Voxel -- Use the voxel remesher.

  * ``QUAD``
Quad -- Use the quad remesher.

  """

  remesh_voxel_adaptivity: float = ...

  """

  Reduces the final face count by simplifying geometry where detail is not needed, generating triangles. A value greater than 0 disables Fix Poles

  """

  remesh_voxel_size: float = ...

  """

  Size of the voxel in object space used for volume evaluation. Lower values preserve finer details

  """

  sculpt_vertex_colors: typing.Union[VertColors, typing.Sequence[MeshVertColorLayer], typing.Mapping[str, MeshVertColorLayer], bpy_prop_collection] = ...

  """

  All vertex colors

  """

  shape_keys: Key = ...

  skin_vertices: typing.Union[typing.Sequence[MeshSkinVertexLayer], typing.Mapping[str, MeshSkinVertexLayer], bpy_prop_collection] = ...

  """

  All skin vertices

  """

  texco_mesh: Mesh = ...

  """

  Derive texture coordinates from another mesh

  """

  texspace_location: typing.Tuple[float, float, float] = ...

  """

  Texture space location

  """

  texspace_size: typing.Tuple[float, float, float] = ...

  """

  Texture space size

  """

  texture_mesh: Mesh = ...

  """

  Use another mesh for texture indices (vertex indices must be aligned)

  """

  total_edge_sel: int = ...

  """

  Selected edge count in editmode

  """

  total_face_sel: int = ...

  """

  Selected face count in editmode

  """

  total_vert_sel: int = ...

  """

  Selected vertex count in editmode

  """

  use_auto_smooth: bool = ...

  """

  Auto smooth (based on smooth/sharp faces/edges and angle between faces), or use custom split normals data if available

  """

  use_auto_texspace: bool = ...

  """

  Adjust active object's texture space automatically when transforming object

  """

  use_customdata_edge_bevel: bool = ...

  use_customdata_edge_crease: bool = ...

  use_customdata_vertex_bevel: bool = ...

  use_mirror_topology: bool = ...

  """

  Use topology based mirroring (for when both sides of mesh have matching, unique topology)

  """

  use_mirror_vertex_groups: bool = ...

  """

  Mirror the left/right vertex groups when painting. The symmetry axis is determined by the symmetry settings

  """

  use_mirror_x: bool = ...

  """

  Enable symmetry in the X axis

  """

  use_mirror_y: bool = ...

  """

  Enable symmetry in the Y axis

  """

  use_mirror_z: bool = ...

  """

  Enable symmetry in the Z axis

  """

  use_paint_mask: bool = ...

  """

  Face selection masking for painting

  """

  use_paint_mask_vertex: bool = ...

  """

  Vertex selection masking for painting

  """

  use_remesh_fix_poles: bool = ...

  """

  Produces less poles and a better topology flow

  """

  use_remesh_preserve_paint_mask: bool = ...

  """

  Keep the current mask on the new mesh

  """

  use_remesh_preserve_sculpt_face_sets: bool = ...

  """

  Keep the current Face Sets on the new mesh

  """

  use_remesh_preserve_vertex_colors: bool = ...

  """

  Keep the current vertex colors on the new mesh

  """

  use_remesh_preserve_volume: bool = ...

  """

  Projects the mesh to preserve the volume and details of the original mesh

  """

  uv_layer_clone: MeshUVLoopLayer = ...

  """

  UV loop layer to be used as cloning source

  """

  uv_layer_clone_index: int = ...

  """

  Clone UV loop layer index

  """

  uv_layer_stencil: MeshUVLoopLayer = ...

  """

  UV loop layer to mask the painted area

  """

  uv_layer_stencil_index: int = ...

  """

  Mask UV loop layer index

  """

  uv_layers: typing.Union[UVLoopLayers, typing.Sequence[MeshUVLoopLayer], typing.Mapping[str, MeshUVLoopLayer], bpy_prop_collection] = ...

  """

  All UV loop layers

  """

  vertex_colors: typing.Union[LoopColors, typing.Sequence[MeshLoopColorLayer], typing.Mapping[str, MeshLoopColorLayer], bpy_prop_collection] = ...

  """

  All vertex colors

  """

  vertex_layers_float: typing.Union[VertexFloatProperties, typing.Sequence[MeshVertexFloatPropertyLayer], typing.Mapping[str, MeshVertexFloatPropertyLayer], bpy_prop_collection] = ...

  vertex_layers_int: typing.Union[VertexIntProperties, typing.Sequence[MeshVertexIntPropertyLayer], typing.Mapping[str, MeshVertexIntPropertyLayer], bpy_prop_collection] = ...

  vertex_layers_string: typing.Union[VertexStringProperties, typing.Sequence[MeshVertexStringPropertyLayer], typing.Mapping[str, MeshVertexStringPropertyLayer], bpy_prop_collection] = ...

  vertex_paint_masks: typing.Union[typing.Sequence[MeshPaintMaskLayer], typing.Mapping[str, MeshPaintMaskLayer], bpy_prop_collection] = ...

  """

  Vertex paint mask

  """

  vertices: typing.Union[MeshVertices, typing.Sequence[MeshVertex], typing.Mapping[str, MeshVertex], bpy_prop_collection] = ...

  """

  Vertices of the mesh

  """

  edge_keys: typing.Any = ...

  """

  (readonly)

  """

  def transform(self, matrix: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]], shape_keys: bool = False) -> None:

    """

    Transform mesh vertices by a matrix (Warning: inverts normals if matrix is negative)

    """

    ...

  def flip_normals(self) -> None:

    """

    Invert winding of all polygons (clears tessellation, does not handle custom normals)

    """

    ...

  def calc_normals(self) -> None:

    """

    Calculate vertex normals

    """

    ...

  def create_normals_split(self) -> None:

    """

    Empty split vertex normals

    """

    ...

  def calc_normals_split(self) -> None:

    """

    Calculate split vertex normals, which preserve sharp edges

    """

    ...

  def free_normals_split(self) -> None:

    """

    Free split vertex normals

    """

    ...

  def split_faces(self, free_loop_normals: bool = True) -> None:

    """

    Split faces based on the edge angle

    """

    ...

  def calc_tangents(self, uvmap: str = '') -> None:

    """

    Compute tangents and bitangent signs, to be used together with the split normals to get a complete tangent space for normal mapping (split normals are also computed if not yet present)

    """

    ...

  def free_tangents(self) -> None:

    """

    Free tangents

    """

    ...

  def calc_loop_triangles(self) -> None:

    """

    Calculate loop triangle tessellation (supports editmode too)

    """

    ...


    """

