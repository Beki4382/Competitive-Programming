class Solution(object):
    def maxFrequency(self, nums, k):
        nums.sort()
        l, r = 0, 0
        total, result = 0, 0
        while r < len(nums):
            total +=nums[r]
            if nums[r]*(r - l +1) <= total + k:
                result = max(result, (r-l + 1))
            else:
                total -= nums[l]
                l+=1
            r+=1
        return result
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
