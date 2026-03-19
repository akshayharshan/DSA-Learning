def maximum_subarray(nums):

    curr_sum = 0
    max_sum = float("-inf")
    for i in range(len(nums)):
        curr_sum  += nums[i]
        max_sum = max(max_sum,curr_sum)
        if curr_sum < 0 :
            curr_sum = 0
        
    return max_sum


nums = [4,-1,2,-7,3,4]
print(maximum_subarray(nums))