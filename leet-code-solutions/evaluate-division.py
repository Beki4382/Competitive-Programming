class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        answer = []
        relation = defaultdict(list)

        for i in range(len(equations)):
            start, end = equations[i][0], equations[i][1]
            wg = values[i]
            relation[start].append((end,wg))
            relation[end].append((start, wg ** -1))

        def dfs(root,val,en):
            if not root in relation or en not in relation:
                return -1
            
            if root == en:
                return val

            seen.add(root)
            for child in relation[root]:
                if child[0] not in seen:
                    res = dfs(child[0], val * child[1], en)
                    if res != -1:
                        return res
            return -1

        for q in queries:
            s,e = q[0], q[1]
            seen = set()
            answer.append(dfs(s,1,e))
        return answer
       
        
        