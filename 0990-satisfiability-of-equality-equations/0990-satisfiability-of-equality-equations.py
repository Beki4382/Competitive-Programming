class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [i for i in range(26)]
        rank = [1 for _ in range(26)]
        
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(node1, node2):
            p1 = find(node1)
            p2 = find(node2)
            
            if rank[p2] > rank[p1]:
                p1, p2 = p2, p1
                
            parent[p2] = p1
            rank[p1] += rank[p2]
            
        for string in equations:
            n1 = ord(string[0]) - 97
            n2 = ord(string[-1]) - 97
            
            if string[1] == "=":
                union(n1, n2)
        
        for string in equations:
            n1 = ord(string[0]) - 97
            n2 = ord(string[-1]) - 97
            
            if find(n1) == find(n2) and string[1] == "!":
                return False
            if find(n1) != find(n2) and string[1] == "=":
                return False
        return True
                
            
            
        