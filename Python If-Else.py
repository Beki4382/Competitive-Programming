def weird_num(n):
    if n % 2 != 0 or 5 < n < 21:
        return("Weird")
    else:
        return("Not Weird")
        


if __name__ == '__main__':
    n = int(input().strip())
    
    print(weird_num(n))
