class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ans = []
        graph = defaultdict(list)
        
        for i in range(len(equations)):
            st, en = equations[i][0], equations[i][1]
            wg = values[i]
            graph[st].append((en,wg))
            graph[en].append((st,wg**-1))
            
        def dfs(root,val,en):
            if root not in graph or en not in graph:
                return -1
                
            if root == en:
                return val
            
            seen.add(root)
            for child in graph[root]:
                if child[0] not in seen:
                    res = dfs(child[0], val*child[1],en)
                    if res!= -1:
                        return res   
            return -1
            
        for q in queries:
            st, en = q[0],q[1]
            seen = set()            
            ans.append(dfs(st,1,en))
        return ans 
           
            
        
               
                
                
                
            
            
            
        
        