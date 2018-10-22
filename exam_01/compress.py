vowel = ["a","e","i","o","u"]
def compress_word(w):
    l = w[1:]
    newW = []
    for letter in l:
        if letter in vowel:
            continue
        newW.append(letter)
    return w[0] + ''.join(newW)

print(compress_word("hollween"))

def sentence(word):
    l = word.split()
    newW = []
    for w in l:
        o = compress_word(w)
        newW.append(o)
    return " ".join(newW)



print(sentence("I like to eat apple pie"))
