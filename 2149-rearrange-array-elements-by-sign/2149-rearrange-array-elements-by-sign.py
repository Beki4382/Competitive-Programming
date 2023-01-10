class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        new_num = [0] * len(nums)
        pos = 0
        neg = 1
        
        for num in nums:
            if num > 0:
                new_num[pos] = num
                pos +=2
            else:
                new_num[neg] = num
                neg += 2
                
        return new_num
            
            
            
                
        