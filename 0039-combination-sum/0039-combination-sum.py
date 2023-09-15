class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        candidSum = 0
        candid = []
        
        def dfs(i, candidSum):
            if i >= len(candidates) or candidSum > target:
                return
            
            if candidSum == target:
                res.append(candid.copy())
                return
            
            
            candid.append(candidates[i])
            candidSum += candidates[i]
            dfs(i, candidSum)
            
            candid.pop()
            candidSum -= candidates[i]
            dfs(i+1, candidSum)
            
        dfs(0, candidSum)
        
        return res
        