class TrieNode:
    def __init__(self):
        self.is_end = False
        self.value = 0
        self.children = [None for _ in range(26)]

class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        for k in key:
            idx = ord(k) - 97
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            
            curr = curr.children[idx]
        curr.is_end = True
        curr.value = val
          
               
    def sum(self, prefix: str) -> int:
        curr = self.root
        count = 0
        for p in prefix:
            idx = ord(p) - 97
            if curr.children[idx]:
                curr = curr.children[idx]
            else:
                return 0
        
        
        stack = [curr]
        while stack:
            node = stack.pop()
            if node.is_end:
                count += node.value
            for child in node.children:
                if child:
                    stack.append(child)
        return count    
               
       


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)