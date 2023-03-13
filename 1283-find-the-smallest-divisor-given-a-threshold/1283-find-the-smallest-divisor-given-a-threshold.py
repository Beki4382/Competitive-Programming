class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        low, high = 1, max(nums)
     
        while low < high:
            mid = low + (high - low) // 2
            
            total = 0
            for num in nums:
                total += ceil(num / mid)
                
            if total > threshold:
                low = mid + 1
            
            elif total <= threshold:
                high = mid
            
        return low
                
            
       