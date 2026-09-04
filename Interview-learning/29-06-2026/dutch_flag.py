def sortColors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:

        if nums[mid] == 0:
            nums[mid],nums[low] = nums[low],nums[mid]

            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1

        else:   # nums[mid] == 2
            nums[high],nums[mid] = nums[mid],nums[high]

            high -= 1


    return nums


print(sortColors([2,1,0,1,2,0]))