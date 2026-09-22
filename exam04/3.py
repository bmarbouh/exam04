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

        found_in_all = True

        for lst in lists:
            if value not in lst:
                found_in_all = False
                break

        if found_in_all:
            result.append(value)

    return result