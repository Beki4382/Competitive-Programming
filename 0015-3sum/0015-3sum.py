class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        output = []
    
        #fix one number and find the other two numbers.
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
                
            left = i+1
            right = len(nums) -1
            
            while left < right:
                sum_of_three = nums[i] + nums[left] + nums[right]
                
                if sum_of_three > 0:
                    right -= 1
                elif sum_of_three < 0:
                    left += 1
                else:
                    arr = []
                    arr.append(num)
                    arr.append(nums[left])
                    arr.append(nums[right])
                    
                    output.append(arr)
                    
                    while left < right and nums[left] == arr[1] :
                        left += 1
                    
                    while left < right and nums[right] == arr[2]:
                        right -= 1
            
                    
        return output
            
            
        