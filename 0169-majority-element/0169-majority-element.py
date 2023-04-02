class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict__={}
        ans=0
        for i in nums:
            dict__[i]=dict__.get(i,0)+1
        print(dict__)
        for i,j in dict__.items():
            if len(nums)//2<j:
                ans=max(ans,i)
        return ans
        