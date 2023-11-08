class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        def is_inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(row, col):
            if not is_inbound(row, col) or grid[row][col] == 0:
                return 1  # It's part of the perimeter
            if visited[row][col]:
                return 0

            visited[row][col] = True
            perimeter = 0

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                perimeter += dfs(new_row, new_col)

            return perimeter

        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        perimeter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += dfs(i, j)

        return perimeter
