class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        read = 0
        write = 0
        
        while read < len(nums):
            if nums[read] != 0:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1
                
            read+=1
            
        