# Move all zeroes at the end of array by maintaining the original order/sequence
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1)

# helper functions
def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]
    return arr

def moveZeroesAtEnd(arr, size):
    count = 0

    for i in range(size):
        # all non-zero element set to the front side of array
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    
    # the remaining places in array are filled with zeroes
    while(count < size):
        arr[count] = 0
        count += 1

    return arr

def moveZeroesAtEndUsingSwap(arr, size):
    count = 0

    for i in range(size):
        # all non-zero element set to the front side of array
        if arr[i] != 0:
            swap(arr, i, count)
            count += 1
    
    return arr
