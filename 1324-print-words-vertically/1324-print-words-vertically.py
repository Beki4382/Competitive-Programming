class Solution:
    def printVertically(self, s: str) -> List[str]:
        array = s.split(" ")
        maxLen = 0
        
        
        for a in array:
            if len(a) > maxLen: 
                maxLen = len(a)
                
    
        solution = [""]*maxLen
        
        
        for word in array:
            for i in range (0,len(solution)):
                if i < len(word): 
                    solution[i] += word[i]
                else: 
                    solution[i] += " "
        
       
        solution2 = []
        for word in solution:
            solution2.append(word.rstrip())
        return solution2
 