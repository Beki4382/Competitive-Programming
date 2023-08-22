class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        ans = []
        
        for i, val in enumerate(tasks):
            val.append(i)
        tasks.sort()
        
        time = tasks[0][0]
        j = 0
        
        while heap or j < len(tasks):
            while j < len(tasks) and tasks[j][0] <= time:
                heapq.heappush(heap, [tasks[j][1], tasks[j][2]])
                j += 1
            if not heap:
                time = tasks[j][0]
            else:
                prosTime, index = heapq.heappop(heap)
                time += prosTime
                ans.append(index)
            
        return ans
            
        
        
        
        
        