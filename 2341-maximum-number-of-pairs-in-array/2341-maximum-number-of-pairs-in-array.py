class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        pair = 0
        
        for cnt in count.values():
            pair += cnt // 2
            
        rem = sum(1 for cnt in count.values() if cnt % 2 != 0)
        return [pair, rem]
