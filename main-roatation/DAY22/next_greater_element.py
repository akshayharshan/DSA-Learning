def next_greater_element(nums):
    result = [-1] * len(nums)
    stack = []

    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            index = stack.pop()
            result[index] = nums[i]
        stack.append(i)
    return result








nums = [2,1,2,4,3]
print(next_greater_element(nums))