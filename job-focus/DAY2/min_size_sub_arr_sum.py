def min_size_sub_arr(nums,target):

    l = 0
    sum = 0
    min_val = float('inf')
    for r in range(len(nums)):
        sum += nums[r]

        while sum >= target :
            min_val = min(min_val,r-l+1)
            sum -= nums[l]
            l +=1
        
    return 0 if min_val == float('inf') else min_val
        
        




print(min_size_sub_arr([1,4,4],4))