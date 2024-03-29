# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def dfs(root):
            # if not root:
            #     return ")"
            left = ""
            right = ""
            
            if not root.left and not root.right:
                return str(root.val) 
            
            if root.left:
                left = "(" + dfs(root.left) + ")"
                
            else:
                left = "()"
                
            if root.right:
                right = "(" + dfs(root.right) + ")"
            
            return str(root.val) + left + right 
            
            
        return dfs(root)