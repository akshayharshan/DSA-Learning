def best_time_buy_sell(prices):
    l =0
    max_profit = 0
    for price in range(1,len(prices)):
        profit = prices[price] - prices[l]
        max_profit = max(profit,max_profit)
        if prices[price] < prices[l]:
            l =price
    return max_profit   
    


prices = [3,1,4]


print(best_time_buy_sell(prices))