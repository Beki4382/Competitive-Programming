n = int(input())
res = 0
for i in range(1, n +1):
    arr = list(map(int, input().split()))
    count = [digit for digit in arr if digit == 1]
    res += len(count)
print(res//2)
