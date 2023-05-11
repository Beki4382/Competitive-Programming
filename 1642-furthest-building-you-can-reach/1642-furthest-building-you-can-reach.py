class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        heap = []
        heapq.heapify(heap)
        
        output = 0
        
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            
            if diff > 0:
                heapq.heappush(heap, diff)
                
            if len(heap) > ladders:
                val = heapq.heappop(heap)
                bricks -= val
                
            if bricks < 0:
                return i
            
        
        return len(heights) -1
                    
                
                
            
                
                
            