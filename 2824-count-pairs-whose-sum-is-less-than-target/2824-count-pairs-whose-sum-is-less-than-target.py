class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        pair_count = 0
        left_index, right_index = 0, len(nums) - 1
        sorted_nums = sorted(nums)
        
        while left_index < right_index:
            if sorted_nums[left_index] + sorted_nums[right_index] < target:
                pair_count += right_index - left_index
                left_index += 1
            else:
                right_index -= 1
                
        return pair_count

        