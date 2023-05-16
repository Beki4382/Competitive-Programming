class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        indegree = [0] * n
        
        if not edges:
            return [0]
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
            indegree[a] += 1
            indegree[b] += 1
            
        
        queue = deque()
        for i in range(n):
            if indegree[i] == 1:
                queue.append(i) 
       
        while n > 2:
            size = len(queue)
            n -= size
            for _ in range(size):
                curr = queue.popleft()
                for adj in graph[curr]:
                    indegree[adj] -= 1
                    if indegree[adj] == 1:
                        queue.append(adj)

        return queue
                    