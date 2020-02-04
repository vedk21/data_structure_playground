from math import floor

# Search on sorted as well as rotated array using binary search
# Time Complexity: O(log n)
# Auxiliary Space Complexity: O(1)
######### NOTE: This algorithm will not work if all elements in the array are not distinct ######### 
def search(arr, startIndex, endIndex, key):
    if startIndex <= endIndex:
        # calculate mid of the arr
        mid = floor((startIndex + endIndex) / 2)
        
        # if arr[mid] is key return the mid
        if arr[mid] == key:
            return mid
        
        # check if startIndex -> mid is sorted or not
        if arr[startIndex] <= arr[mid]:
            # check if key lies in range of arr[startIndex] -> arr[mid]
            if (key >= arr[startIndex]) and (key <= arr[mid]):
                return search(arr, startIndex, mid - 1, key)
            else:
                return search(arr, mid + 1, endIndex, key)
        else:
            # check if key lies in range of arr[mid + 1] -> arr[endIndex]
            if (key >= arr[mid + 1]) and (key <= arr[endIndex]):
                return search(arr, mid + 1, endIndex, key)
            else:
                return search(arr, startIndex, mid - 1, key)
    else:
        return -1
