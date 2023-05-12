class Solution:
    def racecar(self, target: int) -> int:

        pos = 0
        speed = 1
        
        q = deque([(pos, speed)])
        turns = 0
        
        while q:
            
            for i in range(len(q)):
                p,s = q.popleft()
                
                if p == target:
                    return turns
                
                new_p1 = p + s
                new_s1 = s * 2
                
                q.append((new_p1, new_s1))
                
                new_s2 = -1 if s > 0 else 1
                
                if (new_p1) < target and s < 0 or (new_p1) > target and s > 0:
                    q.append((p, new_s2))
                
            turns += 1
            
        return turns
            
        
        