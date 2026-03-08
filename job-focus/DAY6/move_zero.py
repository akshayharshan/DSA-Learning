def move_zero(nums):

    l = 0
    for r in range(len(nums)):

        if nums[r] != 0:
            nums[r],nums[l] = nums[l],nums[r]
            l+=1

    return nums








print(move_zero([5, 1, 0, 7, 8, 3, 9, 0, 4]))