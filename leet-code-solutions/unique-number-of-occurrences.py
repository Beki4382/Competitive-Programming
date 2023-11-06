class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        unique = set()
        for key,val in count.items():
            unique.add(val)
        return len(unique) == len(count)
        