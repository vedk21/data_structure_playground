# Array rotation by moving element one by one technique
def rotate(arr, size, rotateBy):
    if size > 0:
        # repeat the process for number of rotation
        for _ in range(0, rotateBy):
            temp = arr[0]
            # move element i to i - 1 one by one
            for i in range(1, size):
                arr[i - 1] = arr[i]
            # move temp element back into last location in array
            arr[size - 1] = temp
        return arr
    else:
        return arr
