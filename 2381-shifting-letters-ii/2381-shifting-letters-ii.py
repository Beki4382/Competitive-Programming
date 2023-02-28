class Solution:
    def shiftingLetters(self, s: str, sh: List[List[int]]) -> str:
        count_arr = [0]*(len(s)+1)
        string = ""
        
        for row in sh:
            start = row[0]
            end= row[1]
            
            if row[2] == 0:
                count_arr[start] -= 1
                count_arr[end + 1] += 1
            if row[2] == 1:
                count_arr[start] += 1
                count_arr[end + 1] -= 1
                
        for i in range(1, len(count_arr)):
            count_arr[i] += count_arr[i - 1]
        
        
        for i in range(len(s)):
            
            new_char = ord(s[i]) + count_arr[i]%26
            if new_char < 97:
                new_char += 26
            elif new_char > 122:
                new_char -= 26
            
            string += chr(new_char)
        
        return string
            
            
                
                
                
                
            
            
        