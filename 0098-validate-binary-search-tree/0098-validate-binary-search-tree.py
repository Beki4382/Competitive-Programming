# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        min_ = float("-inf")
        max_ = float("inf")
        
        # if not root:
        #     return root
        
        def isValid(root, min_, max_):
            
            if not root:
                return True
            if min_ >= root.val or root.val >= max_:
                return False
            
            val1 = isValid(root.left, min_, root.val)
            val2 = isValid(root.right, root.val, max_)
                
            return val1 and val2
        
        return isValid(root, min_, max_)
                
                
            
            
            
            