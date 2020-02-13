# lib imports
import numpy as np

# Pattern arr[i] = i imports
from Pattern.index_at_element_pattern_solution import arrangeUsingIteration, arrangeUsingSwap

# Pattern arr[i] >= arr[j] even positions, j < i
from Pattern.element_even_position_odd_position_solution import arrange as arrangeEvenOdd

# Pattern alternate positive and negative elements
from Pattern.alternate_positive_negative_numbers_solution import arrange as arrangeAlternatePosNeg, arrangeInSeq as arrangeAlternatePosNegSeq

# Pattern smallest element and then largest element and so on...
from Pattern.smallest_largest_so_on_solution import arrange as arrangeSmallestLargestSoOn

# Pattern to reorder array according to indexes array
from Pattern.reorder_array_according_to_index_array_solution import reorderUsingArray, reorderUsingSort

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
    # arr = Array.array('i', [-1, 3, 5, 8, -1, 0])
    arr = np.array([5, 3, -1, 8, -1, 0], dtype='int')
    indexes = np.array([5, 0, 1, 2, 3, 4], dtype='int')
    printArray(arr, 'Original Array: ')
    printArray(indexes, 'Indexes Array: ')

    # Arrange array such that arr[i] = i or else -1
    # Technique 1
    indexArrangedArray = arrangeUsingIteration(np.copy(arr), len(arr))
    printArray(indexArrangedArray, 'Index element arranged array using rotation technique is: ')

    # Technique 2
    indexArrangedArraySwap = arrangeUsingSwap(np.copy(arr), len(arr))
    printArray(indexArrangedArraySwap, 'Index element arranged array using swap technique is: ')

    # Arrange array such that arr[i] >= arr[j] if i is even and arr[i] <= arr[j] if i is odd, i > j
    # Technique 1
    evenOddArrangedArray = arrangeEvenOdd(np.copy(arr), len(arr))
    printArray(evenOddArrangedArray, 'Elements arranged according to even odd positions: ')
    
    # Arrange array such that positive and negative elements are alternate to each other
    # Technique 1
    alternatePosNegArrangedArray = arrangeAlternatePosNeg(np.copy(arr), len(arr))
    printArray(alternatePosNegArrangedArray, 'Elements after arranging alternate positive and negative: ')

    # Arrange array such that positive and negative elements are alternate to each other maintaining the original sequence
    # Technique 1
    alternatePosNegArrangedSeqArray = arrangeAlternatePosNegSeq(np.copy(arr), len(arr))
    printArray(alternatePosNegArrangedSeqArray, 'Elements after arranging alternate positive and negative (maintaining original sequence): ')
    
    # Arrange array such that smallest number and then largest number so on...
    # Technique 1
    smallestLargestSoOn = arrangeSmallestLargestSoOn(np.copy(arr), len(arr))
    printArray(smallestLargestSoOn, 'Smallest, largest, second smallest, second largest and so on...: ')
    
    # Reorder array according to indexes array
    # Technique 1
    reorderedArrayUsingExtraArray = reorderUsingArray(np.copy(arr), len(arr), np.copy(indexes))
    printArray(reorderedArrayUsingExtraArray, 'Reordered array according to index array using extra array: ')

    # Technique 2
    reorderedArrayUsingSort = reorderUsingSort(np.copy(arr), len(arr), np.copy(indexes))
    printArray(reorderedArrayUsingSort, 'Reordered array according to index array using sorting: ')