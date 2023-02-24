class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        d = {}
        count = 0
        left = 0
        
        for right in range(len(s)):
            d[s[right]] = 1 + d.get(s[right],0)
            
            while right -left + 1 > len(d):
                d[s[left]] -= 1
                if d[s[left]] == 0:
                    d.pop(s[left])
                
                left += 1
               
            count = max(count, right - left + 1)
             
        return count
        