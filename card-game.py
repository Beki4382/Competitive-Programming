n = int(input())
arr = list(map(int, input().split()))
 
sereja = 0
dima = 0
k = 0
j = n-1
i=0
while i < n and k <= j:
    bigCard = max(arr[k], arr[j])
    
    if arr[k] > arr[j]:
        k+=1
    else:
        j -=1
        
    if i%2 == 0:
        sereja += bigCard
    elif i%2 != 0:
        dima += bigCard
    i+=1
print(sereja,dima)
