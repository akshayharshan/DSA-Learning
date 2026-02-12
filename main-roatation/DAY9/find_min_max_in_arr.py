def min_max_arr(nums):
    min_num=float('inf')
    max_num = float('-inf')
    for num in nums:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

            
    return min_num,max_num








nums = [3, 5, 1, 8, 2]
print(min_max_arr(nums))