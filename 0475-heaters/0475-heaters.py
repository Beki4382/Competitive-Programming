class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        ans=[]
        for i in houses:
            res=bisect_left(heaters,i)
            if(res==0):
                ans.append(abs(heaters[res]-i))
            elif (res>= len(heaters)):
                ans.append(abs(heaters[-1]-i))
            else:
                ans.append(min(abs(heaters[res]-i),abs(heaters[res-1]-i)))
            
        return max(ans)