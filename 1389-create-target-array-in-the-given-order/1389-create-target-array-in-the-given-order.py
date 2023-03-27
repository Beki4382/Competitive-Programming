class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        output = []
        for idx in range(len(nums)):
            output.insert(index[idx], nums[idx])
            
        return output
            