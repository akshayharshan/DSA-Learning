def second_largest(nums):
    first = float("-inf")
    second = float("-inf")

    for num in nums:
        if num > first:
            second = first
            first = num
        if num > second and num != first:
            second = num
    if second == float("-inf"):
        return -1
    else:
        return second



nums = [10, 5, 8]

print(second_largest(nums))