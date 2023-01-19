class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        maxElement = -1
        
        right = len(arr)-1
       
        while right > -1:
            if arr[right] > maxElement:
                arr[right],maxElement = maxElement, arr[right]
                
            elif arr[right] < maxElement:
                arr[right] = maxElement
                
            right -= 1
            
        return arr
            
        
        
        
        