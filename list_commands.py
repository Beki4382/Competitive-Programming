if __name__ == '__main__':
    N = int(input())    

commands = []
for i in range(N):
    commands.append(input().split())
    
newList = []

for command in commands:
    if command[0] == "insert":
        newList.insert(int(command[1]),int(command[2]))
        
    elif command[0] == "remove":
        newList.remove(int(command[1]))
        
    elif command[0] == "append":
        newList.append(int(command[1]))
        
    elif command[0] == "sort":
        newList.sort()
    elif command[0] == "pop":
        newList.pop()
        
    elif command[0] == "reverse":
        newList.reverse()
    else:
        print(newList)
    
