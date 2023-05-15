class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        indegree = [0] * n
        d = defaultdict(list)
        res = [set() for i in range(n)]
        
        for edge in edges:
            d[edge[0]].append(edge[1])
            indegree[edge[1]] += 1
       
        
        que = deque()
        
        for i in range(n):
            if not indegree[i]:
                que.append(i)
                
        while que:
            node = que.popleft()
            
            for adj in d[node]:
                indegree[adj] -= 1
                res[adj].add(node)
                
                for nbr in res[node]:
                    res[adj].add(nbr)
                if not indegree[adj]:
                    que.append(adj)
            
            
        for i in range(len(res)):
            res[i] = sorted(res[i])
        return res
        
        