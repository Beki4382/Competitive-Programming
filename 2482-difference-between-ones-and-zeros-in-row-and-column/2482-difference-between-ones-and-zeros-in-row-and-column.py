class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        n = len(grid)
        m = len(grid[0])
        diff = [[0 for i in range(m)]for j in range(n)]
        onesRow = []
        onesCol = []
        count = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count +=1 
            onesRow.append(count)
            count = 0
            
        for i in range(m):
            count = 0
            for j in range(n):
                if grid[j][i] == 1:
                    count += 1
            onesCol.append(count)
        
        for i in range(n):
            for j in range(m):
                ones = onesRow[i] + onesCol[j]
                zeros = (n - onesRow[i]) +  (m - onesCol[j])
                diff[i][j] = ones - zeros          
                
        return diff
                    
                
        