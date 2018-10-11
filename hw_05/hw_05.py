def filterodd(l):
    a = []
    for i in l:
        if i % 2 != 0:
            a.append(i)
    return a

print(filterodd([1,2,3,4,5,6,7]))

def mapsquare(l):
    a = []
    for i in l:
        a.append(i*i)
    return a

print(mapsquare([1,2,3,4]))