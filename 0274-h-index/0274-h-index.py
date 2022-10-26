class Solution(object):
     def hIndex(self, citations):
        n = len(citations)
        ans = 0
        citations.sort()
        for i,c in enumerate(citations):
            if n-i <= c:
                ans = max(ans, n-i)
        return ans
    
        
        