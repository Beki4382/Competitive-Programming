class Solution:
    
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort(reverse = True)
        n = len(nums)
        perimeter = 0
        
        for i in range(n-2):
            
            if nums[i+1] + nums[i+2] > nums[i]:
                
                return nums[i+2] + nums[i+1] + nums[i]
                
        return 0
    
            
            
                
                
        