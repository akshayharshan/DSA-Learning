

def best_time_buy_stock(prices):
    min_price_so_far = prices[0]
    max_profit = 0
    for price in prices:
        if price < min_price_so_far:
            min_price_so_far = price
        profit = price - min_price_so_far
        max_profit = max(max_profit,profit)
    return max_profit






prices = [7,1,5,3,6,4]
print(best_time_buy_stock(prices))    
