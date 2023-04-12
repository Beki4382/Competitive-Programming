class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        MAXN = 2**31 + 1
        for index in range(len(nums)):
            if nums[index] < 0:
                nums[index] = -nums[index] + MAXN
        for pos in range(33):
            count = 0
            for num in nums:
                count += (num&1<<pos != 0)
            if count%3:
                ans |= 1 << pos
        return ans if ans <= 2**31 else MAXN-ans
    
    