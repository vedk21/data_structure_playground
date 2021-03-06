#Left rotation imports
from Left.temp_array_solution import rotate as tempRotate
from Left.rotate_one_by_one_solution import rotate as oneByOneRotate
from Left.juggling_algorithm_solution import rotate as jugglingRotate
from Left.reversal_algorithm_solution import rotate as reversalRotate

# cyclic rotation imports
from Cyclic.cyclic_rotation_solution import cyclicRotate

# print left rotations on array imports
from Left.print_different_rotation_solution import printLeftRotation

# Right rotation imports
from Right.reversal_algorithm_solution import rotate as rightReversalRotate

# main function to try and understand different rotation techniques on array
if __name__ == '__main__':
    arr = [1, 3, 4, 6, 7]
    roatationBy = 2
    print(f'Original Array: {arr}')
    print(f'Rotation By: {roatationBy}')
    
    # Left Rotation
    # Technique 1
    tempRotatedArray = tempRotate(list(arr), len(arr), roatationBy)
    print(f'Rotated Array using temp array technique: {tempRotatedArray}')

    # Technique 2
    oneByOneRotatedArray = oneByOneRotate(list(arr), len(arr), roatationBy)
    print(f'Rotated Array using one by one rotation technique: {oneByOneRotatedArray}')

    # Technique 3
    jugglingRotatedArray = jugglingRotate(list(arr), len(arr), roatationBy)
    print(f'Rotated Array using juggling technique: {jugglingRotatedArray}')

    # Technique 4
    reversalRotatedArray = reversalRotate(list(arr), len(arr), roatationBy)
    print(f'Rotated Array using reversal technique: {reversalRotatedArray}')

    # Cyclic Rotation
    # Technique 1
    cyclicRotatedArray = cyclicRotate(list(arr), len(arr))
    print(f'Cyclic Rotated Array: {cyclicRotatedArray}')

    # Print Left Rotation
    # Technique 1
    print(f'Left Rotated Array by {roatationBy}')
    printLeftRotation(list(arr), len(arr), roatationBy)
    print()

    # Right Rotation
    # Technique 1
    rightReversalRotatedArray = rightReversalRotate(list(arr), len(arr), roatationBy)
    print(f'Right Rotated Array using reversal technique: {rightReversalRotatedArray}')
