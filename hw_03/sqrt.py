def mysqrt(int):
    guess = 5
    while (guess * guess != int):
        print(guess) 
        guess = ((guess) + (int/guess)) / 2
    print(guess)
      
print(mysqrt(21))
        