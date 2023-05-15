class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        n=len(graph)
        visited = set()
        status=[0]*(n)
        res=[]
        def dfs(node):
            if node in visited:
                return False
            
            if graph[node] == []:
                return True
            
            visited.add(node)
            
            for adj in graph[node]:
                if not dfs(adj):
                    return False
                
            visited.remove(node)
            graph[node] = []
            return True
        
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        return res
        