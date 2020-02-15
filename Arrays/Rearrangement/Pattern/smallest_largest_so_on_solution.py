# lib imports
import numpy as np

# Arrange array such that it has smallest number then largest number and so on
# Time Complexity: O(n(log n))
# Auxiliary Space Complexity: O(n)

def arrange(arr, size):

    # create template array copy
    temp = np.copy(arr)

    # sort the array
    temp.sort()

    # iterate over sorted array from both ends
    iterator = 0
    i = 0
    j = size - 1
    while(i <= j):
        arr[iterator] = temp[i]
        # check for array bounds if arr size is odd
        if iterator < size:
            arr[iterator+1] = temp[j]
        i += 1
        j -= 1
        iterator += 2

    return arr

# Time Complexity: O(n(log n))
# Auxiliary Space Complexity: O(1)
def arrangeWithoutExtraSpace(arr, size):
    # make use of remainder and quotient logic
    # Formula: a + b * max = result
    # a = result % max
    # b = result / max

    max_idx = size - 1
    min_idx = 0
    max_elment = arr[size-1] + 1

    for i in range(size):
        if i % 2 == 0:
            arr[i] += (arr[max_idx] % max_elment) * max_elment
            max_idx -= 1
        else:
            arr[i] += (arr[min_idx] % max_elment) * max_elment
            min_idx += 1

    for i in range(size):
        arr[i] /= max_elment

    return arr
