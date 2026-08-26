class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]
        bestProfit = 0
        
        for price in prices:
            if price < buyPrice:
                buyPrice = price
            
            todayProfit = price - buyPrice
            if todayProfit > bestProfit:
                bestProfit = todayProfit
        
        return bestProfit