n = int(input())
d = {"X":"", "S":"-1", "M":"0", "L":"1"}
for i in range(n):
    t_size = input().split()
    t_one = [d[k] for k in t_size[0]]
    t_two = [d[k] for k in t_size[1]]
    t_one.reverse()
    t_two.reverse()
    if t_one[0] == "-1" and t_two[0] == "-1":
        if t_one > t_two:
            print("<")
        elif t_one < t_two:
            print(">")
        else:
            print("=")
    else:
        if t_one > t_two:
            print(">")
        elif t_one < t_two:
            print("<")
        else:
            print("=")
    
