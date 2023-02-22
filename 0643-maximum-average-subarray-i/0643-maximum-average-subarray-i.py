class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left= 0
        right = 0
        max_sum = float("-inf")
        sum_nums =0
        while right < k:
            sum_nums += nums[right]
            right += 1
        max_sum = max(max_sum, sum_nums / k)
        
        while right < len(nums):
            sum_nums += nums[right]
            sum_nums -= nums[left]
            left += 1
            max_sum = max(max_sum, sum_nums / k)
            right += 1
            
        return max_sum
        