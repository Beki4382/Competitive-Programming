class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        
        def isInBound(r,c):
            return 0 <= r < m and 0 <= c < n
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if isInBound(i+1,j) and isInBound(i, j+1):
                    temp =  dungeon[i][j]
                    dungeon[i][j] = max(dungeon[i+1][j], dungeon[i][j+1])
                    dungeon[i][j] += temp
                    
                    if dungeon[i][j] > 0:
                        dungeon[i][j] = 0
        
            
                elif isInBound(i+1, j) and not isInBound(i,j+1):
                    if dungeon[i+1][j] + dungeon[i][j] > 0:
                        dungeon[i][j] = 0
                    else:
                        dungeon[i][j] = dungeon[i+1][j] + dungeon[i][j]
                    
                elif isInBound(i,j+1) and not isInBound(i+1,j):
                    if dungeon[i][j+1] + dungeon[i][j] > 0:
                        dungeon[i][j] = 0
                    else:
                        dungeon[i][j] = dungeon[i][j+1] + dungeon[i][j]
                else:
                    if dungeon[i][j] > 0:
                        dungeon[i][j] = 0
                    
            
        print(dungeon)
        return abs(dungeon[0][0]) + 1      
                    
                    
                    
                    
        
        
        
        
        
        