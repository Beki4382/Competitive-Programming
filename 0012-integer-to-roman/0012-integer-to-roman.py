class Solution:
    def intToRoman(self, num: int) -> str:
        res = []
        d = {
            1 : "I", 
            5 : 'V', 
            10 : "X", 
            50 : "L", 
            100 : "C", 
            500 : "D", 
            1000 : "M"
        }
        
        while num >= 1000: 
            res.append(d[1000])
            num -= 1000 
        
        while num >= 900: 
            res.append(d[100])
            res.append(d[1000])
            num -= 900        
            
        while num >= 500: 
            res.append(d[500])
            num -= 500
        
        while num >= 400: 
            res.append(d[100])
            res.append(d[500])
            num -= 400  
        
        while num >= 100: 
            res.append(d[100])
            num -= 100 
        
        while num >= 90: 
            res.append(d[10])
            res.append(d[100])
            num -= 90  
            
        while num >= 50: 
            res.append(d[50])
            num -= 50 
            
        while num >= 40: 
            res.append(d[10])
            res.append(d[50])
            num -= 40 
        
        while num >= 10: 
            res.append(d[10])
            num -= 10
            
        while num >= 9: 
            res.append(d[1])
            res.append(d[10])
            num -= 400  
        
        while num >= 5:
            res.append(d[5])
            num -= 5 
            
        while num >= 4: 
            res.append(d[1])
            res.append(d[5])
            num -= 400  
        
        while num >= 1: 
            res.append(d[1])
            num -= 1 
            
        return "".join(res)