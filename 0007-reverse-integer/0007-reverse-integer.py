class Solution:
    def reverse(self, x: int) -> int:
        maxNum = (2 ** 31) -1
        minNum = (-2 ** 31)
        flag = True
        num = 0
        
        if x < 0 :
            flag = False
            x = -x
        
        while x > 0:
            lastd = x % 10 
            x = x // 10
            num  = (num * 10) + lastd
            
        if num > maxNum or num < minNum:
            return 0
        if not flag:
            return (-1 * num)
        return num