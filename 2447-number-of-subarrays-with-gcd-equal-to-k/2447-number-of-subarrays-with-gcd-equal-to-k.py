class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        sub_arr = 0
        for i in range(len(nums)):
            gcd = nums[i]
            right = i
            while right < len(nums):
                if math.gcd(gcd, nums[right]) == k:
                    sub_arr += 1
                
                gcd = math.gcd(gcd, nums[right])
                right += 1
                
        return sub_arr

                
        