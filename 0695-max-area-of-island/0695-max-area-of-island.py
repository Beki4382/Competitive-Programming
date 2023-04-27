class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def inBound(row, col):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                return True
            
        directions = [(0,1), (1,0), (0,-1), (-1,0)]    
        def dfs(visited, row, col):
            if grid[row][col] == 0:
                return 0
            
            visited.add((row, col))
            
            res = 1
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                
                if inBound(new_row, new_col) and (new_row, new_col) not in visited:
                    
                    res += dfs(visited, new_row, new_col)

            return res
         
        visited = set()
        output = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans = dfs(visited, i, j)
                output.append(ans)
        final = max(output)
        return final
        
                    
                    
                    
                    
                    
        