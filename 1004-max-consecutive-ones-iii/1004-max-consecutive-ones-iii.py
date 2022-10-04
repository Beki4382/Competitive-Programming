class Solution(object):
    def longestOnes(self, nums, k):
        l,r = 0, 0
        max_len = 0
        
        while r < len(nums):
            if nums[r] == 0:
                k -=1

            if k < 0:
                if nums[l] == 0:
                    k +=1
                l +=1
            r +=1
            
        max_len = r - l    
        return max_len
            
            
            
        
        
        
