class Solution(object):
    def transpose(self, matrix):
        transMat = []
        n_col = len(matrix)
        n_row = len(matrix[0])

        for i in range(n_row):
            transMat.append([0]*n_col)

        for i in range(n_row):
            for j in range(n_col):
                transMat[i][j] = matrix[j][i]
        return transMat
