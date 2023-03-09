class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def positionOfEle(target):
            n = len(nums)
            low, high = 0, n - 1 
            
            while low <= high:
                mid = low + (high - low) // 2
                
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
                    
            return low 
        first = (positionOfEle( target))
        last = (positionOfEle( target + 1 ) -1)
        
        if first > last:
            return [-1, -1]
        
        return [first, last]
    
        
                
                
            
                 
                    
                
        
        