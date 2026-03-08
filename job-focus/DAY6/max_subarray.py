def max_subarray(nums):
    running_sum = 0
    max_sum = float("-inf")

    for r in range(len(nums)):
        running_sum += nums[r]
        max_sum = max(running_sum,max_sum)
        if running_sum< 0:
            running_sum = 0

    return max_sum





nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(nums))