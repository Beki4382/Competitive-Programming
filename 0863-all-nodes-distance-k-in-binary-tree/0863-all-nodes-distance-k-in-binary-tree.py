class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        
        def traverse(node):
            if not node:
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        
        def bfs(target, k):
            queue = deque([(target.val, 0)])  
            visited = set()
            result = []
            
            if k == 0:
                return [target.val]
            
            while queue:
                node_val, distance = queue.popleft()
                
                if distance == k:
                    result.append(node_val)
                
                visited.add(node_val)
                
                if distance < k:
                    for adj in graph[node_val]:
                        if adj not in visited:
                            queue.append((adj, distance + 1))
            
            return result
        
        return bfs(target, k)
