# Array cyclic rotation by one position to right
def cyclicRotate(arr, size):
    if size > 0:
        temp = arr[size - 1]
        for i in range(size - 1, 0, -1):
            arr[i] = arr[i - 1]
        arr[0] = temp
    return arr