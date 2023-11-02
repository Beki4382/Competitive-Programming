class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        if len(nums) < 3:
            return False
        
        inc_stack = [nums[0]]
        dec_stack = []
        min_d = {}
        
        for i in range(1, len(nums)):
            while inc_stack and inc_stack[-1] >= nums[i]:
                inc_stack.pop()
            inc_stack.append(nums[i])
            
            while dec_stack and dec_stack[-1] <= nums[i]:
                dec_stack.pop()
            dec_stack.append(nums[i])
            
            min_d[nums[i]] = inc_stack[0]
            
            if len(dec_stack) >= 2:
                if min_d[ dec_stack[-2] ] < dec_stack[-1]:
                    return True
        return False
                
                
                
            
        