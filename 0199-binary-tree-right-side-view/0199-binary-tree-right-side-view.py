# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        output = []
        queue = [root]
        
        if not root:
            return output
        
        
        while queue:
            
            for _ in range(len(queue)):
                
                temp = queue.pop(0)
                
                if temp.left:
                    queue.append(temp.left)
                    
                if temp.right:
                    queue.append(temp.right)
                    
            output.append(temp.val)
            
        return output
        
        
        
        
            
            
        