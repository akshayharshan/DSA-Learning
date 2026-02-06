
def fixed_sliding_window(nums,k):
    l,r =  0,k
    window_sum = 0
    for i in range(0,k):
        window_sum += nums[i]
    max_sum = window_sum
    while r < len(nums):

        window_sum -= nums[l]
        window_sum += nums[r]
        max_sum = max(max_sum,window_sum)
        r+=1
        l+=1
    return max_sum



nums = [2, 1, 5, 1, 3, 2]
k = 3
print(fixed_sliding_window(nums,k))
