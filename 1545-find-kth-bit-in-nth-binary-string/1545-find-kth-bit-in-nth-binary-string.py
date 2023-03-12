class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def invertReverse(string):
            s = []
            for val in string:
                if val == "0":
                    s.append("1")
                else:
                    s.append("0")
            s.reverse()
            
            return str("".join(s))
        
        def findString(n):
            
            if n == 0:
                return "0"
            
            str = findString( n -1 )
            return str + "1" + invertReverse(str)
        
        output = findString(n)
        return output[k - 1]
        
                
                
        