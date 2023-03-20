class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        for i in range(n):
            num = nums[i]
            new_num = nums[nums[i]]
            nums[i] = num + (n * (new_num % n))
            
        for i in range(n):
            nums[i] //= n
        
        return nums
         