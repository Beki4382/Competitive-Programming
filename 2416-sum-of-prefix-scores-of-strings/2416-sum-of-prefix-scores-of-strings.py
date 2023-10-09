class Trie:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]
        self.count = 0
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        self.root = Trie()
        
        for word in words:
            curr = self.root
            for c in word:
                char = ord(c) -97
                if not curr.children[char]:
                    curr.children[char] = Trie()
            
                curr = curr.children[char]
                curr.count += 1
            curr.is_end = True
            
        ans = []
        for word in words:
            curr = self.root
            total = 0
            for c in word:
                char = ord(c) -97
                total += curr.children[char].count
                curr= curr.children[char]
            ans.append(total)
        return ans
                
        
        
        