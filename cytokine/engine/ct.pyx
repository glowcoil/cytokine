# cython: language_level=3

from libc.stdint cimport uintptr_t

cdef extern from "blender/makesdna/DNA_meshdata_types.h":
    cdef struct MVert:
        float co[3]
        float no[3]
    cdef struct MEdge:
        unsigned int v1, v2
    cdef struct MPoly:
        int loopstart
        int totloop
    cdef struct MLoop:
        unsigned int v
        unsigned int e
    cdef struct MLoopUV:
        float uv[2]
    cdef struct MLoopCol:
        unsigned char r, g, b, a
    cdef struct MFace:
        unsigned int v1, v2, v3, v4
    cdef struct MTFace:
        float uv[4][2]

cdef extern from "blender/makesdna/DNA_mesh_types.h":
    cdef struct BlenderMesh "Mesh":
        int totvert, totedge, totpoly, totloop, totface
        MVert *mvert
        MEdge *medge
        MPoly *mpoly
        MLoop *mloop
        MLoopUV *mloopuv
        MLoopCol *mloopcol
        MFace *mface
        MTFace *mtface

def inspect_mesh(mesh):
    cdef BlenderMesh *blender_mesh
    blender_mesh = <BlenderMesh *><void *><uintptr_t>mesh.as_pointer()
    print(blender_mesh.totloop)
    print(blender_mesh.totface)
    print(blender_mesh.totpoly)
    print(blender_mesh.totvert)
    print(blender_mesh.totedge)
