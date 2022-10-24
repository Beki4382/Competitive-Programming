class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        lnums = nums*2
        ans = [-1]*n
        stack = []
        for i in range (len(lnums)):
            while stack and stack[-1][0] < lnums[i]:
                val, pos = stack.pop()
                ans[pos] = lnums[i]
            if i < n:
                stack.append((lnums[i],i))
        return ans
                
               
        
        
            
       
        