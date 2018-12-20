def countPlurals(line):
    l = line.split(" ")
    plural = 0
    for word in l:
        if word[-1] == "s":
            plural+=1
    return plural

print(countPlurals("hi pets are cools"))

def notPossesive(line):
    l = line.split(" ")
    plural = 0
    for word in l:
        if word[-2] == "'":
            continue
        elif word[-2] != "'" and word[-1] == "s":
            plural+=1
    return plural
print(notPossesive("gorillas gorilla's cats"))
print(notPossesive("rats cats people's foods"))