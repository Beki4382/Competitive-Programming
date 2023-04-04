test = int(input())
for i in range(test):
    num = int(input())
    num2 = num
 
    count = 0
    while ( num & 1) != 1:
        num >>= 1
        count += 1

    num1 = (1 << count)

    if (1 << count)  == num2:
        if num1 % 2 == 0:
            print(num1 + 1)
        else:
            print(num1 + 2)
    else:
        print(num1)
    
    
