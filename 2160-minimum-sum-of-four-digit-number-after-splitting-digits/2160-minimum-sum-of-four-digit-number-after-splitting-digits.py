class Solution:
    def minimumSum(self, num: int) -> int:
        
        num = str(num)
        arr = [num[i] for i in range(len(num))]
        arr.sort()
        p1, p2 = 0, len(num) -1
        
        res = 0
        while p1 < p2:
            n1 = (arr[p1]) + arr[p2]
            res += int(n1)
            p1 += 1
            p2 -= 1
            
        return res
        