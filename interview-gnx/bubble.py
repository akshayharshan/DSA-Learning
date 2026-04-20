def bubble(nums):
    n = len(nums)
    for i in range(n):

        for j in range(0,n - i - 1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums





nums = [5, 3, 8, 4, 2]
print(bubble(nums))