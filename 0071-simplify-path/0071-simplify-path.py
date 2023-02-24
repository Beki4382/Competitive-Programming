class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        new_p = path.split("/")
        
        for val in new_p:
            
            if val == "" or val == ".":
                continue
            if stack and val == "..":
                stack.pop()
            elif val == "..":
                continue
            else:
                stack.append(val)
        
            print(stack)
        string = "/".join(stack)
        return "/" + string
            
        
        