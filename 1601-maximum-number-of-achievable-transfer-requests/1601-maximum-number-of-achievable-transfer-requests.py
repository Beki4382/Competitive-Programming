class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        res = 0
        indegree = [0] * n
        
        def backtrack(i, count):
            
            if i >= len(requests):
                for j in range(n):
                    if indegree[j] != 0:
                        return
                nonlocal res
                res = max(res, count)
                return
                
            indegree[requests[i][0]] -= 1
            indegree[requests[i][1]] += 1
            backtrack(i+1, count + 1)
            
            indegree[requests[i][0]] += 1
            indegree[requests[i][1]] -= 1
            backtrack(i+1, count)
            
        backtrack(0,0)
        return res
        
        