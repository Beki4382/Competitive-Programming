class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
            
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.nums[right]
        else:
            return self.nums[right] - self.nums[left-1]
        

