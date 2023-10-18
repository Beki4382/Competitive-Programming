class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d = {}
        for char in s:
            if char in d:
                return char
            else:
                d[char] = 1

        