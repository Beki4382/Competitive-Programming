class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        nums.sort()
        
        def GCD(num1, num2):
            if (num2 == 0):
                return abs(num1)
            else:
                return GCD(num2, num1 % num2)
            
            
        return GCD(nums[-1], nums[0])
            
        
        