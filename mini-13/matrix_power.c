#include <Python.h>

static PyObject *matrix_multiply(PyObject *a, PyObject *b) {

  Py_ssize_t a_rows, a_cols, b_rows, b_cols;
  PyObject *result, *row, *val;
  double sum;

  a_rows = PyList_Size(a);
  a_cols = PyList_Size(PyList_GetItem(a, 0));
  b_rows = PyList_Size(b);
  b_cols = PyList_Size(PyList_GetItem(b, 0));

  if (a_cols != b_rows) {
    PyErr_SetString(PyExc_ValueError, "Only NxN matrix can be powered");
    return NULL;
  }

  result = PyList_New(a_rows);

  for (Py_ssize_t i = 0; i < a_rows; i++) {
    row = PyList_New(b_cols);
    for (Py_ssize_t j = 0; j < b_cols; j++) {
      sum = 0.0;
      for (Py_ssize_t k = 0; k < a_cols; k++) {
        val = PyList_GetItem(a, i);
        double a_val = PyFloat_AsDouble(PyList_GetItem(val, k));
        val = PyList_GetItem(b, k);
        double b_val = PyFloat_AsDouble(PyList_GetItem(val, j));
        sum += a_val * b_val;
      }
      PyList_SetItem(row, j, PyFloat_FromDouble(sum));
    }
    PyList_SetItem(result, i, row);
  }
  return result;
}

PyObject *foreign_matrix_power(PyObject *self, PyObject *args) {
  PyObject *matrix, *result;
  long power;

  if (!PyArg_ParseTuple(args, "Ol", &matrix, &power) || power < 1) {
    return NULL;
  }

  result = matrix;

  for (long i = 1; i < power; i++) {
    result = matrix_multiply(result, matrix);
    if (!result) {
      return NULL;
    }
  }

  return result;
}

static PyMethodDef MatrixMethods[] = {{"foreign_matrix_power",
                                       foreign_matrix_power, METH_VARARGS,
                                       "matrix power"},
                                      {NULL, NULL, 0, NULL}};

static struct PyModuleDef matrixmodule = {PyModuleDef_HEAD_INIT, "matrix_power",
                                          NULL, -1, MatrixMethods};

PyMODINIT_FUNC PyInit_matrix_power(void) {
  return PyModule_Create(&matrixmodule);
}
