class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        arr = []
       
        for i in range(n):
            arr += [nums[i]]
            arr += [nums[i + n]]
            
        return arr
            