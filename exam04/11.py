def array_rotation_detector(arr1: list, arr2: list) -> bool:
    if len(arr1) != len(arr2):
        return False
    if len(arr1) == 0:
        return True
    
    for i in range(len(arr1)):
        match = True
        for j in range(len(arr2)):
            if arr1[(i + j) % len(arr1)] != arr2[j]:
                match = False
                break
        if match:
            return True
    return False

print(array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]))
print(array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4]))
print(array_rotation_detector([1, 2, 3], [3, 2, 1]))
print(array_rotation_detector([1, 2], [1, 2, 3]))
print(array_rotation_detector([], []))