class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(27)]
        

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        
        for char in word:
            c = ord(char) - 97
            if not curr.children[c]:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True      
        
    def search(self, word: str) -> bool:
        
        def dfs(i,curr):
            for k in range(i,len(word)):
                
                if word[k] == ".":
                    for child in curr.children:
                        if child:
                            if dfs(k+1,child):
                                return True
                    return False

                else:
                    c = ord(word[k]) - 97
                    if  not curr.children[c]:
                        return False
                    curr = curr.children[c]  
                    
            return curr.is_end
            
        return dfs(0,self.root)      
            
            
   
            
        
        
        
        
                
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)