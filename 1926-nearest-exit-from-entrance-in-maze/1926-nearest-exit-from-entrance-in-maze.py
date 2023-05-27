class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        def isInBound(row, col):
            if 0 <= row < len(maze) and 0 <= col < len(maze[0]):
                return True
            else:
                return False
            
        def exit(row, col):
            if (row == 0 or row == len(maze) - 1 or col == 0 or col == len(maze[0]) - 1) and (row, col) != tuple(entrance):
                return True
            else:
                return False
            
        def bfs(node):
            queue = deque([(entrance[0], entrance[1])])
            visited = set([(entrance[0], entrance[1])])
            count = 0
            
            while queue:
                for _ in range(len(queue)):
                    val = queue.popleft()
                    
                    if exit(val[0], val[1]):
                        return count

                    for direction in directions:
                        new_row = val[0] + direction[0]
                        new_col = val[1] + direction[1]

                        if isInBound(new_row, new_col) and maze[new_row][new_col] == "." and (new_row, new_col) not in visited:
                            queue.append((new_row, new_col))
                            visited.add((new_row, new_col))
                count += 1
                
            return -1
        
        return bfs(entrance)
