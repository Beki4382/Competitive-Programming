class Solution(object):
     def removeKdigits(self, num, k):
            if len(num) == k:
                return "0"
            stack = []
            for digit in num:
                while stack and k>0 and digit < stack[-1]:
                    stack.pop()
                    k-=1
                stack.append(digit)
            while stack and k>0:
                stack.pop()
                k-=1
            if not stack and K ==0:
                return "0"
            return str(int("".join(stack[:len(num)-k])))
                    
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
