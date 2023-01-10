class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        output = []
        n = len(boxes)
        
        for i in range(n):
            count = 0
            for j in range(n):
                if boxes[j] == "1":
                    count += abs(i - j)
            output.append(count)
            
        return output
            
                    
        