def search_rotated(nums, target):
    l=0
    r = len(nums) - 1


    while l<= r:
        mid = l + (r-l)//2

        if nums[mid] == target:
            return mid
        if nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid -1
            else:
                l = mid +1
        else:

            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid -1


            


print(search_rotated([6,7,8,9,1,2,3,4],8))