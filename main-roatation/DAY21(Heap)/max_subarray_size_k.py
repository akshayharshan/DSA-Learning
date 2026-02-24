def max_sub_array(nums,k):


    max_sum = float("-inf")
    l = 0
    sum = 0
    for r in range(len(nums)):
        sum+=nums[r]
        if r - l + 1 > k:
            sum-=nums[l]
            l+=1
            
        elif r - l + 1 == k:
            max_sum = max(max_sum,sum)
        
    return max_sum








nums = [-2, -1, -3, -4, -1, -2]
k = 2
print(max_sub_array(nums,k))