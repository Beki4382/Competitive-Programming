class Solution:
    def permute(self, arr: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(ans, seen):
            if len(ans) == len(arr):
                res.append(ans[:])
                return 
            
            for i in arr:
                if i not in seen:
                    ans.append(i)
                    seen.add(i)
                    dfs(ans, seen)
                    ans.remove(i)
                    seen.remove(i)
                    
        dfs([],set())
        return res
                    
                    
        
        
    