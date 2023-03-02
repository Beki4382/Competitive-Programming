class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        sum_ = 0
        res = 0
        d = defaultdict(int)
        d[0] = 1
        
        for num in nums:
            sum_ += num
            val = sum_ % k
            res += d[val]
            d[val] += 1
        return res
            

        