class Trie:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        words.sort()
        self.root = Trie()
        # curr = self.root
        max_ = 0
        ans = ""
        
        
        for word in words:
            curr = self.root
            for i in range(len(word)):
                c = ord(word[i]) -97
                
                if not curr.children[c] and i+1 == len(word):
                    curr.children[c] = Trie()
                    if len(word) > len(ans):
                        
                        ans = word
                elif not curr.children[c] and i + 1 != len(word):
                    break
                curr = curr.children[c]
        return ans
                
            
      
        
        
        