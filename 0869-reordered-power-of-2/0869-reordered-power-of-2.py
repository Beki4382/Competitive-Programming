class Solution:
    def reorderedPowerOf2(self, number: int) -> bool:
        digits = Counter(str(number))
        
        for exponent in range(30):
            if digits == Counter(str(1 << exponent)):
                return True
        return False
