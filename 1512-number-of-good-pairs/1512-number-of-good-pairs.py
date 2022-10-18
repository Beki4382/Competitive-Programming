class Solution(object):
    def numIdenticalPairs(self, nums):
        c = Counter(nums)
        print(c)
        result = 0
        for num in c.keys():
            if c[num] > 1:
                result += c[num] * (c[num]-1)//2
        return result
                
        
        
        
        
        
        