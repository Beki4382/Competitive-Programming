class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        smallers = [0]* len(nums)
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if( j!= i and nums[j] < nums[i]):
                    smallers[i] =j   
        return smallers
            
