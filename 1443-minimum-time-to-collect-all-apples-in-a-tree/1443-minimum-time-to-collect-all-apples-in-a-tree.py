class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        minTime = 0
        
        graph = defaultdict(list)
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        def dfs(node, parent):            
            res = 0
            for child in graph[node]:
                if child != parent:
                    res += dfs(child,node)        
            if hasApple[node] and node != 0:
                hasApple[parent] = True
                return res+2
            return res            
        return dfs(0,0) 
        