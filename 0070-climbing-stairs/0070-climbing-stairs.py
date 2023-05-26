class Solution:
    d = {}
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        if n not in self.d:
            self.d[n] = self.climbStairs(n -1)+ self.climbStairs(n -2)
        return self.d[n]
        