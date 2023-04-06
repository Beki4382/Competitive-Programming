class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        def checker(num1, num2):
            for i in range(len(num1)):
                if num1[i] & num2[i]:
                    return False
            return True
            
        final = []
        for word in words:
            arr = [0] * 26
            for char in word:
                arr[(ord(char) - 97)] = 1
            
            final.append(arr)
        
        max_len = 0
        for i in range(len(final)):
            for j in range(i+1, len(final)):
                result = checker(final[i], final[j])
                if result:
                    max_len = max(max_len, len(words[i]) * len(words[j]))
                
        return max_len
            
        
        
        
        
#         max_len = 0
#         for i in range(len(words)):
#             word_set = set(words[i])
#             for j in range(i, len(words)):
#                 if not word_set & set(words[j]):
#                     max_len = max (max_len ,len(word_set) * len(set(words[j])))
                
#         return max_len

        
        
                
                