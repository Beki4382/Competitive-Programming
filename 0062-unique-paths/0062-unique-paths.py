class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        paths = [[1] * n] * m
        
        for i in range(1, m):
            for j in range(1, n):
                paths[i][j] = paths[i - 1][j] + paths[i][j-1]
                
        return paths[-1][-1]
            
            
        