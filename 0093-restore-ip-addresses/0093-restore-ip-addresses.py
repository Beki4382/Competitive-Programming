class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        
        def backtrack(idx, dots, res):
            if dots == 4 and idx == len(s):
                ans.append(res[:-1])
                return
            if dots > 4:
                return 
            
            for i in range(idx, min(idx + 3, len(s))):
                if int(s[idx : i + 1]) < 256 and ( idx == i or s[idx] != "0"):
                    backtrack( i + 1, dots + 1, res + s[idx : i + 1] + ".")
                    
                    
        backtrack(0, 0, "")
        return ans
                
                
        
        