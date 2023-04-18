class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = [0] * n
        
        for i in range(n):
            arr[i] = start + (2 * i)
            
        res = 0
        for j in range(n):
            res = res ^ arr[j]
            
        return res
        