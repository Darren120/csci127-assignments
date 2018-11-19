def score(w):
    n = w.lower()
    l = list(n)
    score = 0
    for letter in l:
        if letter in "aeioulnrst":
            score += 1
        elif letter in "dg":
            score += 2
        elif letter in "bcmp":
            score += 3
        elif letter in "fhvwy":
            score += 4
        elif letter in "k":
            score += 5
        elif letter in "jx":
            score += 8
        else:
            score += 10
    return score

def list(w):
    a = []
    for letter in w:
        a.append(letter)
    return a
print(score("hello"))