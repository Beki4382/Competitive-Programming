class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = [True for i in range(right + 1)]
        primes[0] = primes[1] = False
        
        i = 2
        while i <= right:
            if primes[i]:
                j = 2 * i
                while j <= right:
                    if primes[j]:
                        primes[j] = False
                    j += i
            i += 1
        
        min_val = float("inf")
        res = [-1,-1]
        stack = []
        
        for i in range(left, right + 1):
            if primes[i]:
                stack.append(i)
            while len(stack) >= 2:
                if abs(stack[0] - stack[1]) <= min_val:
                    
                    min_val = abs(stack[1] - stack[0])
                    res = [stack[0], stack[1]]
                    if min_val <= 2:
                        return res
                stack.pop(0)
                     
        return res
            
            
            
            
            