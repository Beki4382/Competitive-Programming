class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i = 0
        stack = []
        while i < len(asteroids):
            if not stack:
                stack.append(asteroids[i])
            else:
                if stack[-1] < 0 or asteroids[i] > 0:
                    stack.append(asteroids[i])
                else:
                    if stack[-1] == abs(asteroids[i]):
                        stack.pop()
                    elif stack[-1] < abs(asteroids[i]):
                        stack.pop()
                        i -=1
                    
            i += 1

        return stack
            
            