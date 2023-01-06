class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        evens_sum = 0
        answer = []
        
        for num in nums:
            if num % 2 == 0:
                evens_sum += num
        
        for query in queries:
            
            val = query[0]
            idx = query[1]
            
            if nums[idx] % 2 == 0:
                
                if val % 2 == 0:
                    evens_sum += val
                else:
                    evens_sum -= nums[idx]
            else:
                if val % 2 != 0:
                    evens_sum += nums[idx] + val
                
            nums[idx] += val
            answer.append(evens_sum)
            
        return answer
        