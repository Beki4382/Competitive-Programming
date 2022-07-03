def domino():
   sides = list (input().split())
   area = int(sides[0]) * int(sides[1])
   return area//2

print(domino())
