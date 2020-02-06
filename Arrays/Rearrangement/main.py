# lib imports
import array as Array

# Pattern arr[i] = i imports
from Pattern.index_at_element_pattern_solution import arrangeUsingIteration, arrangeUsingSwap

# helper function
def printArray(arr, msg):
    print(msg, end="")
    for i in range(len(arr)):
        if i < len(arr) - 1:
            print(arr[i], end=", ")
        else:
            print(arr[i])

# main function to try and understand different rotation techniques on array
if __name__ == '__main__':
    arr = Array.array('i', [-1, 3, 5, 8, -1, 0])
    printArray(arr, 'Original Array: ')

    # Arrange array such that arr[i] = i or else -1
    # Technique 1
    indexArrangedArray = arrangeUsingIteration(arr, len(arr))
    printArray(indexArrangedArray, 'Index element arranged array using rotation technique is: ')

    # Technique 2
    indexArrangedArraySwap = arrangeUsingSwap(arr, len(arr))
    printArray(indexArrangedArraySwap, 'Index element arranged array using swap technique is: ')