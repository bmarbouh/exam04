def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    result = []
    indices = [0] * len(lists)
    print(indices)
    while True:
        min_value = None
        min_index = -1

        for i in range(len(lists)):
            if indices[i] < len(lists[i]):
                value = lists[i][indices[i]]

                if min_index == -1 or value < min_value:
                    min_value = value
                    min_index = i

        if min_index == -1:
            break

        result.append(min_value)
        indices[min_index] += 1

    return result


merge_sorted_lists([[1, 3, 5], [2, 4, 6]])
