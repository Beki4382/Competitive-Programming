test= int(input())
for t in range(test):
    n = int(input())
    blocks =input().split()
    blocks = list(map(int, blocks))
   
    left_p = 0
    right_p = n-1
    bottom_cube = float("inf")
    
    while left_p < right_p:
        if blocks[left_p] >= blocks[right_p] and bottom_cube >= blocks[left_p]:
            bottom_cube = blocks[left_p]
            left_p += 1
            
        elif blocks[left_p] < blocks[right_p] and bottom_cube >= blocks[right_p]:
            bottom_cube = blocks[right_p]
            right_p -= 1
            
        else:
            print("No")
            break
        
    if left_p == right_p:
        print("Yes")
              
            
