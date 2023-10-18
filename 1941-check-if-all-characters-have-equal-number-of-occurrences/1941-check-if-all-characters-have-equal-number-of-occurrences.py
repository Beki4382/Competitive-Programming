class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = Counter(s)
        length = set()
        for val,key in count.items():
            length.add(key)
        return len(length) == 1
            
        