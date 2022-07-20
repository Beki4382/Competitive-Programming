class Solution(object):
    def topKFrequent(self, nums, k):
        c = Counter(nums)
        newArray= list(set(nums))
        newArray.sort(reverse = True, key = lambda x: c[x])
        
        newList =[]
        return (newArray[:k])
            
            
