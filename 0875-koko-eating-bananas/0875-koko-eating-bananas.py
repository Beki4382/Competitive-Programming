class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def hourCalc(_min):
            min_h = 0
            for i in range(len(piles)):
                if piles[i] % _min == 0:
                    min_h += piles[i] // _min
                else:
                    min_h += piles[i] // _min + 1
                    
            return min_h
        
        
        
        left = 1
        right = max(piles)
        
        while left <= right:
            _mid = left + ( right - left ) // 2
            res = hourCalc(_mid)
            
            if res > h:
                left = _mid + 1
            else:
                right = _mid - 1
                
        return left