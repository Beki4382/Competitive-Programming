class Solution:
    def numMagicSquaresInside(self, g: List[List[int]]) -> int:
        
        n = len(g)
        m = len(g[0])
        count = 0
        
        def calc(row, col):
        
            row_sum = [0, 0, 0]
            col_sum = [0, 0, 0]
            diag1 = g[row][col] + g[row+1][col+1] + g[row+2][col+2]
            diag2 = g[row+2][col] + g[row+1][col+1] + g[row][col+2]
            seen = set()
            
            for i in range(row, row+3):
                for j in range(col, col+3):
                    cell = g[i][j]
                    seen.add(cell)
                    row_sum[i - row] += cell
                    col_sum[j - col] += cell
            for val in seen:
                if 1 > val or val > 9:
                    return False

            return row_sum == col_sum and diag1 == diag2 == row_sum[0] and len(seen) == 9

        for row in range(n-2):
            for col in range(m-2):
                if calc(row,col):
                    count += 1
        return count
        