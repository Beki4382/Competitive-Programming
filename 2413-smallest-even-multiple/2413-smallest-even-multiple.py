class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        greater  = 0
        if 2 > n:
            greater = 2
        else:
            greater = n
        
        while (True):
            if (greater % 2 == 0) and (greater % n == 0):
                lcm = greater
                break
            greater += 1
        return lcm