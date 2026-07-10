
def productExceptSelf(nums):
    left_array = [1] * len(nums)
    right_array = [1] * len(nums)
    result = []

    left_sum = 1
    right_sum = 1

    for i in range(len(nums)):
        j = -i-1
        left_array[i] = left_sum
        right_array[j] = right_sum

        left_sum = left_sum * nums[i]
        right_sum = right_sum * nums[j]
    
    for i in range(len(nums)):
        result.append(left_array[i] * right_array[i])
    return result 
        
        
nums = [1,2,3,4]
print(productExceptSelf(nums))


        