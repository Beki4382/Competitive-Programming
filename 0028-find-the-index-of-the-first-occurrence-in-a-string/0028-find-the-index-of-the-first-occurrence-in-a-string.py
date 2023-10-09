class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        
        hashOfNeedle = 0
        hashOfHaystack = 0
        
        x = len(needle)
        alpha = 27
        
        for i in range(x):
            cNeedle = ord(needle[i]) - 96
            cHay = ord(haystack[i]) -96
            
            hashOfNeedle += cNeedle * (alpha ** (x-i - 1))
            hashOfHaystack += cHay * (alpha ** (x-i - 1) )
        if hashOfHaystack == hashOfNeedle:
            return 0
        l = 0
        r = x
        while r < len(haystack):

            left = ord(haystack[l]) -96
            right = ord(haystack[r]) - 96
            hashOfHaystack -= (left * (alpha ** (x - 1)))
            hashOfHaystack *= alpha 
            hashOfHaystack += right
            if hashOfHaystack == hashOfNeedle:
                return l + 1
            l += 1
            r += 1
        return -1
            
    
        
         
            
        
       
        
        