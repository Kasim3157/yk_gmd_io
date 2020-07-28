from dataclasses import dataclass
from typing import List, Tuple, Union, Type

import mathutils

from yk_gmd_blender.structurelib.base import BaseUnpacker
from yk_gmd_blender.yk_gmd.v2.structure.common.attributestruct import AttributeStruct_Unpack, AttributeStruct
from yk_gmd_blender.yk_gmd.v2.structure.common.checksum_str import ChecksumStrStruct, ChecksumStrStruct_Unpack
from yk_gmd_blender.yk_gmd.v2.structure.common.file import FileData_Common, FilePacker
from yk_gmd_blender.yk_gmd.v2.structure.common.material_base import MaterialBaseStruct
from yk_gmd_blender.yk_gmd.v2.structure.common.matrix import MatrixUnpacker
from yk_gmd_blender.yk_gmd.v2.structure.common.node import NodeStruct_Unpack, NodeStruct
from yk_gmd_blender.yk_gmd.v2.structure.yk1.bbox import BoundsDataStruct_YK1
from yk_gmd_blender.yk_gmd.v2.structure.yk1.header import GMDHeader_YK1_Unpack, UNK12_Unpack, UNK14_Unpack
from yk_gmd_blender.yk_gmd.v2.structure.yk1.material import MaterialStruct_YK1_Unpack, c_uint16, MaterialStruct_YK1
from yk_gmd_blender.yk_gmd.v2.structure.yk1.mesh import MeshStruct_YK1, MeshStruct_YK1_Unpack
from yk_gmd_blender.yk_gmd.v2.structure.yk1.object import ObjectStruct_YK1, ObjectStruct_YK1_Unpack
from yk_gmd_blender.yk_gmd.v2.structure.yk1.vertex_buffer_layout import VertexBufferLayoutStruct_YK1_Unpack, VertexBufferLayoutStruct_YK1


@dataclass(repr=False)
class FileData_YK1(FileData_Common):
    overall_bounds: BoundsDataStruct_YK1

    node_arr: List[NodeStruct]
    obj_arr: List[ObjectStruct_YK1]
    mesh_arr: List[MeshStruct_YK1]
    attribute_arr: List[AttributeStruct]
    material_arr: List[MaterialStruct_YK1]
    matrix_arr: List[mathutils.Matrix]
    vertex_buffer_arr: List[VertexBufferLayoutStruct_YK1]
    vertex_data: bytes  # byte data
    texture_arr: List[ChecksumStrStruct]
    shader_arr: List[ChecksumStrStruct]
    node_name_arr: List[ChecksumStrStruct]
    index_data: List[int]
    meshset_data: bytes
    mesh_matrix_bytestrings: bytes

    unk12: List[List[float]]
    unk13: List[int]  # Is sequence 00, 7C, 7D, 7E... 92 in Kiwami bob
    # # 0x7C = 124
    # # 0x92 = 146 => this is likely a bone address
    # # 24 elements in total
    unk14: List[List[int]]
    flags: List[int]

    def __str__(self):
        s = "{\n"
        for f in self.header_fields_to_copy():
            s += f"\t{f} = {getattr(self, f)}\n"
        for f, _ in self.header_pointer_fields():
            s += f"\t{f} = array[{len(getattr(self, f))}]\n"
        s += "}"
        return s

    @classmethod
    def header_pointer_fields(cls) -> List[Tuple[str, Union[BaseUnpacker, Type[bytes]]]]:
        return FileData_Common.header_pointer_fields() + [
            ("node_arr", NodeStruct_Unpack),
            ("obj_arr", ObjectStruct_YK1_Unpack),
            ("mesh_arr", MeshStruct_YK1_Unpack),
            ("attribute_arr", AttributeStruct_Unpack),
            ("material_arr", MaterialStruct_YK1_Unpack),
            ("matrix_arr", MatrixUnpacker),
            ("vertex_buffer_arr", VertexBufferLayoutStruct_YK1_Unpack),
            ("vertex_data", bytes),
            ("texture_arr", ChecksumStrStruct_Unpack),
            ("shader_arr", ChecksumStrStruct_Unpack),
            ("node_name_arr", ChecksumStrStruct_Unpack),
            ("index_data", c_uint16),
            ("meshset_data", bytes),
            ("mesh_matrix_bytestrings", bytes),
            ("unk12", UNK12_Unpack),
            ("unk13", c_uint16),
            ("unk14", UNK14_Unpack),
        ]

    @classmethod
    def header_fields_to_copy(cls) -> List[str]:
        return FileData_Common.header_fields_to_copy() + [
            "overall_bounds",
            "flags"
        ]


FilePacker_YK1 = FilePacker(
    FileData_YK1,
    GMDHeader_YK1_Unpack
)