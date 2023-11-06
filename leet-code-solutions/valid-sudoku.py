class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        m = len(board[0])
        
        for i in range(n):
            row_val = set()
            
            for j in range(m):
                if board[i][j] != "." :
                    if board[i][j] in row_val:
                        return False
                    row_val.add(board[i][j])
                    
        for j in range(m):
            col_val = set()
            
            for i in range(n):
                if board[i][j] != "." :
                    if board[i][j] in col_val:
                        return False 
                    
                    col_val.add(board[i][j])
                    
        for i in range(3):
            for j in range(3):
                square_val = set()
                
                for x in range(i*3, i*3+3):
                    for y in range(j*3, j*3+3):
                        
                        if board[x][y] != "." :
                            if board[x][y] in square_val:
                                return False
                            square_val.add(board[x][y])
        
        return True
                        
        
                    
                    
            
        