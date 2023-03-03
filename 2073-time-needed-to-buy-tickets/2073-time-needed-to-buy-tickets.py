class Solution:
    def timeRequiredToBuy(self, t: List[int], k: int) -> int:
        
        i = 0
        count = 0
        
        while t[k] != 0:
            
            if t[i] != 0:
                t[i] -= 1
                count += 1
                
            i = (i + 1) % len(t)   
            
        return count
                
            
            
                
            
            
         
        