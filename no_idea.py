from collections import Counter
n, m = input().split( )
arr = input().split()
a =Counter(input().split()) 
b =Counter(input().split())  
happiness = 0
for num in arr:
    if num in a:
        happiness+=1
        a[num] -=1
    elif num in b:
        happiness -=1
        b[num]-=1
print(happiness)
