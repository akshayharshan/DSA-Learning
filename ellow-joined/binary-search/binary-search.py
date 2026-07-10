def binary_search(nums,target):

    r = len(nums) - 1 
    l = 0

    while l <= r:
        mid = (l+r)//2

        if nums[mid] == target:
            return mid
        if  target > nums[mid]:

            l = mid + 1
        elif  target < nums[mid]:

            r = mid - 1

    return -1








nums = [-1,0,3,5,9,12]
target = 9

print(binary_search(nums,target))