class Solution(object):
    def findLonely(self, nums):
        c = Counter(nums)
        print(c)
        result = []
        for num in nums:
            if c[num] == 1 and c[num -1] == 0 and c[num +1]==0:
                result.append(num)
        return result
        
        
        
        
        