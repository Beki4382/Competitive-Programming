class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        sum_ = 0
        max_sum = 0
        left ,right = 0,0
        flag = False
        for num in nums:
            if num > 0:
                flag = True
        if not flag:
            return max(nums)
        while right < len(nums):
            sum_ += nums[right]
            max_sum = max(max_sum, sum_)
            if sum_ < 0:
                left = right
                sum_ = 0
            right += 1
            
        return max_sum
            
        