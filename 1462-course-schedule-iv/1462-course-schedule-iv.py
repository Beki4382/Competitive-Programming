class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = defaultdict(list)
        heap = []
        for pre in prerequisites:
            graph[pre[0]].append(pre[1])
        
        def hasPath(scr, dst):    
            heap = [(0,scr)]
            visited = set()
            
            while heap:
                cost, scr = heapq.heappop(heap)
                if scr in visited:
                    continue 
                visited.add(scr)
                if scr == dst:
                    return True
                
                for child in graph[scr]:
                    if child not in visited:
                        heapq.heappush(heap,(cost +1, child))

            return False
        
        ans = []    
        for scr,dst in queries:
            ans.append(hasPath(scr,dst))
            
        return ans
            
            
            
            
            
            
        
        
            
        