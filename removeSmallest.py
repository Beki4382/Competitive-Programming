tests = int(input())

for _ in range(tests):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    
    p1 = 0
    p2 = 1
    flag = False
    
    while p2 < n:
        if n == 1:
            print("YES")
            break
        
        elif arr[p2] - arr[p1] > 1:
            print("NO")
            flag = True
            break
    
        p1+=1
        p2+=1
        
    if flag == False:
        print("YES")
        
