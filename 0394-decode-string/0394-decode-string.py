class Solution:
    def decodeString(self, s: str) -> str:
        
        num = 0
        string = ""
        stack = []
        
        for i in s:
            if i.isdigit():
                num = num * 10 + int(i) 
                
            elif i == "[":
                stack.append(num)
                stack.append(string)
                string = ""
                num = 0
                
            elif i =="]":
                pre_string = stack.pop()
                pre_num = stack.pop()
                string = pre_string + string * pre_num
            
            else:
                string += i
                
        while stack:
            string  = string + stack.pop()
            
        return string