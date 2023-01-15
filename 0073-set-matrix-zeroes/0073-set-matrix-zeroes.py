class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix)
        m = len(matrix[0])
        
        last_idx = (n-1)*m+(m-1)
        
        zerosIdx = []
        for i in range(last_idx+1):
            if matrix[i//m][i%m] == 0:
                zerosIdx.append(i)

        for i in zerosIdx:
            matrix[i//m] = [0] * m
            for j in range(n):
                matrix[j][i % m] = 0
            
