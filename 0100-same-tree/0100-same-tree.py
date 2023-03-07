# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def same(p, q):
            if (not p) and not q:
                return True
            
            if (not p) and q:
                return False
            if (not q) and p:
                return False
            if q.val != p.val:
                return False
            
            val_l = same(p.left, q.left)
            val_r = same(p.right, q.right)
            return val_l and val_r
        
        return same(p, q)