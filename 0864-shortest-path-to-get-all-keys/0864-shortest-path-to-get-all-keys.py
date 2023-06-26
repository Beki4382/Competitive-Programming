from typing import List
from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        def isInbound(row, col):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                return True
            return False

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        rows = len(grid)
        cols = len(grid[0])
        keyCount = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "@":
                    start = [i, j]

                if grid[i][j].islower():
                    keyCount += 1

        queue = deque([(start[0], start[1], '')])
        visited = set([(start[0], start[1], '')])
        output = 0

        while queue:
            size = len(queue)

            for _ in range(size):
                row, col, keys = queue.popleft()

                if len(keys) == keyCount:
                    return output

                for direction in directions:
                    new_row = row + direction[0]
                    new_col = col + direction[1]

                    if isInbound(new_row, new_col) and grid[new_row][new_col] != "#":
                        cell = grid[new_row][new_col]
                        new_keys = keys
                        if cell.isupper() and cell.lower() not in keys:
                            continue
                        if cell.islower() and cell not in keys:
                            new_keys += cell

                        if (new_row, new_col, new_keys) not in visited:
                            visited.add((new_row, new_col, new_keys))
                            queue.append((new_row, new_col, new_keys))

            output += 1

        return -1
