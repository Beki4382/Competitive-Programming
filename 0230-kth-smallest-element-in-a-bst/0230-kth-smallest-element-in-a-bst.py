# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        
        def smallest(root):
            if root:
                smallest(root.left)
                arr.append(root.val)
                smallest(root.right)
            
        smallest(root)
        return arr[k - 1]
            
        
            
        