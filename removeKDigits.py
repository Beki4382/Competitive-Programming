class Solution(object):
     def removeKdigits(self, num, k):
            stack = []
            if k == len(num):
                return "0"
            for digit in num:
                while stack and digit < stack[-1] and K>0:
                    stack.pop()
                    k-=1
                stack.append(digit)
            return str(int("".join(stack[:len(num)-k])))
            
            
