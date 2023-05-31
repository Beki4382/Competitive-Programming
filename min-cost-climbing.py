class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        def dp(idx):
            
            
            if idx >=n:
                return 0
            
            if idx in memo:
                return memo[idx]
            
            min_cost = min(dp(idx + 1), dp(idx +2 ))
            memo[idx] = min_cost + cost[idx]
            
            return memo[idx]
        return min(dp(0), dp(1))
            
            
        
