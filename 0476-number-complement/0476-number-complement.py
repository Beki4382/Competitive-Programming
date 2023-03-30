class Solution:
    def findComplement(self, num: int) -> int:
        val = 0
        y = num
        while (1 << val) <= y:
            res = (1 << val)
            # print(num)
            num = num ^  (1 << val)
            val += 1
            
        return num 
            
            
            
            
        
        