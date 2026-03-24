def best_time_to_buy_sell(nums):
    l = 0
    max_profix = 0
    for r in range(1,len(nums)):
        profit = nums[r] - nums[l]
        max_profix = max(max_profix,profit)
        if nums[r] < nums[l]:
            l = r
    return max_profix


prices = [5]
print(best_time_to_buy_sell(prices))