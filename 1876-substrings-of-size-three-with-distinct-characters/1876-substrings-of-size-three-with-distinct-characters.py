class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        k = 3
        l = 0
        r = 2
        ans = 0
        while r < len(s):
            if len(set(s[l:r+1])) == k:
                ans += 1
            l += 1
            r += 1
        return ans
            