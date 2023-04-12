class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        source = set()
        sink = set()
        
        for edge in edges:
            source.add(edge[0])
            sink.add(edge[1])
        ans = []
        for val in source:
            if val in sink:
                continue
            ans.append(val)
        return ans
        
        
        