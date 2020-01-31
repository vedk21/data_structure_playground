# Rotated and sorted search key imports
from Binary.sorted_rotated_array_search_solution import search as rotatedBinarySearch

# Pair of sum imports
from PairSum.sorted_rotated_array_pair_of_sum_solution import findPairOfSum, findAllPairOfSum

# Max sum for rotation imports
from MaxSum.max_sum_for_all_rotation_solution import findMaxSum

if __name__ == '__main__':
    arr = [4, 7, 8, 1, 3]
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

    # Find max sum for all rotation on array
    # Technique 1
    maxRotationSum = findMaxSum(list(arr), len(arr))
    print(f'Max sum for all rotation and number of rotation required in array: {maxRotationSum}')