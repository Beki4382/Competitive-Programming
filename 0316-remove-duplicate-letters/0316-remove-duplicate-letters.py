class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_occurance = {}
        for i in range(len(s)):
            last_occurance[ s[i] ] = i
       
        for i, ch in enumerate(s):
            if( ch in seen ):
                continue
            else:
                
                while( stack and stack[-1] > ch and last_occurance[stack[-1]] > i ):
                    removed_char = stack.pop()
                    seen.remove(removed_char)
                seen.add(ch)
                stack.append(ch)
            
        return ''.join(stack)
        
        