import random

def randomList():
    list = []
    for i in range(100):
        list.append(random.randint(1,10))
    return list
print(randomList())
print(len(randomList()))

def max(l):
    max = 0
    for i in l:
        if i > max:
            max = i
    return max
print(max(randomList()))

def freq(l,val):
    freq = 0
    for i in l:
        if i == val:
            freq += 1
    return freq

print(freq(randomList(),3))

def mode(l):
    key = 0
    list = {}
    f = 0
    for i in l:
        f = freq(l,i)
        list[f] = i
        if f > key:
            key = f
    return list[key]

print(mode([2,2,2,2,3,3,3,3,3,3,31,1]))
        
        
        
        
        
        
        
        