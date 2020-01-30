# Array rotation using juggling algorithm technique
# n size of the array and d is the rotation by count
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1)
def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)

def rotate(arr, size, rotateBy):
    if (size > 0) and (rotateBy % size != 0):
        # calculate number of sets required using gcd of size and rotateBy
        sets = gcd(size, rotateBy)
        for i in range(sets):
            temp = arr[i]
            iteration = i
            # repeat for all i + rotateBy elements until the end of array
            while((iteration + rotateBy) < size):
                arr[iteration] = arr[iteration + rotateBy]
                iteration = iteration + rotateBy
            arr[iteration] = temp
    return arr
