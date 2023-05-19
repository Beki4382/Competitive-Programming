from typing import List
from collections import defaultdict
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		
		color = [0] * V
	
		     
		def dfs(node, parent):
		    if color[node] == 1 :
		        return 1
		        
		    color[node] = 1
		    for child in adj[node]:
		        if color[child] == 2 or parent == child:
		            continue
		        if dfs(child, node):
		            return 1
		    
		    color[node] = 2
		    return 0
		    
	    for i in range(v):
	        if color[i] == 2:
	            continue
            if dfs(i, -1):
                return 1
   
		return 0
		


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends