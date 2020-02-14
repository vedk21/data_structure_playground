# standard library packages and modules
import array as ar

# Reorder the array according to index array
# Time Complexity: O(n log(n))
# Auxiliary Space Complexity: O(1)

# function to check if a is greater than b
def isGreater(a, b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)

    if (int(ba) - int(ab)) < (int(ab) - int(ba)):
        return True
    return False

def merge(arr1, arr2):
    result = ar.array('i', [])
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if (isGreater(arr1[i], arr2[j])):
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result

def merge_sort(arr):

    if (len(arr) <= 1):
        return arr

    mid = (len(arr) // 2)
    leftArr = merge_sort(arr[:mid])
    rightArr = merge_sort(arr[mid:])
    arr = merge(leftArr, rightArr)
    return arr

def arrangeToFormLargestNumber(arr, size):
    descendingSortedArray = merge_sort(arr)

    stringArray = [str(i) for i in descendingSortedArray]
    return int("".join(stringArray))
