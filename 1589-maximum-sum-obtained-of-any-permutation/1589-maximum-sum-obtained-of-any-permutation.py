class Solution:
    def maxSumRangeQuery(self, nums: List[int], r: List[List[int]]) -> int:
        n = len(nums)
        arr = [0]* (n + 1)
        nums.sort()
        
        
        for val in r:
            arr[val[0]] += 1
            arr[val[1] + 1] -= 1
            
        for i in range(1, n):
            arr[i] += arr[i - 1]
            
        new_arr = sorted(arr[i] for i in range(n))
        
        sum_ = 0
        for i in range(n):
            sum_ += new_arr[i] * nums[i]
            
        return sum_ % (10 **9 + 7)