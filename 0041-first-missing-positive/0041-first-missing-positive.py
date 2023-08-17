class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        i = 0
        nums = list(set(nums))
        n = len(nums)
        while i < n:
            if nums[i] <= 0 or nums[i] - 1 >= n:
                i += 1
            elif (nums[i] - 1) != i:
                curr = nums[i] -1
                nums[i], nums[curr] = nums[curr], nums[i]
                
            else:
                i += 1
                
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1       
                
            
        