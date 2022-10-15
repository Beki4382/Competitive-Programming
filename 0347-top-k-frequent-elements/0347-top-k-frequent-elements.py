class Solution(object):
    def topKFrequent(self, nums, k):
        c= Counter(nums)
        newArray = list(set(c))
        newArray.sort(reverse= True, key= lambda x: c[x])
        return newArray [:k]
            
        
      
        