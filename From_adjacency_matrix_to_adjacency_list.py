from collections import defaultdict


n = int(input())
d = defaultdict(list)
for i in range(1, n+1):
    arr = list(map(int, input().split()))
    for j in range(len(arr)):
        if arr[j]:
            d[i].append(j + 1)

for key,val in d.items():
    val.sort()
    print(len(val), end= " ", *val)
    print()
