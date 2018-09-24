def fizzBuzz(int):
    i=0
    while (i < int):
        if (i % 3 == 0 & i % 5 == 0):
            i+=1
            print("fizzbuzz")
        elif (i % 3 == 0):
            i+=1 
            print("fizz")
        elif (i % 5 == 0):
            i+=1
            print("buzz")
        else:
            i+=1
            print(i)
            
            
print(fizzBuzz(100))