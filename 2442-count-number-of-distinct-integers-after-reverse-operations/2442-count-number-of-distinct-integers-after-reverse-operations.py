class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        for val in nums:
            
            val = str(val)[::-1]
            numSet.add(int(val))
            
        return len(numSet)
            
            
            