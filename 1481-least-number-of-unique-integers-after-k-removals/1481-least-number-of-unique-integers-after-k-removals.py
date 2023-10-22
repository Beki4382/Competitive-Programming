class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = sorted(Counter(arr).values())
        
        current_count = 0
        unique_ints = len(counts)
        
        for count in counts:
            current_count += count
            if current_count > k:
                return unique_ints
            unique_ints -= 1
        
        return unique_ints
