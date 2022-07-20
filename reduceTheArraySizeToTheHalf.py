from collections import Counter
class Solution(object):
    def minSetSize(self, arr):
        c = Counter(arr)
        print(c)
        newArray = list(set(arr))
        newArray.sort(key=lambda x: c[x])
        
        counter =0
        removed =0
        
        for i in reversed(newArray):
            removed +=c[i]
            counter+=1
            if removed >= len(arr)//2:
                return counter
            
