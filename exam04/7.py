def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    if len(nums) == 0 or k <= 0 or k > len(nums):
        return []

    result = []

    for i in range(len(nums) - k + 1):
        maximum = nums[i]

        for j in range(i, i + k):
            if nums[j] > maximum:
                maximum = nums[j]

        result.append(maximum)

    return result