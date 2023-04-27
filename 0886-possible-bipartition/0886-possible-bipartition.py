class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        d = defaultdict(list)
        for lis in dislikes:
            d[lis[0] -1].append(lis[1] -1)
            
        
        
        def dfs(node, color):
            if ans[node] != -1:
                if ans[node] != color:
                    return False
                return True
                
            
            ans[node] = color
            
            if node not in d:
                return True
            
            for adj in d[node]:
                if not dfs( adj, 1 - color):
                    return False
            return True
          
        for i in d:
            ans = [-1] * n
            if ans[i] == -1 :
                if not dfs( i , 1):
                    return False
        return True
                
            
        