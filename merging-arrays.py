n, m = map(int,input().split())

a= list(map(int,input().split()))
b = list(map(int,input().split()))

newarr = []

p1 = 0
p2 = 0

while p1 < n and p2 < m:
    if a[p1] < b[p2]:
        newarr.append(a[p1])
        p1+=1
    elif b[p2] < a[p1]:
        newarr.append(b[p2])
        p2+=1
    elif a[p1] == b[p2]:
        newarr.append(a[p1])
        newarr.append(b[p2])
        p1+=1
        p2+=1

newarr.extend(a[p1:])
newarr.extend(b[p2:])

print(*newarr)
