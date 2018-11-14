#Darren and Jadeja
def build_word_counts(words):
    d={"call" : []} # a list of dictionaries containing a key: a list of items
    c = words.split()
    for i in range(len(c)): #loops for the amount of occurances in c
        if c[i] in d: # if c contains a key
            d[c[i]].append(c[i+1]) #add the word after the occurance of c[i]
    return d

def clean_data(s):
    result=""
    for letter in s:
        if letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            result = result + letter.lower()
        else:
            result = result + " "
    return result
def textFormatter(filePath):
    filename = filePath
    f = open(filename,encoding='utf-8')
    s = f.read()
    cleaned_string = clean_data(s)
    words = build_word_counts(cleaned_string)
    return words

words = textFormatter("/Users/Bob/desktop/csci127-assignments/hw_08/moby.txt")
print(words)
