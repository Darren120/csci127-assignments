# Darren Zou & Christopher He 
import random

dictionary = {
    "person":"Darren,Chris,Sam,George,Doot",
    "adj":"cool,nice,strong,ugly,handsome",
    "verb":"hit,bake,kick,hug,slam",
    "pluralnoun":"bikes,cars,tables",
    "noun":"chair,oven,laptop,poop,backpack,foot"
    }

sentence = "I am <adj> and i like to <verb> <noun> "
sentence1 = "<person>! is cool"

def madlibs(sentence):
    l = sentence.split()
    res = []
    for w in l:
        if '<' in w and '>' in w:
            key = extract_key(w)
            choice = choose_and_remove_from(key, dictionary) # avoid repeats
            replaced = w.replace(key, choice).replace('<', '').replace('>', '')
            res.append(replaced)
        else:
            res.append(w)
    new_sentence = " ".join(res)
    return new_sentence

def extract_key(s):
    start = s.index('<') + 1
    end = s.index('>')
    return s[start:end]

def choose_and_remove_from(key, dictionary):
    word_bank = dictionary[key].split(',')
    choice = random.choice(word_bank)
    dictionary[key] = dictionary[key].replace("," + choice, "")
    return choice

print(madlibs(sentence))
print(madlibs(sentence1))