class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        print(nums)
        newArray =[]
        for i in range(len(nums)//2):
            newArray.append(nums[i]+nums[-(i+1)])
        return max(newArray)
