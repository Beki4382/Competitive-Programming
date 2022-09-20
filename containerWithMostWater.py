class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) -1
        maxWater = 0
        answer = 0
        while left < right:
            maxWater = (right -left) * min(height[left], height[right])
            answer = max(answer, maxWater)
            if height[left] > height[right]:
                right -=1
            else:
                left += 1
        return answer
            
            
            
