def find_missing_num(nums):

    n = len(nums)
    expect_sum = n * (n+1)//2
    curr_sum =0

    for i in nums:
       curr_sum += i
    
    return  expect_sum - curr_sum


print(find_missing_num([3,0,1]))



