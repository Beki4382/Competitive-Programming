class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        heap = []
        for i in range(len(edges)):
            u, v = edges[i]
            prob = succProb[i]
            graph[u].append((v, prob))
            graph[v].append((u, prob))  

        heap = [(-1.0, start_node)]  
        visited = [0.0] * n  

        while heap:
            pro, scr = heapq.heappop(heap)
            pro = -pro  
            if pro < visited[scr]:
                continue

            for c, child_prob in graph[scr]:
                new_prob = pro * child_prob  
                if new_prob > visited[c]:
                    visited[c] = new_prob
                    heapq.heappush(heap, (-new_prob, c)) 

        return visited[end_node]
