class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        
        evenCount = defaultdict(int)
        oddCount = defaultdict(int)
        
        for i in range(len(nums)):
            if i % 2 == 0:
                evenCount[nums[i]] += 1
            else:
                oddCount[nums[i]] += 1
        
        sortEven = sorted(evenCount.items(), key=lambda x: x[1], reverse=True)
        sortOdd = sorted(oddCount.items(), key=lambda x: x[1], reverse=True)
        if len(sortEven) == 1 or len(sortOdd) == 1:
            if len(sortEven) == 1:
                sortEven.append((None, 0))
            if len(sortOdd) == 1:
                sortOdd.append((None,0))
        
        res1, res2 = 0,0
        if sortEven[0][0] != sortOdd[0][0]:
            return len(nums) - sortEven[0][1] - sortOdd[0][1]
        else:
            res1 = sortEven[0][1] + sortOdd[1][1]
            res2 = sortEven[1][1] + sortOdd[0][1]
            return len(nums) - max(res1, res2)
        
        
        

        