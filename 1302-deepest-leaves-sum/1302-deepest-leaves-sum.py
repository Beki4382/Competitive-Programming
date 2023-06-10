# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        curLayer = [root]
        while curLayer:
            lastSum, nextLayer = 0, [] # init sum to zero
            for node in curLayer:
                lastSum += node.val # rolling sum
                if node.left: nextLayer.append(node.left)
                if node.right: nextLayer.append(node.right)
            curLayer = nextLayer
        return lastSum
