# Quickly print the left rotation of the array (without actually rotating the array)
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1)
def printLeftRotation(arr, size, rotateBy):
    # loop -> start = rotateBy and end = rotateBy + size
    for i in range(rotateBy, (rotateBy + size)):
        print(arr[i%size], end=', ')
