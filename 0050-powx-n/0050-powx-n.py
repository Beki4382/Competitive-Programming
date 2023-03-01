class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n >= 0:
            return self.powCalc( x, n )
        else:
            return 1/self.powCalc( x, -n )
            
            
    def powCalc(self, x, n ):
        if n == 0:
            return 1

        res = self.myPow(x, n//2)

        if (n%2) == 0:
            return res * res
        else:
            return res * res * x

        