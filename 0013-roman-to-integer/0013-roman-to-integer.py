class Solution:
    def romanToInt(self, s: str) -> int:
        
        d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        num = 0
        pre = s[0]
        
        for char in s:
            if d[pre] < d[char]:
                num -= d[pre] * 2
                
            num += d[char]
            pre = char
            
        return num
            
        