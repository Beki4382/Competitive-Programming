# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        output = []
        
        if root:
            queue.append(root)
        
        while queue:
            size = len(queue)
            sibiling = []
            
            for _ in range(size):
                temp = queue.pop(0)
                sibiling.append(temp.val)
            
                if temp.left:
                    queue.append(temp.left)

                if temp.right:
                    queue.append(temp.right)
                
            output.append(sibiling) 
        
        return output
        
        
           
                
        
         
    
        
        
           
       
        
                