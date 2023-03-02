class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        r = 0
        d = {}
        for r in range(len(s)):
            d[s[r]] = 1 + d.get(s[r], 0)
            max_ = max(d.values())
            
            while k < (r - l + 1) - max_:
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    d.pop(s[l])
                l += 1
            res = max(res, r -l +1)
        return res
                
                