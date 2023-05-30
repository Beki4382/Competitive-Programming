class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        route_map = defaultdict(set)
        visited = set()
        
        if source == target:
                return 0
        
        for i, route in enumerate(routes):
            for stop in route:
                route_map[stop].add(i)
                
        queue= deque([(source, 0)])
        
        while queue:
            stop, bus_count = queue.popleft()
            
            if stop == target:
                return bus_count
            
            for route_idx in route_map[stop]:
                if route_idx not in visited:
                    visited.add(route_idx)
                    for route in routes[route_idx]:
                        if route != stop:
                            queue.append((route, bus_count + 1))
                            
        return -1
            
            
            
                
        
        
       