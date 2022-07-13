class Solution(object):
    def kthLargestNumber(self, nums, k):
        intList = list(map(int, nums))
        intList.sort(reverse = True)
        return str(intList[k-1]) 
        
