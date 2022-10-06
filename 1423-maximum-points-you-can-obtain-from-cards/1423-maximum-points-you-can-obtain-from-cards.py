class Solution(object):
    def maxScore(self, cardPoints, k):
        l, r = 0,len(cardPoints)- k
        total = sum(cardPoints[r:])
        result = total
        while r < len(cardPoints):
            total += cardPoints[l] - cardPoints[r]
            result = max(result, total)
            r +=1
            l +=1
        return result
                
            
            
        