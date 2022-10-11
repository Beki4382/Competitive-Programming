class Solution(object):
    def subarraySum(self, nums, k):
        d = {}
        currSum = count = 0
        for num in nums:
            currSum += num
            if currSum == k:
                count+=1
            if currSum - k in d:
                count += d[currSum-k]
            if currSum in d:
                d[currSum] +=1
            else:
                d[currSum] = 1
        return count
        
        
        
        
        
        
        
        
        
        