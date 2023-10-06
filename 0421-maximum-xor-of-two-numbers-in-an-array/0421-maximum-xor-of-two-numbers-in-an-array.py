class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = {}
        maxNum = len(format(max(nums), 'b'))
        numInBin = []
           
        
        for num in nums:
            binNum = format(num, 'b')
            diff = (maxNum) - len(binNum)

            newNum = '0' * diff 
            binNum = newNum + binNum
            numInBin.append(binNum)
        
        def insert(num):
            curr = trie
            for c in num:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
                
        def search(num, n):
            curr = trie
            count = 0
            for i in num:
                if i == "0" and "1" in curr:
                    count += 2 ** (n-1)
                    i = "1" 
                elif i == "1" and "0" in curr:
                    count += 2 ** (n-1)
                    i = "0"
                curr = curr[i]
                n -=1
            return count
        
        for num in numInBin:
            insert(num)
        
        max_num = 0 
        for num in numInBin:
            max_num = max(max_num, search(num, maxNum))

        
        return max_num
            
                
            
          
        
        
            
        
        
        
        