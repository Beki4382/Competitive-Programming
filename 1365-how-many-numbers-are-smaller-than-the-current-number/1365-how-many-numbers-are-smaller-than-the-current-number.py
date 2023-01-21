class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count_arr = [0]*101
        for val in nums:
            count_arr[val] += 1
        
        output = []
        for val in nums:
            count = 0 
            count = sum(count_arr[:val])
            output.append(count)
        return output
            
            
        