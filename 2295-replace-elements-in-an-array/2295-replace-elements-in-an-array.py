class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        d = {}
        for idx, num in enumerate(nums):
            d[num] = idx
            
        for lis in operations:
            if lis[0] in d:
                ind = d[lis[0]]
                d.pop(lis[0])
                d[lis[1]] = ind
                
        for num in d:
            nums[d[num]] = num
        
        return nums
            
       
        
       
        
        