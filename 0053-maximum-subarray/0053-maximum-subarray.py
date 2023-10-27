class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        max_ = nums[0]
        
        for i in range(len(nums)):
            total += nums[i]
            max_ = max(max_, total)
            if total < 0:
                total = 0
        return max_
        
            
        