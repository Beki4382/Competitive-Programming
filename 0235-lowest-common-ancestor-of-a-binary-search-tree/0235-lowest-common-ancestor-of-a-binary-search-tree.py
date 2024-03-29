# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root:
            return root
        def ancestor(root, p, q):
            if p.val <= root.val <= q.val:
                return root
            
            if p.val < root.val:
                return ancestor(root.left, p, q)
            if p.val > root.val:
                return ancestor(root.right, p, q)
                
        if p.val > q.val:
            p, q = q, p
        return ancestor(root, p, q)

        
        