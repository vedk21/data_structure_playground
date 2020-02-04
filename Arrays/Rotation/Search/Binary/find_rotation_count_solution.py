from math import floor

# Find rotation count(k) on sorted as well as rotated array using binary search
# Time Complexity: O(log n)
# Auxiliary Space Complexity: O(1)
######### NOTE: This algorithm will not work if all elements in the array are not distinct ######### 
def findRotationCount(arr, startIndex, endIndex):
    if startIndex <= endIndex:
        # if startIndex and endIndex are same, we found the minimum number
        if startIndex == endIndex:
            return startIndex

        # calculate mid of the arr
        mid = floor((startIndex + endIndex) / 2)

        # if mid < endIndex and arr[mid+1] is less than arr[mid] then mid+1 is the minimum number
        if mid < endIndex and arr[mid+1] < arr[mid]:
            return mid+1
        
        # if mid > startIndex and arr[mid-1] is greater than arr[mid] then mid-1 is minimum number
        if mid > startIndex and arr[mid-1] > arr[mid]:
            return mid

        # now decide the search frame -> right or left
        # if arr[endIndex] > arr[mid] means minimum number lies in the left half of mid
        if arr[endIndex] > arr[mid]:
            return findRotationCount(arr, startIndex, mid - 1)
        # otherwise it belongs to right half of mid
        return findRotationCount(arr, mid + 1, endIndex)

    else:
        return 0
