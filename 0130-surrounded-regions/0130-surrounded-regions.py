class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        
        directions = [(1,0), (0,1), (-1,0),(0,-1)]
        def isInBound(row, col):
            if 0 <= row < len(board) and 0 <= col < len(board[0]):
                return True
            return False
        
        
        seen = set()
        def dfs(row, col):
            
            if board[row][col] == "O":
                board[row][col] = False
            
            for r, c in directions:
                new_r = row + r
                new_c = col + c
                
                if isInBound(new_r, new_c ) and board[new_r][new_c] == "O":
                    board[new_r][ new_c] = False
                    dfs(new_r, new_c)
                

        for i in range(n):
            if board[i][0] == "O":
                dfs(i,0)
                
        for i in range(n):
            if board[i][m-1] == "O":
                dfs(i,m-1)
                    
        for i in range(m):
            if board[0][i] == "O":
                dfs(0,i)
        
        for i in range(m):
            if board[n-1][i] == "O":
                dfs(n-1,i)
                
                
        for i in range(n):
            for j in range(m):
                if board[i][j] == False:
                    board[i][j] = "O"
                    
                else:
                    board[i][j] = "X"
         
                    
    