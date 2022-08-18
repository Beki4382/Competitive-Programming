class Solution(object):
    def carFleet(self, target, position, speed):
        mapdic = {}
        for i in range(len(position)):
            mapdic[position[i]]=speed[i]
            
        sortedMap = dict(sorted(mapdic.items()))
        stack = []
        timeTaken = []
        for i in sortedMap:
            timeTaken.append((target-i)/sortedMap[i])
       
        for i in range(len(timeTaken)):
            while (len(stack) and timeTaken[i]>=stack[-1] ):
                stack.pop()
            stack.append(timeTaken[i])
        return len(stack)
                
