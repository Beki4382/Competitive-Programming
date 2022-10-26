class Solution(object):
    def maxArea(self, height):
        maxWater = 0
        l ,r = 0,len(height)-1
        while l < r:
            maxWater = max(maxWater, (r-l) * min(height[l], height[r]))
            if height[r] > height[l]:
                l +=1
            else:
                r-=1
        return maxWater
        
 