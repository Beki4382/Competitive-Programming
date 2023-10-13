class Solution:
    def countOrders(self, n: int) -> int:
        
        MOD = 10**9 + 7
        
        output = 1

        for i in range(2, n+1):
            val = 2 * i
            output *= (val * (val-1)// 2) 
            
        return output % MOD
            
     