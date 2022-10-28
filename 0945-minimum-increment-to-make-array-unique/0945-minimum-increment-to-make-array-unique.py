class Solution(object):
    def minIncrementForUnique(self, nums):
        
        nums.sort()
        res = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                res += nums[i - 1] + 1 - nums[i]
                nums[i] = nums[i - 1] + 1
        return res
            
        
        