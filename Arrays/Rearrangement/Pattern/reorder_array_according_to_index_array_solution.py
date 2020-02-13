# standard library packages and modules
import array as ar

# Reorder the array according to index array
# Time Complexity: O(n2)
# Auxiliary Space Complexity: O(1)
def reorderUsingArray(arr, size, indexes):
    for i in range(size):

        # unless we find correct number at ith location
        while(indexes[i] != i):
            # swap indexes[i] with indexes[indexes[i]]
            tempIndexValue = indexes[indexes[i]]
            tempArrayValue = arr[indexes[i]]

            indexes[indexes[i]] = indexes[i]
            arr[indexes[i]] = arr[i]

            indexes[i] = tempIndexValue
            arr[i] = tempArrayValue
    
    return arr

def findPivotIndex(arr, secondaryArray, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    pivot = arr[start]
    pivotIndex = start
    # find the appropriate pivot index and return
    for i in range(start + 1, end + 1):
        if arr[i] < pivot:
            # increase pivot index until we find numbers less than pivot element
            pivotIndex += 1
            arr[i], arr[pivotIndex] = arr[pivotIndex], arr[i]
            secondaryArray[i], secondaryArray[pivotIndex] = secondaryArray[pivotIndex], secondaryArray[i]

    return pivotIndex

def quick_sort(arr, secondaryArray, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left < right:
        pivotIndex = findPivotIndex(arr, secondaryArray, left, right)

        # put the pivot element at pivot index
        arr[left], arr[pivotIndex] = arr[pivotIndex], arr[left]
        secondaryArray[left], secondaryArray[pivotIndex] = secondaryArray[pivotIndex], secondaryArray[left]

        resLeft = quick_sort(arr, secondaryArray, left, pivotIndex)
        arr = resLeft['indexes']
        secondaryArray = resLeft['array']
        resRight = quick_sort(arr, secondaryArray, pivotIndex+1, right)
        arr = resRight['indexes']
        secondaryArray = resRight['array']

    return {'indexes': arr, 'array': secondaryArray}

# Reorder the array according to index array using sort
# Time Complexity: O(n log(n))
# Auxiliary Space Complexity: O(1)
def reorderUsingSort(arr, size, indexes):
    # sort the indexes array accordingly original array will be sorted according to indexes
    result = quick_sort(indexes, arr, 0, size - 1)
    return result['array']
