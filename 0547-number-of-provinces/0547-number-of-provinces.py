class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        d = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if j != i and isConnected[i][j] == 1:
                    d[i +1].append(j + 1)
        
        
        def dfs(node):
            if not node:
                return 0
            
            visited.add(node)
            for neighbour in d[node]:
                # print(neighbour)
                if neighbour not in visited:
                    dfs(neighbour)
        
        visited = set()
        count = 0
        for node in range(1, len(isConnected)+1):
            if node not in visited:
                count += 1
                dfs(node)
                
        return count
                
    
        