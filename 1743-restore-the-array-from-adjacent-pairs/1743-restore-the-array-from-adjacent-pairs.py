class Solution:
    def restoreArray(self, adjs: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        indegree = defaultdict(int)
        for i, j in adjs:
            d[i].append(j)
            d[j].append(i)
            indegree[i] += 1
            indegree[j] += 1
            
        que = deque()
        visited = set()
        for val in d:
            if len(d[val]) == 1:
                que.append(val)
                break
         
        ans = []
        while que:
            num = que.popleft()
            
            visited.add(num)
            ans.append(num)
            for child in d[num]:
                if child not in visited:
                        que.append(child)
                
                    
            
        return ans
        
        