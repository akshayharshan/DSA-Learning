# Find Maximum & Minimum in Array


def min_max_arr(nums):
    max_num = float("-inf")
    min_num = float("inf")
    for num in nums:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    return [max_num,min_num]

nums = [1, 5, 7, 2, 9, 3]
print(min_max_arr(nums))
