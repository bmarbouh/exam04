def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    if len(lists) == 0:
        return []
    
    for lst in lists:
        if len(lst) == 0:
            return []
    
    result = []
    for value in lists[0]:
        if value in result:
            continue
        
        check = True
        
        for lst in lists:
            if value not in lst:
                check = False
                break
        if check:
            result.append(value)
    return result

print(list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 3, 5]]))
print(list_intersection_finder([[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]]))
print(list_intersection_finder([[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]]))
print(list_intersection_finder([[1, 2, 3], [4, 5, 6]]))
print(list_intersection_finder([]))
print(list_intersection_finder([[1, 2, 3], []]))
print(list_intersection_finder([[5]]))