class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        d = {}
        
        def dp(curr_amount):
            min_cost = float("inf")
            
            if curr_amount == 0:
                return 0
            if curr_amount < 0:
                return float("inf")
            
            if curr_amount in d:
                return d[curr_amount]
            
            for coin in coins:
                min_cost = min(min_cost, dp(curr_amount - coin) + 1)
            d[curr_amount] = min_cost
                
            return d[curr_amount]
                
        return dp(amount) if dp(amount) != float('inf') else -1
            
        