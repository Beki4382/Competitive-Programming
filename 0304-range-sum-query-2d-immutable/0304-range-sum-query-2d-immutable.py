class NumMatrix:

    def __init__(self, m: List[List[int]]):
        self.m = m
        for row in range(len(self.m)):
            for col in range(len(self.m[0])):
                
                top = self.m[row -1][col] if row -1 > -1 else 0
                left = self.m[row][col - 1] if col -1 > -1 else 0
                dig = self.m[row -1][col - 1] if row -1 > -1 and col -1 > -1 else 0
                self.m[row][col] += top + left - dig
      

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top = self.m[row1 -1][col2] if row1 -1 >= 0 else 0
        left = self.m[row2][col1 -1] if col1 -1 >= 0 else 0
        dig = self.m[row1 - 1][col1 -1] if row1 -1 >= 0 and col1 - 1 >= 0 else 0
        
        curr = self.m[row2][col2]
        return curr- top - left + dig
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)