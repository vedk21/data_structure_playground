# lib imports
import numpy as np

# array movement imports
from Movement.move_all_zeroes_at_end_solution import moveZeroesAtEnd

# helper function
def printArray(arr, msg):
    print(msg, end="")
    print('[', end="")
    for i in range(len(arr)):
        if i < len(arr) - 1:
            print(arr[i], end=", ")
        else:
            print(arr[i], end=']\n')

# main function to try and understand different rearrangement techniques on array
if __name__ == '__main__':
    arr = np.array([0, 3, 0, 4, 8, 0], dtype='int')
    printArray(arr, 'Original Array: ')

    # Move all zeroes at the end of array
    # Technique 1
    movedZeroesArray = moveZeroesAtEnd(np.copy(arr), len(arr))
    printArray(movedZeroesArray, 'After moving all zeroes at the end of array: ')