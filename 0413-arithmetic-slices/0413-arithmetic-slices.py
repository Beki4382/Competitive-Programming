class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        ans = 0
        diff = []
        for i in range(1,n):
            diff.append(nums[i] - nums[i-1])
        m = 1
        for i in range(1,len(diff)):
            if diff[i] == diff[i-1]:
                ans +=m
                m+=1
            else:
                m = 1
        return ans
                
            
            
        
        
        