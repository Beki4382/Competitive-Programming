class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for source, dest, price in flights:
            graph[source].append((dest,price))
        dist = [float("inf")] * n
        dist[src] = 0
     
        heap = [(0,0,src)]
        
        while heap:
            route,prc, scr = heapq.heappop(heap)
          
            for other in graph[scr]:
                if dist[other[0]] > (other[1] + prc) and route <= k:
                    dist[other[0]] = (prc + other[1])
                    heapq.heappush(heap,(route + 1, prc + other[1],other[0] ))
                
        if dist[dst] == float("inf"):
            return -1 
        else:
            return dist[dst]  
        
        
        