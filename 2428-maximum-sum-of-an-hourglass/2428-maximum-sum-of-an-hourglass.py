class Solution(object):
    def maxSum(self, grid):
        maxSum = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(1,row-1):
            for j in range(1,col-1):
                totSum = grid[i-1][j-1] + grid[i-1][j]+grid[i-1][j+1] + grid[i][j] + grid[i+1][j-1] + grid[i+1][j]+grid[i+1][j+1]
                maxSum = max(totSum,maxSum)
        return maxSum
            
            
        