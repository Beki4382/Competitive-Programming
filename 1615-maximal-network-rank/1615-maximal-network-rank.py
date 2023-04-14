class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        d = defaultdict(list)
        for road in roads:
            d[road[0]].append(road[1])
            d[road[1]].append(road[0])
        
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if j in d[i]:
                    count = max(count, len(d[i]) + len(d[j]) - 1)
                    
                else:
                    count = max(count, len(d[i]) + len(d[j]))
                
            
        return count
    