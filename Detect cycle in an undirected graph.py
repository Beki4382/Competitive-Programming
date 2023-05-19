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
