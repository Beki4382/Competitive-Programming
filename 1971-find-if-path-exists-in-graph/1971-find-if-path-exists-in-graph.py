class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        rank = [1 for _ in range(n)]
        parent = [i for i in range(n)]
        
        
        def find(node):
            curr = node
            while curr != parent[curr]:
                curr = parent[curr]
            p = parent[node]
            while parent[node] != curr:
                parent[node] = curr
                node = p
                p = parent[node]
            
            return curr
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if rank[p1] < rank[p2]:
                p1, p2 = p2, p1
                
            parent[p2] = p1
            rank[p1] += rank[p2]
        
            
        for n1, n2 in edges:
            union(n1, n2)
        
        def isConnected(start, end):
            return find(start) == find(end)
                
        return isConnected(source, destination)  
        
            
            