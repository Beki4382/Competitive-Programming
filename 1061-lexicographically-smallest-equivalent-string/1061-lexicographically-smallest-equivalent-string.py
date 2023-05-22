class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        
        parent = [i for i in range(26)]
        rank = [1 for i in range(26)]
        
        def find(node):
            curr = node
            while curr != parent[curr]:
                curr = parent[curr]
            p = parent[node]
            while parent[node] != curr:
                parent[node] = curr
                node = p
                p = parent[node]
            
            return curr
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 < p2: 
                p1, p2 = p2, p1
                
            parent[p1] = p2
        
            
        for i in range(len(s1)):
            n1 = ord(s1[i])- 97
            n2 = ord(s2[i]) -97
            union(n1, n2)
        
        ans = [0] * len(baseStr)
        
        for i in range(len(baseStr)):
            num = (find(ord(baseStr[i]) - 97))
            ans[i] = chr(num + 97)
        
        result = "".join(ans)    
            
            
        return result 
        