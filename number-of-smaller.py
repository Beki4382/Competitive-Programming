n,m = input().split()

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

output = []

p1= 0 
p2 = 0

for p2 in range(int(m)):
    while p1 < int(n) and arr1[p1] < arr2[p2] :
        p1+=1
    output.append(p1)
    
print(*output)
        
