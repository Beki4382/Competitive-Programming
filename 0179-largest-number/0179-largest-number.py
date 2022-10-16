class Solution(object):
    def largestNumber(self, nums):
#         strNums = [str(nums) for num in nums]
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)-1):
#                 if strNums[j]+strNums[i] > strNums[i]+strNums[j]:
#                     strNums[i] = strNums[j]
#                 else:
#                     continue
#         return strNums
                    
                    
            
        
        
        
        
        strNums = [str(num) for num in nums]
        for i in range(len(nums)):
            starting = i
            j = i+1
            for j in range(len(nums)-1):
                if strNums[j]+strNums[i] < strNums[i]+strNums[j]:
                    strNums[i],strNums[j] = strNums[j], strNums[i]
                
                    
        return str(int("".join(strNums)))
       