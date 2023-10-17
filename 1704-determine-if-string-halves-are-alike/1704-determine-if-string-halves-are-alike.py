class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel = {"a","e","i","o","u","A","E","I","O","U"}
        n = len(s)
        half = n // 2
        count1 = 0
        count2 = 0
        
        for i in range(half):
            if s[i] in vowel:
                count1 += 1
        for i in range(half,n):
            if s[i] in vowel:
                count2 += 1
        return count1 == count2
            
            
        
        
        