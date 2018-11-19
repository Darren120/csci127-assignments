def makeacronym(m):
    a=""
    c = m.split()
    for w in c:
        a+=w[0]
    return a
print(makeacronym("laugh out loud"))