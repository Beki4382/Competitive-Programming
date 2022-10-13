class Solution(object):
    def minimumCardPickup(self, cards):
        n = len(cards)
        cardSet = set()
        minLen = sys.maxsize
        l, r = 0,0
        while r < n:
            if cards[r] not in cardSet:
                cardSet.add(cards[r])
            else:
                while cards[r] in cardSet:
                    cardSet.remove(cards[l])
                    minLen = min(minLen, r-l+1)
                    l+=1
                cardSet.add(cards[r])
            r+=1
        if minLen == sys.maxsize:
            return -1   
        return minLen
        
        