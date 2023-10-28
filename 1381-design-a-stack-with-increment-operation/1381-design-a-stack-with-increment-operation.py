class CustomStack:
    def __init__(self, maxSize):
        self.stack = [0] * maxSize
        self.currIndex = 0
        self.maxSize = maxSize

    def push(self, x):
        if self.currIndex < self.maxSize:
            self.stack[self.currIndex] = x
            self.currIndex += 1

    def pop(self):
        if self.currIndex == 0:
            return -1
        else:
            self.currIndex -= 1
            return self.stack[self.currIndex]

    def increment(self, k, val):
        n = min(self.currIndex, k)
        for i in range(n):
            self.stack[i] += val
   

# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)