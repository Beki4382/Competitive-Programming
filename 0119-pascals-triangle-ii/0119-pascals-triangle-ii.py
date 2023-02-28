class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def recur(row_idx):
            if row_idx == 0:
                return [1]
            res = recur(row_idx -1)
            curr = [res[0]]
            
            for i in range(1, len(res)):
                curr.append( res[i-1] + res[i] )
                
            curr.append(1)
            
            return curr
        
        return recur(rowIndex)