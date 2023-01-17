class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for i in range(len(heights)):
            minNum = i
            for j in range(i,len(heights)):
                if heights[minNum] < heights[j]:
                    minNum = j
            heights[i],heights[minNum] = heights[minNum], heights[i]
            names[i] , names[minNum] = names[minNum],names[i] 
        
                    
        return names 
        
        
                    
                    
            