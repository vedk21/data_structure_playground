# Find max sum for all right rotations of an array max(sum(i * arr[i]))
# NOTE: Rj - Rj-1 = arrSum - n * arr[n - j], Also here right rotation is considered
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1)
def findMaxSum(arr, size):
    sum = 0
    currentRotationSum = 0
    # calculate sum of all array elements
    for i in range(size):
        sum += arr[i]
        # calculate i * arr[i] for no rotation (R0)
        currentRotationSum += i * arr[i]    
    
    maxRotationSum = currentRotationSum
    maxSumRotation = 0
    
    # calculate all other rotation sum using given formula from 1 -> size - 1
    for i in range(1, size):
        currentRotationSum += sum - (size * arr[size - i])
        # check if currentRotationSum is greater than maxRotationSum
        if currentRotationSum > maxRotationSum:
            maxRotationSum = currentRotationSum
            maxSumRotation = i

    return {'maxSum':maxRotationSum, 'right_rotation': maxSumRotation}
