# Rearrange array such that arr[arr[i]] becomes i for all elements in array
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1)
def arrangeIndexWise(arr, size):
    # use quotient and remainder technique for this
    # save the remainder as old value and quotient as new value
    # Given: old = a, new = b
    # Formula: a + b * size = result
    for i in range(size):
        # here i is the new value to stored at arr[arr[i]] and
        # arr[arr[i] % size] is old value
        # to get old value result % size
        arr[arr[i] % size] += i * size

    for i in range(size):
        # get the new value and save at arr[i]
        # to get new value result / size
        arr[i] /= size

    return arr
