class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int: 
        graph = defaultdict(list)
        for i, (x, y, r) in enumerate(bombs):
            for j, (p,q,_) in enumerate(bombs):
                
                if i != j and (x - p) ** 2 + (y -q) ** 2 <= r ** 2:
                    graph[i].append(j)
                    
        visited = set()
    
        def dfs(idx, visited):
            if not visited:
                visited = {idx}
            
            visited.add(idx)
            for child in graph[idx]:
                if child not in visited:
                    dfs(child, visited)
                    
            return visited
            
        ans = 0
        for i in range(len(bombs)):
            ans = max(ans, len(dfs(i, visited)))
        return ans