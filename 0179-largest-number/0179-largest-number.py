class Solution(object):
    def largestNumber(self, nums):
        n=len(nums)
        for i, num in enumerate(nums):
            nums[i] = str(num)
        for i in range(n):
            j= i+1
            for j in range(n-1):
                if nums[j]+nums[i] < nums[i]+nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return str(int("".join(nums)))
                    
                    
            
        
        
        
 