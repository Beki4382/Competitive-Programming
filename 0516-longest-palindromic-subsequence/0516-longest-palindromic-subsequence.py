class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        reverse = s[::-1]
        
        memo = [[0 for _ in range(n+1)] for _ in range(n+1)]
        
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s[i] == reverse[j]:
                    memo[i][j] = 1 + memo[i+1][j+1]
                    
                else:
                    memo[i][j] = max(memo[i+1][j], memo[i][j+1])

        return memo[0][0]