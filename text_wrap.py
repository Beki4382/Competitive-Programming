import textwrap

def wrap(string, max_width):  
    newString = []
    for i in range(len(string)):
        if i!=0 and i%max_width== 0:
            newString.append("\n")
        newString.append(string[i])
        var = "".join(newString)
        
    return var

if __name__ == '__main__':
