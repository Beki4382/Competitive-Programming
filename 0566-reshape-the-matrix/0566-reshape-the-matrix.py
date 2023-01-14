class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        n = len(mat)
        m = len(mat[0])
        
        if m*n != r*c:
            return mat
        
        output = [[0]*c for i in range(r)]
        last_idx = (n-1) * m +(m-1)
        
        
        for i in range(last_idx+1):
            
            output[i//c][i%c] = mat[i//m][i%m]
        
        return output
            
        
        
        
        
        
        
        