nums = [1,2,2,2,3,4]
target = 2
l = 0
r = len(nums)-1
s = -1

while l <= r:
    mid = l + (r - l) // 2  ## sometimes r+1 makes the sum much larger number and hard for calclulation but what we do here r-1  --> got the difference and divideb by 2 then that was added to the left results mid number
    if target == nums[mid]:
        s = mid
        l = mid + 1  # for left most boundary we can use (r = mid -1)       
    elif target >  nums[mid]:
         l = mid + 1
    else:
        r = mid - 1
print(s)
    
