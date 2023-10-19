class Solution:
    def numTeams(self, nums: List[int]) -> int:
        
        
        n=len(nums)
        ans=0

        for i in range(n):
            ls=lg=0
            rs=rg=0
            for j in range(i):
                if nums[j]<nums[i]:
                    ls+=1
                else:
                    lg+=1
            
            for k in range(i+1,n):
                if nums[k]>nums[i]:
                    rg+=1
                else:
                    rs+=1
            
            ans+=(ls*rg)+(lg*rs)
        
        return ans
            
        
        