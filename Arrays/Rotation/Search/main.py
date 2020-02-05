# Rotated and sorted search key imports
from Binary.sorted_rotated_array_search_solution import search as rotatedBinarySearch

# Pair of sum imports
from PairSum.sorted_rotated_array_pair_of_sum_solution import findPairOfSum, findAllPairOfSum

# Max sum for rotation imports
from MaxSum.RightRotation.max_sum_for_all_rotation_solution import findMaxSum as findMaxSumRightRotation

# Max sum for rotation imports
from MaxSum.LeftRotation.max_sum_for_all_rotation_solution import findMaxSum as findMaxSumLeftRotation

# Find rotation count(k)
from Binary.find_rotation_count_solution import findRotationCount

# Find rotation for max hamming distance
from HammingDistance.rotation_for_max_hamming_distance_solution import findMaxHammingDistance

# Find element at index for number of rotations
from Binary.element_at_index_for_number_of_rotation_solution import findElement

if __name__ == '__main__':
    arr = [7, 1, 1, 1, 4]
    # [7, 8, 1, 3, 4]
    # [1, 3, 4, 7, 8] 3 + 8 + 21 + 32
    key = 4
    sum = 11
    queries = [(0, 3), (1, 3)]
    index = 0
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

    # Find right rotation count(k) on array
    # Technique 1
    rotationCount = findRotationCount(list(arr), 0, len(arr) - 1)
    print(f'Right rotation count(k) in rotated array: {rotationCount}')

    # Find max hamming disatnce and left rotation count
    # Technique 1
    hammingDistanceRotation = findMaxHammingDistance(list(arr), len(arr))
    print(f'Left rotation and max hamming distance is: {hammingDistanceRotation}')

    # Find element at index after series of rotations
    # Technique 1
    elementAtIndex = findElement(list(arr), len(arr), queries, index)
    print(f'Element at index {index} after these series of rotations {queries}(-999999 if inputs are wrong): {elementAtIndex}')