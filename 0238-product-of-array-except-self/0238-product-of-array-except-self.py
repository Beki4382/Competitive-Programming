class Solution(object):
    def productExceptSelf(self, nums):
        outPut = []
        pro = 1
        for i in range(len(nums)):
            pro = pro *nums[i]
            outPut.append(pro)
        pro = 1
        for i in range(len(nums)-1,0,-1):
            outPut[i] = pro * outPut [i-1]
            pro = pro * nums[i]
        outPut[0] = pro
        return outPut
            
            
        