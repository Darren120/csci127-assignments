def capitalize(name):
    s = name.split(" ",1)[0].capitalize()
    s += " " + name.split(" ",1)[1].capitalize()
    return s 
print(capitalize("darren zou"))
def init(name):
    s = " ".join([name[0].upper() + ". " + name.split(" ",1)[1].capitalize()])
    return s
print(init("darren zou"))

def part_pig_latin(name):
    s = name[1:] 
    s += name[0] + "ay"
    return s
print(part_pig_latin("hello"))

def make_out_word(out, word):
    s = out[0] + out[1] + word + out[-1] + out[-2]
    return s
print(make_out_word("<<>>", "hello"))

def make_tags(tag, word):
    s = "<" + tag + ">" + word + "<" + "/" + tag + ">"
    return s
print(make_tags("D", "hello"))