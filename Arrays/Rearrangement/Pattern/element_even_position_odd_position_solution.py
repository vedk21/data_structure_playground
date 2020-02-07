# lib imports
from math import floor
import numpy as np

# Rearrange array such that element at even position is greater than all of its element before,
# and element at odd position is smaller than all of its element before
# Time Complexity: O(n log(n))
# Auxiliary Space Complexity: O(n)
def arrange(arr, size):
    # find number of even and odd positions in array
    even = int(floor(size / 2))
    odd = size - even

    # create template array copy
    temp = np.array([], dtype='int')
    for i in range(size):
        temp = np.append(temp, [arr[i]])

    # sort the template array
    temp.sort()

    iterator = odd - 1

    # add elements on odd positions
    for i in range(0, size, 2):
        arr[i] = temp[iterator]
        iterator -= 1

    iterator = odd

    # add elements on even positions
    for i in range(1, size, 2):
        arr[i] = temp[iterator]
        iterator += 1
    
    return arr
