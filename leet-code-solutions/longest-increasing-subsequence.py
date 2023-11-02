class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [1 for _ in range(n)]
 
        for i in range(n):
            for j in range(0,i):
                if nums[i] > nums[j]:
                        memo[i] = max(memo[i], memo[j] + 1)
          
        return max(memo)
                        
        
        
        