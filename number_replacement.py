test_cases = int(input())

for i in range(test_cases):
    d = {}
    n = int(input())
    nums = input().split()
    string = input()
    
    for i in range(n):
        if nums[i] not in d:
            d[nums[i]] = string[i]
    newString = "".join(d[i] for i in nums )
    if newString == string:
        print("YES")
    else: 
        print("NO")
        
        
