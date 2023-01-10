from collections import Counter
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        counter = Counter()
        
        for row in grid:
            counter[tuple(row)] += 1
            
        count = 0
        for j in range(len(grid[0])):
            col = []
            for i in range(len(grid)):
                col.append(grid[i][j])
            count += counter[tuple(col)]
        
        return count