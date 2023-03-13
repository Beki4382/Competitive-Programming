class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        presum = 0
        res = 0
        d ={ 0:1 }
        
        for num in nums:
            presum += num
            diff = presum - goal
            
            if diff in d:
                res += d[diff]
            d[presum] = 1 + d.get(presum, 0)
            
        return res
            