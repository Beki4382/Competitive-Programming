class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        
        sorted_nums = []
        while heap:
            sorted_nums.append(heapq.heappop(heap))
        
        return sorted_nums

        