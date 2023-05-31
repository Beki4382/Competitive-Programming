# class Solution:
#     d = {}
#     def tribonacci(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
#         if n == 2:
#             return 1

#         if n in self.d:
#             res = self.d[n]
#         else:
#             res = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
#             self.d[n] = res
#         return res

class Solution:
    def tribonacci(self, n: int) -> int:
        ans = [0] * (n + 1)
        if n == 0:
            return 0
        elif n <= 2:
            return 1

        ans[0] = 0
        ans[1] = 1
        ans[2] = 1

        for i in range(3, n + 1):
            ans[i] = ans[i - 1] + ans[i - 2] + ans[i - 3]

        return ans[n]

              
        