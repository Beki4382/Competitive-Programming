class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        arr = [0] * len(nums)
        l, r = 0, n
        
        for i in range(0, len(nums), 2):
            arr[i] = nums[l]
            arr[i+1] = nums[r]
            l += 1
            r += 1
            
        return arr
            