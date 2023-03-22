class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        max_val = 0
        for i in range(len(accounts)):
            sum_ = sum(accounts[i])
            max_val = max(max_val, sum_)
            
        return max_val
        