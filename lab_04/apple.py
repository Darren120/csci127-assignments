def countApplesAndOranges(s,t,a,b,apples,oranges):
    rangeA = calc(s,t,a)
    rangeO = calc(s,t,a)
    numApples = 0
    numOranges = 0
    for i in apples:
        if i >= rangeA[0] and i <= rangeA[1]:
            numApples+=1
    for i in oranges:
        if i >= rangeO[0] and i <= rangeO[1]:
            numOranges+=1
    return numApples, numOranges
def calc(s,t,a):
    range = []
    range.append(s-a)
    range.append(t-a)
    return range
print(countApplesAndOranges(7,10,4,12,[2,3,-4,7],[3,-2,4]))

