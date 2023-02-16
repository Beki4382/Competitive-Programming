class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_set = {'a','e','i','o','u','A','E','I','O','U'}
        
        new_s = list(s)
    
        i = 0
        j = len(s)-1
        
        while i < j:
            if new_s[i] in vowel_set and new_s[j] in vowel_set :
                new_s[i], new_s[j] = new_s[j], new_s[i]
                i += 1
                j -= 1
            else:
                if new_s[i] in vowel_set:
                    j-=1
                else:
                    i += 1
           
                
                
        return "".join(new_s)
        