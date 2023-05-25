class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        
        n = len(nums)
        mn = float('inf')
        left = min(n, 3)
        right = n-1
        while left <= right and left >= 0:
            mn = min(mn, nums[right]-nums[left])
            left -= 1
            right -= 1
        
        return mn
        