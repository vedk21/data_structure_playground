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
