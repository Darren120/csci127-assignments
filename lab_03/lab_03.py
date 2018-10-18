import random

dictionary = {
    "person":"Darren,Chris,Sam,George,Doot",
    "adj":"cool,nice,strong,ugly,handsome",
    "verb":"hit,bake,kick,hug,slam",
    "pluralnoun":"bikes,cars,tables",
    "noun":"chair,oven,laptop,poop,backpack,foot"
    }

sentence = "I am <adj>! and i like to <verb> <noun> "
sentence1 = "<person>! is cool"

def madlibs(sentence):
    l = sentence.split()
    res = []
    for w in l:
        if '<' in w:
            key = w[1:-1]
            print(w[1:-1])
            has_punc = w.index('>') + 1 < len(w)
            if has_punc:
                key = w[1:-2]
                print(w[1:-2])
            choice = choose_and_remove(key, dictionary)
            if has_punc:
                choice = choice + w[-1]
            res.append(choice)
        else:
            res.append(w)
    new_sentence = " ".join(res)
    return new_sentence

def choose_and_remove(key, dictionary):
    word_bank = dictionary[key].split(',')
    choice = random.choice(word_bank)
    dictionary[key] = dictionary[key].replace("," + choice, "")
    return choice

print(madlibs(sentence))
print(madlibs(sentence1))