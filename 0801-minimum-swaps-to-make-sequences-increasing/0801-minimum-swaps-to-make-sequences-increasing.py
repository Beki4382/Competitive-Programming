class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp_keep = [math.inf] * n
        dp_swap = [math.inf] * n
        dp_keep[0] = 0
        dp_swap[0] = 1

        for i in range(1, n):
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                dp_keep[i] = min(dp_keep[i], dp_keep[i - 1])
                dp_swap[i] = min(dp_swap[i], dp_swap[i - 1] + 1)
            
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                dp_keep[i] = min(dp_keep[i], dp_swap[i - 1])
                dp_swap[i] = min(dp_swap[i], dp_keep[i - 1] + 1)

        return min(dp_keep[-1], dp_swap[-1])

        