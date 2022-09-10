class Solution(object):
    def maxFrequency(self, nums, k):
        nums.sort()
        left,right = 0,0
        result, total_sum = 0,0
        while right < len(nums):
            total_sum += nums[right]
            while nums[right] * (right - left + 1) > total_sum + k:
                total_sum -= nums[left]
                left +=1
            result = max(result, (right - left +1))
            right +=1
        return result
            
        
            
