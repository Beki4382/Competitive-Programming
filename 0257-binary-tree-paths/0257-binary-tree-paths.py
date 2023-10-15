# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        
        def bt(root,path):
            if not root:
                return 
            if not root.right and not root.left:
                ans.append("".join(path) + str(root.val))
                return 
            
            path.append(str(root.val) + "->" )
            bt(root.left, path)
            bt(root.right, path)
            path.pop()
            
        bt(root,[])
        return ans 
    
            
        
        