class Solution:
    def beautySum(self, s: str) -> int:    
        beautySum = 0
        for start in range(len(s)):
            counts = {}
            most = 0
            for end in range(start, len(s)):
               
                newchar = s[end]
                newcharcount = counts.get(newchar, 0) + 1
                counts[newchar] = newcharcount
                if newcharcount > most:
                    most = newcharcount

                least = min(counts.values())

                beautySum += (most - least)
        return beautySum
