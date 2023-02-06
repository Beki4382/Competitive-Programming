from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last = {val:idx for idx,val in enumerate(s)}
        print(last)
        
        output = []
        maxim = 0
        size = 1
        for i,c in enumerate(s):
            maxim = max(maxim, last[c])
            if i == maxim:
                output.append(size)
                size = 1
            
            else:
                size+=1
                
        return output
       
            
        
        
        
        