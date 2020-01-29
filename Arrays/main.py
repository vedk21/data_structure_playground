from Rotation.temp_array_solution import rotate

# main function to try and understand different rotation techniques on array
if __name__ == '__main__':
    arr = [1, 3, 4, 6, 7, 5, 5, 2, 0]
    rotatedArray = rotate(list(arr), len(arr), 5)
    print(f'Original Array: {arr}')
    print(f'Rotated Array: {rotatedArray}')
