class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        x = 0
        for val in operations:
            if val[1] == "-":
                x -= 1
            else:
                x += 1
           
        return x
        