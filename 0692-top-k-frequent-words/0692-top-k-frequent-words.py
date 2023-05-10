class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = defaultdict(int)
        for word in words:
            d[word] += 1
            
        new_d = defaultdict(int)
        heap = []
        heapq.heapify(heap)
        for key,val in d.items():
            new_d[(val, key)] = val
            heapq.heappush(heap, (-val, key))
        
        ans = []
        
        while heap and k > 0:
            val = heapq.heappop(heap)
            ans.append(val[1])
            k -= 1
        return ans
        
        