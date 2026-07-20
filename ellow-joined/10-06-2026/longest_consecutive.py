def longest_consecutive(nums):
    unique_nums = set(nums)
    max_len = 0
    for num in nums:
        if num - 1 not in unique_nums:
            next_num = num + 1
            len = 1
            while next_num in unique_nums:
                len+=1
                next_num+=1
            
            max_len = max(max_len,len)
    return max_len



nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(longest_consecutive(nums))