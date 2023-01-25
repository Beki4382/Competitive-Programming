class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        n = len(nums)
        k = k%n
        p1 = n-k
        
        nums.reverse()
        nums[:k] = nums[:k][::-1]
        nums[k:n] = nums[k:n][::-1]
        
        
        
        