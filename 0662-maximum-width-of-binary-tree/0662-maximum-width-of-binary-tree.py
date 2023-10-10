# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        maxLen = 1
        que = deque([(root, 1)])
        
        while que:
            length = len(que)
            leftIdx, rightIdx = 0,0
            
            for i in range(length):
                node, index = que.popleft()
                if i == 0:
                    leftIdx = index
                if i == length -1:
                    rightIdx = index
                    
                if node.left:
                    que.append((node.left,2*index))
                    
                if node.right:
                    
                    que.append((node.right, 2*index+1))
                
            maxLen = max(maxLen,(rightIdx - leftIdx + 1) )

        return maxLen   
            
        