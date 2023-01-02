class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        lossersDict = {}
        ans = [[],[]]
        
        for match in matches:
            w = match[0]
            l = match[1]
            winners.add(w)
            lossersDict[l] = 1 + lossersDict.get(l,0)
        for losser in lossersDict:
            if lossersDict[losser] == 1:
                ans[1].append(losser)
        for winner in winners:
            if winner not in lossersDict:
                ans[0].append(winner)
        
        ans[0].sort()
        ans[1].sort()
        
        return ans
       
 
        
                
            
                
            
            
        
        