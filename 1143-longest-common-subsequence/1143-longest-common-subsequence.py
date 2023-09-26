class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2) 
        i = n -1
        j = m -1
        
        memo = [[0 for _ in range(m +1)] for _ in range(n+1)]
        
        for i in range(n-1, -1,-1):
            for j in range(m-1, -1, -1):
                if text1[i] == text2[j]:
                    memo[i][j] = 1 + memo[i+1][j+1]
                
                else:
                    memo[i][j] = max(memo[i+1][j], memo[i][j+1])
        return memo[0][0]
            
            
            
            
        
        