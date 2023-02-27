class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d = {}
        left = 0
        right = 0
        count  = Counter(p)
        output =[]
        n = len(p)
        
        if len(p) > len(s):
            return []
        
        while right < n:
            d[s[right]] = 1 + d.get(s[right], 0)
            right +=1
        
        if d == count:
                output.append(left)
        
        while right < len(s):
            d[s[left]] -= 1
            d[s[right]] = 1 + d.get(s[right], 0)
            
            if d[s[left]] == 0:
                d.pop(s[left])
                
            left += 1
            
            if d == count:
                output.append(left)
        
            right += 1
            
        return output
            
      
            
            
                    
            
        