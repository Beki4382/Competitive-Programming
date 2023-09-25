class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        dp = defaultdict(int)
        
        def partition(i, target):
            
            if i >= len(nums) or target <= 0:
                return target == 0
            
            state = (i, target)
            
            if state not in dp:
                dp[state] = partition(i+1, target - nums[i]) or partition(i + 1, target)
            
            return dp[state]
            
        return sum(nums)  % 2 == 0 and partition(0, sum(nums) // 2)
