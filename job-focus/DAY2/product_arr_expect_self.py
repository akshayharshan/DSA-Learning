def product_arr_expect_self(nums):
    result = [1] * len(nums)
    for i in range(len(nums)- 1):
        result[i + 1] = result[i] * nums[i]
    right = 1
    for r in range(len(nums) -1,-1,-1):
        result[r] = result[r] * right
        right = right * nums[r]
    return result





print(product_arr_expect_self([1,2,3,4]))
    