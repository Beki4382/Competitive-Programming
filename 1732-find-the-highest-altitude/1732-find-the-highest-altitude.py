class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = [0] * (len(gain) + 1)
        for i in range(0, len(gain)):
            ans[i+1] = ans[i] + gain[i]
        return max(ans)