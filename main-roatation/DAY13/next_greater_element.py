def next_greater_element(nums):

    stack = []
    result = [-1] * len(nums)
    for i  in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            index = stack.pop()
            result[index] = nums[i]
        stack.append(i)
    return result
       







nums = [2, 1, 2, 4, 3]

print(next_greater_element(nums))