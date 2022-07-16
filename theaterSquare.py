def numberOfFlagStone(n,m,a):
    side1 = n//a
    side2 = m//a
    if (n%a and m%a !=0):
        numberOfFlagStones =  (side1+1)*(side2+1)
    else:
        numberOfFlagStones =  side1*side2
    return numberOfFlagStones

if __name__ == '__main__':
    print(numberOfFlagStone(9,9,4)) 
    
