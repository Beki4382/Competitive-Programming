class Trie:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(27)]
        self.index = 0
class WordFilter:

    def __init__(self, words: List[str]):
        self.root = Trie()
        for idx, word in enumerate(words):
            word += "{"
            length = len(word)
            word += word
            
            for i in range(length):
                curr = self.root
                prefix = word[i:]
              
                for char in prefix:
                    c = ord(char) - 97
                    if not curr.children[c]:
                        curr.children[c] = Trie()
                    
                    curr = curr.children[c]
                    curr.index = idx

                self.is_end = True
               
    def f(self, pref: str, suff: str) -> int:
        curr = self.root
        q = suff + "{" + pref
        
        for i in range(len(q)):
            c = ord(q[i]) - 97
            if not curr.children[c]:
                return -1 
            curr = curr.children[c]
        return curr.index
            
            
        
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)