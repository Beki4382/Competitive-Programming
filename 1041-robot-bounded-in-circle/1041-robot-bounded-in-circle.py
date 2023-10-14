class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = {'N':(0,1), 'E':(1,0), 'S':(0,-1), 'W':(-1,0)}
        
        leftCh = {'N':'W', 'W':'S', 'S':'E', 'E':'N'}
        rightCh = {'N':'E', 'E':'S', 'S':'W', 'W':'N'}
        
        start = [0,0]
        facing = 'N'
        for i in range(len(instructions)):
            if instructions[i] == "G":
                start[0] += directions[facing][0]
                start[1] += directions[facing][1]
         
            elif instructions[i] == "L":
                facing = leftCh[facing]
                
            else:
                facing = rightCh[facing]
      
            
        if facing != 'N' or start == [0,0]:
            return True
        else:
            return False