def binary_search(nums, target):
    l =0
    r = len(nums) - 1

    while l <= r:

        mid = l + (r-l)//2

        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            l = mid+1
        else:
            r = mid - 1
        






nums = [-1,0,3,5,9,12]
target = 9
print(binary_search(nums,target))


# time complexity --- > O(logn)
#space complexty --? o(1)