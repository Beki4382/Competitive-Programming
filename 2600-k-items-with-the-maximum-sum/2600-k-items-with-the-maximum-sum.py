class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        num = numOnes + numZeros + numNegOnes
        
        if numOnes >= k:
            return k
        
        if numZeros + numOnes >= k:
            return numOnes
        
        return numOnes - (k - (numOnes + numZeros))
        
        