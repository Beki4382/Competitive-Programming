set_a = set(input().split())
n = int(input())
otherSets = []

for i in range(n):
    otherSets.append(set(input().split()))

def check_strict_superset(set_a, otherSets):
    for oneSet in otherSets:
        if len(oneSet) >= len(set_a):
            return False
        else:
            for val in oneSet:
                if val not in set_a:
                    return False
    return True    
            
print(check_strict_superset(set_a, otherSets))
        
    
