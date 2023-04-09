class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
    
        count = Counter(deck)
        groups = count.values()
        gcd = math.gcd(*groups)
        if gcd >= 2:
            return True
        else:
            return False
        
            
            
    
        