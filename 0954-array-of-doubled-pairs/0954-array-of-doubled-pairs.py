class Solution(object):
    def canReorderDoubled(self, arr):
        n = [a for a in arr if a<0]
        p= [a for a in arr if a>0]
        arr = sorted(n, reverse = True) +sorted(p)
        c = Counter(arr)
        for num in arr:
            if c[num]==0:continue
            if c[num*2] == 0: return False
            c[num] -=1
            c[num *2] -=1
        return True
       
        
        