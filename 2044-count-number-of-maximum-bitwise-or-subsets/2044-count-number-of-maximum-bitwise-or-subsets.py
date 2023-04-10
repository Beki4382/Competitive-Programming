class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        max_or = ans = 0
        
        for index in range(n):
            max_or |= nums[index]
        
        for index in range(1<<n):
            
            mask = index
            cur_or = 0
            for pos in range(n):
                if mask&1<<pos:
                    cur_or |= nums[pos]
            ans += cur_or == max_or
        return ans
            
    
    
    
    