class Solution(object):
    def numIdenticalPairs(self, nums):
        nums.sort()
        print(nums)
        counter = 0
        for i in range(len(nums)):
            
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    counter = counter+1

        return counter
                
