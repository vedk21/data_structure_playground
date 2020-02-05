# Find array rotation for maximum hamming distance
# Time Complexity: O(n*n)
# Auxiliary Space Complexity: O(2n)
def findMaxHammingDistance(arr, size):
    # create arr with 2*size and duplicate original array
    arrCopy = arr
    for i in range(size):
        arrCopy.append(arr[i])

    maxHammingDistance = 0
    numberOfRotation = 0

    for i in range(1, size):
        j = i
        k = 0
        currentHammingDistance = 0
        while(j < (i + size)):
            # check if original array ele is same as rotated array ele
            if arrCopy[j] != arrCopy[k]:
                currentHammingDistance += 1
            
            # if maxHammingDistance is same as size return maxHammingDistance
            if currentHammingDistance == size:
                return {'distance': currentHammingDistance, 'rotation': numberOfRotation}
            
            j += 1
            k += 1

        if currentHammingDistance > maxHammingDistance:
            maxHammingDistance = currentHammingDistance
            numberOfRotation = i
        
    return {'distance': maxHammingDistance, 'rotation': numberOfRotation}
