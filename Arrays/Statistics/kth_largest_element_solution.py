# lib imports
from math import floor
import numpy as np

# Find kth largest element in array using heapify method
# Time Complexity: O(k + ((n-k)log(k)))
# Auxiliary Space Complexity: O(1)
def getHighestNonLeafNodesIndex(size):
    return floor(size/2) - 1

def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]
    return arr

def getLowestChildValue(arr, size, parentIndex):
    leftChildIndex = 2*parentIndex + 1
    rightChildIndex = 2*parentIndex + 2
    if rightChildIndex >= size:
        return leftChildIndex
    else:
        return leftChildIndex if arr[leftChildIndex] < arr[rightChildIndex] else rightChildIndex

def shiftDown(arr, size, currentIndex):
    # base condition (if leaf node return)
    if currentIndex > getHighestNonLeafNodesIndex(size):
        return arr

    lowestChildIndex = getLowestChildValue(arr, size, currentIndex)
    if(arr[lowestChildIndex] < arr[currentIndex]):
        arr = swap(arr, currentIndex, lowestChildIndex)
        arr = shiftDown(arr, size, lowestChildIndex)

    return arr

def heapify(arr, size):
    nonLeafIndex = getHighestNonLeafNodesIndex(size)
    # loop for all non-leaf elements
    while(nonLeafIndex >= 0):
        arr = shiftDown(arr, size, nonLeafIndex)

        nonLeafIndex -= 1

    return arr

def kthLargestUsingHeapify(arr, size, k):
    if k < 0 or k > size:
        return None
    else:
        arr = heapify(arr, k)

    # go for k -> size -1
    iterator = k
    while(iterator < size):
        if arr[0] < arr[iterator]:
            arr[0] = arr[iterator]
            arr = heapify(arr, k)
        iterator += 1
    
    return arr[0]

# Find kth largest element in array using quick select method
# Time Complexity: O(n2) and Theta(n) average case
# Auxiliary Space Complexity: O(1)
def findPivotIndex(arr, start=0, end=None):
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

    return pivotIndex

def quick_sort(arr, k, size, left=0, right=None,):
    if right is None:
        right = len(arr) - 1

    if left < right:
        pivotIndex = findPivotIndex(arr, left, right)

        # put the pivot element at pivot index
        arr[left], arr[pivotIndex] = arr[pivotIndex], arr[left]

        # if pivotIndex is k then return arr[pivotIndex]
        if (size - pivotIndex) == k:
            return arr[pivotIndex]
        # if pivotIndex is lesser than k then recur left subarray
        if (size - pivotIndex) < k:
            return quick_sort(arr, k, size, left, pivotIndex)
        # if pivotIndex is greater than k then recur right subarray
        if (size - pivotIndex) > k:
            return quick_sort(arr, k, size, pivotIndex+1, right)

def kthLargestUsingQuickSelect(arr, size, k):
    if k > 0 and k <= size:
        return quick_sort(arr, k, size, 0, size - 1)
    else:
        return None

# helper function
def printArray(arr, msg):
    print(msg, end="")
    print('[', end="")
    for i in range(len(arr)):
        if i < len(arr) - 1:
            print(arr[i], end=", ")
        else:
            print(arr[i], end=']\n')

if __name__ == '__main__':
    arr = np.array([5, 3, 10, 8, 14, 0], dtype='int')
    k = 1
    printArray(arr, 'Original Array: ')
    # Find kth largest element in array using healpfy technique
    # Technique 1
    print(f'The {k}th largest element in array using heapify method is: {kthLargestUsingHeapify(np.copy(arr), len(arr), k)}')
    print(f'The {k}th largest element in array using quick select method is: {kthLargestUsingQuickSelect(np.copy(arr), len(arr), k)}')
