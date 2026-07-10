def product_self(nums):
    n = len(nums)
    left_arr = [0] * n
    right_arr = [0] * n

    left_sum = 1
    right_sum = 1

    result = []

    for i in range(len(nums)):
        j = -1-i

        left_arr[i] = left_sum
        right_arr[j] = right_sum

        left_sum = left_sum * nums[i]
        right_sum = right_sum * nums[j]
    
    for i in range(len(nums)):
        result.append(left_arr[i] * right_arr[i])
    return result
    





nums = [1,2,3,4]

print(product_self(nums))