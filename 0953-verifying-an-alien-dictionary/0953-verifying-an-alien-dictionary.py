class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alienDict = {w:i for i,w in enumerate(order)}
        
        wordsList = []
        for word in words:
            temp = []
            for char in word:
                temp.append(alienDict[char])
            wordsList.append(temp)
                
        for i in range(1,len(wordsList)):
            if wordsList[i-1] > wordsList[i]:
                return False
        return True
                