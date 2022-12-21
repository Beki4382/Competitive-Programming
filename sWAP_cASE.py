def swap_case(s):
    arr = [0]*len(s)
    for i in range(len(s)):
        if s[i] == s[i].upper():
            arr[i]=s[i].lower()
        else:
            arr[i] = s[i].upper()
    
    return str(''.join(arr))

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
