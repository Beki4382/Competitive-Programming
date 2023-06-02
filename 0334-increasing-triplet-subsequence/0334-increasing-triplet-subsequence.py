class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        first_num = float("inf")
        sec_num = float("inf")
        
        for num in nums:
            if num > sec_num:
                return True
            
            elif num > first_num:
                sec_num = num
                
            elif num < first_num:
                first_num = num
                
                
        return False
        
        