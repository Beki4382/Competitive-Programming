class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) < 3:
            return False 
    
        maxElement = max(arr)
        idx = arr.index(maxElement)
        
        if idx == 0 or idx+1 == len(arr):
            return False
     
        for i in range(len(arr)):
            if i <= idx-1:
                if arr[i] >= arr[i+1]:
                    return False
            elif i >= idx-1 and i < len(arr)-1:
                if arr[i] <= arr[i+1]:
                    return False
            
        return True
            
            
            
            
            
        