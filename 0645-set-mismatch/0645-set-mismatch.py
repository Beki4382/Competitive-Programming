class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        i = 0
        while i < len(nums):
            while nums[i] != i + 1 and nums[i] != nums[nums[i] -1]:
                temp = nums[i] - 1
                nums[i], nums[temp] = nums[temp], nums[i]
                
            i += 1
            
        ans = []
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                ans.append(nums[i])
                ans.append(i+1)
        return ans
        
        
        