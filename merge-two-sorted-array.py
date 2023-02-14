n,m = input().split()

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

output = []

p1= 0 
p2 = 0
i = 0

while p1 < int(n) and p2 < int(m):
    if arr1[p1] > arr2[p2]:
        output.append(arr2[p2])
        p2+=1
    else:
        output.append(arr1[p1])
        p1+=1
    i+=1
    
output.extend(arr1[p1:])
output.extend(arr2[p2:])

print(*output)
        
        
