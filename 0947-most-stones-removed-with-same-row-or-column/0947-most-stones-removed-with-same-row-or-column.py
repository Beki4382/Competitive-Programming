class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rowd = defaultdict(list)
        cold = defaultdict(list)
        
        parent = [i for i in range(len(stones))]
        rank = [1 for i in range(len(stones))]
        
        for i in range(len(stones)):
            rowd[stones[i][0]].append(i)
            cold[stones[i][1]].append(i)
        
        
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
                
            return parent[node]
        
        def union(node1, node2):
            p1, p2 = find(node1), find(node2)
            
            if rank[p2] > rank[p1]:
                p1, p2 = p2, p1
                
            parent[p2] = p1
            rank[p1] += rank[p2]
            
            
        for lis in rowd.values():
            for i in range(1, len(lis)):
                union(lis[i -1], lis[i])
        
        for lis in cold.values():
            for i in range(1, len(lis)):
                union(lis[i -1], lis[i])
                
                
        for i in range(len(stones)):
            find(i)
            
        return len(stones) - len(set(parent))
        
                