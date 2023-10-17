class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        s += "+"
        operator = ["*", "/", "+","-"]
        ope = "+"
        num = 0
        i = 0
        for i in range(len(s)):
            if s[i] == " ":
                continue 
            elif s[i].isdigit():
                num = (num * 10) + int(s[i])
                
            else:
                if ope == "+":
                    stack.append(num)
                elif ope == "-":
                    stack.append(-num)
                elif ope == "*":
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop()/ num))
                    
                num = 0
                ope = s[i]
        return sum(stack)