class Solution:
    def check(self, nums: List[int]) -> bool:
        
        n = len(nums)
        count = 0
        for i in range(len(nums)):
            if nums[((i+1)%n)] < nums[i]:
                count += 1
                
        return True if count <= 1 else False
    
