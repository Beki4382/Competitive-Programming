class Solution(object):
    def rotate(self, nums, k):
        k =k%len(nums)
        start, end = 0, len(nums)-1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start +=1
            end -=1
        start, end = 0, k-1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start +=1
            end -=1
        start, end = k, len(nums)-1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start +=1
            end -=1
        return nums
        
        