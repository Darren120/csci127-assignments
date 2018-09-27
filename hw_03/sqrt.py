def mysqrt(int):
    guess = 5
    answer = 0
    while (guess * guess != int):
        answer = ((guess) + (int/guess)) / 2
        if guess == answer:
            return "UNSQUARABLE BUTT Closest square root is:", guess
        guess = answer
        print(guess)
        print(guess*guess)       
    return "SqRoot is:", guess
             
             
print(mysqrt(20)) 
print(mysqrt(16))