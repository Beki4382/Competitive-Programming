class Solution(object):
    def totalFruit(self, fruits):
        l , r = 0,0
        fruitsdic = {}
        result = 0
        while r < len(fruits):
            fruitsdic[fruits[r]] = r
            if len(fruitsdic) >= 3:
                minVal = min(fruitsdic.values())
                del fruitsdic[fruits[minVal]]
                l = minVal +1
            result = max(result, r-l+1)
            r +=1
        return result
                
            
                
                
        
        