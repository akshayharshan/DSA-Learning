def house_robber(nums):

    dp = [0] * len(nums)
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0],nums[1])
    prev = nums[0]
    curr = max(nums[0],nums[1])
    for i in range(2,len(nums)):
        prev,curr = curr, max(curr, prev + nums[i])
    return curr




nums = [5, 1, 1, 5]
print(house_robber(nums))