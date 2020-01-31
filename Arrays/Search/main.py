# Binary search imports
from Binary.sorted_rotated_array_search_solution import search as rotatedBinarySearch

if __name__ == '__main__':
    arr = [1, 3, 4, 6, 7]
    key = 4
    print(f'Original Array: {arr}')
    print(f'Search Key: {key}')

    # Binary Search on rotated and sorted array
    # Technique 1
    searchKeyIndex = rotatedBinarySearch(list(arr), 0, len(arr) - 1, key)
    print(f'Search key index in array (-1 if not found): {searchKeyIndex}')