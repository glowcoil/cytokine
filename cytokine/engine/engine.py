import ctypes
import os

mesh = ctypes.cdll.LoadLibrary(os.path.join(os.path.dirname(__file__), "mesh.dylib"))
from_blender_mesh = mesh.from_blender_mesh
from_blender_mesh.argtypes = [ctypes.c_ulong]
from_blender_mesh.restype = ctypes.c_ulong
