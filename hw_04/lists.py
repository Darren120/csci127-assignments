import random

def build_random_list(size,max_value):
    """
    Parameters:
      size : the number of elements in the lsit
      max_value : the max random value to put in the list
    """
    l = [] # start with an empty list

    # make a loop that counts up to size
    i = 0
    while i < size:
        l.append(random.randrange(0,max_value))
        # we could have written this instead of the above line:
        # l = l + [random.randrange(0,max_value)]
        i = i + 1
    return l

print(build_random_list(10,3))

def locate(l, value):
    for item in l:
        if item == value:
            a = 0
            while l[a] != value:
                a+=1
            return a
    return -1

print(locate([1,2,3,5,5,5,5,4],4))

def count(l, value):
    o = 0
    for item in l:
        if item == value:
            o+=1
    return o
        
print(count([1,2,3,5,5,5,5,4,5,5,5,5],5))

def reverse(l):
    a = []
    for item in l:
        a.insert(0,item)
    return a
        
print(reverse([6,5,4,3,2,1]))

def isIncreasing(l):
    a = 0
    for item in l:
        if a <= item:
            a = item
        else:
            return False
    return True
print(isIncreasing([1,2,3,4,5,3,6]))

def palindrome(l):
    if reverse(l) == l:
        return True
    return False
print(palindrome([1235321]))
