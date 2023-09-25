class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minCost = prices[0]
        
        for i in range(1, len(prices)):
            minCost = min(minCost, prices[i])
            maxProfit = max(maxProfit, prices[i]- minCost)
                
        return maxProfit
                