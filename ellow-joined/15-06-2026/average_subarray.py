
def avg_sub_array(nums,k):
    l = 0
    max_avg = float("-inf")
    sum = 0

    if len(nums) < k :
        return False
    for r in  range(len(nums)):
        size = r - l + 1
        sum += nums[r]
        if size > k :
            sum -= nums[l]
            l += 1
        avg = sum / k
        max_avg = max(avg,max_avg)
    return max_avg
        
        


nums = [1, 12, -5, -6, 50, 3]
k = 4

print(avg_sub_array(nums,k))