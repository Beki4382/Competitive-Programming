import collections
class Solution(object):
    def longestSubarray(self, nums, limit):
        left, right = 0,0
        answer =0
        maxdeq = collections.deque([])
        mindeq = collections.deque([])
        
        for right in range(len(nums)):
            while mindeq and mindeq[-1] > nums[right]:
                mindeq.pop()
            mindeq.append(nums[right])
            
            while maxdeq and maxdeq[-1] < nums[right]:
                maxdeq.pop()
            maxdeq.append(nums[right])
   
            if maxdeq[0] - mindeq[0] <= limit:
                answer =max( answer, right -left +1 ) 
                
            else:
                if maxdeq[0] == nums[left]:
                    maxdeq.popleft()
                if mindeq[0] == nums[left]:
                    mindeq.popleft()
                left+=1
        return answer 
            
                
                   
