#include <Python.h>

PyObject *py_test_fn(PyObject *self, PyObject *args) {
    return PyLong_FromLong(1L);
}

static PyMethodDef engine_methods[] = {
    {"test_fn",  py_test_fn, METH_VARARGS, ""},
    {NULL, NULL}
};

static struct PyModuleDef engine =
{
    PyModuleDef_HEAD_INIT,
    "engine",
    "",
    -1,
    engine_methods
};

PyMODINIT_FUNC PyInit_engine(void) {
    return PyModule_Create(&engine);
}
