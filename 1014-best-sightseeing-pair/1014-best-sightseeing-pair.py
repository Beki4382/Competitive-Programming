class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp =[0] * len(values)
        res = 0
        
        for i in range(1, len(values)):
            dp[0] = values[0]
            
            dp[i] = max(dp[i-1], values[i-1] + i-1)
            res = max(res, dp[i] + values[i] - i)
        return res
        