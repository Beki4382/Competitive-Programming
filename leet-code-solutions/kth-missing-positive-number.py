class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr)
        while l < r:
            mid = (l + r) // 2
            if arr[mid] - mid -1 >= k:
                r = mid
            else:
                l = mid + 1
        return l + k
            
        