class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n < 1:
            return False
        if n == 1:
            return True
        
        n = n/2
        return self.isPowerOfTwo(n) 
        
        