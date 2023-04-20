class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def pascal(n):
            if n == 0:
                return [1]
            if n == 1:
                return [1,1]
            n = n-1
            res = pascal(n)
            
            new_res = [1]
            for i in range(1, len(res)):
                new_res.append(res[i] + res[i-1])
            new_res.append(1)
            return new_res
        return pascal(rowIndex)