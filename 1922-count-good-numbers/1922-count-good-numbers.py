class Solution:
    def countGoodNumbers(self, n: int) -> int:

        mod = 10**9 + 7

        def power(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            res = power(x, n // 2) % mod
            res = (res * res ) % mod       
            return (x * res) % mod if n % 2 != 0 else res 
        
        even = n // 2 + n % 2
        odd = n // 2
        
        ans = (power(5, even) % mod) * (power(4, odd) % mod) 
        return ans % mod
    
        
    
            