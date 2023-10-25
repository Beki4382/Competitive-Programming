# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.constructBT(nums, 0, len(nums) - 1)

    def maxNum(self, nums, i, j):
        ans = i
        for k in range(i, j + 1):
            if nums[k] > nums[ans]:
                ans = k
        return ans

    def constructBT(self, nums, i, j):
        if i > j:
            return None

        index = self.maxNum(nums, i, j)
        root = TreeNode(nums[index])
        root.left = self.constructBT(nums, i, index - 1)
        root.right = self.constructBT(nums, index + 1, j)
        return root

        
