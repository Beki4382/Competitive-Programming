class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        arr = [key for (key, val) in count.items() if val == 1]
        return sum(arr)
        