class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        n = len(temperatures)
        ans = [0]*n
        for i in range(n):
            while stack and temperatures[i] > stack[-1][0]:
                val, pos = stack.pop()
                ans[pos] = i-pos 
            stack.append((temperatures[i],i))
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       