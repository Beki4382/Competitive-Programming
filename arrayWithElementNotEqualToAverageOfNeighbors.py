class Solution(object):
    def rearrangeArray(self, nums):
        nums.sort()
        newArray = [0]*len(nums)
        if len(nums)%2 != 0:
            for i in range(len(nums)//2+1):
                newArray[i*2] = nums[i]
            j =1
            for i in range(len(nums)//2+1, len(nums)):
                newArray[j] = nums[i]
                j =j+2
        else:
            for i in range(len(nums)//2):
                newArray[i*2] = nums[i]
            j=1
            for i in range(len(nums)//2, len(nums)):
                newArray[j] = nums[i]
                j =j+2
            
        return newArray
                
       
