def product_self(nums):
    left_sum = 1
    right_sum = 1
    
    n = len(nums)
    right_arr = [1] * n
    left_arr = [1] * n
    result = [1] * n
    for i in range(n):
        j = - 1 - i

        left_arr[i] = left_sum
        right_arr[j] = right_sum

        left_sum = left_sum * nums[i]
        right_sum = right_sum * nums[j]
    for i in range(n):
        result[i] = right_arr[i] * left_arr[i]
    
    print(result)
product_self([1,2,3,4])
