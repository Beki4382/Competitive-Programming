class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        for i in range(len(costs)):
            res = costs[i][1] - costs[i][0]
            diff.append([res, i])
            
        diff.sort()
        l, r = 0, len(diff) -1
        cost = 0
        while l < r:
            li = diff[l][1]
            ri = diff[r][1]
            
            cost += costs[li][1]
            cost += costs[ri][0]
            l += 1
            r -= 1
            
        return cost
            
        
            
        
        