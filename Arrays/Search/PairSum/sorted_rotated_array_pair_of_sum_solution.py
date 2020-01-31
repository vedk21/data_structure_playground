# Search for an pair of sum on sorted as well as rotated array
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1)
######### NOTE: This algorithm will not work if all elements in the array are not distinct #########
def findPairOfSum(arr, size, sum):
    if (size > 1):
        # find max element in the array
        i = 0
        while(i < (size - 1)):
            if arr[i] > arr[i + 1]:
                break
            i += 1
        
        smallestElementIndex = (i + 1) % size
        largestElementIndex = i

        while (smallestElementIndex != largestElementIndex):
            pairSum = arr[smallestElementIndex] + arr[largestElementIndex]
            if pairSum == sum:
                return [smallestElementIndex, largestElementIndex]
            
            # if current pair sum is lesser then move smallestElementIndex to right
            if pairSum < sum:
                smallestElementIndex = (smallestElementIndex + 1) % size
            # else move largestElementIndex to left
            else:
                largestElementIndex = (size + largestElementIndex - 1) % size
        
        # if reached here means no pair with given sum found, return -1
        return -1
    else:
        return -1

def findAllPairOfSum(arr, size, sum):
    if size > 1:
        # find max element in the array
        i = 0
        while(i < (size - 1)):
            if arr[i] > arr[i + 1]:
                break
            i += 1
        
        smallestElementIndex = (i + 1) % size
        largestElementIndex = i

        # keep note of all indexes
        indexes = []

        while(smallestElementIndex != largestElementIndex):
            pairSum = arr[smallestElementIndex] + arr[largestElementIndex]
            if pairSum == sum:
                indexes.append([smallestElementIndex, largestElementIndex])

                # check if smallestElementIndex and largestElementIndex haven't crossed each other
                if smallestElementIndex == ((size + largestElementIndex - 1) % size):
                    return indexes
                if ((smallestElementIndex + 1) % size) == largestElementIndex:
                    return indexes

            # if current pair sum is lesser then move smallestElementIndex to right
            if pairSum < sum:
                smallestElementIndex = (smallestElementIndex + 1) % size
            # else move largestElementIndex to left
            else:
                largestElementIndex = (size + largestElementIndex - 1) % size

        # if reached here and indexes are empty means not a single pair found, return -1
        if len(indexes) > 0:
            return indexes
        else:
            return -1
    else:
        return -1
