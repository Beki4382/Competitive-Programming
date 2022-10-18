from collections import Counter

class Solution:
    def findOriginalArray(self, changed):
        n = len(changed)
        changed.sort()
        c = Counter(changed)
        result = []
        for num in changed:
            if num == 0 and c[num] >=2:
                c[num] -=2
                result.append(num)
            elif num > 0 and c[num] and c[num*2]:
                result.append(num)
                c[num] -=1
                c[num*2] -=1
        if n%2 !=0:
            return []
             
        return result if len(result) == n//2 else []
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
