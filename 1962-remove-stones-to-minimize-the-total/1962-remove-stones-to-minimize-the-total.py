class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        
        for i in range(len(piles)):
            heapq.heappush(heap, -piles[i])
        
        while k:
            val = heapq.heappop(heap)
            val = val//2
            heapq.heappush(heap, val)
            
            k -= 1
        
            
        return -sum(heap)