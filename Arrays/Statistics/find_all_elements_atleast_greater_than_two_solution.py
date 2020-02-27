# lib imports
import array as ar
import sys

# Find kth largest element in array using heapify method
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1)
def findElements(arr, size):
    # find first and second largest element
    first = second = -sys.maxsize

    for i in range(size):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] > second:
            second = arr[i]
    
    # return all elements which are smaller than first and second
    result = ar.array('i', [])
    for i in range(size):
        if arr[i] < first and arr[i] < second:
            result.append(arr[i])

    return result

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
    arr = ar.array('i', [5, 3, 10, 8, 14, 0])
    printArray(arr, 'Original Array: ')
    # Find all elements smaller than two largest elements
    # Technique 1
    result = findElements(arr, len(arr))
    printArray(result, 'The resultant array is: ')