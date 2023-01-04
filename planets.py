from collections import Counter
test_cases = int(input())


for i in range(test_cases):
    
    planets_num, cost = map(int, input().split())
    planets = input().split()
    count = Counter(planets)
    min_cost = 0
    
    for val in count.keys():
        
        min_cost += min(count[val], cost)
    
    print(min_cost)
