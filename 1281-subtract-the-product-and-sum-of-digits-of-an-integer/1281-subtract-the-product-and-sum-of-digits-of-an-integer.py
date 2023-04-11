class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        pro= 1
        sum_ = 0
        for char in n:
            pro = pro * int(char)
            sum_ += int(char)
        return pro - sum_
            
        