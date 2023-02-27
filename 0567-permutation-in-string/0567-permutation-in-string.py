class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        
        if n > m: return False
       
        cnt_s1, cnt_s2 = [0] * 26, [0] * 26
        
        for i in range(n):
            cnt_s1[ord(s1[i]) - ord('a')] += 1
        
        for i in range(m):
            
            cnt_s2[ord(s2[i]) - ord('a')] += 1
            
            if i >= n: cnt_s2[ord(s2[i - n]) - ord('a')] -= 1
            
            if cnt_s1 == cnt_s2: return True
        return False
        