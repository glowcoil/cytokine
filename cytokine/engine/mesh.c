#include "mesh.h"

#include <stdio.h>

#include "blender/makesdna/DNA_mesh_types.h"
#include "blender/makesdna/DNA_meshdata_types.h"

uintptr_t from_blender_mesh(uintptr_t blender_mesh) {
    Mesh *b_mesh = (Mesh *)blender_mesh;

    mesh *m = malloc(sizeof(mesh));
    sb_add(m->verts, b_mesh->totvert);

    return m;
}
