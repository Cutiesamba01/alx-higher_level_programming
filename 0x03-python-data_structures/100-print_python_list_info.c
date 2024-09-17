#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints basic info about a python list
 * @p: a python object list
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, a;
	PyObject *item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "Error: Object is not a Python list\n");
		return;
	}

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %zd\n", size);

	/* Get the allocated size */
	printf("[*] Allocated = %zd\n", PyList_GET_SIZE(p));

	for (a = 0; a < size, a++)
	{
		item = PyList_GET_ITEM(p, a);
		printf("Element %zd: %s\n", Py_TYPE(item)->tp_name);
	}
}
