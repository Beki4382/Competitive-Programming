class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        d = [float("inf")] * (amount + 1)
        d[0] = 0
        
        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    d[i] = min(d[i], d[i - coin] + 1)
                    
        
        return d[amount] if d[amount] != float('inf') else -1
        
        