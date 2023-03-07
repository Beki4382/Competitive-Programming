# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        
        def traverse(root):
            if root:
                traverse(root.left)
                traverse(root.right)
                output.append(root.val)
        traverse(root)
             
        return output
        
   
        
        