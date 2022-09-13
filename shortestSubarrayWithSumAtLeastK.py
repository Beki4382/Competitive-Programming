class Solution:
    def shortestSubarray(self, nums, k):
        deq = deque()
        length = len(nums)
        answer = length + 1
        
        pre = [0] + list(accumulate(nums))

        for i in range(length + 1):
            while deq and pre[i] - pre[deq[0]] >= k:
                answer = min(answer, i - deq.popleft())
            while deq and pre[i] <= pre[deq[-1]]:
                deq.pop()
            deq.append(i)
        if answer <= length:
            return answer  
        else:
            return -1
