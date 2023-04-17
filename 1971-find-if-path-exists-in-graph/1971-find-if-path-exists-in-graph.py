class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        adjList = defaultdict(list)
        
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        

        visited = set()
        def dfs(node, visited, des):
            if node == des:
                return True
            
            visited.add(node)
            for neighbour in adjList[node]:
                if neighbour not in visited:
                    found = dfs(neighbour, visited, des)
                    if found:
                        return True
                    
            return False
        
        return dfs(source, visited, destination)