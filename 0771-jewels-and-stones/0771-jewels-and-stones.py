class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        jewelsSet = set(jewels)
        count = 0
        
        for char in stones:
            if char in jewelsSet:
                count += 1
        
        return count 
                