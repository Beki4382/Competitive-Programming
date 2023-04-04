class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        num_bin = bin(n)
        for i in range(3, len(num_bin)):
            if num_bin[i -1] == num_bin[i]:
                return False
        return True 
    
            
        