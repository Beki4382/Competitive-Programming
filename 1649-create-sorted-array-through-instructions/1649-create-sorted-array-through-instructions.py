class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        
        ans = 0
        nums = []
        for i in instructions:
            left = bisect.bisect_left(nums, i)
            right = bisect.bisect_right(nums,i)
            
            ans += min(left, len(nums)- right)
            bisect.insort(nums,i)
            
        return ans %(10 ** 9 + 7)
            