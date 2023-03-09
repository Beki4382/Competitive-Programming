class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        output = []
        candidates = [i for i in range(1, n + 1)]
        
        def backtrack(num, arr):
            
            if len(arr) == k:
                output.append(arr[:])
                return 
            
            for candid in candidates[num:]:
                arr.append(candid)
                backtrack(num + 1, arr)
                arr.pop()
                num += 1
                
        backtrack(0, [])
        return output