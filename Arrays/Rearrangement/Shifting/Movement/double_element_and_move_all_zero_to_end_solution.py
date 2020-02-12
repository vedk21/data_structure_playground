# internal imports
# pylint: disable=relative-beyond-top-level
from .move_all_zeroes_at_end_solution import moveZeroesAtEndUsingSwap

# If arr[i] == arr[i+1] then double arr[i] and set arr[i] = 0 for every non-zero element
# in the end move all zeroes in the end
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1)
def doubleAndMoveZeroes(arr, size):
    # iterate till size - 1
    i = 0
    while(i < (size - 1)):
        if arr[i] != 0 and arr[i] == arr[i+1]:
            arr[i] = arr[i] * 2
            arr[i+1] = 0
            i += 2
        else:
            i += 1
    
    # move all zeroes to end now
    return moveZeroesAtEndUsingSwap(arr, size)
