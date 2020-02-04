# Rotated and sorted search key imports
from Binary.sorted_rotated_array_search_solution import search as rotatedBinarySearch

# Pair of sum imports
from PairSum.sorted_rotated_array_pair_of_sum_solution import findPairOfSum, findAllPairOfSum

# Max sum for rotation imports
from MaxSum.RightRotation.max_sum_for_all_rotation_solution import findMaxSum as findMaxSumRightRotation

# Max sum for rotation imports
from MaxSum.LeftRotation.max_sum_for_all_rotation_solution import findMaxSum as findMaxSumLeftRotation

if __name__ == '__main__':
    arr = [4, 7, 8, 1, 3]
    # [7, 8, 1, 3, 4]
    # [1, 3, 4, 7, 8] 3 + 8 + 21 + 32
    key = 4
    sum = 11
    print(f'Original Array: {arr}')

    # Binary Search on rotated and sorted array
    # Technique 1
    searchKeyIndex = rotatedBinarySearch(list(arr), 0, len(arr) - 1, key)
    print(f'Search key={key} index in array (-1 if not found): {searchKeyIndex}')

    # Find pair with given sum on rotated and sorted array
    # Technique 1
    pairIndex = findPairOfSum(list(arr), len(arr), sum)
    print(f'Pair of index matching sum={sum} in array ([-1, -1] if not found): {pairIndex}')
    
    # Find all pairs with given sum on rotated and sorted array
    # Technique 1
    pairIndexes = findAllPairOfSum(list(arr), len(arr), sum)
    print(f'Pairs of indexes matching sum={sum} in array ([-1, -1] if not found): {pairIndexes}')

    # Find max sum for all right rotation on array
    # Technique 1
    maxRightRotationSum = findMaxSumRightRotation(list(arr), len(arr))
    print(f'Max sum for all Right rotation and number of rotation required in array: {maxRightRotationSum}')

    # Find max sum for all left rotation on array
    # Technique 1
    maxLeftRotationSum = findMaxSumLeftRotation(list(arr), len(arr))
    print(f'Max sum for all Left rotation and number of rotation required in array: {maxLeftRotationSum}')