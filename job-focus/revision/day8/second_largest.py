def second_largest(nums):
    first = float("-inf")
    second = float("-inf")

    if len(nums) < 2:
        return -1

    for i in range(1,len(nums)):
        if nums[i] > first:
            second = first
            first = nums[i]
        elif nums[i] > second and nums[i] != first :
            second = nums[i]
            
    return first

        


nums = [10,25,7,99,45]
print(second_largest(nums))