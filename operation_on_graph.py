from collections import defaultdict


no_node = int(input())
no_op = int(input())

d = defaultdict(list)
for i in range(no_op):
    operation = list(map(int,  input().split()))
    if operation[0] == 1:
        d[operation[1]].append(operation[2])
        d[operation[2]].append(operation[1])
    if operation[0] == 2:
        print(*d[operation[1]])
