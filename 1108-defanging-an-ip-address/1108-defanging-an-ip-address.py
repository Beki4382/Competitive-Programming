class Solution:
    def defangIPaddr(self, address: str) -> str:
        d = {"." : "[.]"}
        
        ans = []
        for val in address:
            if val == ".":
                ans.append(d[val])
            else:
                ans.append(val)
        return "".join(ans)
            
        