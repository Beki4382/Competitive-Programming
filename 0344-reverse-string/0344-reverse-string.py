class Solution:
    def reverseString(self, s: List[str]) -> None:
        r = len(s)-1
        l = 0
    
        def reverser(string, l, r):
            
            if l >= r:
                return 
            
            string[l], string[r] = string[r], string[l]
            
            reverser(string, l + 1, r - 1)
            
            return string
        
        return reverser(s,l,r)
                
            
        
        