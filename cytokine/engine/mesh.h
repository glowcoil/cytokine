#ifndef MESH_H
#define MESH_H

#include "stretchy_buffer.h"
#include "blender/makesdna/DNA_mesh_types.h"
#include "blender/makesdna/DNA_meshdata_types.h"

typedef struct edge {
    int face;
    int edge;
} edge;

typedef struct face {
    int start;
    int len;
} face;

typedef struct vec3 {
    float x;
    float y;
    float z;
} vec3;

typedef struct mesh {
    vec3 *verts;
    int *loops;
    edge *opposites;
    face *faces;
} mesh;

mesh from_blender_mesh(uintptr_t blender_mesh);

#endif