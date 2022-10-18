class Solution(object):
    def kthLargestNumber(self, nums, k):
        nums = map(int,nums)
        nums.sort(reverse = True)
        return str(nums[k-1])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
 
        
        
        
        
        
        