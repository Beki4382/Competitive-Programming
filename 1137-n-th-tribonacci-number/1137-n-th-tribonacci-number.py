class Solution:
    d = {}
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        if n in self.d:
            res = self.d[n]
        else:
            res = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
            self.d[n] = res
        return res

        
        