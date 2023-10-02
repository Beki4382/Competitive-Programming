class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums) -1
        dp1 = [0] * n
        dp2 = [0] * n
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums)
        
        dp1[0] = nums[0]
        dp2[0] = nums[1]
        
        dp1[1] = max(nums[0], nums[1])
        dp2[1] = max(nums[1], nums[2])
        for i in range(2,len(nums)-1):
            dp1[i] = max(dp1[i-2]+nums[i], dp1[i-1])
        
        for j in range(3,(len(nums))):
            dp2[j-1] = max(dp2[j-3] + nums[j], dp2[j-2])
            
        
        return max(dp1[-1], dp2[-1])