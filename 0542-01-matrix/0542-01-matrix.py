class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        def inBound(i, j):
            if 0 <= i < len(mat) and 0 <= j < len(mat[0]):
                return True
            else:
                return False
        
        directions = [(-1,0), (0,-1), (1,0), (0,1)]
        queue = deque()
        visited = set()
        
        ans = [[0] * len(mat[0]) for _ in range(len(mat))]
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i,j,0))
                    visited.add((i,j))
                    ans[i][j] = 0
                    
        print(ans)
        while queue:
            i, j, d = queue.popleft()
            
            for direction in directions:
                new_i = i + direction[0]
                new_j = j + direction[1]
                
                if inBound(new_i, new_j) and (new_i, new_j)  not in visited:
                    queue.append((new_i, new_j, d+1))
                    ans[new_i][new_j] = d+ 1
                    visited.add((new_i, new_j))
            
        return ans
            
        
                
        