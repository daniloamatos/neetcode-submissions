class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        profit = 0
        while r < len(prices):
            day = prices[r] - prices[l]
            if day > profit:
                profit = day
            elif day < 0:
                l = r
            r+=1
        return profit