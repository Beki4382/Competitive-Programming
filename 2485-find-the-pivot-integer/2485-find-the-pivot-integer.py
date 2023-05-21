class Solution:
    def pivotInteger(self, n: int) -> int:
        val = n*(n+1)//2
        return isqrt(val) if isqrt(val)**2 == val else -1 
        