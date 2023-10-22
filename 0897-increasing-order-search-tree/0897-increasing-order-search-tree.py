# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        queue = [root]
        value_list = []
        
        while queue:
            value_list.append(queue[0].val)
            
            if queue[0].left:
                queue.append(queue[0].left)
                
            if queue[0].right:
                queue.append(queue[0].right)
                
            queue.pop(0)
            
        sorted_values = sorted(value_list)
        new_root = TreeNode(sorted_values[0])
        
        def insert(node, value):
            if node.right:
                return insert(node.right, value)
            else:
                node.right = TreeNode(value)
            
        for value in sorted_values[1:]:
            insert(new_root, value)
        
        return new_root

        