class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]

        for k in range(n - 1, -1, -1):
            for i in range(2):
                for j in range(1, 3):
                    if i == 0:
                        dp[k][i][j] = max(0 + dp[k + 1][0][j],
                                        -prices[k] + dp[k + 1][1][j])

                    if i == 1:
                        dp[k][i][j] = max(0 + dp[k + 1][1][j],
                                        prices[k] + dp[k + 1][0][j - 1])

        return dp[0][0][2]






