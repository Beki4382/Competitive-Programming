class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [1] * 10
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [],
                 [1, 7, 0], [2, 6], [1, 3], [2, 4]]

        
        for i in range(n-1):
            temp = [0]* 10
            for j in range(10):
                for move in moves[j]:
                    temp[j] += dp[move]
            dp = temp
            
        
        return sum(dp)  % (10 **9 + 7)
                    
                    
      