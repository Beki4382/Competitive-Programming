class Solution(object):
    def numberOfSubarrays(self, nums, k):
        d = {}
        count = 0
        preSum = 0
        for num in nums:
            currnum = self.parityind(num)
            preSum +=currnum
            if preSum == k:
                count +=1
            if preSum - k in d:
                count += d[preSum - k]
            if preSum in d:
                d[preSum] +=1
            else:
                d[preSum] = 1
        return count
            
    def parityind(self, num):
        if num %2 == 0:
            return 0
        return 1
        