from distutils.core import setup
from Cython.Build import cythonize

setup(
    name="cytokine",
    ext_modules = cythonize("cytokine/ct.pyx")
)
