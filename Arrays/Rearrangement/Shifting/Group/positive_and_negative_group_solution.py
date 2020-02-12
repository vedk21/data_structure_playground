# Group all negative and positive numbers together such that all negative numbers are before positive
# and maintain the order
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1)

# helper functions
def rightRotate(arr, size, startIndex, endIndex):
    temp = arr[endIndex]
    for i in range(endIndex, startIndex, -1):
        arr[i] = arr[i - 1]
    arr[startIndex] = temp

    return arr

def groupPositiveAndNegative(arr, size):

    positiveNumberIndex = -1
    for i in range(size):

        if positiveNumberIndex >= 0:
            if arr[i] < 0:
                rightRotate(arr, size, positiveNumberIndex, i)
                positiveNumberIndex += 1

        if positiveNumberIndex == -1:
            if arr[i] >= 0:
                positiveNumberIndex = i

    return arr
