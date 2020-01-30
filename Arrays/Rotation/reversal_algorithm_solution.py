# Array rotation by using reversal algorithm
# n size of the array and d is the rotation by count
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1)
def swap(arr, startIndex, endIndex):
    temp = arr[startIndex]
    arr[startIndex] = arr[endIndex]
    arr[endIndex] = temp
    return arr

def reverse(arr, startIndex, endIndex):
    while(startIndex < endIndex):
        arr = swap(arr, startIndex, endIndex)
        startIndex += 1
        endIndex -= 1
    return arr

def rotate(arr, size, rotateBy):
    if (size > 0) and (rotateBy % size != 0):
        # reverse 0 to rotateBy - 1
        arr = reverse(arr, 0, rotateBy - 1)
        # reverse rotateBy to size -1
        arr = reverse(arr, rotateBy, size - 1)
        # reverse complete array now
        arr = reverse(arr, 0, size - 1)
    return arr
