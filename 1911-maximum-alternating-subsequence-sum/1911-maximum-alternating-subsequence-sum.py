class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        memo = {}
        
        def dp(i, parity):
            if i == len(nums):
                return 0
            
            if (i,parity) in memo:
                return memo[(i,parity)]
            
            num = nums[i] if parity else -nums[i]
            memo[(i,parity)] = max(num + dp(i + 1, not parity), dp(i+1, parity))
            return memo[(i,parity)]
        
        return dp(0,True)
            