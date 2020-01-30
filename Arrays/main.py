from Rotation.temp_array_solution import rotate as tempRotate
from Rotation.rotate_one_by_one_solution import rotate as oneByOneRotate
from Rotation.juggling_algorithm_solution import rotate as jugglingRotate
from Rotation.reversal_algorithm_solution import rotate as reversalRotate

# cyclic rotation import
from Rotation.cyclic_rotation_solution import cyclicRotate

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
