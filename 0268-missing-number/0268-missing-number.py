class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        totalNum = n * (n + 1)//2
        currentNum = sum(nums)
        result = totalNum - currentNum
        
        return result
    
        
        