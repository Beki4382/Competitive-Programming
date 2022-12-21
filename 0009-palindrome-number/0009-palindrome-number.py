class Solution(object):
    def isPalindrome(self, x):
        lis = [num for num in str(x)]
        return lis == lis[::-1]
        
        
        
        
        