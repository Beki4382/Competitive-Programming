"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        d = {}
        for i in range(len(employees)):
    
            d[employees[i].id] = i
        def dfs(id):
            
            if employees[d[id]].subordinates == []:
                return employees[d[id]].importance
            
            res = employees[d[id]].importance
            for employeeId in employees[d[id]].subordinates:
                output = dfs(employeeId)
                res += output
                
            return res
                
        return dfs(id)
        