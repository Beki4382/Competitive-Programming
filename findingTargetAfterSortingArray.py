class Solution(object):
    def targetIndices(self, nums, target):
        indices = []
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            min = i
            for j in range(i+1, len(nums)):
                if (nums[j] < nums[min]):
                    min = j
            nums[i], nums[min] = nums[min], nums[i]
        for k in range(len(nums)):
            if(target == nums[k]):
                indices.append(k)
        return indices
