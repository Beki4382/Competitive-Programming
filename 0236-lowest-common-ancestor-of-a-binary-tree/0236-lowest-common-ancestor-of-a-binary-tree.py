# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cache = {root:None}
        que=deque([root])
        while p not in cache or q not in cache:
            node = que.popleft()
            if node.left:
                que.append(node.left)
                cache[node.left] = node
            if node.right:
                que.append(node.right)
                cache[node.right] = node
        
        
        parent = set()
        while p:
            parent.add(p)
            p = cache[p]
      
     
        while q not in parent:
            q = cache[q]
        return q
        
      