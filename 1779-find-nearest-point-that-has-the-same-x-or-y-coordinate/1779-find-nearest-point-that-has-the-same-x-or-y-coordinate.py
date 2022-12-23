class Solution:
    def manhattanDis (self,x1:int, y1:int, x2:int, y2: int):
        xdif = abs(x1 - x2) 
        ydif= abs(y1 - y2)
        if xdif == 0 or ydif == 0:
            return xdif + ydif
        
        return -1
    
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ans = []
        for i in range(len(points)):
            manResult = self.manhattanDis(x, y, points[i][0], points[i][1])
            ans.append(manResult)
        answer = float("inf")
        ansInd = -1
        for i in range(len(ans)):
            if ans[i] < answer and ans[i]!= -1:
                ansInd = i
                answer = ans[i]
        return ansInd
        
            
        
    

        
        
        