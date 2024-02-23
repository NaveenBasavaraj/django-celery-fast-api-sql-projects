class BuySellStock:
    def maxProfit(self, prices):
        maxProfit = 0
        lowestPrice = prices[0]
        
        for price in prices:
            if price < lowestPrice:
                lowestPrice = price
            maxProfit = max(maxProfit, price-lowestPrice)
        return maxProfit
    

res = BuySellStock().maxProfit([100, 200, 50, 78, 10, 68])

print(res)