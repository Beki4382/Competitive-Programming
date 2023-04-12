class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        factors = []
        i = 2
        while i * i <= n:
            while n % i == 0:
                factors.append(i)
                n //= i
            i += 1
        if n > 1:
            factors.append(n)
        
        return sum(factors)