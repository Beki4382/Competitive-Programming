from collections import Counter
class Solution(object):
    def maxOperations(self, nums, k):
        c = Counter(nums)
        maxNum = 0
        seen = set()
        for x in c:
            if x not in seen and (k-x) in c:
                if x == (k-x):
                    maxNum +=c[x]//2
                else:
                    maxNum += min(c[x],c[k-x])
                seen.add(x)
                seen.add((k-x))
        return maxNum
        

        
