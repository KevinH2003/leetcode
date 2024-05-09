class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = prices[0]
        
        for price in prices:
            if price < lowest:
                lowest = price
            if price - lowest > profit:
                profit = price - lowest
            
        return profit
        