class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        d = {0:0, 1:1}
        
        def generator(n):
                if n == 0:
                    return 0
                if n == 1:
                    return 1
                
                if n in d:
                    return d[n]

                else:
                    if n % 2 == 0:
                        d[n] = generator( n // 2)
                        res = d[n]
                        return res
                    elif n % 2 == 1:
                        d[n] = generator( n // 2) + generator(n // 2 + 1)
                        res = d[n]
                        return res
        return max([generator(i) for i in range(n, -1, -1)])
                
               
        
        