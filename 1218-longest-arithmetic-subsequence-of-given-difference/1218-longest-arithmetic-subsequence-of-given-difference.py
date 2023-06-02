class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        d = {}
        res = float("-inf")
        for i in range(len(arr)):
            count = 1
            
            if (arr[i] - difference) in d:
                count += d[(arr[i] - difference)]
                
            d[arr[i]] = count
            
            res = max(res, d[arr[i]])
            
        return res
            
            
        