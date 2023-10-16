class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        max_= max(nums)
        min_ = min(nums)
        diff = max_ - min_
        
        if (max_ - k ) <= (min_ + k):
            return 0
        else:
            diff = (max_ - k ) - (min_ + k)
            return diff
          