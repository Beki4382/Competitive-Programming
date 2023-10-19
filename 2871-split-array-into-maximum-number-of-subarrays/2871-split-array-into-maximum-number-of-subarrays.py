class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        totalScore = nums[0]
        for i in range(1, len(nums)):
            totalScore &= nums[i]
        
        if totalScore != 0:
            return 1
        count = 0
        zeros_count = ~0
        for num in nums:
            zeros_count &= num
            if zeros_count == 0:
                count += 1
                zeros_count = ~0
                
        return count
                    
        
            
        
        