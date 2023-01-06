class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        string = ""
        start = 0
        for idx in spaces:
            string += s[start:idx] + " "
            start = idx
        
        string += s[start:]
        return string
    
            
        
        
            