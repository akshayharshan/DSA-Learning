def sliding_window_max(nums,k):

    result = []
    l = 0
    window_max = float("-inf")

    for r in range(len(nums)):
        if k == r-l+1:
            for w in range(l,r+1):
                window_max = max(window_max,nums[w])
            result.append(window_max)
            l+=1
            window_max = float("-inf")

            
    return result




nums = [9,3,5,1,6]
k = 3
print(sliding_window_max(nums,k))