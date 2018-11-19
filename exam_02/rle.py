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


print(encode("aaabba"))