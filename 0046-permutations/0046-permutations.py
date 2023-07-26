class Solution:
    def permute(self, arr: List[int]) -> List[List[int]]:
        
        ans  = []
        def bt(res,check) :
            if len(res) == len(arr) :
                ans.append(res[:])
                return
            
            for i in arr :
                if i not in check :
                    check.add(i)
                    res.append(i)
                    bt(res,check)
                    res.remove(i)
                    check.remove(i)
        bt([],set())
        return ans