class Solution:
    def countPrimes(self, n: int) -> int:
        res = [True for i in range(n+1)]
        
        
        i = 2
        while i * i <= n:
            if  res[i]:
                j = i * i
                while j <= n:
                    res[j] = False

                    j += i
            i += 1
        count = 0    
        for i in range(2, len(res)-1):
            if res[i]:
                count += 1
                
            
        return count
        
        