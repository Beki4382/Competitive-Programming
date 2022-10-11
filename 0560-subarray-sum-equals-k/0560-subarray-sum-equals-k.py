class Solution(object):
    def subarraySum(self, nums, k):
        d = {}
        acc = count = 0
        for num in nums:
            acc += num
            if acc == k:
                count += 1
            if acc - k in d:
                count += d[acc-k]
            if acc in d:
                d[acc] += 1
            else:
                d[acc] = 1
        return count
                
        
        
        
        
        
        
        
        
        
        