class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        
        def dp(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            if r == 1 and c == 1:
                return 1
            if r == 0 or c == 0:
                return 0
            
            memo[(r,c)] = dp(r-1,c) + dp(r,c-1)
            return memo[(r,c)]
        return dp(m,n)
        
        
            
        