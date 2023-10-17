class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
            
        def binarySearch(q):
            l, r = 0, len(nums)-1
            while l <= r:
                mid = (r+l)//2
               
                if prefix[mid] == q:
                    return mid
                elif prefix[mid] > q:
                    r = mid - 1
                elif prefix[mid] < q:
                    l = mid + 1
            if prefix[mid] > q:
                return mid - 1
            else:
                return mid
        
        ans = []
        for q in queries:
            res = binarySearch(q)
            ans.append(res+1)
        
        return ans 
        
        