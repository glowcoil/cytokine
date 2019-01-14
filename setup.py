from distutils.core import setup, Extension

setup(
    name="engine",
    ext_modules = [
        Extension("cytokine.engine", ["cytokine/engine/bindings.c"])
    ]
)
