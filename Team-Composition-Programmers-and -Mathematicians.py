def possible( pro, mat ):
    return min(pro, mat, (pro + mat)//4 )

tests = int(input())
for test in range(tests):
    pro, mat = map(int, input().split())
    print(possible(pro, mat))


    
