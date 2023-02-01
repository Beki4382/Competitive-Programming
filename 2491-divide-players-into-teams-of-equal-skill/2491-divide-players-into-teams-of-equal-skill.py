class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()
        left = 0
        right = len(skill)-1
        chemistry = 0
        team = skill[left]+ skill[right]
        
        while left < right:
            if skill[left] + skill[right] != team:
                return -1
            chemistry += skill[left]*skill[right]
            left+=1
            right-=1
        return chemistry
            
            