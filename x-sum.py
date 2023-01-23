from collections import defaultdict
tests = int(input())


for test in range(tests):
    n,m  = map(int,input().split())
    
    arr = []
    for row in range(n):
        arr.append(list(map(int, input().split())))
        
        
            
    hashfront = defaultdict(int)
    hashback = defaultdict(int)
    
    for i in range(n):
        for j in range(m):
            hashfront[j-i] += arr[i][j]
            hashback[i+j] += arr[i][j]
    maxresult = 0       
    for i in range(n):
        for j in range(m):
            currentSum = hashfront[j-i] + hashback[j+i] -arr[i][j]
            maxresult = max(maxresult,currentSum)
    
    print(maxresult)
    
