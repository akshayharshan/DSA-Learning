def longestConSeq(nums):
    s = set(nums)
    max_len = 0
    for num in s:
        if num - 1 not in s:
            next_num = num+1
            count = 1
            while next_num in s:
                count+=1
                next_num+=1
            max_len = max(count,max_len)
    return max_len
            




nums = [100,4,200,1,3,2]
print(longestConSeq(nums))