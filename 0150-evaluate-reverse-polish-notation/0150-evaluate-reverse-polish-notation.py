
class Solution(object):
    def calculateResult(self,first,last,x):
                if x=="+":
                    return first+last
                if x =="*":
                    return first*last
                if x =="/":
                    return int(float(first)/last)
                if x =="-":
                    return first-last
            
    def evalRPN(self, tokens):
        operators = ["+", "-", "*", "/"]
        stack = []
        for x in tokens:
            if x =="" or x==" ":
                continue
            if x in operators:
                lastnum = stack.pop()
                firstnum =stack.pop()
                result = self.calculateResult(firstnum,lastnum,x)
                stack.append(result)
            else:
                stack.append(int(x))
                
        return stack.pop()
            
            
        
        