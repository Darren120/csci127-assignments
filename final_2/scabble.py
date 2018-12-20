def canMakeWord(letters,word):
    guess = array(letters)
    w = array(word)
    for letter in w:
        if letter in guess:
            guess.remove(letter)
        else:
            return False           
    return True
def array(word):
    l = []
    for i in word:
        l.append(i)
    return l
print(canMakeWord("ladilmy","daily"))
print(canMakeWord("eerrinn","eerie"))
print(canMakeWord("orrpgma","program"))
print(canMakeWord("orppgma","program"))

def withWild(letters,word):
    guess = array(letters)
    w = array(word)
    for letter in w:
        if letter in guess:
            guess.remove(letter)
        else:
            if "?" in guess:
                guess.remove("?")
                continue
            else:
                return False
    return True
print(withWild("ladilmy","daily"))
print(withWild("e?err??inn","eeeereie"))
print(withWild("orrpgma","program"))
print(withWild("orp?pgma","program"))
        