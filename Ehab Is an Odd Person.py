n = int(input())
arr = list(map(int, input().split()))
odd_num, even_num = False, False

for num in arr:
    if num % 2 == 0:
        even_num = True
    else:
        odd_num = True

if odd_num and even_num:
    arr.sort()

print(*arr)
