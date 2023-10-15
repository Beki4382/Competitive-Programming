class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        dp = [{} for _ in nums]
        longest = 1
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                if diff not in dp[j]:
                    dp[j][diff] = 1
                if diff not in dp[i]:
                    dp[i][diff] = 0
                    
                dp[i][diff] = dp[j][diff] + 1
                
                longest = max(longest, dp[i][diff])
                
        return longest