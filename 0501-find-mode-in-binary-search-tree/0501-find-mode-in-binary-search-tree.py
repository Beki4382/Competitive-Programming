# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        d = defaultdict(int) 
        
        def traverse(root):
            if root:

                traverse(root.left)
                d[root.val] += 1
                traverse(root.right)
                
        traverse(root)

        output = []
        freq_list = list(d.values())
        max_freq = max(freq_list)
        
        for val, freq in d.items():
            if freq == max_freq:
                output.append(val)
        
        
        return output
            
            
        