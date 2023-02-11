class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        maxi = int(c**(0.5))
        right = maxi
        for left in range(maxi+1):
            if left > right:
                return False

            while left**2 + right**2 > c:
                right -= 1

            if left**2 + right**2 == c:
                return True
        