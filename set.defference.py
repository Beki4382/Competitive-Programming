engNews = int(input())
engTakers = input().split()
frenchNews = int(input())
frenchTakers = input().split()

count = 0

for val in engTakers:
    if val not in frenchTakers:
        count += 1
        
print(count) 
