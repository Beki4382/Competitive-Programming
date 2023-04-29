# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(root, num):
            if not root:
                return 0
                
            num.append(root.val)
            
            if not root.left and not root.right:
                val = "".join(map(str, num))
                return int(val)
            
            left_val = dfs(root.left, num[:])
            right_val = dfs(root.right, num[:])
            
            return left_val + right_val
        
        return dfs(root, [])
     