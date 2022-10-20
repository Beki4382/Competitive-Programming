class MyStack(object):

    def __init__(self):
        self.queue = []
        

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        return self.queue.pop()
       
    def top(self):
        return self.queue[-1]
        
    def empty(self):
        if not self.queue:
            return True
        return False
        
