# Rearrange array such that arr[i] = i and if element is not present in array show -1
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1)
def arrangeUsingIteration(arr, size):
    for i in range(size):
        # check if current element is not -1 or i
        if arr[i] != -1 and arr[i] != i:
            # store current element in temp variable
            x = arr[i]

            # check if element is out of array bound
            if x >= 0 and x < size:
                # check until desired place(x) is not -1 or x
                while(arr[x] != -1 and arr[x] != x):
                    # store current arr[x] in temp variable
                    y = arr[x]

                    # save x to arr[x] now
                    arr[x] = x

                    # check if element is out of array bound
                    if y >= 0 and y < size:
                        # assign x as y, to make sure y also goes to its desired location index
                        x = y
                    else:
                        break
                
                # place x to its correct position (this executes if arr[x] == -1 or x)
                arr[x] = x

                # check if arr[i] has correct element, if not save -1
                if arr[i] != i:
                    arr[i] = -1

            else:
                arr[i] = -1

    return arr

def arrangeUsingSwap(arr, size):
    i = 0
    while(i < size):
        # check if element is out of array bound
        if arr[i] >= 0 and arr[i] < size:
            if arr[i] != -1 and arr[i] != i:
                # check if element is out of array bound
                if arr[arr[i]] >= 0 and arr[arr[i]] < size:
                    # swap elements
                    arr[i], arr[arr[i]] = arr[arr[i]], arr[i]
                else:
                    arr[arr[i]] = arr[i]
            else:
                i += 1
        else:
            arr[i] = -1
            i += 1

    return arr