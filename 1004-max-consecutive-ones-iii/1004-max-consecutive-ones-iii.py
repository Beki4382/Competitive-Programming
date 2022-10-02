class Solution(object):
    def longestOnes(self, nums, k):
        
        n = len(nums)
        l, r = 0, 0
        max_len = 0
        
        while r < n:
            if nums[r] == 0:
                if k > 0:
                    r +=1
                    k -=1
                elif l == r:
                    l +=1
                    r +=1
                else:
                    max_len = max(max_len, r-l)
                    if nums[l] == 0:    k+=1
                    l +=1
            else:
                r +=1
        
        max_len = max(max_len, r-l)
        return max_len
            
        
        