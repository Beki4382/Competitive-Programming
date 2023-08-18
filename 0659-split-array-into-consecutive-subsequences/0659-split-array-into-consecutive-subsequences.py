class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        seq = defaultdict(int)
        count = Counter(nums)
        
        for num in nums:
            
            if not count[num]:
                continue
            if seq[num - 1] > 0:
                seq[num - 1] -= 1
                seq[num] += 1
                count[num] -=1
                
            else:
                if (not count[num + 1] or not count[num + 2]):
                    return False
                count[num] -= 1
                count[num +1] -=1
                count[num + 2] -=1
                seq[num + 2] += 1
                
                
        return True
        