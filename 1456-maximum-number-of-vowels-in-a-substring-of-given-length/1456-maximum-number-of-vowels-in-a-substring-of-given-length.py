class Solution(object):
    def maxVowels(self, s, k):
        ans = 0
        maxi = 0

        for i, c in enumerate(s):

            if c in "aeiou":
                maxi += 1
            if i >= k and s[i - k] in "aeiou" :
                maxi -= 1
            ans = max(ans, maxi)

        return ans