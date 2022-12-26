class Solution(object):
    def numIdenticalPairs(self, nums):
        
        result = 0
        count = Counter(nums)
        
        for i in count.values():
            result += i * (i - 1) //2
            
        return result
        
        
        
        
