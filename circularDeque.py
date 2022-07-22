 def insertLast(self, value: int) -> bool:
        if self.isEmpty():
            self.queue[self.tail] =value
            self.size+=1
            
            return True
        elif  self.isFull():
            return False
        else:
            self.tail = (self.tail+1)%self.maxSize
            self.queue[self.tail] = value
            self.size+=1
            return True
        
      
    def deleteFront(self) -> bool:
        if  self.isEmpty():
            return False
        else:
            self.queue[self.head]= None
            if self.size!=1:
                self.head = (self.head+1)%self.maxSize
            self.size-=1
            return True
    
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.queue[self.tail] = None
            if self.size !=1:
                self.tail=(self.tail-1)%self.maxSize
            self.size-=1
            return True
      
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.head]
    
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.tail]
       

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.maxSize


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
