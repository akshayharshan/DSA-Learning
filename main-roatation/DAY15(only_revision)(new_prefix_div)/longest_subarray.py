def longest_subarray(nums,k):

    l = 0
    max_len = 0
    sum =0

    for r in range(len(nums)):
        sum+=nums[r]
        while sum > k:
            sum-=nums[l]
            l+=1
        max_len = max(max_len,r-l+1)
    return max_len







nums = [1,2,1,0,1,1,0]
k = 4

print(longest_subarray(nums,k))