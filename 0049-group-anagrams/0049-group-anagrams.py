class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for s in strs:
            sortedS =''.join(sorted(s))
            if sortedS in hashMap.keys():
                hashMap[sortedS].append(s)
            else:
                hashMap[sortedS].append(s)
        
        return list(hashMap.values())