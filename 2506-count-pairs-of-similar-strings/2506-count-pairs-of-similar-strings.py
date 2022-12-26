class Solution:
    def similarPairs(self, words: List[str]) -> int:
        
        wordDic = {}
        
        for word in words:
            word = sorted(word)
            temp = set(word)
            temp = tuple(temp)
            wordDic[temp] = 1+wordDic.get(temp,0)
        
        ans = 0
        for val in wordDic.values():
            if val > 1:
                ans+= ((val * (val + 1)/2))-val
        return int(ans)
                
            
            
            
        
        