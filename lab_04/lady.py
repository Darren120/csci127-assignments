def count(b):
    color = []
    num = []
    for i in b:
        if i != "_":
            if i not in color:
                color.append(i)
                num.append(1)
            else:
                num[color.index(1)]+=1
    return num

def happy(n, b):
    if n < 3:
        if n == 1 and str[0] == "_":
            return True
        if str[0] == b[1]:
            return True
        else:
            return False
    elif n >= 3:
        for i in count(b):
            if i < 2:
                return False
        return True
    return True

def happyLadyBugs(n,b):
    if happy(n,b) == False:
        return "no"
    elif happy(n,b) == True:
        return "yes"
print(happyLadyBugs(3,"RB_"))