def sliding_window(nums,k):
    max_size = 0
    sum = 0
    l = 0
    for r in range(len(nums)):
        sum+=nums[r]
        while sum > k:
            sum-=nums[l]
            l +=1
        max_size = max(max_size,r-l+1)
            
        
    return max_size
            






nums = [1,2,1,0,1,1,0] 
k = 4

print(sliding_window(nums,k))