class Solution:
    def numSmallerByFrequency(self, q: List[str], w: List[str]) -> List[int]:
        
        def f(s):
            s = list(s)
            s.sort()
            cq = Counter(s)
            
            return cq[s[0]]
        
        for i in range(len(q)):
            q[i] = f(q[i])
            
            
        for j in range(len(w)):
            w[j] = f(w[j])
        
        
        output = []
        w.sort()
        for target in q:
            low = 0
            high = len(w) -1
            while low <= high:
                mid = low + (high - low) // 2
                
                if w[mid] < target + 1:
                    low = mid + 1
                else:
                    high = mid - 1
            output.append(len(w) - low)
                    
            
        return output
            
                    
                
                
            
         
        
        
     
        
        
        
        