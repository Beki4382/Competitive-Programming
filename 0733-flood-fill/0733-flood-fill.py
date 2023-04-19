class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        directions = [(0,1), (1,0), (0,-1),(-1,0)]
        visited = set()
        
       
        def inbound(row, col):
            if 0 <= row < len(image) and 0 <= col < len(image[0]):
                return True
            
        def dfs(row, col):
            
            visited.add((row, col))
            
            for direction in directions:
                
                new_row = row + direction[0]
                new_col = col + direction[1]
            
                if inbound(new_row, new_col)and (new_row, new_col) not in visited:
                    
                    if image[new_row][new_col] == image[sr][sc]:
    
                        image[new_row][new_col] = color
                        dfs(new_row, new_col)
                    
        dfs(sr,sc)
        image[sr][sc] = color
        
        return image
            
        
        
        