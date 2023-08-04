class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_a, int_b = int(a, 2), int(b, 2)
        
        ans = bin(int_a + int_b)
        return ans[2:]
        
        
        