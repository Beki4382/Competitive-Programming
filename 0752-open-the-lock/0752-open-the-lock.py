class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        deadend = set(deadends)
        visited = set ("0000")
        neighbor = []
        turns  = 0
        queue = deque(["0000"])
        
        if "0000" in deadend:
            return -1
        
        while queue:
            for i in range(len(queue)):
                locks = queue.popleft()
                
                if locks in deadend:
                    continue
                if locks == target:
                    return turns
                
                for i in range(len(locks)):
                    numUp = (int(locks[i]) + 1) % 10
                    numDown = (int(locks[i]) - 1) % 10
                    
                    nbr1 = (locks[:i] + str(numUp) + locks[ i + 1 :])
                    nbr2 = (locks[:i]  + str(numDown) + locks[ i + 1 :])
                    
                    for nbr in [nbr1, nbr2]:
                        if nbr not in visited:
                            visited.add(nbr)
                            queue.append(nbr)
            turns += 1
            
        return -1
        
        
        