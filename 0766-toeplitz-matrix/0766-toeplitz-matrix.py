class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        d = defaultdict(int)
        
        n = len(matrix)
        m = len(matrix[0])
        
        key = True
        for i in range(n):
            for j in range(m):
                if i == 0:
                    d[j-i] = matrix[i][j]
                elif j == 0:
                    d[j-i] = matrix[i][j]
                
                elif d[j-i] != matrix[i][j] :
                    return False
                
        return True
        
                  