class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in hash_table:
                return [idx, hash_table[diff]]
            hash_table[num] = idx
        
        
            
        
       