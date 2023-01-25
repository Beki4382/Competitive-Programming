class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right  = 0,1
        while right < len(nums):
            if nums[left] == nums[right]:
                nums.pop(right)
            else:
                right+=1
                left+=1
        return len(nums)

        