class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for w in range(len(nums)):
            while (nums[w]) != w + 1 and nums[w] != 0:
                temp = nums[w] - 1
                nums[w], nums[temp] = nums[temp], nums[w]
        
        for i in range(len(nums)):
            if nums[i] == 0:
                return i + 1
            
        return 0
        
