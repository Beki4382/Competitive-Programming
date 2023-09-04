class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashT = defaultdict(int)
        for val in nums:
            hashT[val] += 1
            if hashT[val] > 1:
                return True
        return False