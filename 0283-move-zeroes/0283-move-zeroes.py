class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        l , r = 0,1
        while r < n:
            if nums[l] !=0:
                l+=1
            else:
                if nums[r] !=0:
                    nums[l], nums[r] = nums[r], nums[l]
                    l+=1
                    
            r+=1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                