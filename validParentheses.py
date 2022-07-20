class Solution(object):
    def isValid(self, s):
        stack = []
        for x in s:
            if x in ["(","{","["]:
                stack.append(x)
            else:
                if not stack:
                    return False
                char=stack.pop()
                if char =='(':
                    if x !=')':
                        return False
                if char =='[':
                    if x !=']':
                        return False
                if char =='{':
                    if x !='}':
                        return False
        if stack:
                return False
        return True
                    
