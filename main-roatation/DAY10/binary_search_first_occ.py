def binary_search_first_occ(nums,target):

    l,r = 0,len(nums)-1
    res = -1
    while l <= r:
        mid = l +(r-l)//2
        if nums[mid] == target:
            res = mid
            r = mid - 1
        elif target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return res





nums = [1,2,2,2,3,4]
target = 2
print(binary_search_first_occ(nums,target))