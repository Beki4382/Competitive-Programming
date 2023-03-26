class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = []
        for sent in sentences:
            count = 0
            for val in sent:
                if val == " ":
                    count += 1
            count += 1
            ans.append(count)
        return max(ans)
        
        