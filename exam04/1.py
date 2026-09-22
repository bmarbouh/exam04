def array_rotation_detector(arr1: list, arr2: list) -> bool:
    if len(arr1) != len(arr2):
        return False

    if len(arr1) == 0:
        return True

    for i in range(len(arr1)):
        match = True

        for j in range(len(arr1)):
            if arr1[(i + j) % len(arr1)] != arr2[j]:
                match = False
                break

        if match:
            return True

    return False