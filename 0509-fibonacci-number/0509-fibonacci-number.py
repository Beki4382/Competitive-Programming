class Solution:
    d = {}
    def fib(self, n: int) -> int:
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        self.d[n] = self.fib(n-1)+ self.fib(n-2)
        if n in self.d:
            return self.d[n]
    
        
        
    
        