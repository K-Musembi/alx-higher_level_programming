#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - print python list information
 * @p: input
 *
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t j;
	PyObject *obj;

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", list->allocated);
	for (j = 0; j < PyList_Size(p); ++j)
	{
		obj = PyList_GetItem(p, j);
		printf("Element %ld: %s\n", j, PyTYPE(obj)->tp_name);
	}
}
