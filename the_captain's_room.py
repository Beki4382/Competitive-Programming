from collections import Counter
n = input()
lis = input()
count = {}
count = Counter(lis)
for i in count:
    if count[i] == 1:
        print(i)
