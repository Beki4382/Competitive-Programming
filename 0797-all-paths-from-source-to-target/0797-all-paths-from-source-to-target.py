class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ans = []
        path = [0]
        
        def dfs(node):
            if node == n -1:
                ans.append(path[:])
                return 
            
            for nbr in graph[node]:
                path.append(nbr)
                dfs(nbr)
                path.pop()
                
        dfs(0)
        return ans
            
            
                
            
                
            
                
            
        
        