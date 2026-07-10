def max_subarray(nums):
    run_sum = 0
    max_sum = float("-inf")

    for i in range(len(nums)):
        run_sum += nums[i]
        max_sum = max(max_sum,run_sum)
        if run_sum < 0:
            run_sum = 0
    return max_sum

    
    


nums = [-5, -2, -8, -1]
print(max_subarray(nums))