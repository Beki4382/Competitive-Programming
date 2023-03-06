class StockSpanner:

    def __init__(self):
        self.stack = []
        self.i = 0

    def next(self, price: int) -> int:
        res = 0
       
        while self.stack and self.stack[-1][1] <= price:
            self.stack.pop()
        

        if not self.stack:
            res = self.i+1
        else:
            res = self.i - self.stack[-1][0]
        
        self.stack.append((self.i,price))
        self.i += 1
        
        return res
        
