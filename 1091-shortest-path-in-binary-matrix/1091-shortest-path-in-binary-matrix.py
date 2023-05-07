class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        moves = [(-1,-1), (0,-1), (1,-1) ,(-1,0) ,(-1,1), (0,1), (1,1), (1,0)]
        n = len(grid)
        m = len(grid[0])
        
        def inbound(row, col):
            if 0 <= row < n and 0 <= col < m:
                return True

        if grid[0][0] or grid[n-1][m-1]:
            return -1

        

        queue = deque([(0, 0, 1)])
        visited = set()
        visited.add((0, 0))

        while queue:
            cell = queue.popleft()
            
            if cell[0] == n -1 and cell[1] == m -1:
                return cell[2]
        
            for move in moves:

                new_row = cell[0] + move[0]
                new_col = cell[1] + move[1]

                if inbound(new_row, new_col) and not grid[new_row][new_col]:
                    if (new_row, new_col) not in visited:
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col, cell[2] + 1))
                        
        return -1
            
       
             
                
        
        
        