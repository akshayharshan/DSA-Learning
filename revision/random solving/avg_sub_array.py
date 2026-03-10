nums = [1,12,-5,-6,50,3]
k = 4
window_sum= sum(nums[:4])
max_avg = window_sum/k

for r in range(k,len(nums)):
    window_sum += nums[r]
    window_sum -= nums[r-k]
    avg = window_sum/k
    max_avg = max(max_avg,avg)

print(max_avg)

