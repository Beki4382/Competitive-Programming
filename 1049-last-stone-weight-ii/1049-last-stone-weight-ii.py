class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        @cache
        def dp(i, s1, s2):
            if i == len(stones):
                return abs(s1-s2)
            withStone = dp(i+1, s1 + stones[i], s2)
            withOutStone = dp(i+1, s1, s2 + stones[i])
            
            return min(withStone,withOutStone)
        return dp(0,0,0)