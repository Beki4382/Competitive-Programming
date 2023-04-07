num = int(input())
num_bit = bin(num)
count = 0
for i in range(2,len(num_bit)):
    if int(num_bit[i]) & 1: 
        count += 1
print(count)
