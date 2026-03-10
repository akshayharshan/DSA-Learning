def sort_colors(nums):

    left = 0
    right = len(nums) -1
    i = 0
    while i <= right:
        if nums[i] == 0:
            nums[left],nums[i] = nums[i],nums[left]
            left+=1
            i +=1
        elif nums[i] == 1:
            i+=1
        else:
            nums[right],nums[i] = nums[i],nums[right]
            right -= 1
    return nums

nums = [2,0,2,1,1,0]
print(sort_colors(nums))