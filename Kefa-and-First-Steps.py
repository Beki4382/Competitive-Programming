test = int(input())
 
arr = list(map(int, input().split()))
maxCount = 0
i = 1
count = 0
while i < test:
    if arr[i-1] <= arr[i]:
        count += 1
        maxCount = max(maxCount, count)
    else:
        count = 0
    i += 1
print(maxCount + 1)
 
