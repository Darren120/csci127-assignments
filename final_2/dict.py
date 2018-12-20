def addline(d, line):
    l = line.lower()
    for letter in l.split():
        d.setdefault(letter[0], [])
        d[letter[0]] += [letter]
    return d

d = {}
print(addline(d,"HI HOW HI ME YOU MY YELLOW"))
print(addline(d,"BIG GREEN GOBB I IS"))
print(addline(d,"I LIKE TO LELELE LOL THINKING"))
print(addline(d,"CHAIR CHALK IS COOL FREE FOOD AYAYA"))
print(addline(d,"ELON MUSK IS GOD OUR LORD AND SAVIOR SAVE US"))

def spellcheck(d, word):
    w = word.lower()
    for l in d.values():
        if w in l:
            return True
    return False
b = addline(d,"HI HOW HI ME YOU MY YELLOW")
print(spellcheck(b,"HI"))
print(spellcheck(b,"NO"))