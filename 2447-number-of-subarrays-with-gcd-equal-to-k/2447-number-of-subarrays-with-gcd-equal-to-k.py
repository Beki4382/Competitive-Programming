class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        sub_arr = 0
        for i in range(len(nums)):
            gcd = nums[i]
            right = i
            while right < len(nums):
                gcd = math.gcd(gcd, nums[right])
                if gcd == k:
                    sub_arr += 1
            
                right += 1
                
        return sub_arr

                
        