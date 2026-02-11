def remove_duplicates(nums):
    l=1
    for r in range(1,len(nums)):

        if nums[r] != nums[r-1]:
            nums[l] = nums[r]
            l+=1
    return l







nums = [-3,-3,-1,0,0,2]
print(remove_duplicates(nums))