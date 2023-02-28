class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        m = len(s1)
        count_s1 = Counter(s1)
        
        for i in range(len(s2)- m + 1):
            
            count_s2 = Counter(s2[i : i + m])
            
            if count_s2 == count_s1:
                return True
            
        return False
            
            