class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        lis = []
        for i in range(1,n+1):
            lis.append(i)
        
        idx = 0
        while n > 1:
            idx = (idx + k-1)%n
            lis.pop(idx)
            n-=1
            
        return lis[0]
            
        
        