class Solution:
    def average(self, salary: List[int]) -> float:
        
        salary.sort()
        total = sum(salary[1:-1])
        n = len(salary)-2
        average = 0
        
        average = (total)/(n)
        return average
        
        
        