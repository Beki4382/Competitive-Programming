class Solution(object):
    def removeDigit(self, number, digit):
        best  = ""
        for i,c in enumerate(number):
            if c== digit:
                current = number[:i] +number[i+1:]
                if best == "" or current >best:
                    best = current
        return best