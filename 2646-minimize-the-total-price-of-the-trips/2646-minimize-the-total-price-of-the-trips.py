class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        graph = defaultdict(list)
        for st,end in edges:
            graph[st].append(end)
            graph[end].append(st)
        
        freq = [0] * n 
        for st, end in trips:
            que = deque([(st, -1)])
            parent = {st: -1}
            while que:
                start, val = que.popleft()
                if start == end:
                    break
                for child in graph[start]:
                    if child != val:
                        que.append((child, start))
                        parent[child] = start
            
            start = end
            while start >= 0:
                freq[start] += 1
                start = parent[start]

        def dfs(start, pa):
        
            full = half = 0 
            for child in graph[start]: 
                if child != pa: 
                    ff, hh = dfs(child, start)
                    full += ff
                    half += min(ff, hh)
            return price[start]*freq[start] + half, price[start]*freq[start]//2 + full
            
        return min(dfs(0, -1))