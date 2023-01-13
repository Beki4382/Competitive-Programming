class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        wordArray = [float("inf")]*26
        for word in words:
            counter = [0] * 26
            
            for char in word:
                idx = ord(char) - 97
                counter[idx] +=1
            
            for i in range(26):
                wordArray[i] = min(wordArray[i], counter[i])
        print(wordArray)
         
                
        output = []
        for i in range(len(wordArray)):
            if wordArray[i] != 0:
                output.extend(chr(i+97)*wordArray[i])
                
        return output
                
            
            
            
                    
        
            
             
                
            
                
                