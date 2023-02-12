class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        n = len(players)
        m = len(trainers)
        players.sort()
        trainers.sort()
        
        p1 = 0
        p2 = 0
        count = 0
        
        while p1 < n and p2 < m:
            if players[p1] <= trainers[p2]:
                count += 1
                p1+= 1
                p2+= 1
            else:
                if players[p1] > trainers[p2]:
                    p2+= 1
                else:
                    p1+=1
        return count
            
                
        