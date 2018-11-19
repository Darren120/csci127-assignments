def encode(w):
    l = []
    v = 1
    for i in range(len(w)):
        if i == len(w) - 1:
            l.append([w[i], v])
            break
        if w[i] == w[i+1]:
            v += 1
        else:
            l.append([w[i], v])
            v = 1
    return l

def decode(l):
    res = ""
    a = 0
    for i in l:
        for a in range(i[1]):
            res+= i[0]
    return res
    
    

print(decode(encode("aaabbaabbbba")))
print(encode("aaabbaabbbba"))
