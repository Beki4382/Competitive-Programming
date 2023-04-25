# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        d = defaultdict(list)
        
        
        def dfs(root, row):
            if root:
                d[row].append(root.val)
                dfs(root.left, row + 1)
                dfs(root.right, row + 1)
                
        dfs(root,0) 
        ans = []
        for val in d.values():
            res = sum(val)/len(val)
            ans.append(res)
        return ans
            
            
            
            
        