class Solution:
    def largestValsFromLabels(self, values, labels, numWanted, useLimit):
        ve = [(values[i], labels[i]) for i in range(len(values))]
        ve.sort(reverse=True)
        i = 0
        m = {}
        ans = 0
        t = 0
        while t < numWanted and i < len(ve):
            v, l = ve[i]
            if l not in m:
                m[l] = 1
                ans += v
                t += 1
                i += 1
            elif m[l] < useLimit:
                m[l] += 1
                ans += v
                t += 1
                i += 1
            else:
                i += 1
        return ans
