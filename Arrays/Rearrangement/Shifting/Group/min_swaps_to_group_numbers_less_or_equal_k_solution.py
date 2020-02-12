# Minimum number of swaps required to group all numbers less or equal to 'k' in array
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1)

# helper functions
def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]
    return arr

def min(a, b):
    if a < b:
        return a
    return b

def groupElementsSwap(arr, size, k):
    count = 0
    largeNumbers = 0
    # count number less or equal to k in arr
    for i in range(size):
        if arr[i] <= k:
            count += 1
    
    # count number of elements more than k in window 0 -> count - 1
    for i in range(count):
        if arr[i] > k:
            largeNumbers += 1
    
    # initialize number swaps to largeNumbers
    swaps = largeNumbers

    left = 0
    right = count
    # find number of swaps in every window of size count
    while(right < size):
        # Decrement count of previous window
        if arr[left] > k:
            largeNumbers -= 1

        if arr[right] > k:
            largeNumbers += 1

        swaps = min(swaps, largeNumbers)
        right += 1
        left += 1

    return swaps

def groupElements(arr, size, k):
    count = 0
    # count number less or equal to k in arr
    for i in range(size):
        if arr[i] <= k:
            count += 1
    
    # swap elements lesset than or equal to 'k' with larger numbers
    i = 0
    j = count
    while(i < count and j < size):

        if arr[i] > k:
            if arr[j] <= k:
                swap(arr, i, j)
                i += 1
            j += 1
        else:
            i += 1

    return arr
