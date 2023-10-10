class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        memo = {}
        n = len(nums1)
        def dp(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == len(nums1) or j == len(nums2):
                return 0
            elif nums1[i] == nums2[j]:
                memo[(i,j)] = 1 + dp(i+1, j+1)
                return memo[(i,j)]
            else:
                memo[(i,j)] = max(dp(i,j+1), dp(i+1,j))
                return memo[(i,j)]
        return dp(0,0)  
                
                        