# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        
        def dfs(root, path, current_sum):
            if not root:
                return
            current_sum += root.val
            path.append(root.val)
            
            if not root.left and not root.right and current_sum == targetSum:
                ans.append(list(path))
            
            dfs(root.left, path, current_sum)
            dfs(root.right, path, current_sum)
            
            path.pop()  
            
        dfs(root, [], 0)
        return ans
