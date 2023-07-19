class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [-1] * len(questions)
        
        def maxCalc(curr, idx):
            if idx >= len(questions):
                return curr
            if dp[idx] == -1:
                point, brainPower = questions[idx]
                
                use = maxCalc(point, idx + 1 + brainPower)
                skip = maxCalc(0, idx + 1)
                
                dp[idx] = max(use, skip)
            return curr + dp[idx]
        return maxCalc(0, 0)
                
                

            
        