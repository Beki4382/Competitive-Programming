class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort(reverse = True)
        print(piles)
        mine = 0
        for i in range(len(piles)//3):
            k = (i*2)+1
            mine += piles[k]
        return mine
            
        