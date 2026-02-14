def longest_sub_array(nums,k):
    l=0
    sum =0
    max_len = 0
    for r in range(len(nums)):
        sum+=nums[r]

        while sum > k:
            sum-=nums[l]
            l+=1
        max_len = max(r-l+1,max_len)
    return max_len

        




nums = [1,2,1,0,1,1,0]
k = 4

print(longest_sub_array(nums,k))