# Array rotation using temperory array technique
# n size of the array and d is the rotation by count
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(d)
def rotate(arr, size, rotateBy):
    if (size > 0) and (rotateBy % size != 0):
        tempArr = []
        # add elements into temp array of size 'rotateBy'
        for i in range(0, rotateBy):
            tempArr.append(arr[i])

        # shift rest of the array
        shiftIndex = 0
        for i in range(rotateBy, size):
            arr[shiftIndex] = arr[i]
            shiftIndex += 1

        # store the temp array elements at the end of array
        shiftBackIndex = size - rotateBy
        tempIndex = 0
        for i in range(shiftBackIndex, size):
            arr[i] = tempArr[tempIndex]
            tempIndex += 1

    return arr
