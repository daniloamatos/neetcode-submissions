class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        profit = 0
        while r < len(prices):
            day = prices[r] - prices[l]
            if day > profit:
                profit = day
            if r == l:
                r+=1
                continue
            elif day < 0:
                l+=1
                continue
            r+=1
        return profit