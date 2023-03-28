class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        w = 0
        while w < len(nums):
            if nums[w] - 1 != w and nums[w] != nums[nums[w]]:
                temp = nums[w]
                nums[w], nums[temp] = nums[temp], nums[w]
                
            else:
                w += 1
                
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return nums[i]
                 