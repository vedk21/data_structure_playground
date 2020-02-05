# Find element at index after queries of rotation on array
# Time Complexity: O(1)
# Auxiliary Space Complexity: O(1)
def findElement(arr, size, queries, index):
    # iterate over queries in reverse order
    for i in range(len(queries) - 1, -1, -1):
        left = queries[i][0]
        right = queries[i][1]

        # check if left, right and index are in bounds of array given
        if left < size and right < size and index < size:
            if index >= left and index <= right:
                if index == left:
                    index = right
                else:
                    index -= 1
        else:
            # means wrong input bounds are given, please check the input
            return -999999
    
    return arr[index]
