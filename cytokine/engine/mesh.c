#include "mesh.h"

mesh from_blender_mesh(uintptr_t blender_mesh) {
    Mesh *b_mesh = blender_mesh;

    mesh m;

    sb_add(&m.verts, b_mesh->totvert);

    printf("%d %d", b_mesh->totpoly, b_mesh->totloop);
}
