# lib imports
import numpy as np

# array movement imports
from Movement.move_all_zeroes_at_end_solution import moveZeroesAtEnd, moveZeroesAtEndUsingSwap
from Movement.double_element_and_move_all_zero_to_end_solution import doubleAndMoveZeroes

# array group imports
from Group.min_swaps_to_group_numbers_less_or_equal_k_solution import groupElementsSwap, groupElements
from Group.positive_and_negative_group_solution import groupPositiveAndNegative

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
    arr = np.array([5, 5, -1, 0, -3, 8, 0], dtype='int')
    search = 4
    printArray(arr, 'Original Array: ')

    # Move all zeroes at the end of array
    # Technique 1
    movedZeroesArray = moveZeroesAtEnd(np.copy(arr), len(arr))
    printArray(movedZeroesArray, 'After moving all zeroes at the end of array: ')

    # Technique 2
    movedZeroesArrayUsingSwap = moveZeroesAtEndUsingSwap(np.copy(arr), len(arr))
    printArray(movedZeroesArrayUsingSwap, 'After moving all zeroes at the end of array using swap technique: ')

    # Min swaps required to group all elements leeser than or equal to 'k'
    # Technique 1
    minSwapRequired = groupElementsSwap(np.copy(arr), len(arr), search)
    print(f'Min swaps required to group all elements leeser than or equal to {search}: ', minSwapRequired)

    # Technique 2
    groupedElementsLessEqualK = groupElements(np.copy(arr), len(arr), search)
    printArray(groupedElementsLessEqualK, f'Array after grouping all elements leeser than or equal to {search} together: ')

    # Group all positive and negative numbers such that all negative numbers are before positive numbers
    # Technique 1
    groupPositiveNegative = groupPositiveAndNegative(np.copy(arr), len(arr))
    printArray(groupPositiveNegative, 'After moving all negatives before positives: ')

    # Double the number if its same as next and non-zero and then move all zeroes at the end
    # Technique 1
    doubleAndMoveZeroesAtEnd = doubleAndMoveZeroes(np.copy(arr), len(arr))
    printArray(doubleAndMoveZeroesAtEnd, 'Double the number if its same as next and non-zero and then move all zeroes at the end: ')