from collections import Counter
class Solution(object):
    def maxOperations(self, nums, k):
        c = Counter(nums)
        ans = 0
        seen = set()
        for num in c:
            if num not in seen and k - num in c:
                if num == (k - num):
                    ans += c[num]//2
                else:
                    ans += min(c[num], c[k-num])
                seen.add(num)
                seen.add(k-num)
        return ans
                
        