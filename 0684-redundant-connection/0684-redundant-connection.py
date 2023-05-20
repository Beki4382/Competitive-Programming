class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        rank = [1] *1001
        parent = [i for i in range(1001)]
        
        
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
            if p1 == p2:
                return False
            
            if rank[p1] < rank[p2]:
                p1, p2 = p2, p1
                
            parent[p2] = p1
            rank[p1] += rank[p2]
            
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
        
                
        
        
            
            
        
    