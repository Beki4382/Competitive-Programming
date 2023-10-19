# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        visited = defaultdict(int)
        ans = []
        def dfs(root):
            if not root:
                return 
            subTree = tuple([dfs(root.left), root.val, dfs(root.right)])
            if subTree in visited and visited[subTree] == 1:
                ans.append(root)
            visited[subTree] += 1
            return subTree
        dfs(root)
                            
        return ans
                
                            
                
        
        