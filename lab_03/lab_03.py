import random

dictionary = {
    "person":"Darren,Chris,Sam,George,Doot",
    "adj":"cool,nice,strong,ugly,handsome",
    "verb":"hit,bake,kick,hug,slam",
    "pluralnoun":"bikes,cars,tables",
    "noun":"chair,oven,laptop,poop,backpack,foot"
    }

sentence = "I am <adj> and i like to <verb> <noun> "
sentence1 = "<person> is <adj>"

def madlibs(sentence):
    sentence = punc(sentence, True)
    l = sentence.split()
    res = []
    for w in l:
        if '<' in w:
            to_replace = w[1:-1]
            word_bank = dictionary[to_replace].split(',')
            res.append(get_random_from_list(word_bank))
        else:
            res.append(w)
    new_sentence = punc(" ".join(res), False)
    return new_sentence

def punc(sentence, bool):
    if bool: 
        sentence = sentence.replace(".", " . ")
        sentence = sentence.replace(",", " , ")
    else: 
        sentence = sentence.replace(" .", ".")
        sentence = sentence.replace(" ,", ",")
    return sentence

def get_random_from_list(l):
    rng = random.randint(0, len(l) - 1)
    return l[rng]

print(madlibs(sentence))
print(madlibs(sentence1))