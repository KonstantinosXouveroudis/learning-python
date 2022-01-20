import numpy as np
import time
import sys


# Comparing numpy arrays to Python's regular lists.

def compare_sizes():
    my_list = range(1000)
    print(sys.getsizeof(1) * len(my_list))  # Size of the list

    np_array = np.arange(1000)
    print(np_array.size * np_array.itemsize)  # Length of np_array * size of one of its elements


def measure_time():
    # Measuring the processing time between Python lists and numpy arrays:
    size = 1000000
    list1 = range(size)
    list2 = range(size)

    array1 = np.arange(size)
    array2 = np.arange(size)

    # Python list
    start = time.time()
    # Adding the corresponding elements of the 2 lists in each corresponding index together
    result = [(x + y) for x, y in zip(list1, list2)]
    # print(result)
    print("The processing of the python lists took ", (time.time() - start) * 1000, " milliseconds")

    # numpy array
    start = time.time()
    result = array1 + array2
    print("The processing of the numpy arrays took ", (time.time() - start) * 1000, " milliseconds")


if __name__ == '__main__':
    measure_time()
