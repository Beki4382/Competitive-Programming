class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        
        for i in range(1, num + 1):
            sum_digit = 0
            
            for digit in str(i):
                sum_digit += int(digit) 
            if sum_digit % 2 == 0:
                count += 1
                
        return count
                
                    
                    