class Solution(object):
    def findOriginalArray(self, changed):
        originalLen = len(changed)//2
        changed.sort()
        double = 0
        if (len(changed)%2 ==0 and changed[0]!= 0):
            for i in range(len(changed)//2):
                double = (changed[i])*2
                changed.remove(double)
            if len(changed) == originalLen:
                return changed
            else:
                return []
        elif (len(changed)%2 ==0 and changed[0] == 0):
            if (changed[0] == changed[1]):
                for i in range(len(changed)//2):
                    double = (changed[i])*2
                    changed.remove(double)
                if len(changed) == originalLen:
                    return changed
                    
            else:
                []
        
        else:
            return []
                
        
