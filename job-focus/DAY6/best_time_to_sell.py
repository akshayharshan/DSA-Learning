def minimum_price_so_far(nums):

    min_price_so_far = nums[0]
    max_profit = 0

    for i in range(len(nums)):
        min_price_so_far = min(min_price_so_far,nums[i])
        profit = nums[i] - min_price_so_far

        max_profit = max(profit,max_profit)
    return max_profit





print(minimum_price_so_far([7,6,4,3,1]))