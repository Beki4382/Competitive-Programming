from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        count = Counter(nums)
        for i in count.values():
            result += i * (i - 1) //2
        return result
            