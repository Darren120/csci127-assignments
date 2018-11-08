def happyLadybugs(b):
    key = "_"
    if isEnough(b): 
        if key in b:
            return "yes"
        return noSpaces(b) 
    else:
        return "no" 

def isEnough(b):
    set = {}
    for i in b:
        if i == '_':
            continue
        set.setdefault(i, 0)
        set[i] += 1
    return min(set.values()) > 1

def noSpaces(b):
    i = 1
    while i < len(b) - 1:
        if b[i - 1] != b[i] and b[i] != b[i + 1]:
            return "no"
        i += 1
    return "yes"
print(happyLadybugs("AAAQQss"))
