class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        closest = float("inf")
       
        for i, num in enumerate(nums):
            
            sum_of_three = 0
            left = i+1
            right = len(nums)-1
            
            while left < right:
                
                sum_of_three = num + nums[left] + nums[right]
                
                if abs(sum_of_three - target) < abs(closest - target):
                    
                    closest = sum_of_three
                
                if sum_of_three == target:
                    return target
                    
                else:
                    if sum_of_three > target:
                        right -= 1
                    else:
                        left += 1
                
        return closest
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
        