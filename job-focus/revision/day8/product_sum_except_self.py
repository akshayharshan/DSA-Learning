def product_sum_except_self(nums):
    arr1 = [1]*len(nums)
    arr2 = [1]*len(nums)
    res = []
    prefix_sum = 1
    suffix_sum = 1
    for i in range(len(nums)):
        j = -i-1
        arr1[i] = prefix_sum
        arr2[j] = suffix_sum

        prefix_sum *= nums[i]
        suffix_sum *= nums[j]
    for i in range(len(nums)):
        res.append(arr1[i] * arr2[i])
    return res









nums = [1,2,3,4]
print(product_sum_except_self(nums))