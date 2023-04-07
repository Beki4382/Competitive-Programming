test = int(input())
for i in range(test):
    n, k = map(int, input().split())
    bin_val = bin(k)
    sum_ = 0
    length = len(bin_val)
    for i in range(2, len(bin_val)):
        if int(bin_val[i]) & 1:
            sum_ += (n ** ((length - 1) -i))
    
    print(sum_ % (10**9 + 7))
