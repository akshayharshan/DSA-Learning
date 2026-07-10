def best_time_to_buy_sell(prices):

    max_profit = 0
    min_price = prices[0]
    
    for price in prices:
        
        if  price < min_price:
            min_price = price
        profit = price - min_price
        
        max_profit = max(max_profit,profit)



    return max_profit 




prices = [7,1,5,3,6,4]
print(best_time_to_buy_sell(prices))