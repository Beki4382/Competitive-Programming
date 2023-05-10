class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        
        
        n = len(matrix)
        m = len(matrix[0])
        
        heap = []
        heapq.heapify(heap)
        
        for i in range(n):
            for j in range(m):
                heapq.heappush(heap, matrix[i][j])
                
                
        print(heap)
        for i in range(k - 1):
            heapq.heappop(heap)
            
        return heapq.heappop(heap)
            
        
        