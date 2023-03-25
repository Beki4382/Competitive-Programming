class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens.sort()
        score = 0
        r = len(tokens) -1
        
        for l in range(len(tokens)):
            
            if l > r:
                break
                
            while power < tokens[l] and score:
                power += tokens[r]
                score -= 1
                r -= 1

            if power >= tokens[l]:
                power -= tokens[l]
                score += 1

        return score
        