class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        left , right = 0,1
        if n==1:
                return nums
        while right < n:
            if nums[left] != 0 :
                left +=1
            else:
                if nums[right] !=0:
                    nums[left] = nums[right]
                    nums[right] = 0
                    left +=1
            right +=1
            
                