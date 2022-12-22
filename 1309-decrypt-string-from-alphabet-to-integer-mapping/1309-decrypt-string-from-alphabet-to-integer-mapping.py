class Solution:
    def freqAlphabets(self, s: str) -> str:
        lis = []
        for i in range(97,123):
            lis.append(chr(i))  
        numDict = {str(i):x for i,x in enumerate(lis, start = 1)}
        res = ""
        i=0
        while i < len(s):
            if i+2 < len(s) and s[i+2] == "#":
                res+= numDict[s[i] + s[i+1]]
                i+=3
            else:
                res+=numDict[s[i]]
                i+=1
        return res
            
        
        