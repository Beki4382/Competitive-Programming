class Solution(object):
    def smallestNumber(self, num):
        sortedArray = sorted(str(abs(num)))
        if num < 0:
            return -int("".join(sortedArray[::-1]))
        elif num ==0:
            return 0
        else:
            i = 0
            while sortedArray[i] =='0':
                i+=1
            sortedArray[0], sortedArray[i] = sortedArray[i], sortedArray[0]
            return int("".join(sortedArray))
                    
                    
                
            
        
        
        
        