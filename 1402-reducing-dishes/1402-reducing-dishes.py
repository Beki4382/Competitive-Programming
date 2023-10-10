class Solution:
    def maxSatisfaction(self, satisfaction):
        satisfaction.sort()  
        
        @cache
        def dp(i, power):
            if i == len(satisfaction):
                return 0
            withDish = (satisfaction[i] * power) + dp(i + 1, power + 1)
            withOutDish = dp(i + 1, power)
            return max(withDish, withOutDish)
        
        return dp(0, 1)
