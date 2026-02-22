def min_size_subarray(nums, target):

    min_len = float('inf')
    sum = 0
    l = 0

    for r in range(len(nums)):

        sum += nums[r]

        while sum >= target:
            min_len = min(min_len,r-l+1)
            sum -= nums[l]
            l+=1
            
    return 0 if min_len == float('inf') else min_len







target = 3
nums = [3]

print(min_size_subarray(nums,target))