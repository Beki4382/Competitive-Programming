class Solution(object):
     def hIndex(self, citations):
            n = len(citations)
            res = 0
            citations.sort()
            if n ==1 and citations[0] == 0:
                return 0
            if n == 1:
                return 1
            for i,j in enumerate(citations):
                if n-i <= j:
                    res = max( res, n-i)
            return res
