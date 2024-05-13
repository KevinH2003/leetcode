class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        max = 0
        
        while right < len(prices):
            print(left, right)
            if prices[right] < prices[left]:
                left = right
                
            if max < prices[right] - prices[left]:
                max = prices[right] - prices[left]
            
            right += 1
            
        return max