class Solution(object):
    def largestNumber(self, nums):
        
        strNums = [str(num) for num in nums]
        for i in range(len(nums)):
            starting = i
            j = i+1
            for j in range(len(nums)-1):
                if strNums[j]+strNums[i] < strNums[i]+strNums[j]:
                    strNums[i],strNums[j] = strNums[j], strNums[i]
                    
        return "".join(map(str, strNums))
            
