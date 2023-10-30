class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        ans = [0] * 101
    
        for st, end in logs:
            st = st - 1950
            end = end - 1950
            ans[st] += 1
            ans[end] -= 1
    
        max_ = ans[0]
        smallest_idx = 0
        for i in range(1, 101):
            ans[i] = ans[i-1] + ans[i]
            if ans[i] > max_:
                max_ = ans[i]
                smallest_idx = i
        return smallest_idx + 1950

         

        