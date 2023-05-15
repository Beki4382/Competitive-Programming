class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        
        for adj in adjacentPairs:
            d[adj[0]].append(adj[1])
            d[adj[1]].append(adj[0])
        
        def find_first(dic) -> int:
            for i in dic:
                if len(dic[i]) == 1:
                    return i
        
        first = find_first(d)
        res = [first]
        visited = {first}
        stack = [d[first]]
        while stack:
            cur = stack.pop()
            for adj in cur:
                if adj not in visited:
                    stack.append(d[adj])
                    visited.add(adj)
                    res.append(adj)
        return res
        