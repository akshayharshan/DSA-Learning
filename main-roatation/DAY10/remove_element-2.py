def remove_element(nums,val):

    l = 0
    for r in range(len(nums)):
        if nums[r] != val:
            nums[l] = nums[r]
            l+=1
    return l



nums = [4,1,4,2,4,3]
val = 4
print(remove_element(nums,val))