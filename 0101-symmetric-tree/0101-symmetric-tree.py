# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
                return root
            
        p = root.left
        q = root.right
        
        def symmetric(p, q):
            
            if not p and not q:
                return True
            
            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
           
            val1 = symmetric(p.left, q.right)
            val2 = symmetric(p.right,q.left )
            
            return val1 and val2
        
        
        return symmetric(p, q) 
            
            

        