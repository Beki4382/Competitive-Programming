class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix)        
        
        for i in range(n):
            for j in range(i):
                matrix[j][i], matrix[i][j] = matrix[i][j],matrix[j][i]
        for row in matrix:
            row = row.reverse()
        
        
        
        
        