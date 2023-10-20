# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0
            
            node_sum = 0

            if low <= node.val <= high:
                node_sum += node.val

            node_sum += dfs(node.left)
            node_sum += dfs(node.right)
            
            return node_sum

        return dfs(root)
