class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        pre_sum = [nums[0]]
        for i in range(1,len(nums)):
            pre_sum.append(pre_sum[i-1] + nums[i])
        
        right_sum = 0
        answer = [0] * len(nums)
        for i in range(len(nums)-1, -1,-1):
            right_sum += nums[i]
            result = abs(pre_sum[i] - right_sum)
            answer[i] = result
            
        return answer
            