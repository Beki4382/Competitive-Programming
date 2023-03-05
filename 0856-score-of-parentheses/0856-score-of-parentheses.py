class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = []
        open = 0
        count = 0
        
        for i, val in enumerate(s):
            
            if val == "(":
                open += 1
            else:
                open -= 1
                if i > 0 and s[i - 1] == "(":
                    count += 2 ** open
        return count

        