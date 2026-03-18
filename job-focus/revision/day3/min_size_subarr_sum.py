def min_size_subarr_sum(nums, target):

    l = 0 
    min_len = float("inf")
    max_sum = 0
    for r in range(len(nums)):
        max_sum += nums[r]

        while max_sum >= target:
            min_len = min(min_len,r-l+1)
            max_sum -= nums[l]
            l+=1
    return 0 if min_len == float("inf") else  min_len




nums = [1,1,1]
target = 10

print(min_size_subarr_sum(nums,target))