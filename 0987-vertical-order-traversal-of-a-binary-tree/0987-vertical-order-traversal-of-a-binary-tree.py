# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res= []
        
        def traverse(row, col, root):
            if root:
                res.append([col, row, root.val])

                traverse(row+1, col-1, root.left)

                traverse(row+1, col+1, root.right)

            return 
        
        traverse(0, 0, root)
        
        keys = sorted(res, key = lambda x : (x[0], x[1], x[2]))
        
        d = defaultdict(list)
        
        for c, r, val in keys:
            d[c].append(val)
        
        ans = []
        for val in d.values():
            ans.append(val)
        
        return ans
            
            
     
            