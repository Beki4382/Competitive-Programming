# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def recu(node):
            if not node:
                return 0
            
            withNode = node.val
            
            if node.left:
                withNode += recu(node.left.left) + recu(node.left.right)
            if node.right:
                withNode += recu(node.right.left) + recu(node.right.right)
            
            
            withoutNode = 0
            withoutNode += recu(node.left) + recu(node.right)
            
            return max(withNode, withoutNode)
        
            
        return recu(root) 