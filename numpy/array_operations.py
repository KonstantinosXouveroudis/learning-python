import numpy as np

def basic_operations():
    # 2D array
    array1 = np.array([[1, 2], [3, 4], [5, 6]])
    print("Array dimensions: ", array1.ndim)
    # ravel() flattens the array and makes it one-dimensional

    print(array1)
    print("Byte size of each individual element in the array: ", array1.itemsize)
    print("Data type of array: ", array1.dtype)
    print("Number of elements ", array1.size)
    print("\n(Rows, Columns): ", array1.shape)
    print("\nReshape:\n ", array1.reshape(2, 3))

    array2 = np.array([[1, 2], [3, 4], [5, 6]], dtype=complex)
    print("\n", array2)

    zeros_array = np.zeros((3, 4))
    print("\n", zeros_array)

    ones_array = np.ones((3, 4))
    print("\n", ones_array)

    print("\n-------------------------------")

    array3 = np.arange(1, 5)
    print("\n", array3)

    array4 = np.arange(1, 5, 2)  # Steps of 2
    print("\n", array4)

    array5 = np.linspace(1, 5, 10)  # Linearly spaced
    print("\n", array5)

    print("Min: ", array5.min(), "\nMax: ", array5.max())


def select_array_parts(a):
    print("\n1st row, 2nd column: ", a[1, 2])  # count from 0
    print("First 2 rows, 2nd column: ", a[0:2, 2])
    print("Last row: ", a[-1])
    print("Last row, first 2 columns: ", a[-1, 0:2])
    print("First 2 rows, last 2 columns:\n ", a[0:2, 1:3])

    print("\nLast 2 columns:\n ", a[:, 1:3])


def iterating_examples(a):
    for row in a:
        print(row)

    print("Flattening the numpy array:")
    for cell in a.flat:
        print(cell)


def array_stack():
    b = np.arange(6).reshape(3, 2)
    c = np.arange(6, 12).reshape(3, 2)

    print("Stacking arrays a and b together (vertical):\n", np.vstack((b, c)))
    print("\nStacking arrays a and b together (horizontal):\n", np.hstack((b, c)))


def array_split():
    c = np.arange(30).reshape(2, 15)
    csplit = np.hsplit(c, 3)
    print("\nOriginal array:\n", c, "\n\nAfter horizontal split:")
    for piece in csplit:
        print(piece)

    csplit = np.vsplit(c, 2)
    print("\nAfter vertical split:")
    for piece in csplit:
        print(piece)


if __name__ == '__main__':
    a = np.array([6, 7, 8])
    # print("First 2 elements:", a[0:2])

    a = np.array([[6, 7, 8], [1, 2, 3], [9, 3, 2]])
    # select_array_parts(a)
    # iterating_examples(a)

    # array_stack()
    # array_split()

    array_bool = a > 4
    print("Indexing with booleans:\n", array_bool)
    print("All array elements greater than 4: ", a[array_bool])

    a[array_bool] = -1
    print("All array elements greater than 4 where replaced with -1:\n", a)

    print()
    a = np.arange(12).reshape(3, 4)
    for x in np.nditer(a, order='C'):  # C order
        print(x)

    print()
    for x in np.nditer(a, order='F'):  # Fortran order
        print(x)

