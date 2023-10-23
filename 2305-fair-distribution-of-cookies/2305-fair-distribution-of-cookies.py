class Solution:
    def __init__(self):
        self.final = float('inf')
    
    def solve(self, i, cookies, k, mask):
        if i == len(cookies):
            ans = float('-inf')
            for it in range(k):
                ans = max(mask[it], ans)
            self.final = min(ans, self.final)
            return
        
        for it in range(k):
            mask[it] += cookies[i]
            self.solve(i + 1, cookies, k, mask)
            mask[it] -= cookies[i]
            if mask[it] == 0:
                break
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        mask = [0] * k
        self.solve(0, cookies, k, mask)
        return self.final
      
    
        