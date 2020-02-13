# Reorder the array according to index array
# Time Complexity: O(n log(n))
# Auxiliary Space Complexity: O(1)
def reorderUsingArray(arr, size, indexes):
    for i in range(size):

        # unless we find correct number at ith location
        while(indexes[i] != i):
            # swap indexes[i] with indexes[indexes[i]]
            tempIndexValue = indexes[indexes[i]]
            tempArrayValue = arr[indexes[i]]

            indexes[indexes[i]] = indexes[i]
            arr[indexes[i]] = arr[i]

            indexes[i] = tempIndexValue
            arr[i] = tempArrayValue
    
    return arr
