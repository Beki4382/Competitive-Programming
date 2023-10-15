class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        seen = set()
        def dfs(path, tile):
            if path:
                seen.add(path)
            
            for j in range(len(tile)):
                dfs(path + tile[j], tile[:j] + tile[j+1:]) 
                
        dfs('', tiles)     
        return len(seen)
