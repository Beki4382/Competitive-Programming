
from collections import Counter
n = input()
lis = []
count = {}
for i in range(int(n)):
    lis.append(input())
count = Counter(lis)
print(len(count))
print(' '.join(str(val) for val in count.values() ))
