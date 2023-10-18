class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt1 = Counter(s)
        cnt2 = Counter(t)
        minStep = 0
        for i,j in cnt2.items():
            if i in cnt1 and j>cnt1[i]:
                minStep += abs(j-cnt1[i])
            elif i not in cnt1:
                minStep += j
        return minStep