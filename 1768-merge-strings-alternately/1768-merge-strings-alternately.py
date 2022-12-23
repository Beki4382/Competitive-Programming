class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        i = 0
        j = 0
        while i < len(word1) or j < len(word2):
            if i == len(word1) and j < len(word2):
                res+=word2[j]
                j +=1
                
            elif i < len(word1) and j == len(word2):
                res+= word1[i]
                i+=1
                
            else:
                res+= word1[i]+word2[j]
                i += 1
                j += 1
        return res
            
            
        