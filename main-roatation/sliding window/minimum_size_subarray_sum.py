def minimum_size_subarray_sum(nums,target):

    min_size = float('inf')
    l =0
    sum = 0
    for r in range(len(nums)):
        sum += nums[r]
        
        while sum >= target:

            min_size = min(min_size,r-l+1)
            sum -= nums[l]
            l+=1
        r +=1
    return 0 if min_size == float('inf') else min_size







target = 7
nums=[2,3,1,2,4,3]

print(minimum_size_subarray_sum(nums,target))