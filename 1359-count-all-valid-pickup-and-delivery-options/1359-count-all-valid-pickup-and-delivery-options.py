class Solution:
    def countOrders(self, n: int) -> int:
        
        MOD = 10**9 + 7
        
        answer = 1 
        for i in range(2, n + 1):
            answer = (answer* (2 * i - 1) * i) % MOD
        return answer