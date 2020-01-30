from Rotation.temp_array_solution import rotate as tempRotate
from Rotation.rotate_one_by_one_solution import rotate as oneByOneRotate
from Rotation.juggling_algorithm_solution import rotate as jugglingRotate

# main function to try and understand different rotation techniques on array
if __name__ == '__main__':
    arr = [1, 3, 4, 6, 7, 5, 5, 2, 0, 12]
    print(f'Original Array: {arr}')

    # Technique 1
    tempRotatedArray = tempRotate(list(arr), len(arr), 5)
    print(f'Rotated Array using temp array technique: {tempRotatedArray}')

    # Technique 2
    oneByOneRotatedArray = oneByOneRotate(list(arr), len(arr), 5)
    print(f'Rotated Array using one by one rotation technique: {oneByOneRotatedArray}')

    # Technique 3
    jugglingRotatedArray = jugglingRotate(list(arr), len(arr), 5)
    print(f'Rotated Array using juggling technique: {jugglingRotatedArray}')
