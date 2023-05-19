class Solution:
        def __init__(self):
            self.graph = {}
            self.rank = []
            self.minimum = []
        
        def find(self, node):
            if self.parent[node] != node:
                self.parent[node] = self.find(self.parent[node])
            
            return self.parent[node]
            
        def union(self, n1, n2, dis):
            p1, p2 = self.find(n1), self.find(n2)
            if self.rank[p2] > self.rank[p1]:
                p1, p2 = p2, p1
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
            self.minimum[p1] = min(self.minimum[p1], self.minimum[p2], dis)
            
                
        def minScore(self, n: int, roads: List[List[int]]) -> int:
            self.parent = {i : i for i in range(n) }
            self.rank = [1 for i in range(n)]
            self.minimum = [float("inf") for _ in range(n)]
            for n1, n2, dis in roads:
                self.union(n1 - 1, n2 - 1, dis)
            
            
            return self.minimum[self.find(0)]
            
            
            
        
        
    