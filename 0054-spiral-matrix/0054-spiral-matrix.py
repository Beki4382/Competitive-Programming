class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        res = []
        step = 0
        while left <= right and top <= bottom:
            match (step % 4):
                case 0:
                    for i in range(left, right+1):
                        res.append(matrix[top][i])
                    top += 1
                case 1:
                    for i in range(top, bottom+1):
                        res.append(matrix[i][right])
                    right -= 1
                case 2:
                    for i in range(right, left-1, -1):
                        res.append(matrix[bottom][i])
                    bottom -= 1
                case 3:
                    for i in range(bottom, top-1, -1):
                        res.append(matrix[i][left])
                    left += 1
            step += 1
        return res