class Solution(object):
    def isArthimetic(self, newArray):
        for i in range(len(newArray)-1):
            if newArray[i+1]-newArray[i] != newArray[1]-newArray[0]:
                return False
            
        return True
        
    def checkArithmeticSubarrays(self, nums, l, r):
        boolVal = []
        for k in range(len(l)):
            new = sorted(nums[l[k]:r[k]+1])
            boolVal.append(self. isArthimetic(new))
        return  boolVal
            
        
