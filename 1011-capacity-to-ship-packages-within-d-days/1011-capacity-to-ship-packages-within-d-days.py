class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def dayCalc(mid_w):
            r = 0
            day = 1
            count = 0
            for r in range(len(weights)):
                count += weights[r]
                if count > mid_w:
                    day += 1
                    count = weights[r]

            return day
        
        
        left = max(weights)
        right = sum(weights)
        
        while left <= right:
            mid_w = left + (right - left) // 2
            
            if dayCalc(mid_w) > days:
                left = mid_w + 1
            else:
                right = mid_w - 1
        
        
        return left
       
        
        
        
        
      
        
        
        