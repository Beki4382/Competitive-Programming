class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num = (x ^ y)
        
        count = 0
        while num > 0:
            count += (num & 1)   
            num >>= 1
        return count
           
        
        
        