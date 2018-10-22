def divide(A,B,u):
    ratio = A/B
    ppl = 0
    while u >= ratio:
        u -= ratio
        ppl+=1
    return ppl
print(divide(5,10,1))

