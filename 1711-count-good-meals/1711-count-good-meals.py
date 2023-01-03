from collections import Counter
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        
        count = Counter(deliciousness)
        good_meal = 0
        n= 22
        
        for meal in deliciousness:
            count[meal] -= 1
            for i in range(n):
                good_meal += count.get(2**i - meal,0)
    
        return good_meal % (10**9 + 7)
                
            
        