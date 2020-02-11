# Rearrange array such that positive and negative elements are alternate to each other,
# if positive or negative numbers are more then arrange them all at end
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1)

# helper functions
def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]
    return arr

def rightRotate(arr, size, startIndex, endIndex):
    temp = arr[endIndex]
    for i in range(endIndex, startIndex, -1):
        arr[i] = arr[i - 1]
    arr[startIndex] = temp

    return arr

def arrange(arr, size):
    # divide array into positive and negative parts
    i = 0
    for j in range(size):
        if arr[j] < 0:
            arr = swap(arr, j, i)
            i += 1

    # get index for positive and negative elements
    positive = i
    negative = 0

    # increase negative index by 2 and positive index by 1 and swap elements
    while(positive < size and negative < positive and arr[negative] < 0):
        arr = swap(arr, positive, negative)
        negative += 2
        positive += 1

    return arr

# Rearrange array such that positive and negative elements are alternate to each other,
# if positive or negative numbers are more then arrange them all at end
# here we maintain the initial sequence
def arrangeInSeq(arr, size):
    outOfPlaceIndex = -1
    
    for i in range(size):

        if outOfPlaceIndex >= 0:
            if (arr[i] < 0 and arr[outOfPlaceIndex] >= 0) or (arr[i] >= 0 and arr[outOfPlaceIndex] < 0):
                arr = rightRotate(arr, size, outOfPlaceIndex, i)

                # rearrange outOfPlaceIndex
                if i - outOfPlaceIndex >= 2:
                    outOfPlaceIndex += 2
                else:
                    outOfPlaceIndex = -1

        if outOfPlaceIndex == -1:
            if (arr[i] < 0 and i % 2 == 0) or (arr[i] >= 0 and i % 2 != 0):
                outOfPlaceIndex = i

    return arr
