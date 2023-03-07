# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        #iterative code for finding val in binary search tree
        while root != None:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        return None
    
    # recursive code 
        
#         if root == None:
#             return None
        
#         if root.val == val:
#             return root
        
#         if root.val > val:
            
#             return self.searchBST(root.left, val)
            
#         else:
#             return self.searchBST(root.right, val)
        