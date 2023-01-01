from collections import defaultdict
d = defaultdict(list)

n, m= input().split()
group_a = []
group_b = []

for i in range(int(n)):
    group_a.append(input())
    
for i in range(int(m)):
    group_b.append(input())
    
for i,val in enumerate(group_a,1):
    d[val].append(str(i))
   
for val in group_b:
    if val in d:
        print(" ".join(d[val]))
    else:
        print("-1")
