class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n < 1:
            return False
        
        if n == 1:
            return True
        
        n = n/4
        return self.isPowerOfFour(n)
        